def getNode(llist, positionFromTail):
    #initialize slow and fast as llist
    slow=llist
    fast=llist
    k=positionFromTail
    #move fast k-times ahead so that distance between slow and fast is k
    while fast is not None and k!=0:
        fast=fast.next
        k-=1
    #now move slow and fast by one step simultaneously
    while fast.next is not None:
        slow=slow.next
        fast=fast.next
    #when fast.next becomes None, nth node from end will be present at slow
    return slow.data
