from django.contrib import admin
from django.urls import path
from gymapp import views
from .middlewares.auth import auth_middleware

admin.site.site_title = 'Welcome to GymHut Dashboard'
admin.site.index_title = 'Welcome to GymHut'
admin.site.site_header = 'Log in to GymHut'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('coursedetails/<str:slug>', views.coursedetails, name='coursedetails'),
    path('pricing', views.pricing, name='pricing'),
    path('services', views.services, name='services'),
    path('blogs', views.blogs, name='blogs'),
    path('blogdetails/<str:slug>',
         views.blogdetails, name='blogdetails'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('schedule', views.schedule, name='schedule'),
    #path('profile/user=<str:slug>', auth_middleware(views.profile), name='profile'),
    #path('activities/user=<str:slug>', auth_middleware(views.activities), name='activities'),
    #path(r'activities/user=(?P<slug>[^/]+)$', auth_middleware(views.activities), name='activity'),
    path('profile/user=<str:slug>', views.profile, name='profile'),
    path('activities/user=<str:slug>',
         views.activities, name='activities'),
    path(r'activities/user=(?P<slug>[^/]+)$',
         views.activities, name='activity'),
    #path('edit/<int:id>', views.edit, name='edit'),
    #path('delete/<int:id>', views.delete, name='delete')
    path('joining', auth_middleware(views.joining), name='joining'),
]
