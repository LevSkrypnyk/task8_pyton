# Словник з успішністю студентів
students = {
    "12345": {
        "name": "Іван Петренко",
        "course": 2,
        "subjects": {
            "Математика": [90, 85, 78],
            "Фізика": [88, 76, 90],
            "Програмування": [95, 98, 97]
        }
    },
    "67890": {
        "name": "Марія Коваленко",
        "course": 3,
        "subjects": {
            "Математика": [75, 80, 85],
            "Фізика": [82, 85, 78],
            "Програмування": [92, 91, 89]
        }
    }
}

# Функція для додавання нового студента
def add_student(group, name, course, subjects):
    if group in students:
        print("Студент з таким номером групи вже існує!")
    else:
        students[group] = {"name": name, "course": course, "subjects": subjects}

# Функція для видалення студента
def remove_student(group):
    try:
        del students[group]
        print(f"Студент {group} видалений.")
    except KeyError:
        print("Студент не знайдений!")

# Функція для сортування студентів за номером групи
def sort_students():
    sorted_students = dict(sorted(students.items()))
    for group, info in sorted_students.items():
        print(f"{group}: {info['name']}, Курс: {info['course']}")

# Виконання
print("Список студентів:")
sort_students()

# Додавання нового студента
test_group = "54321"
test_name = "Олег Василенко"
test_course = 1
test_subjects = {"Математика": [80, 85, 78], "Фізика": [88, 82, 90], "Програмування": [91, 94, 95]}
add_student(test_group, test_name, test_course, test_subjects)

# Видалення неіснуючого студента
remove_student("99999")
remove_student(test_group)