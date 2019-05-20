from django.shortcuts import render

# Create your views here.
from utilizatori.models import User
from django.shortcuts import render


def list(request):
    utilizatori = User.objects.all()
    context = {
        'utilizatori': utilizatori,
    }
    return render(request, 'list.html', context)

