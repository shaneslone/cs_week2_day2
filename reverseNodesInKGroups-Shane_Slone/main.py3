# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    def reverseSegment(head):
        cur = head
        for _ in range(k):
            if cur is None:
                return [head, None, None]
            cur = cur.next
        prev = None
        cur = head
        tail = head
        i = 0
        for _ in range(k): 
            if cur is None:
                return [head, tail, None]
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return [prev, tail, cur]
    head, tail, next_segment = reverseSegment(l)
    next_head = None
    while next_segment is not None:
        next_head, next_tail, next_segment = reverseSegment(next_segment)
        tail.next = next_head
        tail = next_tail     
    return head
    
    
        

