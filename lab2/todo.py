from pathlib import Path
from datetime import datetime

folder = Path("data")
folder.mkdir(exist_ok=True)

file = folder / "journal.txt"


def add_record():
    print("\n--- Добавление записи ---")

    while True:
        try:
            date = input("Введите дату (ГГГГ-ММ-ДД): ")
            datetime.strptime(date, "%Y-%m-%d")
            break
        except:
            print("Ошибка формата даты!")

    text = input("Введите текст наблюдения: ")

    while True:
        try:
            score = int(input("Введите оценку (1–10): "))
            if 1 <= score <= 10:
                break
            print("Введите число от 1 до 10")
        except:
            print("Ошибка ввода!")

    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{date}|{score}|{text}\n")

    print("Запись добавлена!")


def show_records():
    if not file.exists():
        print("Журнал пуст")
        return

    lines = file.read_text(encoding="utf-8").splitlines()

    total = 0

    print("\nДата | Оценка | Текст")

    for row in lines:
        date, score, text = row.split("|")
        total += int(score)

        print(f"{date} | {score} | {text}")

    print()
    print("Всего записей:", len(lines))
    print("Средняя оценка:", round(total / len(lines), 2))


def clear():
    file.write_text("", encoding="utf-8")
    print("Журнал очищен")


while True:

    print("""
=========================
ЖУРНАЛ НАБЛЮДЕНИЙ
=========================
1 Добавить запись
2 Показать записи
3 Очистить журнал
4 Выход
""")

    cmd = input("Выбор: ")

    if cmd == "1":
        add_record()

    elif cmd == "2":
        show_records()

    elif cmd == "3":
        clear()

    elif cmd == "4":
        break

    else:
        print("Неверный ввод")