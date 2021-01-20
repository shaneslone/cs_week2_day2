# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    merged_head = None
    if l1 is None and l2 is None:
        return None
    elif l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.value < l2.value:
        merged_head = l1
        l1 = l1.next
    else:
        merged_head = l2
        l2 = l2.next
    prev = merged_head
    while l1 or l2 is not None:
        if l1 is None:
            prev.next = l2
            prev = prev.next
            l2 = l2.next
        elif l2 is None:
            prev.next = l1
            prev = prev.next
            l1 = l1.next
        elif l1.value < l2.value:
            prev.next = l1
            prev = prev.next
            l1 = l1.next
        else:
            prev.next = l2
            prev = prev.next
            l2 = l2.next
             
    return merged_head
    
    
    
        
        

