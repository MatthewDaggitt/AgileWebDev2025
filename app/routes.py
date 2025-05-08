from flask import redirect, render_template, request, url_for
from app import application
from app.forms import RegisterProjectForm
from app.models import Project, Student
from app import db

@application.route('/')
@application.route('/projects')
def view_projects():
    projects = Project.query.all()
    for p in projects:
        print(p)
    return render_template('index.html', projects=projects)

@application.route('/register', methods=['GET', 'POST'])
def register_project():
    form = RegisterProjectForm()
    
    if request.method == 'POST':
        student_ids = [
            form.student_id_1.data, 
            form.student_id_2.data, 
            form.student_id_3.data, 
            form.student_id_4.data
        ]

        new_project = Project()
        db.session.add(new_project)

        for student_id in student_ids:
            student = Student.query.get(student_id)
            if student is None:
                student = Student(id=student_id)
            
            # TODO Check if any of the students are already assigned to a project
            student.project_id = new_project.id
            db.session.add(student)

        db.session.commit()

        return redirect(url_for('view_projects'))
    
    return render_template('register.html', form=form)

@application.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')