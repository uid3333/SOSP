import os, random, time
from colorama import init, Fore
init(autoreset=True)
pc = 0
rps=['камень','ножницы','бумага']
#ФУНКЦИИ
def clear():
    if os.name=='nt':
        os.system('cls')
    else: os.system('clear')
def load():
    for pc in range(100):
        eq=pc//2
        eq2=50-eq
        print('['+('='*eq)+('-'*eq2)+'] '+str(pc)+'%')
        time.sleep(1/3200)
        clear()
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def green(text):
    print(Fore.GREEN+text)
def red(text):
    print(Fore.RED+text)
#НАЧАЛО
def system():
    while True:
        green('1. Информация о системе')
        green('2. Калькулятор')
        green('3. Камень, ножницы, бумага')
        green('4. Перезагрузка')
        green('5. Выключение')
        choice = input('Введите ваш выбор: ')
        if choice=='1':
            os.system('start https://www.youtube.com/channel/UCcO_FxsPOgnvk2ix7k_hkKg')
            green('Open SnakeOS Premium')
            green('Версия: 1.0.0')
            green('Разработчик: CompTech')
            green('Дата выхода: 06.04.2023 (11.09.2023)')
            green('Слоган компании: Что трудно - то возможно')
            input('Нажмите Enter, чтобы продолжить...')
            cls
            ()
        if choice=='2':
            while True:
                print("Введите 'q', чтобы выйти.")
                evl=input('Введите выражение: ')
                if evl=='q':
                    clear()
                    break
                else:
                    try:
                        res='Результат: '+str(eval(evl))
                        green(res)
                    except:
                        red('Ошибка: Неверное выражение.')
    
        if choice=='3':
            tpci='Введите свой выбор ('+rps[0]+', '+rps[1]+' или '+rps[2]+'):'
            tpc=input(tpci)
            tcc=random.choice(rps)
            print('Змейка выбрала: '+tcc)
            if tpc == rps[0] or tpc == rps[1] or tpc == rps[2]:
                if tpc==tcc:
                    print('Ничья!')
                elif pc==rps[0]:
                    if tcc==rps[1]:
                        print('Вы выиграли!')
                    else:
                        print('Вы проиграли.')

                elif pc==rps[1]:
                    if tcc==rps[2]:
                        print('Вы выиграли!')
                    else:
                        print('Вы проиграли.')

                else:
                    if tcc==rps[0]:
                        print('Вы выиграли!')
                    else:
                        print('Вы проиграли.')
            
            else:
                print('Неверный выбор.')
            input('Нажмите Enter, чтобы продолжить...')
            clear()
        if choice=='4':
            print('Перезагрузка SnakeOS...')
            time.sleep(2)
            break
        if choice=='5':
            print('Выключение SnakeOS...')
            time.sleep(2)
            exit()
while True:
    load()
    system()
