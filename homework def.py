def hello():
    print("Привет!")
hello()
# обычная функция

def your_name(name):
    print("Ваше имя", name, "?")
your_name("Дмитрий")

# принимающая функция
import random # библиотека рандома
def lottery():
    tickets = [1, 2, 3, 4, 5, 6, 7]
    win = random.choice (tickets)
    return win # заверщает функцию

win = lottery() # чтобы была выводилась  функция нужно задать переменную. можно их складывать
# win = lottery()+lottery()
print(win)
# возвращающая функция
def lottery (mon, thue):
    tickets = [1, 2, 3, 4, 5, 6, 7]
    win_1 = random.choice(tickets)
    tickets.remove(win_1)
    win_2 = random.choice(tickets)
    print(mon, thue)
    return win_1, win_2
win_1, win_2 = lottery (mon='понедельник',thue='вторник')
print(win_1, win_2)
# сразу возвращающая функция и принимающая

# def lottery (): #«*args» для обычных параметров и «**kwargs» для именованных(Если мы не знаем сколько параметров будет принимать функция)
#     tickets = [1, 2, 3, 4, 5, 6, 7]
#     win_1 = random.choice(tickets)
#     tickets.remove(win_1)
#     win_2 = random.choice(tickets)
#     print(args)
#     return win_1, win_2
# win_1, win_2 = lottery(1, 2, 3, 4, 5, 6, 7)
# print(win_1, win_2)

# next homework
def print_params (name):
    print (name, name)
print_params ("Дмитрий")
