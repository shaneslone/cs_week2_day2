# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):
    new_node = ListNode(value)
    if l is None:
        l = new_node
        return l
    if value < l.value:
        new_node.next = l
        l = new_node
        return l
    prev = l
    cur = l
    while cur is not None:
        if cur.value > value:
            new_node.next = cur
            prev.next = new_node
            return l
        else:
            if cur.next is None:
                new_node.next = None
                cur.next = new_node
                return l
            else:
                prev = cur
                cur = cur.next

