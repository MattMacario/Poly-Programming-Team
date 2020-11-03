# Matthew Macario Merging two sorted Linked Lists
# For reference:
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def mergeLists(head1, head2):
    # creates the first node of a new list and is a reference for the beginning of the list
    theHead= SinglyLinkedListNode(0)
    curr = theHead

    # while both lists still have nodes with data
    while head1 and head2:

        # if the node from head 1 is less it is added onto the new list
        # and the new list pointer is incremented along with list 1
        if head1.data < head2.data:
            curr.next = SinglyLinkedListNode(head1.data)
            curr = curr.next
            head1 = head1.next

        # if the node from head 2 is less it is added onto the new list
        # and the new list pointer is incremented along with list2
        else:
            curr.next = SinglyLinkedListNode(head2.data)
            curr = curr.next
            head2 = head2.next

    # if list 1 is the only list with data still, the rest of its nodes are appended to the new list
    while head1:
        curr.next = SinglyLinkedListNode(head1.data)
        curr=curr.next
        head1=head1.next

    # if list 2 is the only list with data still, the rest of its nodes are appended to the new list
    while head2:
        curr.next = SinglyLinkedListNode(head2.data)
        curr = curr.next
        head2 = head2.next

    # when there is no more data left, the first node with data from the merged lists is returned
    return theHead.next