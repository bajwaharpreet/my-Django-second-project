from django.shortcuts import render,redirect
from mytodo.models import mytodo

# Create your views here.
def homepage(request):
    alltodos=mytodo.objects.all()
    print(alltodos, "xxxxxxxxx")

    return render(request,"homepage.html",{"alltodo": alltodos})

def myalltodo(request):
    alltodos=mytodo.objects.all()
    return render(request,"alltodos.html",{"alltodo": alltodos})

def savethistodo(request):
    if request.method == "POST":
        title =request.POST.get("title")
        discription =request.POST.get("desc")
        imx= request.FILES.get("imgg")

        savethis = mytodo(title = title, discription = discription, myimage = imx)
        savethis.save()
        

    return redirect("home")
def donetodo(request):
    todo = mytodo.objects.get(id = id)

    todo.tododone=True
    todo.save()

    return redirect("home")
     
    