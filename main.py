import random
from collections import Counter

CLASS_SIZE = 70
OPT_CHOOSERS = 60
SMALLEST = 96
LARGEST = 100

OPT_CHOICE = 97

GAMES_AMOUNT = 2500
SIMULATIONS_AMOUNT = 5000


class Student:
    def __init__(self, choice: int):
        self.choice: int = choice
        self.sum_utility: int = 0
        self.games_count: int = 0

    def __repr__(self):
        return f"Choice: {self.choice}, Average utility: {self.average_utility()}"

    def average_utility(self):
        if self.games_count == 0:
            return 0
        return self.sum_utility / self.games_count


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
