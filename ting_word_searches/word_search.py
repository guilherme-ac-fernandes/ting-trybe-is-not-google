from ting_file_management.queue import Queue


def generate_word_report(word, file_name, occurrences):
    return {
        "palavra": word,
        "arquivo": file_name,
        "ocorrencias": occurrences
    }


def create_word_report(word, file_data, content=False):
    lines_search = []
    for position, line in enumerate(file_data['linhas_do_arquivo']):
        if word.casefold() in line.casefold():
            lines_report = {
                "linha": position + 1,
            }

            if content:
                lines_report["conteudo"] = line

            lines_search.append(lines_report)

    return lines_search


def exists_word(word, instance: Queue):
    word_search = []
    for file_index in range(len(instance)):
        file_data = instance.search(file_index)
        lines_search = create_word_report(word, file_data)

        if len(lines_search) > 0:
            file_name = file_data['nome_do_arquivo']
            report = generate_word_report(word, file_name, lines_search)
            word_search.append(report)

    return word_search


def search_by_word(word, instance: Queue):
    word_search = []
    for file_index in range(len(instance)):
        file_data = instance.search(file_index)
        lines_search = []
        lines_search = create_word_report(word, file_data, True)

        if len(lines_search) > 0:
            file_name = file_data['nome_do_arquivo']
            report = generate_word_report(word, file_name, lines_search)
            word_search.append(report)

    return word_search
