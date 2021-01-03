from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage
# Create your views here.
from django.http import HttpResponse

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'first_app/index.html',context=date_dict)
# steps 1 and 2 of MTV paradigm
