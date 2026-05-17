class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = self.head
        self.head = self.head.next
        sorted_head.next = None

        cur = self.head
        while cur:
            nxt = cur.next
            if cur.data < sorted_head.data:
                cur.next = sorted_head
                sorted_head = cur
            else:
                p = sorted_head
                while p.next and p.next.data < cur.data:
                    p = p.next
                cur.next = p.next
                p.next = cur
            cur = nxt

        self.head = sorted_head

    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node()
        tail = dummy
        p1, p2 = list1.head, list2.head

        while p1 and p2:
            if p1.data <= p2.data:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        tail.next = p1 if p1 else p2

        merged = LinkedList()
        merged.head = dummy.next
        list1.head = None
        list2.head = None
        return merged

if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    llist.delete_node(10)

    print("\nЗв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    # Пошук елемента у зв'язному списку
    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)

    print("\nРеверс списку:")
    llist.reverse()
    llist.print_list()

    print("\nСортування вставками:")
    llist.sort()
    llist.print_list()

    list_a = LinkedList()
    for value in (1, 3, 5, 7):
        list_a.insert_at_end(value)

    list_b = LinkedList()
    for value in (2, 4, 6, 8):
        list_b.insert_at_end(value)

    print("\nОб'єднання двох відсортованих списків:")
    merged = LinkedList.merge_sorted(list_a, list_b)
    merged.print_list()
