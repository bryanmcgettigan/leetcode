# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    prev=None
    curr = head
    while curr:
        next = curr.next
        
        curr.next=prev
        prev=curr
        curr=next
    return prev
# Create the linked list
values = [1, 2, 3, 4, 5]
head = ListNode(values[0])
current = head

for val in values[1:]:
    current.next = ListNode(val)
    current = current.next

# Print the linked list
current = head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next

head = reverseList(head)

current = head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next
    