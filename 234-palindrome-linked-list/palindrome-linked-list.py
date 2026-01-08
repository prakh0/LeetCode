# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check_list = []
        while head:
            check_list.append(head.val)
            head = head.next
        lo,hi = 0, len(check_list)-1
        while lo < hi:
            if check_list[lo] != check_list[hi]:
                return False
            lo += 1
            hi -= 1
        return True