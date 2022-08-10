class QueueException(Exception):
    """Дек переполнен или пуст."""
    pass


class DoubleEndedQueue:
    '''Очередь.'''
    def __init__(self, m):
        self._queue = [None] * m
        self._max_n = m
        # Голова очереди
        self._head = 0
        # Хвост очереди
        self._tail = 0
        # Размер очереди
        self._size = 0

    def _is_empty(self):
        '''Очередь пуста.'''
        return self._size == 0

    def _calc_index(self, cursor, flag=True):
        '''Метод для вычисления индекса.'''
        if flag:
            cursor = cursor + 1
        else:
            cursor = cursor - 1
        return cursor % self._max_n

    def push_front(self, value):
        '''Добавить элемент в начало дека.'''
        # Если очередь заполнена - значение добавлено не будет
        if self._size != self._max_n:
            self._queue[self._tail] = value
            self._tail = self._calc_index(self._tail)
            self._size += 1
        else:
            raise QueueException()

    def pop_back(self):
        '''Вывести последний элемент дека и удалить его.'''
        if self._is_empty():
            raise QueueException()
        elem = self._queue[self._head]
        self._queue[self._head] = None
        self._head = self._calc_index(self._head)
        self._size -= 1
        return elem

    def push_back(self, value):
        '''Добавить элемент в конец дека.'''
        # Если очередь заполнена - значение добавлено не будет
        if self._size != self._max_n:
            # Если очередь пуста,
            # то добавление элемента в конец деки
            # происходит начиная с головы
            if self._size == 0:
                self._queue[self._tail] = value
                self._tail = self._calc_index(self._tail)
            else:
                self._head = self._calc_index(self._head, False)
                self._queue[self._head] = value
            self._size += 1
        else:
            raise QueueException()

    def pop_front(self):
        '''Вывести первый элемент дека и удалить его.'''
        if self._is_empty():
            raise QueueException()
        self._tail = self._calc_index(self._tail, False)
        elem = self._queue[self._tail]
        self._queue[self._tail] = None
        self._size -= 1
        return elem

if __name__ == '__main__':
    # Количество команд
    n = int(input())
    # Максимальный размер дека
    m = int(input())
    # Инициализация очереди
    q = DoubleEndedQueue(m)
    # парсинг команд
    for inpt in range(n):
        text = str(input()).split(" ")
        operation = {
            'push_front': q.push_front,
            'push_back': q.push_back,
            'pop_front': q.pop_front,
            'pop_back': q.pop_back,
        }
        try:
            if len(text) > 1:
                operation[text[0]](int(text[1]))
            else:
                print(operation[text[0]]())
        except QueueException:
            print('error')
