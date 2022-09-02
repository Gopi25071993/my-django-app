from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.views.decorators.http import require_http_methods
from django.template import loader
from myapp.form import StuForm, StudentForm, EmployeesForm
from myapp.functions import handle_uploaded_file
from myapp.functions import handle_uploaded_file
from myapp.models import Employee, Employees
from django.core.exceptions import ObjectDoesNotExist
import csv
from reportlab.pdfgen import canvas
# Create your views here.


def home(request):
    return HttpResponse("<h2>Hello, Welcome to Django</h2>")


def index(request):
    # now = datetime.datetime.now()
    # html = "<html><body>Now time is %s.</body></html>" % now
    # return HttpResponse(html) # Rendering the template in HttpResponse
    # a = 0
    # if a:
    #     return HttpResponseNotFound("<h1>Page not found!</h1>")
    # else:
    #     return HttpResponse("<h1>Page found!!!</h1>")
    name = {"man": "Gopi" }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(name))


@require_http_methods(['GET'])
def show(request):
    return HttpResponse("<h1>This is HTTP GET request.</h1>")


@require_http_methods(['GET'])
def hello(request):
    return HttpResponse("<h1>This is Http GET Request from Hello</h1>")


def studentform(request):
    stu = StuForm()
    return render(request,"student_form.html", {"form":stu})

def student_form(request):
    if request.method =="POST":
        print("inside view:", request.POST)
        student = StudentForm(request.POST, request.FILES or None)
        if student.is_valid():
            handle_uploaded_file(request.POST['file'])
            return HttpResponse("File uploaded successfully!!!")
    else:
        student = StudentForm()
    return render(request,"student_form2.html",{'form':student})

def emp(request):
    if request.method == "POST":
        form = EmployeesForm(request.POST)
        if form.is_valid():
            try:
                return redirect("/")
            except:
                pass
    else:
        form = EmployeesForm()
    return render(request,'employee_form.html',{'form':form})


def methodinfo(request):
    return HttpResponse("Http request is: "+ request.method)

def getdata(request):
    try:
        data = Employee.objects.get(id=12)
    except ObjectDoesNotExist:
        return HttpResponse("Exception: Data not found")
    return HttpResponse(data)


def set_session(request):
    request.session['sname'] = 'Gopi'
    request.session['semail'] = 'gopi@gmai.com'
    return HttpResponse("Session is set")

def get_session(request):
    student_name = request.session['sname']
    student_email = request.session['semail']
    return HttpResponse(student_name + " " + student_email)

def set_cookies(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie("java-tutorial", 'javatpoint.com')
    return response


def get_cookies(request):
    tutorial = request.COOKIES['java-tutorial']
    return HttpResponse('java tutorial @: '+ tutorial)

def get_file(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment; filename = file.csv"
    employees = Employees.objects.all()
    writer = csv.writer(response)
    for employee in employees:
        writer.writerow([employee.eid, employee.ename, employee.econtact])
    # writer.writerow(['1001', 'John', 'Domil', 'CA'])
    # writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', 'Testing'])
    return response

def get_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename=mypdffile.pdf"
    p= canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100, 700, "Hello, Gopinath")
    p.showPage()
    p.save()
    return response