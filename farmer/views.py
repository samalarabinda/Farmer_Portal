from django.shortcuts import render,redirect,HttpResponse,get_object_or_404

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserInformation
from .context_data import context_data
from django.contrib.auth.models import Permission
from .models import Farmer_details
from django.core.mail import send_mail
from .models import CustomUser
# Create your views here.

def user_register(request):
    data=""
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")


        user=CustomUser.objects.filter(email=email)

        if user.exists():
            data="User name already Exists!"
            return render(request,"user_register.html",{"data":data})
        

        user=CustomUser.objects.create(
                username=username,
                email =email
                
            )
        user.set_password(password)
        user.save()

        return redirect("farmer_form/")
        data="Congratulations your Account Created successfully 😊"        
        
    return render(request,"user_register.html",{"context":data})



def user_login(request):
    data=""
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        print(CustomUser.objects.filter(email=email))
        if not CustomUser.objects.filter(email=email).exists():
            data="Incorrect username or password."
            return render(request,"user_login.html",{"data":data})
        
        user=authenticate(email=email,password=password)

        if user is None:
            data="Incorrect username or password."
            return render(request,"user_login.html",{"context":data})
        
        else:
            login(request,user)
            # return redirect("/service")
            return redirect("/user_dashboard")
             
    return render(request,"user_login.html")

# User Dashboard

@login_required(login_url="/login")
def user_dashboard(request):
    return render(request,"User_Dashboard.html")

#User add Product

@login_required(login_url="/login")
def user_product_add(request):
    return render(request,"user_product_add.html")
#User Product List

@login_required(login_url="/login")
def User_Product_details(request):
    data=""
    hold=UserInformation.objects.filter(user=request.user)
    context={
             "add":hold
         }
   
    if request.method == 'POST':
         uname=request.POST.get("name")
         uplace =request.POST.get("place")
         ublock =request.POST.get("block")
         udate =request.POST.get("date")
         product_name  =request.POST.get("product_name")
         product_weight =request.POST.get("product_weight")
         add=UserInformation(uname=uname,uplace=uplace,ublock=ublock,udate=udate,product_name=product_name,product_weight=product_weight,user=request.user)
         add.save()
         hold=UserInformation.objects.filter(user=request.user)
         data="Your Product added Successfully 😊"
         context={
             "add":hold,
             "data":data
         }
        #  return render(request,"UserAccount.html",context)
         return render(request,"user_Product_add.html",context)
    return render(request,"User_Product_details.html",context)
#User Meeting

@login_required(login_url="/login")
def User_meeting(request):
    return render(request,"User_meeting.html")



@login_required(login_url="/login")
def user_logout(request):
    logout(request)
    return redirect("/login")

# agent logout
@login_required(login_url="/agent-login")
def agent_logout(request):
    logout(request)
    return redirect("/agent_logout")

@login_required(login_url="/login")
def user_update(request,id):
    queryset=UserInformation.objects.get(id=id)
    
    if request.method=="POST":
        
    
        uname=request.POST.get("name")
        uplace =request.POST.get("place")
        ublock =request.POST.get("block")
        udate =request.POST.get("date")
        product_name  =request.POST.get("product_name")
        product_weight =request.POST.get("product_weight")
        
        queryset.uname=uname
        queryset.uplace=uplace
        queryset.ublock=ublock
        queryset.udate=udate
        queryset.product_name=product_name
        queryset.product_weight=product_weight

        queryset.save()
        
        return redirect("/service")
    

    flow={
        "update_user":queryset
    }

    return render(request,"user_update.html",flow)


#Agent product Edit
@login_required(login_url="/login")
def agent_update(request,id):
    queryset=UserInformation.objects.get(id=id)
    
    
    if request.method=="POST":
        
    
        uname=request.POST.get("name")
        uplace =request.POST.get("place")
        ublock =request.POST.get("block")
        udate =request.POST.get("date")
        product_name  =request.POST.get("product_name")
        product_weight =request.POST.get("product_weight")
        
        queryset.uname=uname
        queryset.uplace=uplace
        queryset.ublock=ublock
        queryset.udate=udate
        queryset.product_name=product_name
        queryset.product_weight=product_weight

        queryset.save()
        data="plz reselect Your state to see the changes that you currently made"   
        # return redirect("/agent-state")
        return render(request,"agent_state.html",{"data":data})
        
        # return render(request,"agent_table.html",context)
    

    flow={
        "update_user":queryset
    }

    return render(request,"user_update.html",flow)
    
    

#Agent product Edit End




# Product Manager Register And login
def agent_register(request):
    data=""
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")


        user=CustomUser.objects.filter(email=email)

        if user.exists():
            data="User name already Exist!"
            return render(request,"vendor_register.html",{"data":data})
        

        user=CustomUser.objects.create(
                username=username,
                email=email
                
            )
        user.set_password(password)
        user.save()

        # return redirect("/")
        data="Congratulations your Account Created successfully 😊,plz Login." 
        send_mail(
           "Subject here",
           "your account will be activated soon...",
           "arabinda2919@gmail.com",
           [email],
           fail_silently=False,
        )       
        
    return render(request,"vendor_register.html",{"context":data})




def agent_login(request):
    data=""
    if request.method=="POST":
        email=request.POST.get("email")
        print(email)
        password=request.POST.get("password")
        print(password)
        print(CustomUser.objects.filter(email=email))
        if not CustomUser.objects.filter(email=email).exists():
            
            data="Incorrect username or password."
            return render(request,"agent_login.html",{"data":data})
        
        user=authenticate(request,email=email,password=password)
        print(user)
        
        if user is None:
            data="Incorrect username or password."
            return render(request,"agent_login.html",{"context":data})
        
        else:
            login(request,user)
            if user.is_staff:
                return redirect("/agent-state")
                
            else:
               data="Your account is not activated !"
               return render(request,"agent_login.html",{"userdata":data})
            
             
    return render(request,"agent_login.html")


@login_required(login_url="/login")
def agent_state(request):
    return render(request,"agent_state.html")
   


global context
@login_required(login_url="/login")
def agent_table(request):
    if request.method == 'POST' and request.POST.get("district")=="":
        return render(request,"agent_state.html")
        
           
    if request.method == 'POST':
         
         ablock =request.POST.get("block")
         print(ablock)
         hold = UserInformation.objects.filter(ublock=ablock)
         print(hold)
         data="Your Product added Successfully 😊"
         context={
             "add":hold,
             "data":data
         }
         context_data.update(context)    
         
    print(context_data)
    return render(request,"agent_table.html", context_data)
    
@login_required(login_url="/login")    
def login_or_register(request):
     if request.user.is_staff and request.user.is_superuser:
      return redirect('/admin') 
     elif request.user.is_staff:
         return redirect('/agent-state') 
     else:
         return redirect('user_dashboard') 
          
      




def farmer_form(request):
    if request.method=="POST":
        your_name=request.POST.get('yourName')
        father_name=request.POST.get('fatherName')
        mobile_number=request.POST.get('mobileNumber')
        mail_id=request.POST.get('mailId')
        aadhaar_number=request.POST.get('aadhaarNumber')
        pan_card_number=request.POST.get('panNumber')
        land_area=request.POST.get('landArea')
        account_number=request.POST.get('accountNumber')
        ifsc_code=request.POST.get('ifscCode')
        bank_name=request.POST.get('bankName')
        loan_details=request.POST.get('loanDetails')
        first_time_investment_size=request.POST.get('investmentSize')
        job_card_number=request.POST.get('jobCardNumber')
        farmer_name1=request.POST.get('farmerName1')
        mobile_number1=request.POST.get('mobileNumber1')
        land1=request.POST.get('land1')
        another_farmer_name =request.POST.get('anotherFarmerName')
        mobile_number2=request.POST.get('mobileNumber2')
        land_area2=request.POST.get('landArea2')
        store=Farmer_details(your_name=your_name,father_name=father_name,mobile_number=mobile_number,mail_id=mail_id,aadhaar_number=aadhaar_number,pan_card_number=pan_card_number,
                            land_area=land_area, account_number= account_number,ifsc_code=ifsc_code, bank_name= bank_name,loan_details=loan_details,
                            first_time_investment_size=first_time_investment_size,job_card_number=job_card_number,farmer_name1=farmer_name1,mobile_number1=mobile_number1,
                             land1=land1,another_farmer_name=another_farmer_name,mobile_number2=mobile_number2,land_area2=land_area2   )

        store.save()
        return redirect("login")   
        
    return render(request, 'farmer_form.html')





#paginations


      
      