# while True:
#     namber = int (input("inter int: "))
#     if namber % 2 == 0:
#         print("четное число")
#         #continue - завершает последующий код
#     else:
#         print("нечетное число")
#         break # завершает цикл
# #ilif - добавляется к if иногда
# print("finish")
#for
for i in ("HELLO"): # i j k  обычно для одного цикла "i" и переменные только для этого цикла
    print (i)
list_ = ["one", "two", "three"]
for i in list_:
    print (i)
    if i == "three":
        list_.remove(i)
print(list_)
list_ = ["one", "two", "three"]

for i in range(5): # ФУНКЦИЯ ФОР ПОВТОРИТ 5 РАЗ  А РЕЙНДЖ ВЕРНЕТ ПОСЛЕДОВАТЕЛЬНОСТЬ с 0 до 4
    print (i)

for i in range(len(list_)): # С помощью функции len() можно подсчитать:
#Количество символов в строке.
#Количество цифр в числе, если перевести его в строку.
#Количество байт в строке (если указать кодировку).
    print (list_)# Len посчитало кол-во символов в списке list_ (3шт)
# а for павторит цикл 3 раза
print(list_)
for i in range(len(list_)):
    list_[i]= (" :) ")
# print(list_)
# # Сложение элементов (так не делают, но для примера):
# list_2 = [1, 2, 2, 3, 7]
# print(list_2)
# sum_ = 0
# #
# # # Let's create a multiplication table создадим таблицу умножения
# # for i in range(1, 11): # где i - это 1
# #     #фунция range принимает три последовательности start(начало), stop(обязательный), step(шаг)
# #     for j in range(1, 11): # где j - это  тоже 1
# #         print(f'{i} x {j} = {i*j}')
# #
# # dict = {'a' : 1, 'b' : 2, 'c' : 3} # для словаря
# # for i in dict:
# #     print(i, dict[i])