from django.contrib import admin
from django.urls import path
from leaveapp.views import *
urlpatterns = [
    
    path('apply_leave/',apply_leave,name='apply_leave'),
    path('my_leaves/',my_leaves,name='my_leaves'),
    path('view_leaves/',view_leaves,name='view_leaves'),
    path('approve/<int:id>/',approve_leave,name='approve_leave'),
    path('reject/<int:id>/',reject_leave,name='reject_leave'),
]