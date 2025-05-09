from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from app import login

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)

    password_hash = db.Column(db.String(128))

    project = db.relationship('Project', back_populates='students')

    def __str__(self):
        return f"Student {self.id} {self.project_id}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return Student.query.get(id)

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
    