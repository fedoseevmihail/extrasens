import random
print("\n\tДобро пожаловать! Загадайте двузначное число!")
a = 10
b = 99
hum_num=int(input("Введите случайное число от 10 до 99, которое экстрасенс попытается угадать\n"))
es_num = random.randint(a,b)
while es_num != hum_num:
    print ("Число экстрасенса: ",es_num)
    result = input("Напишите 'Да', если экстрасенс угадал; напишите 'Б', если Ваше число больше; напишите 'М', если Ваше число меньше\n")
    if result == 'Да':
        hum_num = es_num
        print ("Экстрасенс угадал Ваше число.")
        break
    elif result == 'Б':
        a = es_num + 1
        es_num = random.randint(a,b)
    elif result == 'М':
        b = es_num - 1
        es_num = random.randint(a,b)
    input("Нажмите Enter")
print ("Экстрасенс угадал Ваше число ", hum_num)
input ("Спасибо!")
