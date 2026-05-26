var myGraphData = {
    "directed": true,
    "multigraph": false,
    "graph": {
        "scoring_rules": {
            "Broad Age": 5,
            "Specific Gen": 4,
            "Addressee": 3,
            "Context": 2,
            "Speaker": 1
        },
        "max_penalty": 15
    },
    "nodes": [
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Male - Neutral - Male spk"
        },
        {
            "type": "attribute",
            "category": "Broad Age",
            "id": "Age: Same Age"
        },
        {
            "type": "attribute",
            "category": "Specific Gen",
            "id": "Gen: Exactly same age"
        },
        {
            "type": "attribute",
            "category": "Addressee Gender",
            "id": "Target: Male"
        },
        {
            "type": "attribute",
            "category": "Social Context",
            "id": "Context: Neutral"
        },
        {
            "type": "attribute",
            "category": "Speaker Gender",
            "id": "Spk: Male spk"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Male - Neutral - Female spk"
        },
        {
            "type": "attribute",
            "category": "Speaker Gender",
            "id": "Spk: Female spk"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Female - Neutral - Male spk"
        },
        {
            "type": "attribute",
            "category": "Addressee Gender",
            "id": "Target: Female"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Female - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Madarin",
            "term_i": "我 (wǒ)",
            "term_you": "你 (nǐ)",
            "label": "Madarin: 我 (wǒ)/你 (nǐ)",
            "id": "Instance_f84837"
        },
        {
            "type": "instance",
            "language": "Cantonese",
            "term_i": "我 (ngo5)",
            "term_you": "你 (nei5)",
            "label": "Cantonese: 我 (ngo5)/你 (nei5)",
            "id": "Instance_6c6710"
        },
        {
            "type": "instance",
            "language": "Teochew",
            "term_i": "我 (guá)",
            "term_you": "你 (lí)",
            "label": "Teochew: 我 (guá)/你 (lí)",
            "id": "Instance_5c824c"
        },
        {
            "type": "instance",
            "language": "Nepali",
            "term_i": "म (ma)",
            "term_you": "तँ (ta) / तिमी (timi)",
            "label": "Nepali: म (ma)/तँ (ta) / तिमी (timi)",
            "id": "Instance_54ba62"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Male - Informal - Male spk"
        },
        {
            "type": "attribute",
            "category": "Social Context",
            "id": "Context: Informal"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Male - Informal - Female spk"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Female - Informal - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Female - Informal - Female spk"
        },
        {
            "type": "instance",
            "language": "Urdu",
            "term_i": "میں",
            "term_you": "تم (tum)",
            "label": "Urdu: میں/تم (tum)",
            "id": "Instance_727bd0"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Male - Formal - Male spk"
        },
        {
            "type": "attribute",
            "category": "Social Context",
            "id": "Context: Formal"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Male - Formal - Female spk"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Female - Formal - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Same Age - Exactly same age - Female - Formal - Female spk"
        },
        {
            "type": "instance",
            "language": "Urdu",
            "term_i": "میں",
            "term_you": "آپ (aap)",
            "label": "Urdu: میں/آپ (aap)",
            "id": "Instance_32b66d"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "tôi/mình",
            "term_you": "bạn",
            "label": "Vietnamese: tôi/mình/bạn",
            "id": "Instance_8f9fbd"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "tui",
            "term_you": "bạn",
            "label": "Vietnamese: tui/bạn",
            "id": "Instance_e74aaa"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "tao",
            "term_you": "mày",
            "label": "Vietnamese: tao/mày",
            "id": "Instance_be7aa3"
        },
        {
            "type": "schema_path",
            "id": "Younger - Younger (same gen) - Male - Neutral - Male spk"
        },
        {
            "type": "attribute",
            "category": "Broad Age",
            "id": "Age: Younger"
        },
        {
            "type": "attribute",
            "category": "Specific Gen",
            "id": "Gen: Younger (same gen)"
        },
        {
            "type": "schema_path",
            "id": "Younger - Younger (same gen) - Male - Neutral - Female spk"
        },
        {
            "type": "schema_path",
            "id": "Younger - Younger (same gen) - Female - Neutral - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Younger - Younger (same gen) - Female - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Mandarin",
            "term_i": "我 (wǒ)",
            "term_you": "你 / 小 + name (nǐ / xiǎo)",
            "label": "Mandarin: 我 (wǒ)/你 / 小 + name (nǐ / xiǎo)",
            "id": "Instance_78a5c4"
        },
        {
            "type": "instance",
            "language": "Cantonese",
            "term_i": "我 (ngo5)",
            "term_you": "細佬 (sai3 lou2)",
            "label": "Cantonese: 我 (ngo5)/細佬 (sai3 lou2)",
            "id": "Instance_7ac91f"
        },
        {
            "type": "instance",
            "language": "Cantonese",
            "term_i": "我 (ngo5)",
            "term_you": "細妹 (sai3 mui6)",
            "label": "Cantonese: 我 (ngo5)/細妹 (sai3 mui6)",
            "id": "Instance_aa951b"
        },
        {
            "type": "instance",
            "language": "Teochew",
            "term_i": "我 (guá)",
            "term_you": "细弟 (sè-tī)",
            "label": "Teochew: 我 (guá)/细弟 (sè-tī)",
            "id": "Instance_ae2ca5"
        },
        {
            "type": "instance",
            "language": "Teochew",
            "term_i": "我 (guá)",
            "term_you": "细妹 (sè-muē)",
            "label": "Teochew: 我 (guá)/细妹 (sè-muē)",
            "id": "Instance_3a9562"
        },
        {
            "type": "instance",
            "language": "Nepali",
            "term_i": "म (ma)",
            "term_you": "तँ (ta) / तिमी (timi)",
            "label": "Nepali: म (ma)/तँ (ta) / तिमी (timi)",
            "id": "Instance_c83a74"
        },
        {
            "type": "schema_path",
            "id": "Younger - Younger (same gen) - Male - Informal - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Younger - Younger (same gen) - Male - Informal - Female spk"
        },
        {
            "type": "schema_path",
            "id": "Younger - Younger (same gen) - Female - Informal - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Younger - Younger (same gen) - Female - Informal - Female spk"
        },
        {
            "type": "instance",
            "language": "Urdu",
            "term_i": "میں",
            "term_you": "تم (tum) or تو (tu)",
            "label": "Urdu: میں/تم (tum) or تو (tu)",
            "id": "Instance_373a7d"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "anh",
            "term_you": "em",
            "label": "Vietnamese: anh/em",
            "id": "Instance_35bc7a"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "chị",
            "term_you": "em",
            "label": "Vietnamese: chị/em",
            "id": "Instance_dc47a1"
        },
        {
            "type": "schema_path",
            "id": "Older - Older (same gen) - Male - Neutral - Male spk"
        },
        {
            "type": "attribute",
            "category": "Broad Age",
            "id": "Age: Older"
        },
        {
            "type": "attribute",
            "category": "Specific Gen",
            "id": "Gen: Older (same gen)"
        },
        {
            "type": "schema_path",
            "id": "Older - Older (same gen) - Male - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Mandarin",
            "term_i": "我 (wǒ)",
            "term_you": "哥哥 (gēge)",
            "label": "Mandarin: 我 (wǒ)/哥哥 (gēge)",
            "id": "Instance_05f3a8"
        },
        {
            "type": "schema_path",
            "id": "Older - Older (same gen) - Female - Neutral - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Older - Older (same gen) - Female - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Mandarin",
            "term_i": "我 (wǒ)",
            "term_you": "姐姐 (jiějie)",
            "label": "Mandarin: 我 (wǒ)/姐姐 (jiějie)",
            "id": "Instance_c6a5dd"
        },
        {
            "type": "instance",
            "language": "Cantonese",
            "term_i": "我 (ngo5)",
            "term_you": "哥哥 (go1 go1)",
            "label": "Cantonese: 我 (ngo5)/哥哥 (go1 go1)",
            "id": "Instance_a5e91a"
        },
        {
            "type": "instance",
            "language": "Cantonese",
            "term_i": "我 (ngo5)",
            "term_you": "姐姐 (ze2 ze2)",
            "label": "Cantonese: 我 (ngo5)/姐姐 (ze2 ze2)",
            "id": "Instance_49057b"
        },
        {
            "type": "instance",
            "language": "Teochew",
            "term_i": "我 (guá)",
            "term_you": "阿兄 (a-hiang)",
            "label": "Teochew: 我 (guá)/阿兄 (a-hiang)",
            "id": "Instance_416628"
        },
        {
            "type": "instance",
            "language": "Teochew",
            "term_i": "我 (guá)",
            "term_you": "阿姐 (a-jié)",
            "label": "Teochew: 我 (guá)/阿姐 (a-jié)",
            "id": "Instance_a0e633"
        },
        {
            "type": "instance",
            "language": "Nepali",
            "term_i": "म (ma)",
            "term_you": "तपाईं (tapai) and हजुर (Hajur)",
            "label": "Nepali: म (ma)/तपाईं (tapai) and हजुर (Hajur)",
            "id": "Instance_f2ab8e"
        },
        {
            "type": "instance",
            "language": "Urdu",
            "term_i": "میں",
            "term_you": "بھائی (bhai / bhaiya)",
            "label": "Urdu: میں/بھائی (bhai / bhaiya)",
            "id": "Instance_786ec9"
        },
        {
            "type": "instance",
            "language": "Urdu",
            "term_i": "میں",
            "term_you": "باجی (baji / apa)",
            "label": "Urdu: میں/باجی (baji / apa)",
            "id": "Instance_b39746"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "em",
            "term_you": "anh",
            "label": "Vietnamese: em/anh",
            "id": "Instance_79f159"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "em",
            "term_you": "chị",
            "label": "Vietnamese: em/chị",
            "id": "Instance_ae44ac"
        },
        {
            "type": "schema_path",
            "id": "Older - Parents' gen - Male - Neutral - Male spk"
        },
        {
            "type": "attribute",
            "category": "Specific Gen",
            "id": "Gen: Parents' gen"
        },
        {
            "type": "schema_path",
            "id": "Older - Parents' gen - Male - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Mandarin",
            "term_i": "我 (wǒ)",
            "term_you": "叔叔 (shūshu)",
            "label": "Mandarin: 我 (wǒ)/叔叔 (shūshu)",
            "id": "Instance_26cd37"
        },
        {
            "type": "schema_path",
            "id": "Older - Parents' gen - Female - Neutral - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Older - Parents' gen - Female - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Mandarin",
            "term_i": "我 (wǒ)",
            "term_you": "阿姨 (āyí)",
            "label": "Mandarin: 我 (wǒ)/阿姨 (āyí)",
            "id": "Instance_1bec79"
        },
        {
            "type": "instance",
            "language": "Cantonese",
            "term_i": "我 (ngo5)",
            "term_you": "叔叔 (suk1 suk1)",
            "label": "Cantonese: 我 (ngo5)/叔叔 (suk1 suk1)",
            "id": "Instance_ae5866"
        },
        {
            "type": "instance",
            "language": "Cantonese",
            "term_i": "我 (ngo5)",
            "term_you": "阿姨 (aa3 ji4)",
            "label": "Cantonese: 我 (ngo5)/阿姨 (aa3 ji4)",
            "id": "Instance_d50e74"
        },
        {
            "type": "instance",
            "language": "Teochew",
            "term_i": "我 (guá)",
            "term_you": "阿叔 (a-zik)",
            "label": "Teochew: 我 (guá)/阿叔 (a-zik)",
            "id": "Instance_9eb1a4"
        },
        {
            "type": "instance",
            "language": "Teochew",
            "term_i": "我 (guá)",
            "term_you": "阿姨 (a-î)",
            "label": "Teochew: 我 (guá)/阿姨 (a-î)",
            "id": "Instance_fc2eaa"
        },
        {
            "type": "instance",
            "language": "English",
            "term_i": "-",
            "term_you": "uncle",
            "label": "English: -/uncle",
            "id": "Instance_a16730"
        },
        {
            "type": "instance",
            "language": "English",
            "term_i": "-",
            "term_you": "aunty",
            "label": "English: -/aunty",
            "id": "Instance_20f320"
        },
        {
            "type": "instance",
            "language": "Nepali",
            "term_i": "म (ma)",
            "term_you": "तपाईं (tapai) and हजुर (Hajur)",
            "label": "Nepali: म (ma)/तपाईं (tapai) and हजुर (Hajur)",
            "id": "Instance_8b4154"
        },
        {
            "type": "instance",
            "language": "Urdu",
            "term_i": "میں",
            "term_you": "Uncle / چچا (chacha)",
            "label": "Urdu: میں/Uncle / چچا (chacha)",
            "id": "Instance_b27f72"
        },
        {
            "type": "instance",
            "language": "Urdu",
            "term_i": "میں",
            "term_you": "Aunty /خالہ (khala)",
            "label": "Urdu: میں/Aunty /خالہ (khala)",
            "id": "Instance_521a9c"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "con/cháu",
            "term_you": "chú/cậu",
            "label": "Vietnamese: con/cháu/chú/cậu",
            "id": "Instance_276130"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "con/cháu",
            "term_you": "cô/dì",
            "label": "Vietnamese: con/cháu/cô/dì",
            "id": "Instance_1eeb0e"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "con/cháu",
            "term_you": "bác",
            "label": "Vietnamese: con/cháu/bác",
            "id": "Instance_cdc15c"
        },
        {
            "type": "schema_path",
            "id": "Older - Grandparents' gen - Male - Neutral - Male spk"
        },
        {
            "type": "attribute",
            "category": "Specific Gen",
            "id": "Gen: Grandparents' gen"
        },
        {
            "type": "schema_path",
            "id": "Older - Grandparents' gen - Male - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Mandarin",
            "term_i": "我 (wǒ)",
            "term_you": "爷爷 (yéye)",
            "label": "Mandarin: 我 (wǒ)/爷爷 (yéye)",
            "id": "Instance_d0b7a1"
        },
        {
            "type": "schema_path",
            "id": "Older - Grandparents' gen - Female - Neutral - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Older - Grandparents' gen - Female - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Mandarin",
            "term_i": "我 (wǒ)",
            "term_you": "奶奶 (nǎinai)",
            "label": "Mandarin: 我 (wǒ)/奶奶 (nǎinai)",
            "id": "Instance_57790f"
        },
        {
            "type": "instance",
            "language": "Cantonese",
            "term_i": "我 (ngo5)",
            "term_you": "爺爺 (je4 je4)",
            "label": "Cantonese: 我 (ngo5)/爺爺 (je4 je4)",
            "id": "Instance_77e105"
        },
        {
            "type": "instance",
            "language": "Cantonese",
            "term_i": "我 (ngo5)",
            "term_you": "奶奶 (naai5 naai5)",
            "label": "Cantonese: 我 (ngo5)/奶奶 (naai5 naai5)",
            "id": "Instance_54b8f6"
        },
        {
            "type": "instance",
            "language": "Teochew",
            "term_i": "我 (guá)",
            "term_you": "阿公 (a-gong)",
            "label": "Teochew: 我 (guá)/阿公 (a-gong)",
            "id": "Instance_c16c30"
        },
        {
            "type": "instance",
            "language": "Teochew",
            "term_i": "我 (guá)",
            "term_you": "阿嬷 (a-má)",
            "label": "Teochew: 我 (guá)/阿嬷 (a-má)",
            "id": "Instance_b2b61a"
        },
        {
            "type": "instance",
            "language": "Urdu",
            "term_i": "میں",
            "term_you": "دادا جی (dada ji) / دادی جی (dadi ji) or نانا جی (nana ji) / نانی جی (nani ji)",
            "label": "Urdu: میں/دادا جی (dada ji) / دادی جی (dadi ji) or نانا جی (nana ji) / نانی جی (nani ji)",
            "id": "Instance_4a5581"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "con/cháu",
            "term_you": "ông",
            "label": "Vietnamese: con/cháu/ông",
            "id": "Instance_11a4fa"
        },
        {
            "type": "instance",
            "language": "Vietnamese",
            "term_i": "con/cháu",
            "term_you": "bà",
            "label": "Vietnamese: con/cháu/bà",
            "id": "Instance_48d213"
        },
        {
            "type": "schema_path",
            "id": "Older - Exactly same age - Male - Neutral - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Older - Exactly same age - Male - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Darija",
            "term_i": "ana",
            "term_you": "nta",
            "label": "Darija: ana/nta",
            "id": "Instance_823aa0"
        },
        {
            "type": "schema_path",
            "id": "Older - Exactly same age - Female - Neutral - Male spk"
        },
        {
            "type": "schema_path",
            "id": "Older - Exactly same age - Female - Neutral - Female spk"
        },
        {
            "type": "instance",
            "language": "Darija",
            "term_i": "ana",
            "term_you": "nti",
            "label": "Darija: ana/nti",
            "id": "Instance_d615e4"
        }
    ],
    "edges": [
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Instance_f84837"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Instance_6c6710"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Instance_5c824c"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Instance_54ba62"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Male spk",
            "target": "Instance_e74aaa"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Instance_f84837"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Instance_6c6710"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Instance_5c824c"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Instance_54ba62"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Neutral - Female spk",
            "target": "Instance_e74aaa"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Instance_f84837"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Instance_6c6710"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Instance_5c824c"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Instance_54ba62"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Male spk",
            "target": "Instance_e74aaa"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Instance_f84837"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Instance_6c6710"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Instance_5c824c"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Instance_54ba62"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Neutral - Female spk",
            "target": "Instance_e74aaa"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Male - Informal - Male spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Male - Informal - Male spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Male - Informal - Male spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Male - Informal - Male spk",
            "target": "Context: Informal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Male - Informal - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Informal - Male spk",
            "target": "Instance_727bd0"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Informal - Male spk",
            "target": "Instance_be7aa3"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Male - Informal - Female spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Male - Informal - Female spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Male - Informal - Female spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Male - Informal - Female spk",
            "target": "Context: Informal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Male - Informal - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Informal - Female spk",
            "target": "Instance_727bd0"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Informal - Female spk",
            "target": "Instance_be7aa3"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Female - Informal - Male spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Female - Informal - Male spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Female - Informal - Male spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Female - Informal - Male spk",
            "target": "Context: Informal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Female - Informal - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Informal - Male spk",
            "target": "Instance_727bd0"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Informal - Male spk",
            "target": "Instance_be7aa3"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Female - Informal - Female spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Female - Informal - Female spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Female - Informal - Female spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Female - Informal - Female spk",
            "target": "Context: Informal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Female - Informal - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Informal - Female spk",
            "target": "Instance_727bd0"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Informal - Female spk",
            "target": "Instance_be7aa3"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Male - Formal - Male spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Male - Formal - Male spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Male - Formal - Male spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Male - Formal - Male spk",
            "target": "Context: Formal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Male - Formal - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Formal - Male spk",
            "target": "Instance_32b66d"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Formal - Male spk",
            "target": "Instance_8f9fbd"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Male - Formal - Female spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Male - Formal - Female spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Male - Formal - Female spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Male - Formal - Female spk",
            "target": "Context: Formal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Male - Formal - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Formal - Female spk",
            "target": "Instance_32b66d"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Male - Formal - Female spk",
            "target": "Instance_8f9fbd"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Female - Formal - Male spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Female - Formal - Male spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Female - Formal - Male spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Female - Formal - Male spk",
            "target": "Context: Formal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Female - Formal - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Formal - Male spk",
            "target": "Instance_32b66d"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Formal - Male spk",
            "target": "Instance_8f9fbd"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Same Age - Exactly same age - Female - Formal - Female spk",
            "target": "Age: Same Age"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Same Age - Exactly same age - Female - Formal - Female spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Same Age - Exactly same age - Female - Formal - Female spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Same Age - Exactly same age - Female - Formal - Female spk",
            "target": "Context: Formal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Same Age - Exactly same age - Female - Formal - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Formal - Female spk",
            "target": "Instance_32b66d"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Same Age - Exactly same age - Female - Formal - Female spk",
            "target": "Instance_8f9fbd"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Age: Younger"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Gen: Younger (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Instance_78a5c4"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Instance_7ac91f"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Instance_ae2ca5"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Instance_c83a74"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Male spk",
            "target": "Instance_35bc7a"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Younger - Younger (same gen) - Male - Neutral - Female spk",
            "target": "Age: Younger"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Female spk",
            "target": "Gen: Younger (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Younger - Younger (same gen) - Male - Neutral - Female spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Younger - Younger (same gen) - Male - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Younger - Younger (same gen) - Male - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Female spk",
            "target": "Instance_78a5c4"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Female spk",
            "target": "Instance_7ac91f"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Female spk",
            "target": "Instance_ae2ca5"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Neutral - Female spk",
            "target": "Instance_c83a74"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Younger - Younger (same gen) - Female - Neutral - Male spk",
            "target": "Age: Younger"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Male spk",
            "target": "Gen: Younger (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Younger - Younger (same gen) - Female - Neutral - Male spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Younger - Younger (same gen) - Female - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Younger - Younger (same gen) - Female - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Male spk",
            "target": "Instance_78a5c4"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Male spk",
            "target": "Instance_aa951b"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Male spk",
            "target": "Instance_3a9562"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Male spk",
            "target": "Instance_c83a74"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Age: Younger"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Gen: Younger (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Instance_78a5c4"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Instance_aa951b"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Instance_3a9562"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Instance_c83a74"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Neutral - Female spk",
            "target": "Instance_dc47a1"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Younger - Younger (same gen) - Male - Informal - Male spk",
            "target": "Age: Younger"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Younger - Younger (same gen) - Male - Informal - Male spk",
            "target": "Gen: Younger (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Younger - Younger (same gen) - Male - Informal - Male spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Younger - Younger (same gen) - Male - Informal - Male spk",
            "target": "Context: Informal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Younger - Younger (same gen) - Male - Informal - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Informal - Male spk",
            "target": "Instance_373a7d"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Younger - Younger (same gen) - Male - Informal - Female spk",
            "target": "Age: Younger"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Younger - Younger (same gen) - Male - Informal - Female spk",
            "target": "Gen: Younger (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Younger - Younger (same gen) - Male - Informal - Female spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Younger - Younger (same gen) - Male - Informal - Female spk",
            "target": "Context: Informal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Younger - Younger (same gen) - Male - Informal - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Male - Informal - Female spk",
            "target": "Instance_373a7d"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Younger - Younger (same gen) - Female - Informal - Male spk",
            "target": "Age: Younger"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Younger - Younger (same gen) - Female - Informal - Male spk",
            "target": "Gen: Younger (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Younger - Younger (same gen) - Female - Informal - Male spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Younger - Younger (same gen) - Female - Informal - Male spk",
            "target": "Context: Informal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Younger - Younger (same gen) - Female - Informal - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Informal - Male spk",
            "target": "Instance_373a7d"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Younger - Younger (same gen) - Female - Informal - Female spk",
            "target": "Age: Younger"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Younger - Younger (same gen) - Female - Informal - Female spk",
            "target": "Gen: Younger (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Younger - Younger (same gen) - Female - Informal - Female spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Younger - Younger (same gen) - Female - Informal - Female spk",
            "target": "Context: Informal"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Younger - Younger (same gen) - Female - Informal - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Younger - Younger (same gen) - Female - Informal - Female spk",
            "target": "Instance_373a7d"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Gen: Older (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Instance_05f3a8"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Instance_a5e91a"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Instance_416628"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Instance_f2ab8e"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Instance_786ec9"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Male spk",
            "target": "Instance_79f159"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Gen: Older (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Instance_05f3a8"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Instance_a5e91a"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Instance_416628"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Instance_f2ab8e"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Instance_786ec9"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Male - Neutral - Female spk",
            "target": "Instance_79f159"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Gen: Older (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Instance_c6a5dd"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Instance_49057b"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Instance_a0e633"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Instance_f2ab8e"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Instance_b39746"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Male spk",
            "target": "Instance_ae44ac"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Gen: Older (same gen)"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Instance_c6a5dd"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Instance_49057b"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Instance_a0e633"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Instance_f2ab8e"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Instance_b39746"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Older (same gen) - Female - Neutral - Female spk",
            "target": "Instance_ae44ac"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Gen: Parents' gen"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Instance_26cd37"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Instance_ae5866"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Instance_9eb1a4"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Instance_a16730"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Instance_8b4154"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Instance_b27f72"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Instance_276130"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Male spk",
            "target": "Instance_cdc15c"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Gen: Parents' gen"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Instance_26cd37"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Instance_ae5866"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Instance_9eb1a4"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Instance_a16730"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Instance_8b4154"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Instance_b27f72"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Instance_276130"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Male - Neutral - Female spk",
            "target": "Instance_cdc15c"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Gen: Parents' gen"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Instance_1bec79"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Instance_d50e74"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Instance_fc2eaa"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Instance_20f320"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Instance_8b4154"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Instance_521a9c"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Instance_1eeb0e"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Male spk",
            "target": "Instance_cdc15c"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Gen: Parents' gen"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Instance_1bec79"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Instance_d50e74"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Instance_fc2eaa"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Instance_20f320"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Instance_8b4154"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Instance_521a9c"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Instance_1eeb0e"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Parents' gen - Female - Neutral - Female spk",
            "target": "Instance_cdc15c"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Gen: Grandparents' gen"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Instance_d0b7a1"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Instance_77e105"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Instance_c16c30"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Instance_4a5581"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Male spk",
            "target": "Instance_11a4fa"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Gen: Grandparents' gen"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Instance_d0b7a1"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Instance_77e105"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Instance_c16c30"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Instance_4a5581"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Male - Neutral - Female spk",
            "target": "Instance_11a4fa"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Gen: Grandparents' gen"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Instance_57790f"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Instance_54b8f6"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Instance_b2b61a"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Instance_4a5581"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Male spk",
            "target": "Instance_48d213"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Gen: Grandparents' gen"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Instance_57790f"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Instance_54b8f6"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Instance_b2b61a"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Instance_4a5581"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Grandparents' gen - Female - Neutral - Female spk",
            "target": "Instance_48d213"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Exactly same age - Male - Neutral - Male spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Exactly same age - Male - Neutral - Male spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Exactly same age - Male - Neutral - Male spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Exactly same age - Male - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Exactly same age - Male - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Exactly same age - Male - Neutral - Male spk",
            "target": "Instance_823aa0"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Exactly same age - Male - Neutral - Female spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Exactly same age - Male - Neutral - Female spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Exactly same age - Male - Neutral - Female spk",
            "target": "Target: Male"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Exactly same age - Male - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Exactly same age - Male - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Exactly same age - Male - Neutral - Female spk",
            "target": "Instance_823aa0"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Exactly same age - Female - Neutral - Male spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Exactly same age - Female - Neutral - Male spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Exactly same age - Female - Neutral - Male spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Exactly same age - Female - Neutral - Male spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Exactly same age - Female - Neutral - Male spk",
            "target": "Spk: Male spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Exactly same age - Female - Neutral - Male spk",
            "target": "Instance_d615e4"
        },
        {
            "type": "HAS_BROAD_AGE",
            "source": "Older - Exactly same age - Female - Neutral - Female spk",
            "target": "Age: Older"
        },
        {
            "type": "HAS_SPECIFIC_GEN",
            "source": "Older - Exactly same age - Female - Neutral - Female spk",
            "target": "Gen: Exactly same age"
        },
        {
            "type": "HAS_TARGET",
            "source": "Older - Exactly same age - Female - Neutral - Female spk",
            "target": "Target: Female"
        },
        {
            "type": "HAS_CONTEXT",
            "source": "Older - Exactly same age - Female - Neutral - Female spk",
            "target": "Context: Neutral"
        },
        {
            "type": "HAS_SPEAKER",
            "source": "Older - Exactly same age - Female - Neutral - Female spk",
            "target": "Spk: Female spk"
        },
        {
            "type": "HAS_PRONOUN",
            "source": "Older - Exactly same age - Female - Neutral - Female spk",
            "target": "Instance_d615e4"
        }
    ]
};