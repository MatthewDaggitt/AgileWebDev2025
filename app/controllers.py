from app.models import Student
from app import db


def try_to_login_user(student_id, password, registering):
    student = Student.query.get(student_id)
    if registering:
        if student:
            return f"User {student.id} already exists"
        else:
            student = Student(id=student_id)
            student.set_password(password)
            db.session.add(student)
            db.session.commit()
            return student

    else:
        if not student:
            return 'User does not exist'
        elif not student.check_password(password):
            return 'Wrong password'
        else:
            return student
        