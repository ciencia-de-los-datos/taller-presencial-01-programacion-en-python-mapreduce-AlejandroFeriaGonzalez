import os

def load_input(input_directory) -> list[tuple[str, str]]:
    lista = []
    for d in os.listdir(input_directory):
        with open(os.path.join(input_directory, d), "r") as archivo:
            for linea in archivo:
                lista.append((d, linea))
    return lista