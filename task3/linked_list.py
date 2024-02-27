class Node:
    def __init__(self, prev=None, data=None, nxt=None):
        self.data = data
        self.nxt = nxt
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        super().__init__()
        self.head: Node = None
        self.tail: Node = None
        self.length = 0

    def append(self, data):
        if len(self) == 0:
            node = Node(None, data, None)
            self.head = node
            self.tail = node
            self.length += 1
            return

        node = Node(self.tail, data, None)
        self.tail.nxt = node
        self.tail = node
        self.length += 1

    def insert(self, data, index):
        index = self.translate_index(index)

        if index == self.length: 
            self.append(data)
            return

        if index == 0:  
            if len(self) == 0:
                self.append(data)
                return

            node = Node(None, data, self.head)
            self.head.prev = node
            self.head = node
            self.length += 1
            return

        prev = self.get_node(index - 1)
        node = Node(prev, data, prev.nxt)
        prev.nxt.prev = node
        prev.nxt = node
        self.length += 1

    def __iter__(self):
        data_list = [self.head.data]
        last = self.head
        for _ in range(len(self) - 1):
            data_list.append(last.nxt.data)
            last = last.nxt

        return iter(data_list)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return list(self)[index]

    def __setitem__(self, index, data):
        index = self.translate_index(index)
        self.get_node(index).data = data

    def __delitem__(self, index):
        index = self.translate_index(index)
        node = self.get_node(index)

        prev = node.prev
        node.prev.nxt = node.nxt
        node.nxt.prev = prev
        self.length -= 1

    def translate_index(self, index):
        if index > self.length or index < -len(self):
            raise IndexError

        if index < 0:
            index += len(self)

        return index

    def get_node(self, index) -> Node:
        last = self.head
        if index == 0:
            return last

        for i in range(len(self) - 1):
            if i == index - 1:
                return last.nxt
            last = last.nxt

        raise IndexError