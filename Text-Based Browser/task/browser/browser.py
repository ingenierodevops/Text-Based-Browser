import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup


nytimes_com = ""
bloomberg_com = ""


def save_page(pagina, path, comando):
    puntos = comando.count('.')
    nombre = comando.split(".")[puntos - 1]
    with open(os.path.join(path,nombre), 'w') as fichero:
        fichero.write(pagina)
        fichero.close()

def print_file(file_name):
    with open(file_name, 'r') as fichero:
        print(fichero.read())
        fichero.close()

def pedir_pagina(pagina):
    if "http" not in pagina:
        pagina = "https://" + pagina
    r = requests.get(pagina)
    soup = BeautifulSoup(r.content, 'html.parser')
    #pagina = soup.find_all()
    cadena = ""
    #for lines in pagina:
    #    if lines.name == 'h1' or lines.name == 'h2' or lines.name == 'h3' or lines.name == 'h4' or lines.name == 'h5' or lines.name == 'h6' or lines.name == 'p' or lines.name == 'a' or lines.name == 'ul' or lines.name == 'ol' or lines.name == 'li':
    #        cadena = cadena + lines.text

    pagina = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "p", "a", "ul", "ol", "li"])
    for lines in pagina:
        cadena = cadena + lines.text
    #cadena = soup.get_text()
    print(cadena)
    return cadena


# write your code here

args = sys.argv
carpeta = args[1]
if not os.access(carpeta,os.F_OK):
    os.mkdir(carpeta)
    if not os.access(carpeta, os.F_OK):
        print("error al crear la carpeta")
else:
    # print("la carpeta existe la limpiamos")
    for file in os.listdir(carpeta):
        if os.path.isfile(file):
            os.remove(file)
# os.chdir(carpeta)
# print(os.getcwd())

full_path = os.path.join(os.getcwd(), carpeta)
# print(full_path)

historial_stack = deque()

comando = ""
comando = input()
current = ""
comando_anterior = "none"
while comando != "exit":
    if comando == "bloomberg":
        print_file(os.path.join(full_path, comando))
        historial_stack.append(bloomberg_com)
    elif comando == "nytimes":
        print_file(os.path.join(full_path, comando))
        historial_stack.append(nytimes_com)
    elif "." in comando:
        if comando == 'bloomberg.com':
            bloomberg_com = pedir_pagina(comando)
            historial_stack.append(bloomberg_com)
            save_page(bloomberg_com, full_path, comando)
        elif comando == "nytimes.com":
            nytimes_com = pedir_pagina(comando)
            historial_stack.append(nytimes_com)
            save_page(nytimes_com, full_path, comando)
        else:
            texto_pagina = pedir_pagina(comando)
            historial_stack.append(texto_pagina)
            save_page(texto_pagina, full_path, comando)
            # print("Error: Please insert a correct URL")
    elif comando == "back":
        if len(historial_stack) != 0:
            if comando_anterior != "back":
                historial_stack.pop()  # current page not showed in back
            print(historial_stack.pop())
    else:
        print("Error: Incorrect URL")
    comando_anterior = comando
    comando = input()
