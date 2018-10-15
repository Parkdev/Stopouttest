from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import School, Student


def school_list(request)
    school = School.objects.all()
    # templates/blog/post_detail.html
    # post가 가진 title, text, author, created_date, published_date를 적절히 출력
    context = {
        'school': school,
    }

    return render(request, 'school/school_list.html', context)


def school_detail(request, pk)
    school = School.objects.get(id=pk)

    context = {
        'school': school,
    }

    return render(request, 'school/school_detail.html', context)


def students_list(request)
    student = Student.objects.all()

    context = {
        'student': student,
    }
    return render(request, 'school/student_list.html', context)


def students_detail(request, pk)
    student = Student.objects.get(id=pk)

    context = {
        'student': student,
    }
    return render(request, 'school/student_detail.html', context)
