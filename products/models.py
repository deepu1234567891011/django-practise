from django.db import models

# Create your models here.
# class studentdatabse(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     salary=models.IntegerField()
#     dept=models.CharField(max_length=100)

# class Employeedb(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     salary=models.IntegerField()
#     age=models.IntegerField()
#     dept=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Contact(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     message=models.TextField(default='')

#     def __str__(self):
#         return self.name


# class Student(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()

# class StudentProfile(models.Model):
#     student=models.OneToOneField(Student,on_delete=models.CASCADE)
#     city=models.CharField(max_length=100)
#     phone=models.CharField(max_length=15)

# class Employee(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     salary=models.IntegerField()
# class EmployeeProfile(models.Model):
#     employee=models.OneToOneField(Employee,on_delete=models.CASCADE)
#     address=models.CharField(max_length=100)
#     phone=models.CharField(max_length=100)

# class Department(models.Model):
#     name=models.CharField(max_length=100)
#     def __str__(self):
#         return self.name
# class StaffMember(models.Model):
#     name=models.CharField(max_length=100)
#     salary=models.IntegerField()
#     department=models.ForeignKey(Department,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name

# class Course(models.Model):
#     name=models.CharField(max_length=100)
#     def __str__(self):
#         return self.name
# class Trainee(models.Model):
#     name=models.CharField(max_length=100)
#     courses=models.ManyToManyField(Course)
#     def __str__(self):
#         return self.name