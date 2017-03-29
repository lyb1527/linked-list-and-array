'''
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together the nodes of the two
lists and sorted in ascending order.

Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
'''
def mergeTwoLists(self, l1, l2):
    dummy = ListNode(0)
    tmp = dummy
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    if l1 != None:
        tmp.next = l1
    else:
        tmp.next = l2
    return dummy.next
