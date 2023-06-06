# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('[ename]', color="#EDB85E")
define n = Character("Хисуи", color = "#8DECF6")
define r = Character("Незнакомка", color = "#8DECF6")

#Музыка и звуки
define audio.wakeup = "audio/wakeup.mp3"

#Питон тут
# init python:
#     def ChangeImage(images, speaking = False):
#         if speaking == True:
#             renpy.show(images)
#         else:
#             renpy.show(images, what = images.MatrixColor(images + ".png", images.matrix.brightness(-0.5)))

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
# 1-3 сцены
    scene bg room
    with fade

    $ ename = renpy.input ("Введите имя персонажа")

    show hero

    e "*Бормочет*"

    e "Следовательно моя... Нет. Следовательно наша работа... Нет, нет. Таким образом наша проделанная работа... Да почему наша вообще. Я же один этот проект пишу."

    e "Так ладно, не отвлекаться! Осталось только дописать вывод и у меня будет ещё часик, чтобы поспать..."

    e "Лишь бы дописать вывод. И ещё чуть-чуть практическую подправить... И ещё теоретическую отредактировать..."

    e "Ещё и кофе закончился, как на зло. Выплатят стипендию, надо будет купить... И молока тоже. Последние три кружки без молока пошли так себе."

    e "*быстро печатает на клавиатуре*"

    e "Мой... Нет, нет. Наш проект оказывает неизмеримую помощь всему ученому сообществу. ВСЕ! Закончил! Наконец-то! Теперь можно ещё часик поспать до пары."

    scene bg pc
    with fade
    play music wakeup

#    e "*звонок будильника*"
    e "Что? Уже?"
    e "Почему я этого не заметил?!"

    stop music fadeout 1

    scene bg room
    with fade
    show hero

    e "Ёперный театр, вот и отдохнули часик. Вот и сдали групповой проект."
    e "Ладно, уже не важно. Нужно быстро на флешку перекинуть и бежать на автобус. Если опять опоздаю на пару, то препод этот проект вообще смотреть не станет."

#8 сцена
    scene bg peschera
    with fade
    show hero fantazia agitated:
        xalign 0.0001
        yalign 0.25
        zoom 0.7
    with dissolve

    e " Мхм… Что..?"

    show girl norm f:
        xalign 0.9999
        yalign 0.25
        zoom 0.7
    with dissolve
    pause 1.0
#     $ ChangeImage("r", speaking = True)
#     $ ChangeImage("e", speaking = False)
    r "О! Ты очнулся!"
#     $ ChangeImage("r", speaking = False)
#     $ ChangeImage("e", speaking = True)
    e " Что? Кто ты такая? Где я? Ох, чёрт, как же мне отсюда домой добираться… Помимо всех проблем ещё не хватало очнуться не пойми где… бу-бу-бу…"
#     $ ChangeImage("r", speaking = True)
#     $ ChangeImage("e", speaking = False)
    r "Эй, ты тут? Давай знакомиться! Тебя как зовут? Я Хисуи Дора, но для тебя можно просто Хису."
#     $ ChangeImage("r", speaking = False)
#     $ ChangeImage("e", speaking = True)
    e " [ename]. Где я? Точнее мы. Где мы?"
#     $ ChangeImage("n", speaking = True)
#     $ ChangeImage("e", speaking = False)
    n " Как где? Мы в самом лучшем месте на свете. Мы в твоем мире. Неужели не помнишь? Ты такой забавный."
#     $ ChangeImage("n", speaking = False)
#     $ ChangeImage("e", speaking = True)
    e " Что за чушь ты несёшь? Мне надо домой срочно, я не успею переделать проект, а если я и в этот раз получу незачё…"
#     $ ChangeImage("n", speaking = True)
#     $ ChangeImage("e", speaking = False)
    n " Стой, стой, стой! Какие зачёты?"
#     $ ChangeImage("n", speaking = True)
#     $ ChangeImage("e", speaking = False)
    n "А, я поняла! Так ты не из местных получается?"
#     $ ChangeImage("n", speaking = False)
#     $ ChangeImage("e", speaking = True)
    e "Из каких местных-неместных? Верни меня домой."
#     $ ChangeImage("n", speaking = True)
#     $ ChangeImage("e", speaking = False)
    n " Ну погоди же ты. Пойдём скорее на свежий воздух, там всё и обсудим."
#  10
# 11
# 12
    scene black
    with fade
    e " Какой кошмар с этой больницей, я ничего не успеваю, совершенно. Так, спокойно, сейчас что-нибудь поем, и садиться переделывать проект. Спокойно, я всё успею."
# 13
    scene bg room
    e "Как же хочется есть, а в холодильнике совсем пустота, ещё и денег нет. Видимо голодная смерть – ближайшее, что меня ждёт. Ох, пережить ещё один день. Спокойной ночи, неудачник Я."
    #выцветание
    scene bg pc
    with fade
    play music wakeup
    "..."
    stop music fadeout 1

    scene bg room

    e "Будто и не ложился. очередной день-испытание. Надеюсь, хоть сегодня деньги придут, а лучше пусть грузовик собьёт."

# 14
    scene black
    with fade
    "[ename] собирается с силами и идёт на учёбу."
    "После очередного бесполезного дня и занятий в течение него, [ename] направляется домой"
# 15 (пока оставить)
# 16
    scene bg kupon
    with fade
    e " Мои страдания были услышаны! Ох, наконец у меня будет свежая и горячая еда. Какое счастье."
    e "Так, надо скорее, пока кафе не закрылось."
    return

