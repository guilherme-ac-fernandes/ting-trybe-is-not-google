from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    path_files = [instance.search(index)['nome_do_arquivo']
                  for index in range(len(instance))]

    if path_file not in path_files:
        data = txt_importer(path_file)
        dict_data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(data),
            'linhas_do_arquivo': data,
        }

        instance.enqueue(dict_data)
        print(dict_data, file=sys.stdout)


def remove(instance: Queue):
    try:
        dict_removed = instance.dequeue()
    except IndexError:
        print('Não há elementos', file=sys.stdout)
    else:
        path_file = dict_removed['nome_do_arquivo']
        print(f'Arquivo {path_file} removido com sucesso', file=sys.stdout)


def file_metadata(instance: Queue, position):
    try:
        dict_search = instance.search(position)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
    else:
        print(dict_search, file=sys.stdout)
