from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")


def projects (request):
    projects_show=[
        
        {
            'title': ' Flask CRUD',
            'path': 'images/CRUD.PNG',
        },

          {
            'title': 'To To List',
            'path': 'images/todolist.PNG',
        },
         {
            'title': 'Portfolio Website',
            'path': 'images/portfolio.PNG',
        }
        # {
        #     'title': 'Event Management System',
        #     'path': 'images/event.PNG',
        # }


    ]
    return render (request,"projects.html",{"projects_show": projects_show})


def experience(request):
    experience=[
        {"company":"Codenera Pvt Ltd",
         "position":"Python Full Stack developer trainee",
         "year":"6 month"},

        {"company":"Unicus Infolabs Pvt ltd",
         "position":"Python Software Engineer",
         "year":"8 month"}
    ]
    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")

def education(request):
    return render (request, "education.html")


def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/suraj_kumar_cv.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="suraj_kumar_cv.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)
