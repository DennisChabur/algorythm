class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append_(self, volume):
        end = Node(volume)
        pointer = self
        while pointer.next:
            pointer = pointer.next
        pointer.next = end

    def reverse_list(self, head, tail=None):
        while head:
            head.next, tail, head = tail, head, head.next
        return tail




