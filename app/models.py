from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_one = db.Column(db.String(8), nullable=False)
    student_two = db.Column(db.String(8), nullable=False)
    student_three = db.Column(db.String(8), nullable=False)
    student_four = db.Column(db.String(8), nullable=False)

    @property
    def students(self):
        return [self.student_one, self.student_two, self.student_three, self.student_four]

    def is_student_assigned(student_id):
        return Project.query.filter(
            (Project.student_1 == student_id) |
            (Project.student_2 == student_id) |
            (Project.student_3 == student_id) |
            (Project.student_4 == student_id)
        ).first() is not None