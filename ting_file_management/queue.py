from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def enqueue(self, value):
        self._list.append(value)

    def dequeue(self):
        if len(self._list) == 0:
            return None
        return self._list.pop(0)

    def search(self, index):
        if 0 <= index < len(self._list):
            return self._list[index]
        raise IndexError

    def __str__(self):
        str_items = ""
        for i in range(len(self._list)):
            value = self._list[i]
            str_items += str(value)
            if i + 1 < len(self._list):
                str_items += ", "
        return "Queue(" + str_items + ")"
