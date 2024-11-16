import os
from bs4 import BeautifulSoup
from googletrans import Translator, LANGUAGES
import logging

logging.basicConfig(level=logging.ERROR)


def translate_html(file_path, output_path, source_lang='en', target_lang='pt'):
    translator = Translator()

    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Traduzir texto dentro das tags <h1> a <h6> e <p>, mantendo os emojis e HTML
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        try:
            if tag.string:  # Se o tag contém apenas texto
                translated_text = translator.translate(tag.string.strip(), src=source_lang, dest=target_lang).text
                if translated_text:
                    tag.string.replace_with(translated_text)
            else:
                # Traduzir mantendo o HTML interno
                for sub_content in tag.contents:
                    if isinstance(sub_content, str):
                        translated_text = translator.translate(sub_content.strip(), src=source_lang,
                                                               dest=target_lang).text
                        if translated_text:
                            tag.contents[tag.contents.index(sub_content)] = translated_text
        except Exception as e:
            logging.error(f"Error translating tag: {tag}, error: {e}")

    # Salvar o resultado traduzido
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(str(soup))


# Configurar os caminhos de entrada e saída
input_file = 'README.md'
translations_dir = 'translations'

# Iterar sobre os arquivos na pasta Translations
for filename in os.listdir(translations_dir):
    if filename.startswith('README_') and filename.endswith('.md'):
        target_lang = filename.split('_')[1].split('.')[0]
        if target_lang in LANGUAGES:
            output_file = os.path.join(translations_dir, filename)
            translate_html(input_file, output_file, target_lang=target_lang)
        else:
            logging.error(f"Invalid target language: {target_lang} in file: {filename}")
