import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import Mark, Schoolkid, Chastisement, Lesson, Commendation


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
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

    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except ObjectDoesNotExist:
        print("Скрипт не нашел такого ученика. Проверь пожалуйста имя и попробуй еще раз.")
        exit()
    except MultipleObjectsReturned:
        print("В базе данных несколько учеников с таким именем. Уточни запрос и попробуй еще раз.")
        exit()

    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title__contains=subject
    )

    if not lessons:
        print("Скрипт не нашел таких уроков. Проверь название урока и попробуй еще раз")
        exit()

    lesson = random.choice(lessons)
    commendation = random.choice(commendation_examples)

    Commendation.objects.create(
        text=commendation,
        created=lesson.date,
        subject=lesson.subject,
        teacher=lesson.teacher,
        schoolkid=schoolkid
    )
