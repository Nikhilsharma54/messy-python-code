GRADE_LIMITS = [(90, "A"), (75, "B"), (60, "C")]


def calculate_average(marks):
    """Return the average of a list of marks."""
    return sum(marks) / len(marks)


def get_grade(average):
    """Return the letter grade for an average mark."""
    for limit, grade in GRADE_LIMITS:
        if average >= limit:
            return grade
    return "F"


def print_result(student, marks):
    average = calculate_average(marks)
    print(f"{student}: average {average:.1f}, grade {get_grade(average)}")


if __name__ == "__main__":
    print_result("Student 1", [88, 92, 79])
    print_result("Student 2", [55, 61, 70])
