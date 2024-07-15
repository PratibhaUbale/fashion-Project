from django.shortcuts import render,HttpResponse,redirect
from call_app.models import Msg
# from django.views import View

# Create your views here.
def About(request):
    return HttpResponse('this is about page')


def Home(request):
    return HttpResponse('This is home page')

def create(request):
    if request.method == 'POST':
        # print("method is:",request.method)
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        # print("data is :",n)
        # return HttpResponse("Insert data into database")
        return redirect('/')
    else:
        # print("method is:",request.method)
        return render(request,'create.html')

# def hello(request):
#     context= {}
#     context['products']=[
#        {'id':1,'name':'samsung','cat':'mobile','price':2000}, 
#        {'id':2,'name':'samsung','cat':'mobile','price':2000}, 
#        {'id':3,'name':'samsung','cat':'mobile','price':2000}, 
#        {'id':4,'name':'samsung','cat':'mobile','price':2000}, 

#     ]
#     return render(request,'hello.html',context)

def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
    # return HttpResponse("data featched from database")