import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            return print('Formato inválido', file=sys.stderr)

        with open(path_file, mode='r') as file:
            file_created = [string.replace('\n', '') for string in file]

    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)

    else:
        return file_created
