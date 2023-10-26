from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students = Student.objects.all()
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')

    return render(request, 'myapp/students.html', {'students': students, 'form': form})

def courses(request):
    courses = Course.objects.all()
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')

    return render(request, 'myapp/courses.html', {'courses': courses, 'form': form})

def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    not_registered_courses = Course.objects.exclude(students=student)

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            course = Course.objects.get(pk=course_id)
            student.courses.add(course)

    return render(request, 'myapp/details.html', {'student': student, 'not_registered_courses': not_registered_courses})

