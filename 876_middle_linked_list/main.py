# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodeList = []
        while head:
            nodeList.append(head)
            head=head.next
        
        lenNodeList=int(round(len(nodeList)/2))

        return nodeList[lenNodeList]

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)


solution = Solution()

node = solution.middleNode(head1)

print(node.val)