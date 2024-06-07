import random
from collections import Counter

from consts import GAMES_AMOUNT, SIMULATIONS_AMOUNT
from student import Student


def travelers_dilemma(student1: Student, student2: Student) -> tuple[int, int]:
    if student1.choice == student2.choice:
        return student1.choice, student1.choice
    elif student1.choice > student2.choice:
        return student2.choice - 2, student2.choice + 2
    elif student1.choice < student2.choice:
        return student1.choice + 2, student1.choice - 2
    raise Exception('Impossible to get here')


def find_max_utility_student(students: list[Student]) -> Student:
    max_student: Student = Student(0)
    for student in students:
        if student.average_utility() > max_student.average_utility():
            max_student = student
    return max_student


def run_simulation() -> int:
    students: list[Student] = ([Student(100) for _ in range(65)] + [Student(99) for _ in range(0)] +
                               [Student(98) for _ in range(0)] + [Student(97) for _ in range(0)] +
                               [Student(96) for _ in range(0)] + [Student(95) for _ in range(0)])
    for _ in range(GAMES_AMOUNT):
        student1, student2 = random.choices(students, k=2)
        utility1, utility2 = travelers_dilemma(student1, student2)
        student1.sum_utility += utility1
        student2.sum_utility += utility2
        student1.games_count += 1
        student2.games_count += 1
    max_student = find_max_utility_student(students)
    # print(f'Winner: {max_student}')
    return max_student.choice


def run_many():
    results: list[int] = [run_simulation() for _ in range(SIMULATIONS_AMOUNT)]
    counter: Counter = Counter(results)
    print(counter)


if __name__ == '__main__':
    run_many()
