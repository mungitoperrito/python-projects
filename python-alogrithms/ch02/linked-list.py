class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

linked_list = Node("a", Node("b", Node("c", Node("d"))))

print(linked_list.next.next.value)

