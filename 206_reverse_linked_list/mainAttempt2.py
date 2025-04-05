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
    stack = []
    while head:
        stack.append(head)
        head = head.next
    newNode=stack.pop()
    holder = ListNode()
    while len(stack)>1:
        holder=stack.pop()
        newNode.next =holder
        newNode=holder
    return newNode




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
