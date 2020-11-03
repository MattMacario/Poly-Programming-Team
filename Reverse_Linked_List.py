#  Matthew Macario Reversing a Linked List
# For reference:
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def reverse(head):
    #takes care of the edge case of making the next node None
    curr = head
    nextHead = head.next
    head.next=None
    prevHead=curr
    head=nextHead

    #Continues the loop until it reaches the end
    while head is not None:
        curr=head
        nextHead=head.next
        head.next=prevHead
        prevHead=curr
        head=nextHead
        #returns previous head since loop stops on None
    return prevHead