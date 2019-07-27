from django.shortcuts import render
import math


# Create your views here.
def calc(request):
    if request.method == "POST":
        p = int(request.POST['Amount'])
        i = float(request.POST['Rate'])
        n = int(request.POST['Tenur'])
        emi1 = (p*i/12/100)
        emi2 = (1+i/12/100)**n
        emi3 = (1+i/12/100)**n-1
        emi = emi1*emi2/emi3
        print(emi)
        return render(request,'Schedule.html',{'emi':emi,'p':p,'i':i,'n':n})
    return render(request,'index.html')