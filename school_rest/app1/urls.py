from django.urls import path
from .views import new_student,get_students,get_single_student,update_student,delete_student
urlpatterns = [
    path('add_std/',new_student),
    path('get_std/',get_students),
    path('get_std/<int:id>/',get_single_student),
    path('update_std/<int:id>/',update_student),
    path('delete_std/<int:id>/',delete_student),

]
