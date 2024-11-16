import os
import re
from translate import Translator

def translate_to_portuguese(content):
    """Traduz o conteúdo do inglês para português."""
    translator = Translator(to_lang="pt")
    try:
        translated = translator.translate(content)
        return translated
    except Exception as e:
        print(f"Erro ao traduzir: {e}")
        return content  # Retorna o conteúdo original se houver erro.

def translate_tags(content):
    """
    Traduz apenas o texto dentro das tags <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, <p>.
    """
    def translate_match(match):
        tag_open = match.group(1)
        inner_text = match.group(2)
        tag_close = match.group(3)

        # Traduz apenas o conteúdo interno da tag
        translated_text = translate_to_portuguese(inner_text)
        return f"{tag_open}{translated_text}{tag_close}"

    # Expressão regular para capturar as tags e seu conteúdo
    tag_pattern = r"(<(h[1-6]|p)[^>]*>)(.*?)(</\2>)"
    translated_content = re.sub(tag_pattern, translate_match, content, flags=re.DOTALL)
    return translated_content

def sync_readme():
    readme_original = "README.md"
    readme_translated = "README_ptbr.md"

    if not os.path.exists(readme_original):
        print(f"Arquivo {readme_original} não encontrado!")
        return

    # Lê o conteúdo do README.md
    with open(readme_original, "r", encoding="utf-8") as f:
        content = f.read()

    # Tradução apenas das tags especificadas
    translated_content = translate_tags(content)

    # Salva o conteúdo traduzido em README_ptbr.md
    with open(readme_translated, "w", encoding="utf-8") as f:
        f.write(translated_content)

    print(f"Sincronização concluída! Tradução salva em {readme_translated}")

if __name__ == "__main__":
    sync_readme()
