from django.shortcuts import render,redirect
import random
import datetime


def index(request):
    if 'total' not in request.session:
        request.session['total']
    else:
        request.session['total']=0
    try:
        request.session['a']
    except:
        request.session['a']=" "

    return render(request,'ninja_gold/index.html')

def process_money(request,place):
    time=datetime.datetime.now().strftime("(%Y/%m/%d %-I:%M %p)") #none leading zero...-I

    # if request.POST: only when we want to take actual form inputs
    if place=="farm":
        money=random.randint(10,20)
    elif place=="cave":
        money=random.randint(5,10)
    elif place=="house":
        money=random.randint(2,5)
    elif place=="casino":
        money=random.randint(-50,50)
    if money > 0:
        request.session['a']+="<p class='green'> Earned {} golds from the {}!({})</p>".format(money, place, time)
    else:
        request.session['a']+="<p class='red'>Lost {} golds from the {}!({})</p>".format(-1*money, place, time)
    request.session['total']+=money
    return redirect('/')

def clear(request):
    request.session['a']=" "
    request.session['total']=0
    return redirect('/')
