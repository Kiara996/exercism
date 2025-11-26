class School:
    def __init__(self):
        self.database = {}
        self.addition_results = []

    def add_student(self, name, grade):
        for students_in_grade in self.database.values():
            if name in students_in_grade:
                self.addition_results.append(False)
                return False

        if grade not in self.database:
            self.database[grade] = []

        self.database[grade].append(name)
        self.addition_results.append(True)
        return True

    def roster(self):
        full_roster = []
        sorted_grades = sorted(self.database.keys())

        for kelas in sorted_grades:
            students = sorted(self.database[kelas])
            full_roster.extend(students)
        return full_roster

    def grade(self, grade_number):
        if grade_number not in self.database:
            return []
        return sorted(self.database[grade_number])

    def added(self):
        return self.addition_results
