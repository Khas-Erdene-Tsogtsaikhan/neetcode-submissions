# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # i notice that the reordered list is converging into the middle starting
        # and then from the end. what i currently see is that
        # divide the list into two, and then just set a loop using the tactic for 
        # merging two lsits
        

        fast = head
        mid = head

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        second = mid.next
        mid.next = None
        

#reverse the mid list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # prev and then curr two litss
        curr = head
        # prev = 1, 2, 3
        # curr = 4, 5, 6
        # prev.next = curr
        while prev:
            temp = curr.next
            temp2 = prev.next
            curr.next = prev
            prev.next = temp
            curr = temp
            prev = temp2


        return prev



            

            




            


