from agents import function_tool

@function_tool
def get_all_subjects():
    return "All subjects are: Islamiat, Logic, Arabic, Trigonometry, English"

@function_tool
def get_school_days():
    return "School days are: Monday, Tuesday, Wednesday, Thursday"

@function_tool
def get_all_parts_of_speech():
    return "Parts of speech are: Noun, Pronoun, Verb, Adjective, Adverb, Preposition, Conjunction, Interjection"
