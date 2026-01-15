from django.shortcuts import render
from django.http import FileResponse, Http404
from .models import Hero, About, Skill, TimelineEvent, Project


def home(request):
    hero = Hero.objects.first()
    return render(request, 'home.html', {'hero': hero})


from .models import CV

def about(request):
    context = {
        "about_info": About.objects.first(),
        "skills": Skill.objects.all(),
        "timeline": TimelineEvent.objects.all(),
        "cvs": CV.objects.all(),  
    }
    return render(request, "about.html", context)



def services(request):
    return render(request, 'services.html')




def download_cv(request):
    about_info = About.objects.first()
    if about_info and about_info.cv:
        return FileResponse(
            about_info.cv.open('rb'),
            as_attachment=True,
            filename="Mcondisi_CV.pdf",
            content_type='application/pdf'
        )
    raise Http404("CV not found")
