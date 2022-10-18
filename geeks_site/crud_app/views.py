from django.shortcuts import render
from django.http import HttpResponse
#from .forms import InputForm
from .forms import GeeksForm
from .models import GeeksModel
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 
 
""" def index(request):
  #return HttpResponse("Hello! welcome to my app")
# Create your views here.
    context ={}
    #context['form']= InputForm()
    context['form'] = GeeksForm()
    return render(request, "home.html", context) """

def home_view(request):
    context = {}
    #print(request.GET)
    form = GeeksForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "home.html", context)
"""     print(request.POST)
    context = {}
    form = GeeksForm(request.POST or None) """

 
    
    # logic of view will be implemented here
    #return render(request, "home.html")

from django.forms import formset_factory
  
def formset_view(request):
    context ={}
  
    # creating a formset
    #GeeksFormSet = formset_factory(GeeksForm)
    GeeksFormSet = formset_factory(GeeksForm, extra = 3)
    #formset = GeeksFormSet()
    
    #GeeksFormSet = formset_factory(GeeksForm, extra = 5)
    formset = GeeksFormSet(request.POST or None)
    #formset = GeeksFormSet()
      
    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
               
      
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)

from django.forms import modelformset_factory
  
def modelformset_view(request):
    context ={}
  
    # creating a formset and 5 instances of GeeksForm
    GeeksFormSet = modelformset_factory(GeeksModel, fields =['title', 'description'], extra = 3)
    formset = GeeksFormSet()
  
              
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context) 
   

from django.shortcuts import render
  
# create a function
""" def geeks_view(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"'Hey there welcome to my app'",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "geeks.html", context) """

# import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime
 
# create a function
def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html) 

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)

from django.views.generic.list import ListView

 
class GeeksList(ListView):
 
    # specify the model for list view
    model = GeeksModel
     

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)

from django.shortcuts import render
 
# relative import of forms
from .models import GeeksModel
 
 
def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
         
    return render(request, "detail_view.html", context)

#update
 
# after updating it will redirect to detail_View
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
          
    return render(request, "detail_view.html", context)
 
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

#delete

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 
from .models import GeeksModel
 
 
# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)