import random
from django.shortcuts import render

# Create your views here. #제일많이 작업하는곳
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{"name" : "족발", "price" : 30000},{"name" : "치킨", "price" : 18000},{"name" : "피자", "price" : 13000},{"name" : "초밥", "price" : 21000},]
    pick = random.choice(menus)
    context = {
        'pick' : pick,
        'name' : name,
        'menus': menus
    }
    return render(request, 'dinner.html', context)    
