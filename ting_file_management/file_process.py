from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    path_file_names = [instance.search(index)['nome_do_arquivo']
                       for index in range(len(instance))]

    if path_file not in path_file_names:
        data = txt_importer(path_file)
        dict_data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(data),
            'linhas_do_arquivo': data,
        }

        instance.enqueue(dict_data)
        print(dict_data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
