from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('show', views.show, name='show'),
    path('hello', views.hello, name='hello'),
    path('studentform', views.studentform, name='studentform'),
    path('studentform2', views.student_form, name='studentform2'),
    path('employeeform', views.emp, name='employeeform'),
    path('info', views.methodinfo, name='info'),
    path('get', views.getdata, name='get'),
    path('ssession',views.set_session, name='ssession'),
    path('gsession',views.get_session, name='gsession'),
    path('scookie',views.set_cookies, name='scookie'),
    path('gcookie',views.get_cookies, name='gcookie'),
    path('csv', views.get_file, name='csv'),
    path('pdf', views.get_pdf, name='pdf'),
]