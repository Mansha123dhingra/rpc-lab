class StudentProfile:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades


def validate_types(data):
    if not isinstance(data["name"], str):
        raise TypeError("name must be string")

    if not isinstance(data["id"], int):
        raise TypeError("id must be int")

    if not isinstance(data["grades"], list):
        raise TypeError("grades must be list")

    for g in data["grades"]:
        if not isinstance(g, int):
            raise TypeError("each grade must be int")


def calculate_grade_average(profile):
    return sum(profile.grades) / len(profile.grades)


def handle_request(data):
    validate_types(data)
    student = StudentProfile(data["name"], data["id"], data["grades"])
    return calculate_grade_average(student)
