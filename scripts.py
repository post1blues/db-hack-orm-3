import random
import os
import django
import textwrap


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from datacenter.models import Mark, Schoolkid, Chastisement, Lesson, Commendation


def get_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        exit("Скрипт не нашел такого ученика. Проверь пожалуйста имя и попробуй еще раз.")
    except Schoolkid.MultipleObjectsReturned:
        exit("В базе данных несколько учеников с таким именем. Уточни запрос и попробуй еще раз.")
    return schoolkid


def fix_marks(full_name):
    schoolkid = get_schoolkid(full_name)
    marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(full_name):
    schoolkid = get_schoolkid(full_name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(full_name, subject):
    commendation_examples = [
        "Молодец!", "Отлично!", "Лучше, чем я ожидал", "Ты меня приятно удивил!",
        "Великолепно", "Прекрасно!", "Очень обрадовал", "Здорово!", "Хвалю!",
        "Я тобой горжусь", "Потрясающе!", "Ты как всегда точен",
        "Ты растешь над собой", "Настоящий молодец", "Я вижу, как ты стараешься!",
        "Так держать!", "Изумительно!", "Просто молодец!", "Лучший в классе!"
    ]

    schoolkid = get_schoolkid(full_name)

    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title__contains=subject
    )

    if not lessons:
        exit("Скрипт не нашел таких уроков. Проверь название урока и попробуй еще раз")

    lesson = random.choice(lessons)
    commendation = random.choice(commendation_examples)

    Commendation.objects.create(
        text=commendation,
        created=lesson.date,
        subject=lesson.subject,
        teacher=lesson.teacher,
        schoolkid=schoolkid
    )


if __name__ == "__main__":

    print("Привет! Этот скрипт позволит сделать твою школьную жизнь проще!")

    while True:
        answer = input(textwrap.dedent("""\
        Введи:
        1 - если хочешь исправить свои оценки на 5-ки;
        2 - если хочешь убрать все замечания преподавателей;
        3 - если хочешь добавить похвалу;
        exit - если хочешь завершить работу программы
        """)).strip()

        if answer == "exit":
            exit("Пока!")
        elif answer in ["1", "2", "3"]:
            input_full_name = input(
                "Введи Имя и Фамилию (как это записано в электронном журнале):\n"
            ).strip()

            if answer == "1":
                fix_marks(input_full_name)
            elif answer == "2":
                remove_chastisements(input_full_name)
            else:
                input_subject = input(
                    "Введи предмет (как записано в электронном журнале):\n"
                ).strip()
                create_commendation(input_full_name, input_subject)
            print("Готово!\nХочешь изменить что-то еще?")

        else:
            print("Не понимаю что ты хочешь. Попробуй еще раз.")
            continue




