from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def account(request):
    return render(request,'account.html')
def loans(request):
    return render(request,'loans.html')
def cards(request):
    return render(request,'cards.html')