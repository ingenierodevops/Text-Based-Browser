import sys
import os
from collections import deque

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def save_page(pagina, path, comando):
    nombre = comando.split(".")[0]
    with open(os.path.join(path,nombre), 'w') as fichero:
        fichero.write(pagina)
        fichero.close()

def print_file(file_name):
    with open(file_name, 'r') as fichero:
        print(fichero.read())
        fichero.close()
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
            print(bloomberg_com)
            historial_stack.append(bloomberg_com)
            save_page(bloomberg_com, full_path, comando)
        elif comando == "nytimes.com":
            print(nytimes_com)
            historial_stack.append(nytimes_com)
            save_page(nytimes_com, full_path, comando)
        else:
            print("Error: Please insert a correct URL")
    elif comando == "back":
        if len(historial_stack) != 0:
            if comando_anterior != "back":
                historial_stack.pop()  # current page not showed in back
            print(historial_stack.pop())
    else:
        print("Error: Incorrect URL")
    comando_anterior = comando
    comando = input()
