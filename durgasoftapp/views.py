from django.shortcuts import render
from durgasoftapp.models import Service,ContactData
def home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request,'aboutus.html')
def contact(request):
    if request.method=="POST":
        sname1=request.POST.get('sname')
        semail1=request.POST.get('semail')
        smobile1=request.POST.get('smobile')
        slocation1=request.POST.get('slocation')
        cdata=ContactData(
            name=sname1,
            email=semail1,
            mobile=smobile1,
            location=slocation1
        )
        cdata.save()
        return render(request,'contact.html')
    else:
        return render(request, 'contact.html')

def services(request):
    pdata = Service.objects.filter()
    return render(request, 'services.html', {'pdata': pdata})


def gallery(request):
    return render(request,'gallery.html')

