from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse


def index(request):
	mymembers=Members.objects.all().values()
	template=loader.get_template("index.html")
	context={
	"mymembers":mymembers,
	}
	return HttpResponse(template.render(context,request))

# Create your views here.
def add(request):
	template=loader.get_template("add.html")
	return HttpResponse(template.render({},request))

def addcomment(request):
	x=request.POST.get('course',False)
	y=request.POST.get('star',False)
	z=request.POST.get('cmt',False)
	member=Members(course_name=x,star_rating=y,comments=z)
	member.save()
	return HttpResponseRedirect(reverse("index"))
