import ipywidgets as widgets
from IPython.display import display, HTML
import time
import threading

class NotebookLanguageGameApp:
    def __init__(self, all_mode1_items, all_mode2_items):
        self.all_mode1_items = all_mode1_items
        self.all_mode2_items = all_mode2_items
        
        # Discover available languages
        self.available_langs = sorted(list(set([i.get("language", "np") for i in all_mode1_items + all_mode2_items])))
        if not self.available_langs:
            self.available_langs = ["np"]
            
        self.current_items = []
        self.current_index = 0
        self.score = 0
        
        self.build_ui()
        
    def build_ui(self):
        self.out = widgets.Output()
        
        # Header
        self.header = widgets.HTML("<h2>Multilingual Literacy Game</h2>")
        
        # Selectors
        self.lang_selector = widgets.Dropdown(
            options=self.available_langs,
            value=self.available_langs[0],
            description='Language:'
        )
        
        self.mode_selector = widgets.Dropdown(
            options=[('Mode 1: Transliteration to Grapheme', 1), ('Mode 2: English to Target Language', 2)],
            value=1,
            description='Mode:'
        )
        
        self.start_btn = widgets.Button(description="Start Session", button_style='primary')
        self.start_btn.on_click(self.start_session)
        
        self.controls_box = widgets.HBox([self.lang_selector, self.mode_selector, self.start_btn])
        
        # Game Area
        self.progress = widgets.IntProgress(value=0, min=0, max=10, description='Progress:')
        self.score_label = widgets.Label(value="Score: 0 / 0")
        
        self.prompt_display = widgets.HTML("<h1 style='text-align: center; font-size: 3em;'>-</h1>")
        self.audio_btn = widgets.Button(description="🔊 Play Audio", disabled=True, icon="play", layout=widgets.Layout(margin='0 auto', display='block'))
        self.audio_btn.on_click(self.play_audio)
        
        self.options_box = widgets.HBox([], layout=widgets.Layout(justify_content='center', padding='20px'))
        self.feedback_display = widgets.HTML("<h3 style='text-align: center; height: 30px;'></h3>")
        
        self.next_btn = widgets.Button(description="Next Question", disabled=True, layout=widgets.Layout(margin='0 auto', display='block'))
        self.next_btn.on_click(self.next_question)
        
        self.game_box = widgets.VBox([
            widgets.HBox([self.progress, self.score_label], layout=widgets.Layout(justify_content='space-between')),
            self.prompt_display,
            self.audio_btn,
            self.options_box,
            self.feedback_display,
            self.next_btn
        ], layout=widgets.Layout(display='none', align_items='stretch', padding='20px', border='1px solid #ccc', width='600px'))
        
        self.main_box = widgets.VBox([self.header, self.controls_box, self.game_box, self.out])
        
    def show(self):
        display(self.main_box)
        
    def start_session(self, b):
        mode = self.mode_selector.value
        lang = self.lang_selector.value
        
        source_items = self.all_mode1_items if mode == 1 else self.all_mode2_items
        self.current_items = [item for item in source_items if item.get("language") == lang]
        
        if not self.current_items:
            with self.out:
                self.out.clear_output()
                print(f"No items available for language '{lang}' in mode {mode}.")
            return
            
        self.out.clear_output()
        self.current_index = 0
        self.score = 0
        self.progress.max = len(self.current_items)
        self.progress.value = 0
        
        self.controls_box.layout.display = 'none'
        self.game_box.layout.display = 'flex'
        
        self.render_question()
        
    def render_question(self):
        if self.current_index >= len(self.current_items):
            self.end_session()
            return
            
        item = self.current_items[self.current_index]
        self.progress.value = self.current_index
        self.score_label.value = f"Score: {self.score} / {self.current_index}"
        
        # Reset UI state
        self.feedback_display.value = "<h3 style='text-align: center; height: 30px;'></h3>"
        self.next_btn.disabled = True
        self.audio_btn.disabled = True
        
        mode = item["mode"]
        if mode == 1:
            self.prompt_display.value = f"<h1 style='text-align: center; font-size: 3em;'>{item['transliteration']}</h1>"
            if item.get("audio_placeholder") or item.get("audio_path"):
                self.audio_btn.disabled = False
        else:
            self.prompt_display.value = f"<h1 style='text-align: center; font-size: 3em;'>{item['english_prompt']}</h1>"
            
        # Render options
        buttons = []
        for opt in item["options"]:
            btn = widgets.Button(description=opt, layout=widgets.Layout(width='100px', height='80px', margin='10px'))
            btn.style.font_weight = 'bold'
            
            def on_click(b, selected=opt):
                self.handle_answer(selected)
            btn.on_click(on_click)
            buttons.append(btn)
            
        self.options_box.children = buttons
        
    def play_audio(self, b):
        def _play():
            self.audio_btn.description = "🔊 Playing..."
            time.sleep(1)
            self.audio_btn.description = "🔊 Play Audio"
        threading.Thread(target=_play).start()
        
    def handle_answer(self, selected):
        item = self.current_items[self.current_index]
        mode = item["mode"]
        correct_answer = item.get("correct_grapheme", item.get("correct_nepali"))
        
        is_correct = (selected == correct_answer)
        if is_correct:
            self.score += 1
            self.feedback_display.value = f"<h3 style='color: green; text-align: center;'>Correct!</h3>"
        else:
            self.feedback_display.value = f"<h3 style='color: red; text-align: center;'>Incorrect. Correct: {correct_answer}</h3>"
            
        if mode == 2 and item.get("correct_transliteration"):
             self.feedback_display.value = self.feedback_display.value.replace("</h3>", f" <span style='color: #666; font-size: 0.8em;'>(transliteration: {item['correct_transliteration']})</span></h3>")
            
        self.score_label.value = f"Score: {self.score} / {self.current_index + 1}"
        
        for btn in self.options_box.children:
            btn.disabled = True
            if btn.description == correct_answer:
                btn.style.button_color = 'lightgreen'
            elif btn.description == selected and not is_correct:
                btn.style.button_color = 'salmon'
                
        self.next_btn.disabled = False
        
    def next_question(self, b):
        self.current_index += 1
        self.render_question()
        
    def end_session(self):
        self.prompt_display.value = "<h1 style='text-align: center;'>Session Complete!</h1>"
        self.progress.value = self.progress.max
        self.feedback_display.value = f"<h3 style='text-align: center;'>Final Score: {self.score} / {len(self.current_items)}</h3>"
        self.options_box.children = []
        self.next_btn.disabled = True
        self.audio_btn.disabled = True
        
        # Show reset button
        reset_btn = widgets.Button(description="Back to Menu", button_style='warning', layout=widgets.Layout(margin='0 auto', display='block'))
        reset_btn.on_click(lambda b: self.reset_app())
        self.options_box.children = [reset_btn]
        
    def reset_app(self):
        self.controls_box.layout.display = 'flex'
        self.game_box.layout.display = 'none'
        self.out.clear_output()
