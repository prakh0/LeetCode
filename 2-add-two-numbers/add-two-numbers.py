# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(num1,num2,carry):
            if not num1 and not num2 and carry == 0:
                return None
            val1 = num1.val if num1 else 0
            val2 = num2.val if num2 else 0

            total = val1 + val2 + carry
            new_carry = total // 10
            node = ListNode(total % 10)

            node.next = helper(
                num1.next if num1 else None,
                num2.next if num2 else None,
                new_carry
            )
            return node
        return helper(l1,l2,0)