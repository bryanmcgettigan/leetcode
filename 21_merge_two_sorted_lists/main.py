# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def mergeTwoLists(head1, head2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = ListNode()
    op = dummy
    while head1 and head2:
        if head1.val<head2.val:
            op.next=head1
            head1=head1.next
        else:
            op.next=head2
            head2=head2.next
        op = op.next

    op.next = head1 if head1 else head2
    return dummy.next


# Function to print the linked list
def printList(curr):
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# First linked list: 5 -> 10 -> 15
head1 = ListNode(5)
head1.next = ListNode(10)
head1.next.next = ListNode(15)

# Second linked list: 2 -> 3 -> 20
head2 = ListNode(2)
head2.next = ListNode(3)
head2.next.next = ListNode(20)

res = mergeTwoLists(head1, head2)

printList(res)