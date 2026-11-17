from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views import View
# from .models import Employeedb
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# from .models import Student,StudentProfile,Employee,EmployeeProfile,Department,StaffMember,Course,Trainee

# from .forms import contact


# Create your views here.


# def home(request):
#     return render(request,'index.html',{'name':'Deepu'})

# def about(request):
#     return HttpResponse('This is about page')

# class studentview(View):
#     def get(self,request):
#         student=studentdatabse.objects.create(
#             name="deepika",
#             email="deepikavicharapu@gmail.com",
#             salary=50000,
#             dept="IT department"
#         )
#         return HttpResponse("data register successfully!!....")


# class employeeview(View):
    # def get(self,request):
    #     employee=Employeedb.objects.create(
    #        name="deepu",
    #        email="deepu@gmail.com",
    #        salary=40000,
    #        age=23,
    #        dept="IT"

    #     )
        # return HttpResponse("data register successfully__!!____")

# class updateview(View):
#     def get(self,request,id):
#         emp=Employeedb.objects.get(id=id)
#         emp.salary=50000
#         emp.save()
#         return HttpResponse("data updated successfully deepika!!!")

# class deleteview(View):
#     def get(self,request,id):
#         emp=Employeedb.objects.get(id=id)
#         emp.delete()
#         return JsonResponse({"message": f"data deleted successfully"})

# @method_decorator(csrf_exempt,name='dispatch') 
# class employeeview(View):
#     def post(self,request):
#         data=json.loads(request.body)
#         employee=Employeedb.objects.create(
#             name=data['name'],
#             email=data['email'],
#             salary=data['salary'],
#             age=data['age'],
#             dept=data['dept']
#         )
#         return JsonResponse({
#             "message":"data added success!!",
#             # "name":employee.name
#         })

    # def get(self,request):
    #     employee=Employeedb.objects.all().values()
    #     return JsonResponse({
    #         "message":"data fetched success!!",
    #         "data":list(employee)
    #     })
        
    # def put(self,request):
    #     data=json.loads(request.body)
    #     employee=Employeedb.objects.get(id=data['id'])
                             
    #     employee.name=data['name']
    #     employee.email=data['email']
    #     employee.salary=data['salary']
    #     employee.age=data['age']
    #     employee.dept=data['dept']
    #     employee.save()
    #     return JsonResponse({
    #         "message":"data updated successfully!!"
    #     })

    # def delete(self,request):
    #     id=request.Get.get('id')
    #     employee=Employeedb.objects.get(id=id)
    #     employee.delete()
    #     return JsonResponse({
    #         "message":"data deleted successfully"
    #     })




# def employee_form(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             Employeedb.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 age=form.cleaned_data['age'],
#                 salary=form.cleaned_data['salary']
#             )
#             form.save()
#             return redirect('add-employee')
#     else:
    #     form = EmployeeForm()                        
    
    # return render(request,'employee.html',{'form':form})
        






# def contact_view(request):
#     if request.method == "POST":
#         form=contact(request.POST)
#         if form.is_valid():
#             # contact.objects.create(
#             #     name=form.cleaned_data['name'],
#             #     email=form.cleaned_data['email'],
#             #     message=form.cleaned_data['message']
#             # )
#             form.save()
#             return  redirect('add-contactform')
#     else:
#         form = contact() 
#     return render(request,'contactform.html',{'form':form})
# 
# products=[
#     {'id':1,'name':'phone','cost':1000},
#     {'id':2,'name':'washing machine','cost':14000},
#     {'id':3,'name':'VIVOmobile','cost':15000},
#     {'id':4,'name':'ac','cost':80000},
#     {'id':5,'name':'bag','cost':200}
# ] 


# def products_view(req):
#     print('hi')
#     if req.method =="POST":
#         p_name=req.POST.get('name')
#         p_cost=req.POST.get('cost')
#         id=len(products)+1
#         new_prod={
#             "id":id,
#             "name":p_name,
#             "cost":p_cost
#         }
#         products.append(new_prod)
#     return render(req,'home.html',{'products':products})
#     return JsonResponse({"status":200})



# def crud(request):
#     if request.method == "POST":
#         name=request.POST.get('name')
#         course=request.POST.get('course')
#         marks=request.POST.get('marks')
#     return render(request,'crud.html')

# students_data=[]
# def crud(request):
#     if request.method == "POST":
#         name=request.POST.get('Name')
#         course=request.POST.get('Course')
#         marks=request.POST.get('Marks')

#         student={
#             'name':name,
#             'course':course,
#             'marks':marks
#         }
#         students_data.append(student)
#     return render(request,'read crud.html',{'students':students_data})




# def update_student(request,id):
#     student_to_update=None
#     for s in students_data:
#         if s['id'] == id:
#             student_to_update=s
#             break

    # if request.method == "POST":
    #     name=request.POST.get('Name')
    #     course=request.POST.get('Course')
    #     marks=request.POST.get('Marks')

    #     student={
    #         'id':len(students_data)+1,
    #         'name':name,
    #         'course':course,
    #         'marks':marks
    #     }
    #     students_data.append(student)
    # return render(request,'read crud.html',{'students':students_data})

# students=[]
# def create_view(request):
#     if request.method == "POST":
#         name=request.POST.get('name')
#         age=request.POST.get('age')
#         course=request.POST.get('course')
#         students.append({
#             'id':len(students)+1,
#             'name':name,
#             'age':age,
#             'course':course
#         })
#         return redirect('Read')
#     return render(request,'create.html')
    

# def read_view(request):
#     return render(request,'read.html',{'students':students})


# def update_view(request,id):
#     for student in students:
#         if student['id'] == id:
#             if request.method == 'POST':
#                 student['name']=request.POST.get('name')
#                 student['age']=request.POST.get('age')
#                 student['course']=request.POST.get('course')
#                 return redirect('Read')
#             return render(request,'update.html',{'student':student})

# def delete_view(request,id):
#     global students
#     students=[s for s in students if s['id']!=id]
#     return redirect('Read')


# class user_registration(View):

#     def get(self,request):
#         return render(request,"reg.html")

#     def post(self,request):
#         if request.method == "POST":
#             username=request.POST.get("user_name")
#             email=request.POST.get("user_mail")
#             password=request.POST.get("user_password")
#             p2=request.POST.get("confirm_password")

            # if password!=p2:
            #     return HttpResponse("<h1>password dont match!!check once!!</h1>")
            #     # password validation
            # try:
            #     validate_password(password)
            # except ValidationError as e:
            #     return HttpResponse(e.messages)
            #     # username validation
            # if User.objects.filter(username=username).exists():
            #     return HttpResponse("Username already exists!")
            #     # email validation
            # if User.objects.filter(email=email).exists():
            #     return HttpResponse("Email already exista!!")
            
            # u=User.objects.create_user(username=username,email=email,password=password)
            # return HttpResponse("<h1>register successfull!!</h1>")


# def login_user(request):
#     if request.method == "POST":
#         username=request.POST.get("user_name")
#         password=request.POST.get("user_password")
        
#         user=authenticate(request,username=username,password=password)
        
#         if user is not None:
#             login(request,user)
#             return HttpResponse("<h1>Login SuccessFully!!</h1>")
#         else:
#             return HttpResponse("<h1Invalid username!!</h1>")
#     else:
#         return render(request,"login.html")


# def logout_user(request):
#     logout(request)
#     messages.success(request,"Logged out Successfully!!")
#     return redirect("login")



# def add_student(request):
#     s= Student.objects.create(name="deepika",email="deepu@gmail.com") 
#     StudentProfile.objects.create(student=s,city="Hyderabad",phone="1234567890")
#     s=Student.objects.get(id=1)
#     print(s.studentprofile.city)
#     return HttpResponse("Student and profile created successfully!!")

# def add_employee(request):
#     e1=Employee.objects.create(name="sri",email="sri@gmail.com",salary=25000)
#     EmployeeProfile.objects.create(employee=e1,address="HYD",phone=1234567890)

#     e2=Employee.objects.create(name="deepika",email="deepika@gmail.com",salary=30000)
#     EmployeeProfile.objects.create(employee=e2,address="kphb",phone=3987654321)

#     e3=Employee.objects.create(name="swapna",email="swa@gmail.com",salary=31000)
#     EmployeeProfile.objects.create(employee=e3,address="miyapur",phone=3987653421)

#     print(e3.employeeprofile.address)
#     return HttpResponse("Employees and profiles added successfully!!")


# def add_department(request):
#     d1=Department.objects.create(name="PYTHON")
#     StaffMember.objects.create(name="vinnay",salary=231,department=d1)
#     d2=Department.objects.create(name="AI")
#     StaffMember.objects.create(name="deepu",salary=38000,department=d2)
#     d3=Department.objects.create(name="PANDAS")
#     StaffMember.objects.create(name="deepu",salary=38000,department=d3)
#     d4=Department.objects.create(name="REACT")
#     StaffMember.objects.create(name="deepu",salary=38000,department=d4)
#     d5=Department.objects.create(name="JAVASCRIPT")
#     StaffMember.objects.create(name="deepu",salary=38000,department=d5)
#     return HttpResponse("depaartment & employee addedd successfully!!")

# def add_course(request):
#     c1=Course.objects.create(name="Djnago")
#     c2=Course.objects.create(name="Djnagorestapi")
#     c3=Course.objects.create(name="html")
#     c4=Course.objects.create(name="llm")
#     t1=Trainee.objects.create(name="deepika")
#     t1.courses.add(c1,c2,c3,c4)
#     return HttpResponse("Couses & Deprtment addedd succssfully!!")
       
       
       
       # sessions
def set_session(request):
    request.session['username']='vicharapu sriDeepika'
    return HttpResponse("Session Created Successfully!!")

def get_session(request):
    username=request.session.get('username')
    return HttpResponse(f"Welcome {username}")

    # cookies

def set_cookie(request):
    response=HttpResponse("Cookie Created Successfully")
    response.set_cookie('username','sriDeepika')
    return response 

    
        