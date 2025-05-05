from flask import redirect, render_template, request, url_for
from app import application
from app.forms import RegisterProjectForm
from app.models import Project
from app import db
from flask import flash

@application.route('/')
@application.route('/projects')
def view_projects():
    return render_template('index.html', projects=Project.query.all())

@application.route('/register', methods=['GET', 'POST'])
def register_project():
    form = RegisterProjectForm()
    
    if request.method == 'POST':
        student1 = form.student_id_1.data
        student2 = form.student_id_2.data
        student3 = form.student_id_3.data
        student4 = form.student_id_4.data

        # Check if any of the students are already assigned to a project

        new_project = Project(student_one=student1, student_two=student2, student_three=student3, student_four=student4)

        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('view_projects'))
    
    return render_template('register.html', form=form)