class LinkNode(object):

    def __init__(self, key, val, prev_node=None, next_node=None):
        self.key = key
        self.val = val
        self.prev = prev_node
        self.next = next_node


class DoubleLinkList(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

        self.head = None
        self.tail = None

    def append(self, node):
        """

        :param node:
        :return:

        append a node to the double link list last
        """
        if self.size == self.capacity:
            raise ValueError("The double link list has been full.")

        self.size += 1

        if self.head is None:
            self.head = self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def delete(self, node):
        """

        :param node:
        :return node:

        delete a node in double link list. switch(node):
           1.node == self.head
           2.node == self.tail
           3.node in the double link list middle
        """
        if self.size == 0:
            raise ValueError("can not delete empty double link list")

        self.size -= 1

        if node == self.head:
            if node.next:
                node.next.prev = None

            self.head = node.next
        elif node == self.tail:
            if node.prev:
                node.prev.next = None

            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        return node


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_look_up = {}
        self.cache_list = DoubleLinkList(capacity)

    def get(self, key):
        if key not in self.cache_look_up:
            return -1

        node = self.cache_look_up[key]
        self.cache_list.delete(node)
        self.cache_list.append(node)

        return node.val

    def put(self, key, value):
        if key in self.cache_look_up:
            node = self.cache_look_up[key]
            node.val = value
            self.cache_list.delete(node)
            self.cache_list.append(node)
        else:
            if self.capacity == self.cache_list.size:
                head_node = self.cache_list.delete(self.cache_list.head)
                del self.cache_look_up[head_node.key]

            new_node = LinkNode(key, value)
            self.cache_look_up[key] = new_node
            self.cache_list.append(new_node)