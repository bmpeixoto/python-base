"""
Hello World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    expor LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Bruno Maruca"
__license__ = "Unlicense"


import os

current_language = "en_US"


msg = " Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao. Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"

print(msg)


preco = 10
quantidade = 5
total = preco * quantidade
print(f"O total da sua compra é {total}")
