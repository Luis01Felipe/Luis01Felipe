from bs4 import BeautifulSoup
from translate import Translator

def translate_html(file_path, output_path, source_lang='en', target_lang='pt'):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)

    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Traduzir texto, mantendo os emojis e HTML
    for tag in soup.find_all():
        if tag.name not in ['script', 'style']:
            if tag.string:  # Se o tag contém apenas texto
                translated_text = translator.translate(tag.string.strip())
                tag.string.replace_with(translated_text)
            elif tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                # Ajustar para evitar texto todo maiúsculo
                translated_text = translator.translate(tag.get_text().strip()).title()
                tag.clear()
                tag.insert(0, translated_text)
            elif tag.name == 'p':
                # Traduzir mantendo o HTML interno
                for sub_content in tag.contents:
                    if isinstance(sub_content, str):
                        translated_text = translator.translate(sub_content.strip())
                        tag.contents[tag.contents.index(sub_content)] = translated_text

    # Salvar o resultado traduzido
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(str(soup))

# Configurar os caminhos de entrada e saída
input_file = 'README.md'
output_file = 'README_ptbr.md'
translate_html(input_file, output_file)
