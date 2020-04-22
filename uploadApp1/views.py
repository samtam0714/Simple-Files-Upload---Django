from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def uploadImage(request):
    print("Request Handing......")
    #print(request.FILES['image'])
    p = request.FILES['image'];
    from .models import User
    user = User(pic = p)
    user.save();
    return render(request, 'index.html')