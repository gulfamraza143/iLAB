def lenOfLL(head):
    l=0
    while head is not None:
        l+=1
        head=head.next
    return l

def findMergeNode(head1, head2):
    #calculate length of both the lists
    n1=lenOfLL(head1)
    n2=lenOfLL(head2)
    #calculate the difference between both the list
    k=abs(n1-n2)
    #if list1 is greater than list2, move list1 by k-times ahead
    if(n1>n2):
        while(k!=0):
            head1=head1.next
            k-=1
    else:
        #if list2 is greater than list1, move list2 by k-times ahead
        while(k!=0):
            head2=head2.next
            k-=1
    #move head1 and head2 simultaneouly until they point to the same address
    while(head1!=head2):
        head1=head1.next
        head2=head2.next
    #return the data when both head1 and head2 point to the same address
    return head1.data