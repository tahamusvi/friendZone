from django.shortcuts import render
from accounts.models import User


def home(request):
    users = User.objects.all()
    return render(request,'info/homeSecond.html',{'users' : users})
#---------------------------------------------------------------------------------------
def setReason(request,username,reason):
    user = User.objects.get(username = username)
    user.reason = reason
    user.save()


    return render(request,'info/setReasonPage.html')
#---------------------------------------------------------------------------------------
def setReasonlist(request,reason):
    users = User.objects.filter(reason = reason)
    amount = 0
    for user in users:
        amount += 1
    return render(request,'info/setReason.html',{'users' : users,'amount':amount,'reason':reason})
#---------------------------------------------------------------------------------------
def setReasonPage(request):
    return render(request,'info/setReasonPage.html')
#---------------------------------------------------------------------------------------
def charts(request):
    return render(request,'info/charts/chartList.html')
#---------------------------------------------------------------------------------------
def DonutChart(request):
    university = User.objects.filter(reason = 'u').count()
    highschool = User.objects.filter(reason = 'h').count()
    Friend = User.objects.filter(reason = 'a').count()
    game = User.objects.filter(reason = 'g').count()
    school = User.objects.filter(reason = 's').count()
    other = User.objects.filter(reason = 'o').count()
    family = User.objects.filter(reason = 'f').count()
    instagram = User.objects.filter(reason = 'i').count()

    return render(request,'info/charts/DonutChart.html',{"university" : university,"highschool" : highschool,
    "Friend" : Friend,"game" : game,"school" : school,"other" : other,
    "family" : family,"instagram" : instagram,
    })
#---------------------------------------------------------------------------------------
def lineChart(request):
    university = User.objects.filter(reason = 'u').count()
    highschool = User.objects.filter(reason = 'h').count()
    Friend = User.objects.filter(reason = 'a').count()
    game = User.objects.filter(reason = 'g').count()
    school = User.objects.filter(reason = 's').count()
    other = User.objects.filter(reason = 'o').count()
    family = User.objects.filter(reason = 'f').count()
    instagram = User.objects.filter(reason = 'i').count()

    return render(request,'info/charts/lineChart.html',{"university" : university,"highschool" : highschool,
    "Friend" : Friend,"game" : game,"school" : school,"other" : other,
    "family" : family,"instagram" : instagram,
    })
#---------------------------------------------------------------------------------------
def lineChartPercentage(request):
    factor = 100 / User.objects.all().count()

    university = User.objects.filter(reason = 'u').count() * factor
    highschool = User.objects.filter(reason = 'h').count() * factor
    Friend = User.objects.filter(reason = 'a').count() * factor
    game = User.objects.filter(reason = 'g').count() * factor
    school = User.objects.filter(reason = 's').count() * factor
    other = User.objects.filter(reason = 'o').count() * factor
    family = User.objects.filter(reason = 'f').count() * factor
    instagram = User.objects.filter(reason = 'i').count() * factor

    return render(request,'info/charts/lineChart.html',{"university" : university,"highschool" : highschool,
    "Friend" : Friend,"game" : game,"school" : school,"other" : other,
    "family" : family,"instagram" : instagram,
    })
#---------------------------------------------------------------------------------------
def radarChart(request):
    factor = 100 / User.objects.all().count()
    university = User.objects.filter(reason = 'u').count()
    highschool = User.objects.filter(reason = 'h').count()
    Friend = User.objects.filter(reason = 'a').count()
    game = User.objects.filter(reason = 'g').count()
    school = User.objects.filter(reason = 's').count()
    other = User.objects.filter(reason = 'o').count()
    family = User.objects.filter(reason = 'f').count()
    instagram = User.objects.filter(reason = 'i').count()

    return render(request,'info/charts/radarChart.html',{"factor": factor,"university" : university,"highschool" : highschool,
    "Friend" : Friend,"game" : game,"school" : school,"other" : other,
    "family" : family,"instagram" : instagram,
    })
#---------------------------------------------------------------------------------------
def ordersPage(request):
    return render(request,'info/orders.html')
#---------------------------------------------------------------------------------------
def orderingByReason(request):
    all = User.objects.all().count()
    factor = 100 / User.objects.all().count()
    university = User.objects.filter(reason = 'u').count()
    highschool = User.objects.filter(reason = 'h').count()
    Friend = User.objects.filter(reason = 'a').count()
    game = User.objects.filter(reason = 'g').count()
    school = User.objects.filter(reason = 's').count()
    other = User.objects.filter(reason = 'o').count()
    family = User.objects.filter(reason = 'f').count()
    instagram = User.objects.filter(reason = 'i').count()
    return render(request,'info/orders/reasonOrdering.html',{"all" : all,"factor": factor,"data" : {"university" : [university,university*factor],"highschool" : [highschool,highschool*factor],
    "Friend" : [Friend,Friend*factor],"game" : [game,game*factor],"school" : [school,school*factor],"other" : [other,other*factor],
    "family" : [family,family*factor],"instagram" : [instagram,instagram*factor]},
    })
