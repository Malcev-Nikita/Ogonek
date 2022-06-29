################################################################################
## Запуск игры (splashscreen)
################################################################################
init python:
    style.mm_root.background = u'#000000'

init:
    image movie = Movie(size=(config.screen_width, config.screen_height))

label main_menu:
    scene black
    show movie with fade
    $ renpy.music.play("gui/main.mpg", channel="movie", loop=-1)
    play music "audio/main_menu_music.ogg" fadein 5
    jump main_menu_screen

################################################################################
## Сюжет
################################################################################

## Персонажи ###################################################################
define YoungMan = Character("Молодой человек")
define Ferapontov = Character("Ферапонтов")
define Krasin = Character("Красин")
define Nikitenko = Character("Никитенко")
define Tonya = Character("Тоня")
define Klava = Character("Клава")
define Toporkov = Character("Топорков")

## Начало сюжета (Глава 1) #####################################################
label start:
    stop movie #без этого видео не остановится


    "Звонок из прошлого оторвал меня от чистки картофеля."

    return
