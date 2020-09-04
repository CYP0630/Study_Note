class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
    
    #Read
    def get(self, location):
        cur = self.head
        for i in range(location):
            cur = cur.next
        return cur.val
    
    #Update
    def set(self, location, val):
        cur = self.head
        for i in range(location):
            cur = cur.next
        cur.val = val

    #Add
    def add(self, location, val):
        if location > 0:
            pre = self.head
            for i in range(location - 1):
                pre = pre.next
            new_node = ListNode(val)
            new_node.next = pre.next
            pre.next = new_node
        elif location == 0:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node
    
    #Remove
    def remove(self, locatiom):
        if location > 0:
            pre = self.head
            for i in range(location - 1):
                pre = pre.next
            pre.next = pre.next.next
        elif location == 0:
            self.head = self.head.next

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()

    def is_empty(self):
        return self.head is None

print('test my LinkedList')
linked_list = MyLinkedList()
linked_list.add(0, 1)
linked_list.add(1, 3)
linked_list.add(2, 5)
linked_list.add(3, 7)
linked_list.traverse()
print('\n')

print('test add function')
linked_list.add(0, 9)
linked_list.add(1, 100)
linked_list.traverse()

def build_linkedlist():
    print('Build LinkedList')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    return node_1

def run_linkedlist_example():
    print('LinkedList Example')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)
    
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    
    cur = node_1
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')

def quiz_1():
    print('Quiz_1')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node_2 = node_3

    cur = node_1
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')


run_linkedlist_example()
quiz_1()
