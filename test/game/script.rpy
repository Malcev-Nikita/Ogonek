## Персонажи

define Ferapontov = Character("Ферапонтов")


## Видео

init -2:
    image mm_bg = Movie(play="gui/main.mpg", size=(1920, 1080))


## Заставка

label splashscreen:
    play music "audio/main_menu_music.ogg" fadein 5
    scene black
    pause(0.5)


## Стартовый экран

label main_menu:
    scene mm_bg with fade
    jump main_menu_screen


# Диалоги

label start:
    "Звонок из прошлого оторвал меня от чистки картофеля."

    return
