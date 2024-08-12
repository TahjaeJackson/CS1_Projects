


def ll_remove(head, val):
    p = None
    n = head

    while n!= None:
        if n.data == val:
            p.next = n.next

        p = n.next