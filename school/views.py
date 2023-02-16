from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(marks=70)
    # student_data = Student.objects.exclude(marks=70)
    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by('-marks')
    # student_data = Student.objects.order_by('?')
    # student_data = Student.objects.order_by('id').reverse()[0:3]
    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name', 'city')
    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('id', 'name', named=True)
    # student_data = Student.objects.using('default')
    # student_data = Student.objects.dates('pass_date', 'month')
    
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1, all=True)

    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=6, roll=106)
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=107)
    student_data = Student.objects.filter(Q(id=6) | Q(roll=105))

    print("Return:", student_data)
    print()
    print("SQL Query:", student_data.query)
    return render(request, 'school/home.html', {'students':student_data})