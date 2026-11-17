from django.contrib import admin

# Register your models here.
from app1.models import students

class students_admin(admin.ModelAdmin):
    list_display=['student_id','student_name','student_age']
    ordering=['student_id']
admin.site.register(students,students_admin)



