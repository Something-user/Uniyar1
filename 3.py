from re import *

# Обработчик строки для "свёртывания"
def handler(string):
    result_string = ''
    pattern = r'([A-Za-z])\1*'
    
    for m in finditer(pattern,string):
        result_string+=((m.group(0))[0])+str(len(m.group(0)))

    return result_string


# Обработчик для расшифровывания строки
def reverse_handler(string):
    result_string = ''
    for i in range(0,len(string)-1,2): # Строка всегда с чётной длиной
                                       # сначала символ потом кол-во повторений
        result_string += (string[i])*int(string[i+1])

    return result_string

# Ввод строки пользователем
while True:
    user_string = input("Введите строку из латинских букв: ")
    if(user_string):
        break
    
    else:
        print("Вы не ввели строку.")
    


if handler(user_string):
    print("Обработанная строка:",handler(user_string))
    print("Расшифрованная строка:",reverse_handler(handler(user_string)))

else:
    print("Строку обработать невозможно")

