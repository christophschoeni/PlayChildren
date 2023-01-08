import datetime
from .models import Learn
from datetime import date
from django.shortcuts import render
from qr_code.qrcode.utils import MeCard, VCard, EpcData, VEvent, EventClass, EventTransparency, EventStatus, WifiConfig, Coordinates, QRCodeOptions

# Create your views here.
def index(request):
    learnings = Learn.objects.all()
    
    
    event = VEvent(
        uid="some-event-id",
        summary="Vacations",
        start=datetime.datetime(2022, 8, 6, hour=8, minute=30),
        end=datetime.datetime(2022, 8, 17, hour=12),
        location="New-York, Statue de la Liberté",
        geo=(40.69216097988203, -74.04460073403436),
        categories=["PERSO", "holidays"],
        status=EventStatus.CONFIRMED,
        event_class=EventClass.PRIVATE,
        transparency=EventTransparency.OPAQUE,
        organizer="foo@bar.com",
        url="https://bar.com",
        description= ""
        )
        
    context = dict(
        learnings = learnings,
        event=event,
        options_example=QRCodeOptions(size='t', border=6, error_correction='L'),
    )
    
    
    
    return render(request, 'learning/index.html', context=context)



def scanner(request):
    return render(request, 'learning/scanner.html')