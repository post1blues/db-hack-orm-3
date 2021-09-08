# Скрипты для работы с БД школы
Короткие функции, написанные с целью помочь ученикам
делать свою жизнь в школе лучше, изменяя вдойки
и тройки на пятерки, удаляя замечания учителей 
и оставляя себе похвалы "от учителей" :)

## Описание функций
Код состоит из трех функций:
1. `fix_marks` - функция принимает как аргумент объект модели Schoolkid, 
после чего делает выборку из БД двоек и троек данного школьника и меняет их
на пятерки;
2. `remove_chastisements` - функция принимает как аргумент объект модели Schoolkid,
делает выборку из БД всех замечаний данного школьника и удаляет их;
3. `create_commendation` - функция принимает в себя два аргумента: Имя и Фамилию
(к примеру `Иван Фролов`) и название предмета (к примеру `Математика`). 
После чего находит в БД данного студента и уроки, и создает для случайного урока 
запись в БД с похвалой данного ученика от учителя.

## Как установить и использовать
Для работы скрипта необходимо скачать и установить 
приложение ["Электронный дневник школы"](https://github.com/devmanorg/e-diary/).

После этого скачайте файл `scripts.py` и положите в 
корень приложения рядом с файлом `manage.py`.

Все! Остается просто запустить скрипт командой `python scripts.py` и 
следовать дальнейшим инструкциям программы.

Пример интерфейса можно посмотреть на скрине:

![Скриншот](https://image.prntscr.com/image/EzloxOy5TmOhkGu--hJJ0g.png)

## Цель проекта
Код написан в учебных целях в рамках модуля Django проекта
[Devman](https://dvmn.org/).

