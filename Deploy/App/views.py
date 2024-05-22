from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserPersonalForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import UserPersonalModel
import numpy as np

# Create your views here.
def Landing_1(request):
    return render(request,"1_landing.html")
    
def Register_2(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')
        else:
            print("form error")

    context = {'form': form}
    return render(request, "2_Register.html", context)

    
def Login_3(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,"3_Login.html", context)
    
def Home_4(request):
    return render(request,"4_Home.html")

def Teamates_5(request):
    return render(request,"5_Teamates.html")

def Domain_Result_6(request):
    return render(request,"6_Domain_Result.html")

def Problem_Statement_7(request):
    return render(request,"7_Problem_Statement.html")
    
from django.contrib import messages
from .forms import UserPersonalForm

def Per_Info_8(request):
    if request.method == 'POST':
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
            # Redirect to a different page after successful form submission
            messages.success(request,'Personal_information saved successfully')
            return render(request, '8_Per_Info.html', {'form': form})
        else:
            # Print form errors to the console for debugging
            print(form.errors)
            # Add a message to inform the user about form errors
            messages.error(request, 'Please correct the errors in the form.')
    else:
        # This part of the code will execute for GET requests
        form = UserPersonalForm()

    # Render the '8_Per_Info.html' template with the form
    return render(request, '8_Per_Info.html', {'form': form})



import joblib
Model = joblib.load('C:/Users/RV Yukesh/Music/MAIN_PROJECT/CODE/Deploy/App/RFC.pkl')
from django.shortcuts import render


def Deploy_9(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=object)]
        print(final_features)
        prediction = Model.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(f'output{output}')
        if output == 'Normal':
            return render(request, '9_Deploy.html', {"prediction":"Not Attacked"})
        elif output == 'Attack':
            return render(request, '9_Deploy.html', {"prediction":"Attacked"})
    else:
        return render(request, '9_Deploy.html')
    # return render(request, '9_Deploy.html', {'form': form})


    
def Per_Database_10(request):
    models = UserPersonalModel.objects.all()
    return render(request,'10_Per_Database.html',{'models':models})

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("Login_3")