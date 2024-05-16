list_car = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for i in list_car:
    print("Я езжу на автомобиле марки ", i)
cars_count = 0
for i in list_car[0:5:2]:
    cars_count += 10
    print(f' Количество авто : {cars_count }',i)
