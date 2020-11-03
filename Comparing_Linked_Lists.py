# Matthew Macario Comparing Linked Lists
# For reference:
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def compare_lists(llist1, llist2):
    # continues the loop as long as one list has not ended AKA NONE
    while llist1 is not None or llist2 is not None:
       # if one list is None and the other is not, they are not equal so a 0 is returned
        if llist1 is None or llist2 is None:
            return 0
        # if the data of the nodes for both lists are equal, they are both moved forward one node
        elif  llist1.data == llist2.data:
            llist1 = llist1.next
            llist2 = llist2.next
        # if the nodes are any other combination they are not equal so a 0 is returned
        else:
            return 0
    # this will only be reached if both lists' current nodes are None, after they are equal so 1 is returned
    return 1
