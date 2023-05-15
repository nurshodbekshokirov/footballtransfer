from django.shortcuts import render, redirect
from django.db.models import Sum

from .models import *

def about(request):
    return render(request,'about.html')

def club(request):
    data = {'club': Club.objects.annotate(umum_summa=Sum('futbolchilari__tr_narxi')).order_by('-umum_summa')}
    return render(request,  'clubs.html', data)

def player(request):
    data = {'player':Player.objects.all().order_by('-tr_narxi')}
    return render(request, 'players.html', data)


def latest_transfer(request):
    data = {'trans': Transfer.objects.order_by('-narxi')}
    return render(request, 'latest-transfers.html', data)
def davlat(request,soz):
    data = {'davlat':Club.objects.filter(davlat=soz),
            'mamlakat':soz}
    return render(request, 'england.html', data)

def u20(request):
    from datetime import date, timedelta
    bugun = date.today()
    boshi = bugun - timedelta(days=20*365)
    pl = Player.objects.filter(t_yil__range=[boshi, bugun])



    data = {
        'players':pl,
        'h_yil': bugun.year
    }
    return render(request, 'U-20 players.html', data)

def arxive(request):
    h_mavsum = Hozirgi_mavsum.objects.last().hozirgi_mavsum
    data = {
        'Transferlar': Transfer.objects.filter(mavsum__lt=h_mavsum).values('mavsum').distinct().order_by('-mavsum')
    }
    return render(request, 'transfer-archive.html', data)

def bitta_mavsum(request, soz):
    data = {
        'mavsumgaoid': Transfer.objects.filter(mavsum=soz)
    }
    return render(request, '2017-18season.html', data)

def bitta_club(request,son):
    data = {
        'club': Player.objects.filter(club=Club.objects.get(id=son))
    }
    return render(request, 'country-clubs.html', data)
def stats(request):
    return render(request, 'stats.html')

def transfer_record(request):
    data = {
        'tra': Transfer.objects.filter(narxi__gt=50).order_by('-narxi')[0:100]
    }
    return render(request, 'transfer-records.html', data)



