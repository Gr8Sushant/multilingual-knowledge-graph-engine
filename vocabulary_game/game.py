import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import pickle
import threading

IMG_SIZE = (380, 380)
LANGUAGES = ['urdu', 'darija', 'nepali', 'vietnamese']

# ── concept definitions: image path, visual group, imagenet_id ────────────────
# imagenet_id links to the graph — None means not in UKC, skip for that language
CONCEPTS = {
    'cow':      ('15/animals/cow.jpg',          'animals',     'n02403454'),
    'goat':     ('15/animals/goat.jpg',         'animals',     'n02416519'),
    'horse':    ('15/animals/horse.jpg',        'animals',     'n02374451'),
    'sheep':    ('15/animals/sheep.jpg',        'animals',     'n02411705'),
    'hen':      ('15/birds/hen.jpg',            'birds',       'n01792640'),
    'duck':     ('15/birds/duck.jpg',           'birds',       'n01846331'),
    'parrot':   ('15/birds/parrot.jpg',         'birds',       'n01816887'),
    'pigeon':   ('15/birds/pigeon.jpg',         'birds',       'n01811909'),
    'bread':    ('15/bread/bread.jpg',          'bread',       'n07679356'),
    'biscuit':  ('15/bread/biscuit.jpg',        'bread',       'n07693972'),
    'cake':     ('15/bread/cake.jpg',           'bread',       'n07628870'),
    'flour':    ('15/bread/flour.jpg',          'bread',       'n07569106'),
    'shirt':    ('15/clothing/shirt.jpg',       'clothing',    'n04197391'),
    'glove':    ('15/clothing/glove.jpg',       'clothing',    'n03441112'),
    'shoe':     ('15/clothing/shoe.jpg',        'clothing',    'n04199027'),
    'sock':     ('15/clothing/sock.jpg',        'clothing',    'n04254777'),
    'pear':     ('15/fruits/pear.jpg',          'fruits',      'n07767847'),
    'coconut':  ('15/fruits/coconut.jpg',       'fruits',      'n07773238'),
    'guava':    ('15/fruits/guava.jpg',         'fruits',      'n07765361'),
    'mango':    ('15/fruits/mango.jpg',         'fruits',      'n12761284'),
    'bed':      ('15/furniture/bed.jpg',        'furniture',   'n02818832'),
    'curtain':  ('15/furniture/curtain.jpg',    'furniture',   'n03151077'),
    'door':     ('15/furniture/door.jpg',       'furniture',   'n03221720'),
    'pillow':   ('15/furniture/pillow.jpg',     'furniture',   'n03938244'),
    'mosque':   ('15/building/mosque.jpg',      'building',    'n03788195'),
    'hospital': ('15/building/hospital.jpg',    'building',    'n03540595'),
    'hotel':    ('15/building/hotel.jpg',       'building',    'n03542333'),
    'prison':   ('15/building/prison.jpg',      'building',    'n04005630'),
    'doctor':   ('15/profession/doctor.jpg',    'profession',  'n10020890'),
    'farmer':   ('15/profession/farmer.jpg',    'profession',  'n10078806'),
    'soldier':  ('15/profession/soldier.jpg',   'profession',  'n10622053'),
    'teacher':  ('15/profession/teacher.jpg',   'profession',  'n10694258'),
    'bride':    ('15/people/bride.jpg',         'people',      'n09874618'),
    'girl':     ('15/people/girl.jpg',          'people',      'n10129825'),
    'man':      ('15/people/man.jpg',           'people',      'n10287213'),
    'woman':    ('15/people/woman.jpg',         'people',      'n10787470'),
    'egg':      ('15/dairy/egg.jpg',            'dairy',       'n01460457'),
    'butter':   ('15/dairy/butter.jpg',         'dairy',       'n07848338'),
    'honey':    ('15/dairy/honey.jpg',          'dairy',       'n07858978'),
    'milk':     ('15/dairy/milk.jpg',           'dairy',       'n07844042'),
    'comb':     ('15/accessories/comb.jpg',     'accessories', 'n03075097'),
    'glasses':  ('15/accessories/glasses.jpg',  'accessories', 'n04272054'),
    'handbag':  ('15/accessories/handbag.jpg',  'accessories', 'n02774152'),
    'key':      ('15/accessories/key.jpg',      'accessories', 'n03613294'),
    'face':     ('15/body parts/face.jpg',      'body',        'n05600637'),
    'eye':      ('15/body parts/eye.jpg',       'body',        'n05311054'),
    'hand':     ('15/body parts/hand.jpg',      'body',        'n05564590'),
    'mouth':    ('15/body parts/mouth.jpg',     'body',        'n05302499'),
    'bicycle':  ('15/transport/bicycle.jpg',    'transport',   'n02834778'),
    'bus':      ('15/transport/bus.jpg',        'transport',   'n02924116'),
    'car':      ('15/transport/car.jpg',        'transport',   'n02958343'),
    'truck':    ('15/transport/truck.jpg',      'transport',   'n04490091'),
}

# ── graph lookup ──────────────────────────────────────────────────────────────

def build_word_lookup(graph_path='urdu_game_graph.pkl'):
    """
    Load graph, return dict: imagenet_id -> {lang: preferred_word}
    Uses preferred_<lang> attribute on concept nodes (set by graph_builder).
    """
    with open(graph_path, 'rb') as f:
        G = pickle.load(f)
    lookup = {}
    for nid, data in G.nodes(data=True):
        if data.get('node_type') != 'concept':
            continue
        iid = data.get('imagenet_id', '')
        if not iid:
            continue
        langs = {}
        for lang in LANGUAGES:
            word = data.get(f'preferred_{lang}', '').strip()
            if word:
                langs[lang] = word
        if langs:
            lookup[iid] = langs
    return lookup

def get_word(lookup, concept_key, language):
    """
    Get word from graph via imagenet_id.
    Returns None if concept not in graph or no word for this language.
    """
    iid = CONCEPTS[concept_key][2]
    if iid and iid in lookup:
        return lookup[iid].get(language)
    return None

# ── game ──────────────────────────────────────────────────────────────────────

class WordImageGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Image → Word Game")
        self.root.configure(bg='#f5f5f5')

        self.language = tk.StringVar(value='urdu')
        self.score = 0
        self.total = 0
        self.answered = False
        self.img_cache = {}
        self.queue = []
        self.lookup = {}
        self.graph_ready = False

        self._build_ui()
        threading.Thread(target=self._load_graph_bg, daemon=True).start()

    def _load_graph_bg(self):
        self.lookup = build_word_lookup()
        self.graph_ready = True
        self.root.after(0, self.next_question)

    def _build_ui(self):
        top = tk.Frame(self.root, bg='#f5f5f5', pady=8)
        top.pack(fill=tk.X, padx=12)

        tk.Label(top, text="Language:", bg='#f5f5f5', font=('Arial', 11)).pack(side=tk.LEFT)
        lang_menu = ttk.Combobox(top, textvariable=self.language,
                                  values=LANGUAGES, state='readonly', width=12)
        lang_menu.pack(side=tk.LEFT, padx=6)
        lang_menu.bind('<<ComboboxSelected>>',
                        lambda e: [setattr(self, 'queue', []), self.next_question()])

        self.score_label = tk.Label(top, text="Score: 0 / 0",
                                     bg='#f5f5f5', font=('Arial', 11, 'bold'))
        self.score_label.pack(side=tk.RIGHT)

        self.img_label = tk.Label(self.root, bg='#ccc', text="Loading...",
                                   font=('Arial', 14),
                                   width=IMG_SIZE[0], height=IMG_SIZE[1])
        self.img_label.pack(pady=(10, 4))

        self.hint_label = tk.Label(self.root, text="", font=('Arial', 13, 'bold'),
                                    bg='#f5f5f5', fg='#555')
        self.hint_label.pack(pady=2)

        btn_frame = tk.Frame(self.root, bg='#f5f5f5')
        btn_frame.pack(pady=10, padx=20, fill=tk.X)
        self.word_buttons = []
        for i in range(4):
            btn = tk.Button(btn_frame, text="", font=('Arial', 14),
                            width=20, height=2, wraplength=240,
                            cursor='hand2',
                            command=lambda i=i: self.check_answer(i))
            btn.grid(row=i//2, column=i%2, padx=8, pady=6, sticky='ew')
            self.word_buttons.append(btn)
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        self.feedback_label = tk.Label(self.root, text="",
                                        font=('Arial', 13, 'bold'), bg='#f5f5f5')
        self.feedback_label.pack(pady=4)

        self.next_btn = tk.Button(self.root, text="Next →", font=('Arial', 11),
                                   command=self.next_question, state=tk.DISABLED,
                                   bg='#4a90d9', fg='white', padx=16, pady=4)
        self.next_btn.pack(pady=6)

    def _get_valid_quiz_concepts(self, lang):
        """Return concepts that have a word in the target language from the graph."""
        return [k for k in CONCEPTS if get_word(self.lookup, k, lang) is not None]

    def next_question(self):
        if not self.graph_ready:
            return

        self.feedback_label.config(text='')
        self.next_btn.config(state=tk.DISABLED)
        self.answered = False
        for btn in self.word_buttons:
            btn.config(state=tk.DISABLED, bg='SystemButtonFace', fg='black', text='')

        lang = self.language.get()
        valid = self._get_valid_quiz_concepts(lang)

        if not valid:
            self.hint_label.config(text="No words available for this language.")
            return

        # refill queue
        if not self.queue or not any(k in valid for k in self.queue):
            self.queue = [k for k in valid]
            random.shuffle(self.queue)

        # pick next valid concept
        key = None
        while self.queue:
            candidate = self.queue.pop(0)
            if candidate in valid:
                key = candidate
                break

        if key is None:
            return

        path, group, _ = CONCEPTS[key]
        correct_word = get_word(self.lookup, key, lang)

        # distractors: same group first, then other groups
        # only include concepts that have a word in this language
        same = [k for k in CONCEPTS
                if k != key
                and CONCEPTS[k][1] == group
                and get_word(self.lookup, k, lang) is not None]
        diff = [k for k in CONCEPTS
                if k != key
                and CONCEPTS[k][1] != group
                and get_word(self.lookup, k, lang) is not None]
        random.shuffle(same)
        random.shuffle(diff)
        distractor_keys = (same + diff)[:3]
        distractor_words = [get_word(self.lookup, k, lang) for k in distractor_keys]

        # build options — only as many as we have
        options = [(correct_word, True)] + [(w, False) for w in distractor_words]
        random.shuffle(options)

        self.correct_idx = next(i for i, (_, c) in enumerate(options) if c)

        # show only available buttons
        for i, btn in enumerate(self.word_buttons):
            if i < len(options):
                btn.config(text=options[i][0], state=tk.NORMAL)
            else:
                btn.config(text='', state=tk.DISABLED)

        self.hint_label.config(text=f"English: {key}")

        # load image
        if key not in self.img_cache:
            try:
                img = Image.open(path).convert('RGB').resize(IMG_SIZE)
                self.img_cache[key] = ImageTk.PhotoImage(img)
            except Exception:
                self.img_cache[key] = None

        photo = self.img_cache[key]
        if photo:
            self.img_label.config(image=photo, text='', bg='black')
            self.img_label.image = photo
        else:
            self.img_label.config(image='', text='No image', bg='#ccc',
                                   font=('Arial', 14))

    def check_answer(self, idx):
        if self.answered:
            return
        self.answered = True
        self.total += 1
        for btn in self.word_buttons:
            btn.config(state=tk.DISABLED)

        if idx == self.correct_idx:
            self.score += 1
            self.word_buttons[idx].config(bg='#4caf50', fg='white')
            self.feedback_label.config(text="Correct!", fg='#4caf50')
        else:
            self.word_buttons[idx].config(bg='#f44336', fg='white')
            self.word_buttons[self.correct_idx].config(bg='#4caf50', fg='white')
            self.feedback_label.config(text="Wrong!", fg='#f44336')

        self.score_label.config(text=f"Score: {self.score} / {self.total}")
        self.next_btn.config(state=tk.NORMAL)


if __name__ == '__main__':
    root = tk.Tk()
    app = WordImageGame(root)
    root.mainloop()
