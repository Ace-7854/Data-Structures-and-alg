class LinkedListNode: 
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    def __init__(self): 
        self.head = None 
        self.size = 0

    def add(self, value=0): 
        new_node = LinkedListNode()
        new_node.value = value 
        if self.head is None:
            self.head = new_node
            self.size += 1 
        else:
            current = self.head 
            while current.next is not None: 
                current = current.next 
            current.next = new_node 
            self.size += 1

    def display(self):
        current = self.head
        while current is not None: 
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def search(self, target):
        index = 0
        current = self.head
        while current is not None:
            if current.value == target:
                return index
            else: 
                index += 1
                current = current.next
        
        return -1
    
    def del_at_index(self, index): 
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next 
            self.size -= 1

    def del_by_value(self, value):
        current = self.head 
        while current is not None: 
            if current.value == value:
                self.del_at_index(self.search(value)) 
                return 
            else: 
                current = current.next
    
    def __get_node_values(self):
        values = [] 
        current = self.head 
        while current is not None: 
            values.append(current.value) 
            current = current.next 
        return values

    def reverse(self):
        values = self.__get_node_values()
        return values[::-1]

def get_node_values(head):
    values = [] 
    current = head 
    while current is not None: 
        values.append(current.value) 
        current = current.next 
    return values

def select_target(linked_list):
    import random 
    values = get_node_values(linked_list.head)
    print(f"Values in the linked list: {values}") 
    if not values: 
        return None 
    return random.choice(values)

def main():
    import random 
    linked_list = LinkedList() 
    for _ in range(10): 
        linked_list.add(random.randint(1,100)) 
    print(f"{linked_list.size}")
    linked_list.display() 
    target = select_target(linked_list)
    print(f"Searching for {target}: {linked_list.search(target)}") 
    linked_list.del_by_value(target) 
    print(f"After deleting {target}:") 
    linked_list.display()
    reversed_values = linked_list.reverse()
    print(f"Reversed values: {reversed_values}")

if __name__ == "__main__":
    main()
            