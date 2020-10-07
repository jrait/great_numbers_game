from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'number_to_guess' in request.session:
        print(f"The number to guess is still {request.session['number_to_guess']}")

    else:
        request.session['number_to_guess']=random.randrange(0,100)
        print(f"The number to guess is {request.session['number_to_guess']}")
    if 'count' not in request.session:
        request.session['count'] = 0
    
    return render(request, 'index.html')

def guess(request):
    request.session['number'] = int(request.POST ['number'])
    if request.session['number'] == request.session['number_to_guess']:
        request.session['correct'] = True
        request.session['too_low'] = False
        request.session['too_high'] = False
        request.session['count']+=1
    elif request.session['number'] < request.session['number_to_guess']:
        request.session['correct'] = False
        request.session['too_low'] = True
        request.session['too_high'] = False
        request.session['count']+=1
    elif request.session['number'] > request.session['number_to_guess']:
        request.session['correct'] = False
        request.session['too_low'] = False
        request.session['too_high'] = True
        request.session['count'] += 1
    return redirect('/')

def restart(request):
    request.session.clear()
    return redirect('/')

