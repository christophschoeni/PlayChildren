from django.shortcuts import render
from .models import Learn
# Create your views here.
def index(request):
    learnings = Learn.objects.all()
    
    context = {
        'learnings': learnings
    }
    return render(request, 'learning/index.html', context)
