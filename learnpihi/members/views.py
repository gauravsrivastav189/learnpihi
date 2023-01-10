from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
	mymembers=Members.objects.all().values()
	output=''
	for x in mymembers:
		output+=x[course_name]
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
	x=request.POST['course_name']
	y=request.POST['star_rating']
	z=request.POST['comments']
	member=Members(course_name=x,star_rating=y,comments=z)
	member.save()
	return HttpResponseRedirect(reverse("index"))