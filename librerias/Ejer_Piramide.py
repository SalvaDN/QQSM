import os
import shutil

path = r"C:/Users/EMCO-/Desktop/CURSO BÁSICO EN CIBEROPERACIONES - OPERADOR DE INVESTIGACIÓN DIGITAL (IOD)/Automatización de Tareas mediante Python/PythonProject/librerias"
os.mkdir(path + '/piramide')

base = 10


with open(path + '\\piramide\\piramide.txt', 'w') as f:
    for piramide in range (1, base +1):
        espacios = ' ' * (base - piramide)
        asteriscos = '*' * (2* piramide -1)

        piram_ok = (espacios + asteriscos + '\n')

        f.write(piram_ok)






