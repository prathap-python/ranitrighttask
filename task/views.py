from django.shortcuts import render
from django.http import HttpResponse
from task.models import Details,Search,GetImages
import urllib.request
import re
def home(request):
    return  render(request,"task/index.html")
def view1(request):
    msg=None
    if request.method=="POST":
        Name=request.POST.get("Name")
        Url=request.POST.get("Url")
        Phonenumber=request.POST.get("Phonenumber")
        try:
            data = Details.objects.all().get(Name__iexact=Name)
        except Details.DoesNotExist:
            d=Details(Name=Name,Url=Url,Phonenumber=Phonenumber)
            d.save()
        else:
            msg="Name already exists"

    return render(request,"task/home.html",{'msg':msg})
def view2(request):
    search=False
    data=None
    msg=None
    if request.method=="POST":
        s=request.POST.get("search")
        x=Search(SearchedName=s)
        x.save()
        try:
            data=Details.objects.all().get(Name__iexact=s)
        except Details.DoesNotExist:
            msg="Entered name not found in db "
            return render(request,"task/search.html",{'msg':msg,'data':data,'search':search})
        else:
            search=True

    return render(request,"task/search.html",{'search':search,'data':data,'msg':msg})
def view3(request):
    imgurls=None
    url=None
    if request.method=="POST":
        url=request.POST.get("url")
        x=GetImages(EnteredLink=url)
        x.save()
        urlcontent=urllib.request.urlopen(url).read().decode('utf-8')
        imgurls=re.findall('img.*?src="(.*?)"',urlcontent)
    return render(request,"task/images.html",{'imgurls':imgurls,'url':url})

# Create your views here.
