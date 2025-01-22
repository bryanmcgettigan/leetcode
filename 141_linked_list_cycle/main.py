# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hmap = {}
        pos =0
        if not head.next:
            return False
        while head:
            if head in hmap:
                return True
            hmap[head] = pos
            pos = pos+1
            head=head.next
        return False


# Create nodes
values = [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21, 5]
nodes = [ListNode(x) for x in values]

# Link nodes
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]


# Head of the linked list
head = nodes[0]
print(head.hasCycle(head))