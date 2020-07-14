from django.shortcuts import render
from .models import *
from django.contrib import messages


def index(request):
    courses = Course.objects.all().order_by('-id')[:3]
    blogs = Blog.objects.all().order_by('-date_created')[:3]
    context = {'courses': courses, 'blogs': blogs}
    return render(request, 'mainsite/index.html', context)


def about(request):
    context = {}
    return render(request, 'mainsite/about.html', context)


def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        messages.info(request, 'Thank you for Contacting us ' +
                      name + ", We shall get back to you very soon")

        print(message)
        print(name)
        print(email)
        print(subject)

    context = {}
    return render(request, 'mainsite/contact.html', context)


def blogsingle(request, blog_id):
    blogs = Blog.objects.all().order_by('-date_created')[:7]
    blog = Blog.objects.get(pk=blog_id)
    comments = BlogComments.objects.filter(post=blog).order_by('-id')
    if request.method == 'POST':
        name = request.user.username
        email = request.user.email
        comment = request.POST['comment']
        BlogComments.objects.create(
            post=blog, name=name, email=email, comment=comment)

    context = {'blog': blog, 'comments': comments, 'blogs': blogs}
    return render(request, 'mainsite/blogpost.html', context)


def blog(request):
    courses = Course.objects.all().order_by('-id')[:3]
    blogs = Blog.objects.all().order_by('-id')[:10]
    context = {'blogs': blogs, 'courses': courses}
    return render(request, 'mainsite/blog.html', context)


def courses(request):
    courses = Course.objects.all().order_by('tag')
    context = {'courses': courses}
    return render(request, 'mainsite/courses.html', context)


def courseDetails(request, course_id):
    course = Course.objects.get(pk=course_id)
    lesson = lessons.objects.filter(course=course).order_by('postion')
    reviews = coursefeedback.objects.filter(course=course).order_by('-id')
    if request.method == 'POST':
        name = request.user.username
        comment = request.POST['feedback']
        coursefeedback.objects.create(
            course=course, name=name, comment=comment)
    context = {'course': course, 'lesson': lesson, 'reviews': reviews}
    return render(request, 'mainsite/courseDetails.html', context)


def courseLesson(request, lesson_id):
    lesson = lessons.objects.get(pk=lesson_id)
    reviews = lessonfeedback.objects.filter(lesson=lesson).order_by('-id')
    if request.method == 'POST':
        name = request.user.username
        comment = request.POST['feedback']
        lessonfeedback.objects.create(
            lesson=lesson, name=name, comment=comment)

    context = {'lesson': lesson,'reviews':reviews}
    return render(request, 'mainsite/lesson.html', context)
