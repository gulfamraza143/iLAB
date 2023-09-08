def reverse(llist):
    #return llist when the list is empty
    if llist is None:
        return llist
    #return llist when we have a single node
    if llist.prev is None and llist.next is None:
        return llist
    #intialize curr as llist
    curr=llist
    #swap the prev and next of curr 
    while curr.next is not None:
        curr.prev,curr.next=curr.next,curr.prev
        curr=curr.prev
    #Since the last node is not linked, again swap prev and next of curr
    curr.prev,curr.next=curr.next,curr.prev
    #now the head/llist becomes curr
    return curr