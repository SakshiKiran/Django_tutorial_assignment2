""" from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  #path('',views.index),
  path('', views.home_view),
] """

from django.contrib import admin
from django.urls import path
from .models import GeeksModel
from . import views
#from .views import geeks_view
from .views import list_view
#from .views import GeeksList
from .views import detail_view
from .views import update_view
from .views import delete_view




#now import the views.py file into this code

urlpatterns=[
  path('admin/',admin.site.urls),
  path('add/',views.home_view),
  path('add/',views.formset_view),
  path('add/',views.modelformset_view),
  #path('', geeks_view),
  path('', views.list_view),
  #path('', GeeksList.as_view()),
  path('', views.create_view),
  path('<id>', detail_view ),
  path('<id>/update', update_view ),
  path('<id>/delete', delete_view ),

]

 
