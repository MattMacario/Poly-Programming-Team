# Matthew Macario Merging two sorted Linked Lists
# For reference:
#class Node(object):
#   def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node


def has_cycle(head):

    # Creates a list to store the data that has already been passed over
    dataList=[]

    # if the first head is None then it is impossible to have a cycle
    if head==None:
        return False

    # loops as long as the head is not None and checks the heads.data member
    # if the data member is already stored in the list, true is returned to signify a cycle
    while head:
        if head.data in dataList:
            return True

        # If the data is not in the list, it is added and the head is incremented
        else:
            dataList.append(head.data)
            head=head.next
    # function reaches this point only if it has reached a None head before a cycle
    #returns false to signify there is no cycle
    return False