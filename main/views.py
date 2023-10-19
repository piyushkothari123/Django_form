from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ResponseForm 

# Create your views here.
def home(request):
   if request.method=='POST':
      form = ResponseForm(request.POST)
      if form.is_valid():
        # print(form.name,form.phone,form.Query_date,form.Query)
        return HttpResponse('Thank You') 
   else:
      form = ResponseForm()
    
    
    
   return render(request,'index.html',{'form':form})
   


        