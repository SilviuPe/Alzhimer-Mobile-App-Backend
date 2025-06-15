from googletrans import Translator


def translate_text_live(query : str,src : str,dest : str) -> dict:

    translator_engine = Translator()

    translated_text = translator_engine.translate(query, src=src, dest=dest)
    print(translated_text)
    return {
        'message' : translated_text.text
    }