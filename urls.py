from django.contrib import admin
from django.urls import path
# from .views import employeeview,deleteview
from .import views
from products.views import user_registration

urlpatterns = [
    # path('home/',views.home),
    # path('about/',views.about)
    # path('add/',studentview.as_view(),name='add-student')
    # path('add/',employeeview.as_view(),name='add-employee'),
    # path('delete/<int:id>/',deleteview.as_view(),name='delete-employee'),
    # path('update/<int:id>/',updateview.as_view(),name='update-employee'),
    # path('delete/<int:id>/',deleteview.as_view(),name='delete-employee')
    # path('add/',views.employee_form,name='add-employee')
    # path('add/',views.contact_view,name='add-contactform')
    # path('',views.products_view),
    # path('',views.crud,name='crud'),
    # path('update/<int:id>/',views.update_student,name='update-student')
    # path('',views.create_view,name='Create'),
    # path('read/',views.read_view,name='Read'),
    # path('update/<int:id>/',views.update_view,name='Update'),
    # path('delete/<int:id>/',views.delete_view,name="Delete"),
    path('registration/',user_registration.as_view(),name='registration'),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    
]

