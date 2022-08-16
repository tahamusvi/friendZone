from django.shortcuts import render
from accounts.models import User,City


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


    reason_data =  {"university" : [university,university*factor],"highschool" : [highschool,highschool*factor],
    "Friend" : [Friend,Friend*factor],"game" : [game,game*factor],"school" : [school,school*factor],"other" : [other,other*factor],
    "family" : [family,family*factor],"instagram" : [instagram,instagram*factor]}

    return render(request,'info/orders/reasonOrdering.html',{"all" : all,"factor": factor,"data" :reason_data,
    })
#---------------------------------------------------------------------------------------
def setCity(request,username,cityName):
    city = City.objects.get(name = cityName)
    user = User.objects.get(username = username)
    user.city = city
    user.save()

    cities = City.objects.all()
    return render(request,'info/sets/setCityPage.html',{"cities" : cities})
#---------------------------------------------------------------------------------------
def orderingByCity(request):
    all = User.objects.all().count()
    factor = 100 / User.objects.all().count()

    cities = sorted(City.objects.all(), key=lambda a: -a.amount())


    data = {}
    for city in cities:
        data[city.name] = [city.amount(),city.amount()*factor]

    return render(request,'info/orders/cityOrdering.html',{"all" : all,"factor": factor,"data" : data
    })
#***************************************************************************************************
def lineChartPercentageCity(request):
    factor = 100 / User.objects.all().count()
    data = {}
    index = 0
    cities = City.objects.all()                                                 #option1
    cities_orderd = sorted(City.objects.all(), key=lambda a: -a.amount())        #option2
    cities2 =  sorted(City.objects.all(), key=lambda a: a.name)                 #option3
    for city in cities_orderd:
        data[city.name] = city.user.all().count()*factor



    return render(request,'info/charts/chartOnData.html',{"data" : data})
#***************************************************************************************************
def setCitylist(request,cityName):
    city = City.objects.get(name = cityName)
    users = User.objects.filter(city = city)
    amount = 0
    for user in users:
        amount += 1

    cities = City.objects.all()
    return render(request,'info/sets/setCity.html',{"cities" : cities,'users' : users,'amount':amount,'city':cityName})
#---------------------------------------------------------------------------------------
def setCityPage(request):
    cities = City.objects.all()

    return render(request,'info/sets/setCityPage.html',{"cities" : cities})
#---------------------------------------------------------------------------------------
def setsPage(request):
    return render(request,'info/sets/setsPage.html')
#---------------------------------------------------------------------------------------
def setRatePage(request):
    return render(request,'info/sets/setRate.html')
#---------------------------------------------------------------------------------------
def setRateByCityPage(request):
    cities = City.objects.all()
    return render(request,'info/sets/rate/setRateByCityPage.html',{"cities" : cities})
#---------------------------------------------------------------------------------------
def setRateByCityList(request,cityName):
    city = City.objects.get(name = cityName)
    users = User.objects.filter(city = city)
    amount = 0
    for user in users:
        amount += 1

    cities = City.objects.all()
    return render(request,'info/sets/rate/setRateByCity.html',{"cities" : cities,'users' : users,'amount':amount,'city':cityName})
#---------------------------------------------------------------------------------------
def setRate(request,Rate,username):
    user = User.objects.get(username=username)
    user.Rating = Rate
    user.save()

    return setRateByCityList(request,user.city.name)
#---------------------------------------------------------------------------------------
def orderingByRate(request):
    all = User.objects.all().count()
    RateAll = sum(item.totalUserRate() for item in City.objects.all())
    RateAllperPerson = RateAll / all

    factor = 100 / User.objects.all().count()

    cities = sorted(City.objects.all(), key=lambda a: -a.totalUserRate())


    data = {}
    for city in cities:
        data[city.name] = [city.averageUserRate(),city.totalUserRate(),city.amount()]

    return render(request,'info/orders/rateOrdering.html',{"all" : all,"RateAll":RateAll,"RateAllperPerson":RateAllperPerson,"factor": factor,"data" : data
    })
#---------------------------------------------------------------------------------------
def orderingByUser(request):
    all = sorted(User.objects.all(), key=lambda a: -a.Rating)


    return render(request,'info/orders/userOrdering.html',{"all" : all
    })
