# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def mergeTwoLists(head1, head2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    new_list = []
    while head1 is not None:
        new_list.append(head1.data)
        head1=head1.next
    
    while head2 is not None:
        new_list.append(head2.data)
        head2 = head2.next

    new_list.sort()
    dummy = Node(-1)
    curr = dummy

    for value in new_list:
        curr.next = Node(value)
        curr = curr.next

    return dummy.next 

# Function to print the linked list
def printList(curr):
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

# First linked list: 5 -> 10 -> 15
head1 = Node(5)
head1.next = Node(10)
head1.next.next = Node(15)

# Second linked list: 2 -> 3 -> 20
head2 = Node(2)
head2.next = Node(3)
head2.next.next = Node(20)

res = mergeTwoLists(head1, head2)

printList(res)