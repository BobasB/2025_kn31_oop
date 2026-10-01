from dataclasses import dataclass, field


def validate_score(score: float) -> None:
    if not isinstance(score, (int, float)) or isinstance(score, bool):
        raise TypeError("Оцінка має бути числом.")
    if not 0 <= score <= 100:
        raise ValueError("Оцінка має бути від 0 до 100.")
    return None


def calculate_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("Неможливо обчислити середнє без оцінок.")
    for score in scores:
        validate_score(score)
    return sum(scores) / len(scores)


def letter_grade(score: float) -> str:
    validate_score(score)
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


@dataclass
class GradeBook:
    _grades: dict[str, list[float]] = field(default_factory=dict)

    def add_grade(self, student: str, score: float) -> None:
        name = student.strip()
        if not name:
            raise ValueError("Ім'я учня не може бути порожнім.")
        validate_score(score)
        self._grades.setdefault(name, []).append(score)

    def get_average(self, student: str) -> float:
        name = student.strip()
        if name not in self._grades:
            raise KeyError(f"Учня не знайдено: {name}")
        return calculate_average(self._grades[name])

    def get_letter_grade(self, student: str) -> str:
        return letter_grade(self.get_average(student))

    def students(self) -> list[str]:
        return sorted(self._grades)


def main() -> None:
    grade_book = GradeBook()
    grade_book.add_grade("Олена", 92)
    grade_book.add_grade("Олена", 84)
    grade_book.add_grade("Андрій", 67)

    for student in grade_book.students():
        average = grade_book.get_average(student)
        grade = grade_book.get_letter_grade(student)
        print(f"{student}: середній бал {average:.1f} ({grade})")


if __name__ == "__main__":
    main()