def has_cycle(head):
    #initialize slow and fast as head
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        #move slow by one step
        slow=slow.next
        #move fast by two steps
        fast=fast.next.next
        #if slow and fast meet, there is a loop and return true
        if slow==fast:
            return True
    #return false if there is no loop
    return False