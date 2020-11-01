# используется для сортировки
from operator import itemgetter

class Book:

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Libertycity:

    def __init__(self, id, name,size, id_of_book):
        self.id = id
        self.name = name
        self.size = size
        self.bk_id = id_of_book

class Libertycity_Book:
    
    def __init__(self, id_of_book, id_of_Libertycity):
        self.id_of_book = id_of_book
        self.id_of_Libertycity = id_of_Libertycity

Book = [
    Book(1, 'Книга 1'),
    Book(2, 'Книга 2'),
    Book(3, 'Книга 3'),


    Book(11, 'Четвертая книга'),
    Book(22, 'Пятая книга'),
    Book(33, 'Шестая книга')
]

Libertycity = [
    Libertycity(1,'Имени Ленина',  2200, 1),
    Libertycity(2,'1 библиотека', 2500, 3),
    Libertycity(3,'Бауманская библиотека', 2200, 3),
    Libertycity(4,'Главная библиотека всеся руси', 5000, 2),
    Libertycity(5,'Бибофф', 8000, 3)
]

Libertycity_Book = [
    Libertycity_Book(1,1),
    Libertycity_Book(2,2),
    Libertycity_Book(3,3),
    Libertycity_Book(3,4),
    Libertycity_Book(5,5),

    

    Libertycity_Book(11,1),
    Libertycity_Book(22,2),
    Libertycity_Book(33,3),
    Libertycity_Book(33,4),
    Libertycity_Book(33,5)
]

def main():
    

    
    one_to_many = [( b.name, b.size, a.name) 
        for a in Book 
        for b in Libertycity 
        if b.bk_id == a.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, d.id_of_book, d.id_of_Libertycity) 
        for c in Book
        for d in Libertycity_Book 
        if c.id == d.id_of_book]
    
    many_to_many = [(b.name, b.size, name_of_book) 
        for name_of_book, id_of_book, id_of_Libertycity in many_to_many_temp
        for b in Libertycity if b.id== id_of_Libertycity]

    print('Задание В1')
    first_res = {} 

    for l in Libertycity:
        if 'И' == l.name[0]:
            libertycity = list((filter(lambda i: i[0] == l.name, one_to_many)))
            l_stud_names = [f[2] for f in libertycity]
            first_res[l.name] = l_stud_names

    print(first_res)
    
    
    
    print('\nЗадание B2')
    second_res_unsort = []
    
    for d in Book:
        
        libertycity = list(filter(lambda i: i[2]==d.name, one_to_many))
         
        if len(libertycity) > 0:
            second_res_unsort.append((d.name, min([a[1] for a in libertycity])))
    second_res = sorted(second_res_unsort, key=itemgetter(1))
    print(second_res)

    print('\nЗадание B3')
    third_res = sorted(many_to_many, key=itemgetter(0))
    print(third_res)


if __name__ == '__main__':
    main()
