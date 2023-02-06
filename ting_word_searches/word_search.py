from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    word_search = []
    for file_index in range(len(instance)):
        file_data = instance.search(file_index)
        lines_search = []
        for position, line in enumerate(file_data['linhas_do_arquivo']):
            if word.casefold() in line.casefold():
                lines_search.append({
                    "linha": position + 1,
                })
        if len(lines_search) > 0:
            word_search.append({
                "palavra": word,
                "arquivo": file_data['nome_do_arquivo'],
                "ocorrencias": lines_search
            })
    return word_search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
