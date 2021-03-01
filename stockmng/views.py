from django.shortcuts import render

# Create your views here.

def home(request):
     title='Welcome:This is the Home Page'
     form ='Welcome:This is the Home Page'
     context={
     "title":title,
     "test":form,
     }
     return render(request,'home.html',context)

def list_item(request):
     title='List of list_items'
     queryset=Stock.objects.all()
     context={
     "title":title,
     "queryset":queryset,
     }
     return render(request,'list_items.html',context)
