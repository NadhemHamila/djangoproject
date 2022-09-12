from sched import scheduler
from django.shortcuts import render
from .models import Scheduler
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    """View function for home page of site."""

    schedulers = Scheduler.objects.all().count()

    context = {
        'num_books': schedulers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)