from django.shortcuts import render

# Create your views here.

def website(request):
    return render(request, 'web.html')
    
def anime_list(request):
    return render(request, 'animes_list.html')

def anime_list_2(request):
    return render(request, 'animes_list2.html')

def anime_list_3(request):
    return render(request, 'animes_list3.html')

def ongoing(request):
    return render(request, 'ongoing_list.html')

def ongoing_2(request):
    return render(request, 'ongoing_list2.html')

def upcoming(request):
    return render(request, 'upcoming_list.html')

def upcoming_2(request):
    return render(request, 'upcoming_list2.html')

def completed(request):
    return render(request, 'completed_list.html')

def web_2(request):
    return render(request, 'web2.html')

def web_3(request):
    return render(request, 'web_3.html')

def login(request):
    return render(request, 'login_list.html')

def password(request):
    return render(request, 'pwd.html')
