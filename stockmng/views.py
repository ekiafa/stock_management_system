from django.shortcuts import render
from .models import Stock
from .forms import StockCreateForm,StockSearchForm
from django.shortcuts import render,redirect
# Create your views here.

def home(request):
     title='Welcome:This is the Home Page'
     form ='Welcome:This is the Home Page'
     context={
     "title":title,
     "test":form,
     }
     return render(request,'home.html',context)

def list_items(request):
     title='List of list_items'
     form=StockSearchForm(request.Post or None)
     queryset=Stock.objects.all()
     context={
     "title":title,
     "queryset":queryset,
     }
     if request.method=="POST":
        queryset=Stock.objects.filter(name_icontains=form['name'].value(),
                                    sector_icontains=form['sector'].value())
            context={"form":form,"header"=header,"queryset"=queryset,
     }

     return render(request,'list_items.html',context)

def add_items(request):
     form= StockCreateForm(request.POST or None)
     if form.is_valid():
         form.save()
         return redirect('/list_items')
     context={
         "form" :form,
         "title":"Add Item",
     }
     return render(request,"add_items.html",context)