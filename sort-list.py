'''
Sort a linked list in O(n log n) time using constant space complexity.

Have you met this question in a real interview? Yes
Example
Given 1->3->2->null, sort it to 1->2->3->null.
'''

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        ans = []
        tmp = head
        while tmp != None:
            ans.append(tmp.val)
            tmp = tmp.next

        ans.sort()
        tmp = head
        for i in ans:
            tmp.val = i
            tmp = tmp.next
        return head
