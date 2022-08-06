from django.shortcuts import render
from accounts.models import User


def home(request):
    users = User.objects.all()
    return render(request,'info/home.html',{'users' : users})



def setReason(request,username,reason):
    user = User.objects.get(username = username)
    user.reason = reason
    user.save()

    return render(request,'info/setReasonPage.html')


def setReasonlist(request,reason):
    users = User.objects.filter(reason = reason)
    amount = 0
    for user in users:
        amount += 1
    return render(request,'info/setReason.html',{'users' : users,'amount':amount,'reason':reason})



def setReasonPage(request):
    return render(request,'info/setReasonPage.html')
