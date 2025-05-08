from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)

    project = db.relationship('Project', back_populates='students')

    def __str__(self):
        return f"Student {self.id} {self.project_id}"
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    students = db.relationship('Student', back_populates='project')

    def is_student_assigned(student_id):
        return Project.query.filter(
            (Project.student_1 == student_id) |
            (Project.student_2 == student_id) |
            (Project.student_3 == student_id) |
            (Project.student_4 == student_id)
        ).first() is not None
    
    def __str__(self):
        return f"Project {self.id} {self.students}"
    