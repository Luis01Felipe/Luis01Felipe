import googletrans
from googletrans import Translator
import re

# Instanciar o tradutor
translator = Translator()

def traduzir_html(html):
    # Traduzir apenas o texto, ignorando as tags HTML
    def traduzir_texto(match):
        # Pega o texto dentro da tag ou entre as tags de <p>, <h1>, etc.
        texto = match.group(1)
        # Traduz o texto e mantém o emoji
        texto_traduzido = translator.translate(texto, src='en', dest='pt').text
        return f"{texto_traduzido}"

    # Expressão regular para encontrar o texto dentro das tags HTML (tags como <h1>, <p>, <h2>, etc.)
    html_traduzido = re.sub(r'>([^<]+)<', traduzir_texto, html)
    
    return html_traduzido

# Exemplo de HTML
html = """
<h3>📖 Alterar Linguagem Natural</h3>
<a href="https://github.com/Luis01Felipe/Luis01Felipe/blob/main/README_ptbr.md" target="_blank">
<img alt="Brazilian Portuguese (PT-BR)" src="https://img.shields.io/badge/Brazilian_Portuguese-%237289DA.svg?logo=portuguese&amp;logoColor=white"/>
</a>
<a href="https://github.com/Luis01Felipe/Luis01Felipe/blob/main/README.md" target="_blank">
<img alt="English (US)" src="https://img.shields.io/badge/English-%2300A400.svg?logo=english&amp;logoColor=white"/>
</a>
<h1>Olá, sou Luis Felipe</h1>
<div>
<h2>Sobre mim</h2>
<p> 
        I am a developer passionate about technology, currently studying Computer Science at Universidade Paulista (UNIP), where I am also the class representative. I am currently deepening my knowledge in Artificial Intelligence, backend systems development, Data Science, and data manipulation with MySQL databases. 
        <br/><br/> 
        Throughout my academic and professional journey, I have developed projects that integrate facial recognition, data analysis, and access control, applying machine learning techniques. Additionally, I share my passion for AI by teaching workshops and creating educational materials to help others explore the potential of this amazing field. 
        <br/><br/> 
        My goal is to build efficient and scalable solutions, always focusing on user experience and technological innovation. When I am not programming, I am exploring games, anime, movies, or simply learning something new to stay ahead. 
    </p>
<h2>O QUE VENHA</h2>
<p>Atualmente, estou focado nas demandas da universidade e à procura de um estágio. Apesar de não ter projetos pessoais em andamento, estou envolvido em projetos colaborativos com organizações, onde posso aplicar e ampliar meus conhecimentos.</p>
</div>
"""

# Traduzir o HTML
html_traduzido = traduzir_html(html)

# Exibir o resultado
print(html_traduzido)
