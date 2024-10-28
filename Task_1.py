# Визначення класу вузла
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Визначення класу однозв'язного списку
class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання нового елемента в кінець списку
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Виведення елементів списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування вставками для однозв'язного списку
    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, head, node):
        if not head or node.data < head.data:
            node.next = head
            return node
        current = head
        while current.next and current.next.data < node.data:
            current = current.next
        node.next = current.next
        current.next = node
        return head

    # Об'єднання двох відсортованих списків
    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node(0)
        tail = dummy
        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


# Створення та заповнення списків
list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(4)

list2 = LinkedList()
list2.append(2)
list2.append(6)
list2.append(5)


print("Original List 1:")
list1.print_list()
list1.reverse()
print("Reversed List 1:")
list1.print_list()

list1.insertion_sort()
print("Sorted List 1:")
list1.print_list()

# Об'єднання двох відсортованих списків
merged_list = LinkedList.merge_sorted(list1.head, list2.head)
print("Merged Sorted List:")
merged_list.print_list()
