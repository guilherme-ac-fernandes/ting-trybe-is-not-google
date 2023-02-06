from ting_file_management.priority_queue import PriorityQueue
import pytest

mock_files_data = [
    {
        'nome_do_arquivo': 'file_with_ten_elements.txt',
        'qtd_linhas': 10,
        'linhas_do_arquivo': [*range(1, 11, 1)],
    },
    {
        'nome_do_arquivo': 'file_with_two_elements.txt',
        'qtd_linhas': 2,
        'linhas_do_arquivo': [*range(1, 3, 1)],
    },
    {
        'nome_do_arquivo': 'file_with_four_elements.txt',
        'qtd_linhas': 4,
        'linhas_do_arquivo': [*range(1, 5, 1)],
    },
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    assert len(priority_queue) == 0

    for file_data in mock_files_data:
        priority_queue.enqueue(file_data)

    assert len(priority_queue) == len(mock_files_data)

    assert priority_queue.search(0) == mock_files_data[1]
    assert priority_queue.search(1) == mock_files_data[2]
    assert priority_queue.search(2) == mock_files_data[0]
    assert priority_queue.dequeue() == mock_files_data[1]

    with pytest.raises(IndexError):
        priority_queue.search(999)
