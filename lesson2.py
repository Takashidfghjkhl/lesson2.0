name = input("Привет тебе, странник, как тебя зовут ?")
print(f"Мне приятно знать твоё имя, {name}! Самое время отправиться в путишествие!")
artifact_one = False
artifact_two = False
artifact_three = False
points = 0
print(f"""{name} - ты начинаешь игру с 0 очков. В ходе игры ты будешь получаться очки, за которые ты сможешь приобрести интересные вещи и артефакты, которые помогут тебе достичь победы.
За каждый правильный ответ ты будешь получать очки:
за правильный ответ на 1-ое задание: 10 очков
за правильный ответ на 2-ое задание: 20 очков
за правильный ответ на 3-ое задание: 30 очков""")
question_one = input("Первый вопрос:\n Что всегда наступает, но никогда не приходит?")
if question_one == "завтра":
    points+=10
    artifact_one=True
    print(f"правильно! теперь у тебя {points} очков")
else:
    print(f"неправильно! у тебя всё ещё {points} очков")
question_two = input("Второй вопрос:\n Что идёт из города в город, но при этом не движется?")
if question_two == "дорога": 
    points+=20
    artifact_two=True
    print(f"правильно! теперь у тебя {points} очков")
else:
    print(f"неправильно! у тебя всё ещё {points} очков")    
question_three= input("Третий вопрос:\n Какой город является столицей Вьетнама?")
if question_three == "ханой":
    points+=30
    artifact_three=True
    print(f"правильно! теперь у тебя {points} очков")
else:
    print(f"неправильно! у тебя всё ещё {points} очков")
print("""Ты завершил испытание, можешь проследовать в магазин и выбрать себе что-нибудь одно:
1. молодильное яблоко 13 points
2. волшебный клубок 27 points
3. мороженое 14 points
4. ковер-самолёт 30 points
5. пропустить""")
choice = input("твой выбор:")
if choice == "1" and points > 13:
    points-=13
    print("Теперь у тебя есть молодильное яблоко!")
elif choice == "2" and points > 27:
    points-=27
    print("Теперь у тебя есть волшебный кубок!")
elif choice == "3" and points > 14:
    points-=14
    print("Теперь у тебя есть мороженое!")
elif choice == "4" and points > 30:
    points-=30
    print("Теперь у тебя есть ковёр самолёт!")
elif choice == "5":
    print("Заходите ещё!")
else:
    print("Недостаточно очков")

if artifact_one and artifact_two and artifact_three:
    print("Поздравляем, ты победил! счёт: 60 очкрв")
elif artifact_one and artifact_two:
    print(f"К сожалению, ты не нашёл третий артефакт. счёт: {points} очков")
elif artifact_one and artifact_three:
    print(f"К сожалению, ты не нашёл второй артефакт. счёт: {points} очков")
elif artifact_two and artifact_three:
    print(f"К сожалению, ты не нашёл первый артефакт. счёт: {points} очков")
elif artifact_two or artifact_three or artifact_one:
    print(f"К сожалению, ты не нашёл два артифакта. счёт: {points} очков")
else:
    print("Ты не нашёл ни одного артифакта")