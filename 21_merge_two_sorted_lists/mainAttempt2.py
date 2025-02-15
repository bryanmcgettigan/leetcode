# Definition for singly-linked list.
##TODO

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self,head1, head2):
        holder = head2
        while holder:
            if not head1:
                break
            if holder.val >=head1.val:
                holder = holder.next
                holder.next = head1.next
            else:
                head1=head1.next
        return head1



solution = Solution()
# Creating the first linked list: 1 → 2 → 4
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

# Creating the second linked list: 1 → 3 → 4
head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" → " if current.next else "\n")
        current = current.next


node = (solution.mergeTwoLists(head1,head2))

print_linked_list(node)