from traceback import format_exception_only
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import Http404

from first.models import Game
#from django.contrib.auth.views import LoginView, LogoutView #login
#from django.views.generic.edit import CreateView #signup
#from django.contrib.auth.forms import UserCreationForm

#class LoginInterfaceView(LoginView):
 #   template_name = 'first/login.html'
#except Pet.DoesNotExist:
  #  raise Http404('pet not found')

#class SignUpView(CreateView):
 #   form_class = UserCreationForm
 #   template_name = 'first/register.html'
 #   success_url = 'first/success'

def index(request):

    return render(request, 'first/index.html')
# Create your views here.
def oursite(request):

    return render(request, 'first/oursite.html')

#PS5 GAMES
def PS5(request):

    return render(request, 'first/ps5.html')

"""
def fifa22(request):

    return render(request, 'first/fifa22.html')


def callofduty(request):

    return render(request, 'first/callofduty.html')


def ratchetandclank(request):

    return render(request, 'first/ratchetandclank.html')
"""

#XBOX GAMES
def XBOX(request):

    return render(request, 'first/xbox.html')

"""
def forza(request):

    return render(request, 'first/forza.html')

def halo(request):

    return render(request, 'first/halo.html')

def ghostrecon(request):

    return render(request, 'first/ghostrecon.html')
"""
#PC GAMES

def PC(request):

    return render(request, 'first/pc.html')
"""
def minecraft(request):

    return render(request, 'first/minecraft.html')

def fortnite(request):

    return render(request, 'first/fortnite.html')

def pubg(request):

    return render(request, 'first/pubg.html')
    """

def underdevel(request):

    return render(request, 'first/underdevel.html')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        games = Game.objects.filter(title__contains=searched) 

        return render(request, 'first/search.html', {'searched' : searched, 'games':games})
    
    else:

        return render(request, 'first/search.html')

 
#def home(request):
   # return HttpResponse('<p>home view</p>')

#def pet_detail(request, pet_id):
   # return HttpResponse(f'<p>pet_detail view with id {pet_id}</p>')