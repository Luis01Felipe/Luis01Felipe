import os
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

def sync_readme():
    readme_original = "README.md"
    readme_translated = "README_ptbr.md"

    if not os.path.exists(readme_original):
        print(f"Arquivo {readme_original} não encontrado!")
        return

    # Lê o conteúdo do README.md
    with open(readme_original, "r", encoding="utf-8") as f:
        content = f.read()

    # Tradução
    translated_content = translate_to_portuguese(content)

    # Salva o conteúdo traduzido em README_ptbr.md
    with open(readme_translated, "w", encoding="utf-8") as f:
        f.write(translated_content)

    print(f"Sincronização concluída! Tradução salva em {readme_translated}")

if __name__ == "__main__":
    sync_readme()
