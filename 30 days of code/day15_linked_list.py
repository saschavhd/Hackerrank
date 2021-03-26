class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def __init__(self):
        self.head = None

    def insert(self, head, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return self.head
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
        return self.head

if __name__ == '__main__':
    mylist = Solution()
    T = int(input())
    head = None
    for _ in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    mylist.display(head)
