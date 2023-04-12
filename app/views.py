from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from app.models import *
def display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_Topic.html',d)
def display_Webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='r')
    LOW=Webpage.objects.filter(name__startswith='ra')
    LOW=Webpage.objects.filter(name__endswith='j')
    LOW=Webpage.objects.filter(name__endswith='aj')
    LOW=Webpage.objects.filter(name__in=('dhoni','raj','rahul'))
    LOW=Webpage.objects.filter(name__contains='h')
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{5}')
    LOW=Webpage.objects.filter(name__endswith='raj')
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(Q(name='dhoni')& Q(mail='dhonigmail.com'))
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__endswith='raj')
    d={'webpages':LOW}
    return render(request,'display_Webpage.html',d)
def Access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='1998-10-23')
    LOA=AccessRecord.objects.filter(date__gte='1998-10-23')
    LOA=AccessRecord.objects.filter(date__lt='2000-11-23')
    LOA=AccessRecord.objects.filter(date__lte='2000-11-23')
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__year='1989')
    LOA=AccessRecord.objects.filter(date__month='11')
    LOA=AccessRecord.objects.filter(date__day='23')
    LOA=AccessRecord.objects.filter(date__year__gt='1989')
    LOA=AccessRecord.objects.filter(date__year__lt='2000')
    d={'access':LOA}
    return render(request,'Access.html',d)