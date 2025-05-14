from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from app.controllers import try_to_login_user
from app.forms import LoginForm, RegisterProjectForm
from app.models import Project, Student
from app import db
from app.blueprints import blueprint


@blueprint.route('/')
@blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == "POST":
        student_id = form.student_id.data
        password = form.password.data
        registering = form.register.data

        result = try_to_login_user(student_id, password, registering)
        if isinstance(result, Student):
            login_user(result)
            return redirect(url_for('main.view_projects'))    
        else:
            flash(result, 'error')

    return render_template('login.html', form=form)

@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@blueprint.route('/projects')
@login_required
def view_projects():
    projects = Project.query.all()
    for p in projects:
        print(p)
    return render_template('index.html', projects=projects)

@blueprint.route('/register', methods=['GET', 'POST'])
@login_required
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

        return redirect(url_for('main.view_projects'))
    
    return render_template('register.html', form=form)
