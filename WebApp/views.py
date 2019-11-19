from django.shortcuts import render
import datetime

# Create your views here.
def Date_View(request):
    date = datetime.datetime.now()
    name = "PYTHON DJANGO"
    dic = {'dt_now': date, 'name': name}
    return render(request, 'WebApp/Welcome.html', dic)
