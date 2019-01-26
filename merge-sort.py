import unittest

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

def create_linked_list(arr):
    head = Node(arr[0])
    curr = head

    for i in range(1, len(arr)):
        curr.set_next(Node(arr[i]))
        curr = curr.get_next()

    return head

def linked_list_to_list(head):
    curr = head

    arr = []
    while (curr != None):
        arr.append(curr.get_data())
        curr = curr.get_next()

    return arr

def divide(arr):
    result = []
    divided = True
    for head in arr:
        test = head
        count = 0
        while test != None:
            test = test.get_next()
            count += 1

        if count >= 2:
            divided = False 

    if divided:
        return arr

    for head in arr:
        
        temp = head
        curr = temp
        
        if curr.get_next() != None:
            a = Node(curr.get_data())
            a_head = a
            curr = curr.get_next()
            b = Node(curr.get_data())
            b_head = b
            curr = curr.get_next()

            turn = True

            while curr != None:
                if turn == True:
                    a.set_next(curr)
                    a = a.get_next()
                    turn = False
                else:
                    b.set_next(curr)
                    b = b.get_next()
                    turn = True
                curr = curr.get_next()
                a.set_next(None)
                b.set_next(None)

            result.append(a_head)
            result.append(b_head)
        else:
            curr.set_next(None)
            result.append(curr)

    return divide(result)

def mend(arr):
    n = [x.get_data() for x in arr]
    index = n.index(min(n))
    head = arr[index]
    temp = head
    arr.pop(index)
    n.pop(index)

    for i in range(len(arr)):
        index = n.index(min(n))
        temp.set_next(arr[index])
        temp = temp.get_next()
        arr.pop(index)
        n.pop(index)
    
    return head

def merge_sort(head):
    res = divide([head])
    return mend(res)

class tests(unittest.TestCase):
    def test1(self):
        linked = create_linked_list([1,10,14,2,5,12])
        ordered = linked_list_to_list(create_linked_list([1,2,5,10,12,14]))
        res = linked_list_to_list(merge_sort(linked))
        self.assertEqual(res, ordered)


unittest.main()