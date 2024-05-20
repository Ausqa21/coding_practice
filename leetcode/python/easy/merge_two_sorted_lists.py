"""
constraints
--
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

base cases
--
[] [] => []
[] [x] => [x]
[x] [] => [x]

pseudocode
--
values = []
unpack all values into values
sort values in desc order
use bottom up to create final linkedlist
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode<{self.val}, {self.next}>"

from typing import Optional


def x(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    values = []

    if list1 is None and list2 is None:
        return ListNode("")

    if list1 is None or list1.val is None:
        return list2

    if list2 is None or list2.val is None:
        return list1

    if list1.val is None and list2.val is None:
        return ListNode("")

    while True:
        values.append(list1.val)
        if not list1.next:
            break
        list1 = list1.next

    while True:
        values.append(list2.val)
        if not list2.next:
            break
        list2 = list2.next

    values.sort(reverse=True)

    output = ListNode(values[0], None)

    for x in values[1:]:
        output = ListNode(x, output)

    return output



if __name__ == "__main__":
    # base cases
    list1 = ListNode(None)
    list2 = ListNode(0)
    list3 = ListNode(2, ListNode(6))
    list4 = ListNode(5)
    print(x(list1, list1))
    print(x(None, None))
    print(x(list1, list2))
    print(x(list1, list3))
    print(x(list3, list2))
    print(x(list3, list4))
    print(ListNode(""))