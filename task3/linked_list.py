
class Node:
    def __init__(self, prev_node=None, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return f"Node({self.data})"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        if self.length == 0:
            node = Node(None, data, None)
            self.head = node
            self.tail = node
        else:
            node = Node(self.tail, data, None)
            self.tail.next_node = node
            self.tail = node
        self.length += 1

    def insert(self, data, index):
        index = self._translate_index(index)

        if index == self.length:
            self.append(data)
            return
        elif index == 0:
            if self.length == 0:
                self.append(data)
            else:
                node = Node(None, data, self.head)
                self.head.prev_node = node
                self.head = node
            self.length += 1
            return

        prev_node = self._get_node(index - 1)
        node = Node(prev_node, data, prev_node.next_node)
        prev_node.next_node.prev_node = node
        prev_node.next_node = node
        self.length += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next_node

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        index = self._translate_index(index)
        return self._get_node(index).data

    def __setitem__(self, index, data):
        index = self._translate_index(index)
        self._get_node(index).data = data

    def __delitem__(self, index):
        index = self._translate_index(index)
        node = self._get_node(index)
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.head = node.next_node
        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.tail = node.prev_node
        self.length -= 1

    def _translate_index(self, index):
        if index < -self.length or index >= self.length:
            raise IndexError("Index out of range")
        if index < 0:
            index += self.length
        return index

    def _get_node(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next_node
        return current
