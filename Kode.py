# Отредактированный проект

import time
import random
import sys
import os

r = random.randint  # Сокращение для удобства вызова randint
# ===========================
# Игры
# ===========================

# ---------------------------
# Функция бота №1 — игра "Doors"
# ---------------------------
def doors_game():
    inventory = []
    monsters = ["dead_man", "ghost"]

    # Функция попытки побега
    def escape():
        att = r(1, 20)
        if att > 15:
            print("Вы успешно сбежали")
            return True
        else:
            print("Вы мертвы")
            sys.exit(1)

    # Функция случайного боя с монстром
    def random_event_battle():
        random_monsters = random.choice(monsters)

        if random_monsters == "ghost":
            player_health = 25
            monster_health = 10
            print("На вас напал призрак!")
            ans = input("""Защищаться = 1
бежать = 2
""")
            if ans == "1":
                while monster_health > 0 and player_health > 0:
                    command = input("Что ты хочешь сделать? (ударить): ")
                    if command == "ударить":
                        player_damage = r(5, 10)
                        monster_health -= player_damage
                        print("Вы нанесли монстру", player_damage)
                        if monster_health <= 0:
                            print("Вы победили!")
                            break

                        monster_damage = r(10, 11)
                        player_health -= monster_damage
                        print("Монстр нанес вам", monster_damage)
                        print("Ваше здоровье:", player_health)
                        print("Здоровье монстра:", monster_health)
                    else:
                        print("Некорректная команда.")

                if player_health <= 0:
                    print("Вы погибли.")
                    sys.exit(1)

            else:
                if not escape():
                    sys.exit(1)

        elif random_monsters == "dead_man":
            player_health = 25
            monster_health = 10
            print("На вас напал мертвец!")
            ans = input("""Защищаться = 1
бежать = 2
""")
            if ans == "1":
                while monster_health > 0 and player_health > 0:
                    command = input("Что ты хочешь сделать? (ударить): ")
                    if command == "ударить":
                        player_damage = r(5, 10)
                        monster_health -= player_damage
                        print("Вы нанесли монстру", player_damage)
                        if monster_health <= 0:
                            print("Вы победили!")
                            break

                        monster_damage = r(5, 9)
                        player_health -= monster_damage
                        print("Монстр нанес вам", monster_damage)
                        print("Ваше здоровье:", player_health)
                        print("Здоровье монстра:", monster_health)
                    else:
                        print("Некорректная команда.")

                if player_health <= 0:
                    print("Вы погибли.")
                    sys.exit(1)

            else:
                if not escape():
                    sys.exit(1)

    # Начало игры
    print("Здраствуй, приключенец! Ты должен зачистить старое подземелье.")
    print("Твои глаза замечают гельетину позади короля...")

    ans = input('Теперь выбор за тобой... Что ты выберешь? Я готов = 1, Иди лесом!!! = 2: ')
    if ans == '2':
        print("Посмотрю ты смелый... КАЗНИТЬ ЕГО")
        print("Твое приключение закончилось, даже не начавшись...")
        sys.exit(1)
    else:
        print("Ну вот и хорошо.")
        print("Змеиная ухмылка пробегает по лицу короля...")
        print("Перед тобой вход в пещеру. В инвентаре есть:")

        # Добавляем начальные предметы в инвентарь, если их там нет
        if "Сух.паек" not in inventory:
            inventory.append("Сух.паек")
        if "Веревка 5 метров" not in inventory:
            inventory.append("Веревка 5 метров")
        if "Керосинавая лампа" not in inventory:
            inventory.append("Керосинавая лампа")

        print(", ".join(inventory))

    ans1 = input('В голове появляется план: подождать немного и бежать! Идти в подземелье = 1, бежать = 2: ')

    if ans1 == '2':
        escape_chance = r(1, 50)
        if escape_chance >= 40:
            print("Поздравляю, ты успешно сбежал!")
            return
        else:
            print("Король был предусматрительнее, тебя поймали.")
            sys.exit(1)
    else:
        print("Ты проходишь по темным залам подземелья...")
        print("Дальше проход преграждает массивная дверь. Она закрыта, нужен ключ.")

    command = input("Введите команду (осмотреться): ")
    if command == "осмотреться":
        search = r(1, 45)
        if search >= 40:
            print("Ты запнулся о камень, под ним был ключ. Тебе повезло.")
            if "Ключ" not in inventory:
                inventory.append("Ключ")
        elif search >= 30:
            print("Ты отыскал проход между камнями. Пройдя туда, обнаруживаешь яму, в которой лежит ключ. Ты смог его достать, но пришлось пожертвовать веревкой.")
            if "Ключ" not in inventory:
                inventory.append("Ключ")
            if "Веревка 5 метров" in inventory:
                inventory.remove("Веревка 5 метров")
        else:
            random_event_battle()
    else:
        print("Некорректная команда.")

    command = input("Введите команду (открыть дверь): ")
    if command == "открыть дверь":
        if "Ключ" in inventory:
            inventory.remove("Ключ")
            print("Дверь открыта, преграда позади.")
        else:
            print("Нет ключа, дверь не открыть.")

    print("А вот и ты!")
    print("Восклицает неизвестный голос.")
    print("Прошло испытание, и на тебя падают монеты.")
    if "Монеты" not in inventory:
        inventory.append("Монеты")

    command = input("Введите команду (осмотреться): ")
    if command == "осмотреться":
        print("Ты нашел торговца, это кобольд.")
        print("Он говорит что-то непонятное...")
        print("Ты можешь купить один из предметов за монеты.")
        print("Список: Факел, Похлебка, Отмычки")
        ans3 = input("Введите 1, 2 или 3: ")
        if ans3 == "1" and "Факел" not in inventory:
            inventory.append("Факел")
            if "Монеты" in inventory:
                inventory.remove("Монеты")
        elif ans3 == "2" and "Похлебка" not in inventory:
            inventory.append("Похлебка")
            if "Монеты" in inventory:
                inventory.remove("Монеты")
        elif ans3 == "3" and "Отмычки" not in inventory:
            inventory.append("Отмычки")
            if "Монеты" in inventory:
                inventory.remove("Монеты")

    print("Инвентарь:", inventory)

    print("Что это!? Свет в конце тоннеля...")
    print("Заметив свет, ты ускоряешься...")
    print("На улице свежий воздух... Свобода.")


# ---------------------------
# Квиз (Quiz)
# ---------------------------
def quizz():

    correct_ans = 0

    print("Добро пожаловать в квиз")

    name = input("Введите свое имя: ")
    time.sleep(1)
    age = input("А теперь свой возраст: ")
    os.system('clear')
    
    time.sleep(1)
    ans1 = int(input("Вопрос 1: Какой вес земли? варианты ответа: 12833132.32 тонн, 0: "))
    time.sleep(1)
    if ans1 == 0:
        print("Ого, не думал что кто-то ответит верно")
        correct_ans += 1
    else:
        print("О похоже ты ошибся, ничего впереди есть еще задания")
    time.sleep(2)
    os.system('clear')

    ans2 = input("Как расшифровывается СССР? Варианты ответа: синие соковыжималки сидят резво; Союз Советских Социалистических Республик; собрание сурикатов сегодня раки: ")
    time.sleep(1)
    if ans2 == "Союз Советских Социалистических Республик":
        print("Кто ты воин!?")
        correct_ans += 1
    else:
        print("Я не удивлен")
    time.sleep(1)
    os.system('clear')

    ans3 = input("Сколько тебе лет? варианты ответов: они здесь не нужны: ")
    time.sleep(1)
    if ans3 == age:
        print("Молодец!")
        correct_ans += 1
    else:
        print("Ты хочешь сказать что за {age} лет ты не смог запомнить свой возраст?")
    time.sleep(1)
    os.system('clear')
    
    ans4 = input("Ответь на простой вопрос: что это за вещество дигидромонооксид. Здесь тоже просто: ")
    time.sleep(1)
    if ans4 == "H2O":
        print("У кого спросил?")
        correct_ans += 1
    else:
        print("Учебник химии в руки и иди учи!")
    time.sleep(1)
    os.system('clear')

    ans5 = input("Ну специально для тебя. какой это вопрос по счету? варианты ответа: Я отказываюсь писать сюда ответы: ") 
    time.sleep(1)
    if ans5 == "5":
        print("Ого! жаль я не считал...")
        correct_ans += 1
    else:
        print("Ты совсем не следишь за игрой? Ну и ладно, я пошел!")
        sys.exit(1)
    time.sleep(1)
    os.system('clear')

    ans6 = input("Когда умер Михаил Горшок? Варианты ответов: 19 июля 2013 года; вчера; Я не знаю кто это.: ")
    time.sleep(1)
    if ans6 == "19 июля 2013 года":
        print("О как молодец")
        correct_ans += 1
    else:
        print("Хм тебя сжечь или да?")
    time.sleep(1)
    os.system('clear')

    print("Ваша статистика:")
    print("Возраст игрока:", age)
    print("Имя игрока:", name)
    print("Количество правильных ответов:", correct_ans)
    time.sleep(5)
    os.system('clear')

# ---------------------------
# Игра "Мит"
# ---------------------------
def mit():
    print('Вы заходите в таверну.')
    time.sleep(1)
    print('С уставшим видом садидесь за ближащий столик.')
    time.sleep(1)
    print('Через какое-то время к вам подходит мужчина.')
    time.sleep(1)
    print('Здраствуй путник! Не желаешь сыграть, со старым Митом?')
    ans = input("Да/Нет")
    os.system('clear')



    while ans == "да":
        mit = r(1, 6)
        you = r(1, 6)
        mit1 = r(1, 6)
        you1 = r(1, 6)
        
        
        time.sleep(1)
        print('Ты выбросил:', you, '+', you1, '=', you + you1)
        time.sleep(1)
        print('Мит выбросил:', mit, '+', mit1, '=', mit + mit1)
        time.sleep(1)
        
        if (you + you1) == (mit + mit1):
            print("Ох, похоже ничья")
        elif (you + you1) > (mit + mit1):
            print("Неплохо бросил! Ты победил!")
        else:
            print("Ничего, в следующий раз повезет. Мит победил!")

        ans = input("Ну что еще раз? (да/нет): ")
        os.system('clear')

    print("Бывай, может потом еще поиграем.")
    time.sleep(2)
    os.system('clear')

# ===========================
# Полезные Программы
# ===========================


# ---------------------------
# Кликер
# ---------------------------
def click():
    click = 0
    print("Чтобы играть нажимайте Enter")
    time.sleep(2)

    while click != 10000:
        input()
        click += 1
        print(click)

    print("Тебе совсем делать нечего?")


# ---------------------------
# Калькулятор
# ---------------------------
def calculator():
    while True:
        print("""Выберите действие:
    1. +
    2. -
    3. /
    4. *
    5. Exit
    """)

        action = input()
        os.system('clear')
        if action == "5" or action == "Exit":
            break
        number = int(input("Выберите первое число: "))
        number1 = int(input("Выберите второе число: "))
        os.system('clear')

        print("Происходит действие...")
        time.sleep(1)

        if action == "1" or action == "+":
            print(number + number1)
        elif action == "2" or action == "-":
            print(number - number1)
        elif action == "3" or action == "/":
            if number1 != 0:
                print(number / number1)
            else:
                print("Ошибка: Деление на ноль!")
        elif action == "4" or action == "*":
            print(number * number1)
        else:
            print("Некорректное действие.")

# ---------------------------
# Таймер
# ---------------------------
def timer():
    while True:
        measurement_system = int(input("""--measurement system--
1. Hours
2. Minutes
3. Seconds
4. Exit
"""))
        os.system('clear')
        if measurement_system == 1:
            times = int(input("Введите время (в часах): "))
            times = times * 3600
            os.system('clear')
        elif measurement_system == 2:
            times = int(input("Введите время (в минутах): "))
            times = times * 60
            os.system('clear')
        elif measurement_system == 3:
            times = int(input("Введите время (в секундах): "))
            os.system('clear')
        else:
            print("Некорректный выбор системы измерения.")
            os.system('clear')
            return

        while times != 0:
            print(times)
            time.sleep(1)
            times -= 1
            
            if times % 10 == 0:
              os.system('clear')

        print("Таймер окончен")
        os.system('clear')

# ---------------------------
# Игра "Тир"
# ---------------------------

recharge_rate = 3  # время перезарядки магазина (секунды)
experience = 0  # опыт игрока
chance_luck = (experience, 10)  # диапазон для выпадения очков
komp_health = 10  # здоровье компьютера
player_health = 10  # здоровье игрока
  

victory_score = 0  # общий счет побед

# счет игры
comp_score = 0  # счет компьютера (не используется в коде, но оставил)
player_score = 0  # счет игрока (используется в тренировке)
def shoot():


  victory_score = 0  # общий счет побед

# счет игры
  comp_score = 0  # счет компьютера (не используется в коде, но оставил)
  player_score = 0  # счет игрока (используется в тренировке)


def training():
  global player_score, experience, recharge_rate, chance_luck  # чтобы менять глобальные переменные
  player_score = 0

  print("Зарядка магазина")
  player_score = 0
  time.sleep(recharge_rate)
  while player_score < 10:
      change = r(*chance_luck)  # получаем случайное число от experience до 10
      print("Вы попали в", change, "очков")
      if change >= 5:
          player_score += 1  # увеличиваем счет игрока при попадании >= 5
      print("Перезарядка магазина")
      time.sleep(recharge_rate)
  print("Вы закончили тренировку")
  time.sleep(1)
  experience += 1  # увеличиваем опыт после тренировки
  if recharge_rate != 1:
      recharge_rate -= 1  # уменьшаем время перезарядки
  chance_luck = (experience, 10)  # обновляем диапазон для выпадения очков
  os.system('clear')

def show_info():
  # вывод информации о победах и опыте
  print("Количество побед:", victory_score)
  print("Ваш опыт:", experience)
  time.sleep(3)
  os.system('clear')


def duel():
  global komp_health, player_health, victory_score
  print("Вы вышли на дуель...")
  time.sleep(2)
  komp_health = 10  # восстанавливаем здоровье компьютера перед дуэлью
  player_health = 10  # восстанавливаем здоровье игрока перед дуэлью
  print("Зарядка магазина")
  time.sleep(1)
  while komp_health > 0 and player_health > 0:
    player_damage = r(*chance_luck)  # урон игрока
    komp_health -= player_damage
    print("Вы нанесли противнику", player_damage)
    if komp_health <= 0:
      print("Вы победили!")
      victory_score += 1
      time.sleep(3)
      os.system('clear')
      break

    komp_damage = r(1, 10)  # урон компьютера
    player_health -= komp_damage
    print("Противник нанес вам", komp_damage)
    time.sleep(1)
    print("Ваше здоровье:", player_health)
    print("Здоровье противника:", komp_health)
    time.sleep(1)

    if player_health <= 0:
      print("Вы погибли.")
      sys.exit(1)
    print("Перезарядка магазина")
    time.sleep(recharge_rate)

def shooting_gallery():
    # Главное меню игры
  while True:
    ans_482 = int(input("""
1. Game
2. Info
3. Duel
4. Exit
Введите номер действия: 
"""))
    if ans_482 == 1:
      os.system('clear')
      training()
    elif ans_482 == 2:
      os.system('clear')
      show_info()
    elif ans_482 == 3:
      os.system('clear')
      duel()
    elif ans_482 == 4:
      os.system('clear')
      print("Выход из игры. До свидания!")
      break
    else:
      os.system('clear')
      print("Неверный ввод, попробуйте снова.")
# ---------------------------
# Главное меню
# ---------------------------
while True:
    print("""
-----menu-----
1. Game
2. Useful program
3. Game creator
4. Exit
""")

# Выбор команды
    command = input("Выберите команду: ")
    os.system('clear')

    if command == "1":
        print("""
-Game selection-
1. "Doors" game
2. "Quizz"
3. "Mit" game
4. "Click" game
5. "Shooting gallery"
""")
        command2 = input("Какую игру выберешь? ")
        os.system('clear')

        if command2 == "1":
            print("Loading Doors game")
            time.sleep(3)
            os.system('clear')
            doors_game()

        elif command2 == "2":
            print("Loading Quizz")
            time.sleep(3)
            os.system('clear')
            quizz()

        elif command2 == "3":
            print("Loading Mit game")
            time.sleep(3)
            os.system('clear')
            mit()

        elif command2 == "4":
            print("Loading Click")
            time.sleep(3)
            os.system('clear')
            click()
    
        elif command2 == "5":
            print("Loading Shooting gallery")
            time.sleep(3)
            os.system('clear')
            shooting_gallery()

    elif command == "2":
        print("""-Program selection-
1. Calculator
2. Timer
""")
        command2 = input()
        os.system('clear')

        if command2 == "1":
            print("Loading Calculator")
            time.sleep(3)
            os.system('clear')
            calculator()

        if command2 == "2":
            print("Loading Timer")
            time.sleep(3)
            os.system('clear')
            timer()

    elif command == "3":
        print("-------Creator info-------")
        print("Viktor Sekerin is the creator of this code")
        print("This exclusive version is 0.5")
        print("This version was created on 07/06/2025")
        time.sleep(10)
        os.system('clear')

    elif command == "4":
        print("Всего доброго!")
        break
    
    else:
      print("Неверный ввод, попробуйте еще раз")
      time.sleep(3)
      os.system('clear')








