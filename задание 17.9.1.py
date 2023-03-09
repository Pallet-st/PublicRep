class Node: # класс элемента
    def __init__(self, value = 0, next_ = None): # инициализируем
        self.value = value # значением
        self.next = next_ # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)

class LinkedList: # класс списка
    def __init__(self): # инициализируем пустым
        self.first = None
        self.last = None
        
    def clear(self): # очищаем список
        self.__init__()
    
    def __str__(self): # функция печати 
        R = ''
        
        pointer = self.first # берем первый указатель
        while pointer is not None: # пока указатель не станет None
            R += str(pointer.value) # добавляем значение в строку
            pointer = pointer.next # идем дальше по указателю
            if pointer is not None: # если он существует добавляем пробел
                R += ' '
        return R
        
    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node=Node(value, self.first)
            self.first = new_node
        
    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node    
            self.last = new_node
            
    def popleft(self):
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last: # если список содержит только один элемент
            node = self.first # сохраняем его
            self.__init__() # очищаем
            return node # и возвращаем сохраненный элемент
        else:
            node = self.first # сохраняем первый элемент
            self.first = self.first.next # меняем указатель на первый элемент
            return node # возвращаем сохраненный
            
    def popright(self): 
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last: # если список содержит только один элемент
            node = self.first # сохраняем его
            self.__init__() # очищаем
            return node # и возвращаем сохраненный элемент
        else:
            node = self.last # сохраняем последний
            pointer = self.first # создаем указатель
            while pointer.next is not node: # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None # обнуляем указатели, чтобы
            self.last = pointer # предпоследний стал последним
            return node # возвращаем сохраненный
            
    def __iter__(self): # объявляем класс как итератор
        self.current = self.first # в текущий элемент помещаем первый
        return self # возвращаем итератор

    def __next__(self): # метод перехода
        if self.current is None: # если текущий стал последним
            raise StopIteration # вызываем исключение
        else:
            node = self.current # сохраняем текущий элемент
            self.current = self.current.next # совершаем переход
            return node # и возвращаем сохраненный
            
    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count       
        
def Find(array, element, left, right): 
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует

    middle = (right+left) // 2 # находим середину
    #if middle<=1:
    #    return False
    if array[middle-1]<element and array[middle] >= element: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < array[middle] and element < array[middle-1]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return Find(array, element, left, middle-1)
    else: # иначе в правой
        return Find(array, element, middle+1, right)

    #Блок ввода данных
StrIn=input('Введите последовательность чисел через пробел: ')
Chislo=0
Chislo=int(input('Ведите натуральное число: '))
            
    #Преобразование введенной строки в список
ls_StrIn=StrIn.split()
Posled=[]
for i in range(0,len(ls_StrIn)):
    Posled.append(int(ls_StrIn[i]))

#Сортировка
Posled.sort()

    #Вывод на печать        
print(ls_StrIn)
print(Posled)
#print(Posl.__str__())
print(Find(Posled,Chislo,0,len(Posled)-1))