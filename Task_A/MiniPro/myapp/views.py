from django.shortcuts import render,redirect
from .models import Info
from django.contrib import messages
def home(request):
    try:
        users = Info.objects.all()
        user_names = [user.name for user in users]
        user_sports = [user.sport for user in users]
        request.session['user_info'] = list(zip(user_names, user_sports))
        if request.method == "POST":  
            user_name = request.POST['name']
            user_sport = request.POST['sport']
            user_file = request.FILES['file']
            info = Info.objects.create(
                name=user_name,
                sport=user_sport,
                file=user_file
            )
            messages.error(request, f"User Info creation of {info.name} successful")
            return redirect('home')  
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
    return render(request, 'home.html', {'users': users})

def delete(request):
    try:
        if request.method == "POST":  
            user_name = request.POST['name']
            info=Info.objects.get(name=user_name)
            info.delete()
            messages.success(request, f"User Info Deletion of {info.name} successful")
            return redirect('home')  
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('home')
    return render(request, 'home.html', {'users': users})