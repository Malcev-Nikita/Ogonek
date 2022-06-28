################################################################################
## Запуск игры (splashscreen)
################################################################################
init python:
    style.mm_root.background = u'#000000'

init:
    #на весь экран
    image movie = Movie(size=(config.screen_width, config.screen_height))

label main_menu:
    scene black
    pause(0.5)
    scene movie
    $ renpy.music.play("gui/main.mpg", channel="movie", loop=False)
    play music "audio/main_menu_music.ogg" fadein 5
    jump main_menu_screen

################################################################################
## Сюжет
################################################################################

## Персонажи ###################################################################
define Ferapontov = Character("Ферапонтов")

## Начало сюжета (Глава 1) #####################################################
label start:
    stop movie #без этого видео не остановится
    "Звонок из прошлого оторвал меня от чистки картофеля."

    return
