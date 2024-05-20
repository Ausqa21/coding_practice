"""
def x(l1,l2):
    output1 = []
    output2 = []
    result = 0

    while True:
        output1.append(l1.val)
        if not l1.next:
            break
        l1 = l1.next

    while True:
        output2.append(l2.val)
        if not l2.next:
            break
        l2 = l2.next
    
    output1 = output1.reverse()
    output2 = output2.reverse()
    total = int("".join(output1)) + int("".join(output2))



"""





# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode<{self.val} - {self.next}>"

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output1 = []
        output2 = []
        total = 0

        while True:
            output1.append(l1.val)
            if not l1.next:
                break
            l1 = l1.next

        while True:
            output2.append(l2.val)
            if not l2.next:
                break
            l2 = l2.next
        
        output1.reverse()
        output2.reverse()
        print(output1, output2)
        total = int("".join([str(a) for a in output1])) + int("".join([str(a) for a in output2]))
        print(total)

        total_str = str(total)
        l3 = ListNode(int(total_str[0]), None)
        for x in total_str[1:]:
            l3 = ListNode(int(x), l3)
            
        return l3

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    l3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    print(Solution().addTwoNumbers(l1, l2))
    print(Solution().addTwoNumbers(l3, l4))
    