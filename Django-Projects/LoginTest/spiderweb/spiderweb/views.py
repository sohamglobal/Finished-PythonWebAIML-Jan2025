from django.shortcuts import render, redirect

def homepage(request):
    return render(request,"index.html")

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("userid")
        password = request.POST.get("password")
        if username == "admin" and password == "admin":
            request.session["is_logged_in"] = True
            request.session["username"] = username   
            return redirect("dashboard")
        else:
            return render(request,"login.html",{"error":"Invalid credentials"})
            print("Invalid credentials")
    #return render(request,"login.html")

def dashboard(request):
    if not request.session.get("is_logged_in"):
        return redirect("homepage")
    username= request.session.get("username")
    return render(request,"dashboard.html",{"username":username})

def logout(request):
    request.session.flush()  # Clear the session data
    return redirect("homepage")