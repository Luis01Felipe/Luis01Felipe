from bs4 import BeautifulSoup
from translate import Translator
import re

def translate_html(file_path, output_path, source_lang='en', target_lang='pt'):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)

    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Função para preservar emojis
    def translate_with_preserve_emojis(text):
        # Emojis são caracteres Unicode, então vamos preservá-los durante a tradução
        emojis = re.findall(r'[\U0001F600-\U0001F64F'   # Emoticons
                            r'\U0001F300-\U0001F5FF'   # Símbolos e pictogramas
                            r'\U0001F680-\U0001F6FF'   # Transporte e mapas
                            r'\U0001F700-\U0001F77F'   # Alquimia
                            r'\U0001F780-\U0001F7FF'   # Geometria
                            r'\U0001F800-\U0001F8FF'   # Símbolos adicionais
                            r'\U0001F900-\U0001F9FF'   # Emojis modificados
                            r'\U0001FA00-\U0001FA6F'   # Novos emojis
                            r'\U0001FA70-\U0001FAFF'   # Mais emojis
                            r'\U00002702-\U000027B0'   # Símbolos gráficos
                            r'\U0001F004-\U0001F0CF'   # Cartas de jogo
                            r'\U0000A9\U0000AE\U0000B1]', text)  # Emojis diversos
        text_without_emojis = re.sub(r'[\U0001F600-\U0001F64F'
                                     r'\U0001F300-\U0001F5FF'
                                     r'\U0001F680-\U0001F6FF'
                                     r'\U0001F700-\U0001F77F'
                                     r'\U0001F780-\U0001F7FF'
                                     r'\U0001F800-\U0001F8FF'
                                     r'\U0001F900-\U0001F9FF'
                                     r'\U0001FA00-\U0001FA6F'
                                     r'\U0001FA70-\U0001FAFF'
                                     r'\U00002702-\U000027B0'
                                     r'\U0001F004-\U0001F0CF'
                                     r'\U0000A9\U0000AE\U0000B1]', '', text)
        
        # Traduzir o texto sem os emojis
        translated_text = translator.translate(text_without_emojis.strip())

        # Restaurar os emojis na tradução
        for emoji in emojis:
            translated_text += emoji
        return translated_text

    # Traduzir texto, mantendo os emojis e HTML
    for tag in soup.find_all():
        if tag.name not in ['script', 'style']:
            if tag.string:  # Se a tag contém apenas texto
                translated_text = translate_with_preserve_emojis(tag.string.strip())
                tag.string.replace_with(translated_text)
            elif tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                # Ajustar para evitar texto todo maiúsculo
                translated_text = translate_with_preserve_emojis(tag.get_text().strip())
                tag.clear()
                tag.insert(0, translated_text)
            elif tag.name == 'p':
                # Traduzir mantendo o HTML interno
                for sub_content in tag.contents:
                    if isinstance(sub_content, str):
                        translated_text = translate_with_preserve_emojis(sub_content.strip())
                        tag.contents[tag.contents.index(sub_content)] = translated_text

    # Salvar o resultado traduzido
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(str(soup))

# Configurar os caminhos de entrada e saída
input_file = 'README.md'
output_file = 'README_ptbr.md'
translate_html(input_file, output_file)
