from django.urls import path, include
from . import views

app_name='mainsite'

urlpatterns = [
    #path('profile/', include('Accounts.urls')),
    path('',views.index,name='index'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('about-us/',views.about,name='about_us'),
    path('contact-us/',views.contact,name='contact_us'),
    path('blog/<str:blog_id>/',views.blogsingle,name='blog_single'),
    path('blog/',views.blog,name='blog'),
    path('courses/',views.courses,name='courses'),
    path('course-Details/<str:course_id>/',views.courseDetails,name='CourseDetails'),
    path('lessons/<str:lesson_id>/',views.courseLesson,name='Course_lessons')
]
