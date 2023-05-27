


class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # GET методы
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    #SET методы
    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next




class LinkedList(object):
    def __init__(self):
        self.head = None
    #Добавления нового элемента
    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    # Вывод списка на печать
    def show(self):
        cur_node = self.head
        output = ''
        while cur_node != None:
            output += str(cur_node.get_data()) + '-->'
            cur_node = cur_node.get_next()
        print(output + 'None')

    # Возврат длина листа
    def len(self):
        cur_node = self.head
        count = 0
        while cur_node != None:
            count += 1
            cur_node = cur_node.get_next()
        return count
    # Добавление в начало
    def push_front(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

     # Удаление последнего элемента
    def remove_back(self):
        cur_node = self.head
        while cur_node.get_next().get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    # Разворот массива
    def reverse(self):
        prev = None
        cur_node = self.head
        next = None
        while cur_node != None:
            next = cur_node.get_next()
            cur_node.set_next(prev)
            prev = cur_node
            cur_node = next
        self.head = prev



my_list = LinkedList()
my_list.append(23)
my_list.append(356)
my_list.append(666)
my_list.append(777)

my_list.push_front(1)

my_list.show()
my_list.reverse()
my_list.show()








