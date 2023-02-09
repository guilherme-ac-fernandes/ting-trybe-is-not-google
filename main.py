from ting_file_management.queue import Queue
from ting_file_management.file_process import process
from ting_file_management.file_process import remove
from ting_file_management.file_process import file_metadata
from ting_word_searches.word_search import exists_word
from ting_word_searches.word_search import search_by_word


if __name__ == "__main__":
    queue = Queue()
    process('statics/arquivo_teste.txt', queue)
    process('statics/nome_pedro.txt', queue)

    print('--> Primeiro Elemento da Fila:', queue.search(0))
    print('--> Segundo Elemento da Fila:', queue.search(1))

    file_metadata(queue, 0)  # Retorna o Primeiro Elemento
    file_metadata(queue, 1)  # Retorna o Segundo Elemento
    file_metadata(queue, 99)  # Retorna "Posição inválida"

    print(exists_word('adoção', queue))
    print(search_by_word('adoção', queue))

    remove(queue)  # Arquivo statics/arquivo_teste.txt removido com sucesso
    remove(queue)  # Arquivo statics/nome_pedro.txt removido com sucesso
    file_metadata(queue, 0)  # Retorna "Posição inválida"
