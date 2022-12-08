from django.shortcuts import render
from .forms import ThingForm


def home(request):
    #adding form to veiws
    form = ThingForm()
    return render(request, 'home.html', {'form': form})