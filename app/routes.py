from flask import redirect, render_template, request, url_for
from app import application
from app.forms import RegisterProjectForm
from app.models import Project

projects = [
    Project(students=[ "00123456", "00123452", "00123453", "00123451"]),
    Project(students=[ "00123457", "00123453", "00123452", "00123456"])
    ]

@application.route('/projects')
def view_projects():
    return render_template('index.html', projects=projects)

@application.route('/register', methods=['GET', 'POST'])
def register_project():
    form = RegisterProjectForm()
    
    if request.method == 'POST':
        student1 = form.student_id_1.data
        student2 = form.student_id_2.data
        student3 = form.student_id_3.data
        student4 = form.student_id_4.data
        new_project = Project(students=[student1, student2, student3, student4])
        projects.append(new_project)
        return redirect(url_for('view_projects'))
    
    return render_template('register.html', form=form)