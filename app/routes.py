from app import application
from flask import render_template, request, redirect

from app.forms import StudentForm

@application.route('/index')
def home():
    return render_template('index.html')

@application.route('/signup', methods=['GET', 'POST'])
def signup():
    form = StudentForm()
    print(request.method)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            student1 = form.student1.data
            student2 = form.student2.data
            student3 = form.student3.data
            student4 = form.student4.data

            print(student1, student2, student3, student4)
            # Here you would typically save the data to a database or process it further
            return redirect('home')
        else:
           render_template('signup.html', form=form)
         
    return render_template('signup.html', form=form)
