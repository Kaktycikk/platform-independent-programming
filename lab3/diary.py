from pathlib import Path
from datetime import datetime
import json

folder = Path("data")
folder.mkdir(exist_ok=True)

file = folder / "notes.json"


def load_notes():
    if file.exists():
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_notes(notes):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)


def create_note():

    title = input("Заголовок: ")
    text = input("Текст: ")

    now = datetime.now()

    note = {
        "date": now.strftime("%d.%m.%Y %H:%M"),
        "title": title,
        "text": text
    }

    notes = load_notes()

    notes.append(note)

    save_notes(notes)

    print("Заметка сохранена")


def show_notes():

    notes = load_notes()

    if not notes:
        print("Заметок нет")
        return

    for i in notes:

        print()
        print("Дата:", i["date"])
        print("Заголовок:", i["title"])
        print("Текст:", i["text"])

    print()
    print("Количество заметок:", len(notes))


def find_date():

    date = input("Введите дату (ДД.ММ.ГГГГ): ")

    notes = load_notes()

    found = False

    for i in notes:

        if i["date"].startswith(date):

            print()
            print("Дата:", i["date"])
            print("Заголовок:", i["title"])
            print("Текст:", i["text"])

            found = True

    if not found:
        print("Ничего не найдено")


while True:

    print("""
=========================
ДНЕВНИК ЗАМЕТОК
=========================

1 Создать заметку
2 Показать заметки
3 Найти по дате
4 Выход
""")

    cmd = input("Выбор: ")

    if cmd == "1":
        create_note()

    elif cmd == "2":
        show_notes()

    elif cmd == "3":
        find_date()

    elif cmd == "4":
        break

    else:
        print("Ошибка")