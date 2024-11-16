import os
from bs4 import BeautifulSoup
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


def translate_html_tags(content):
    """Traduza apenas o conteúdo de tags específicas dentro de um arquivo HTML."""
    soup = BeautifulSoup(content, "html.parser")
    tags_to_translate = ["h1", "h2", "h3", "h4", "h5", "h6", "p"]

    for tag in soup.find_all(tags_to_translate):
        if tag.string:  # Verifica se há texto simples na tag
            translated_text = translate_to_portuguese(tag.string)
            tag.string.replace_with(translated_text)

    return str(soup)


def sync_readme():
    readme_original = "README.md"
    readme_translated = "README_ptbr.md"

    if not os.path.exists(readme_original):
        print(f"Arquivo {readme_original} não encontrado!")
        return

    # Lê o conteúdo do README.md
    with open(readme_original, "r", encoding="utf-8") as f:
        content = f.read()

    # Copia todo o conteúdo e traduz apenas as tags especificadas
    translated_content = translate_html_tags(content)

    # Salva o conteúdo traduzido em README_ptbr.md
    with open(readme_translated, "w", encoding="utf-8") as f:
        f.write(translated_content)

    print(f"Sincronização concluída! Tradução salva em {readme_translated}")


if __name__ == "__main__":
    sync_readme()
