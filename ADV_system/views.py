from django.shortcuts import render
from .models import Advertiser, Ad, AddAdvForm


def viewAds(request):
    return render(request, 'PublisherView.html',
                  {'Advertisers': Advertiser.objects.all(), 'Ads': Ad.objects.all()})


def addAd(request):
    if request.method == 'POST':
        form = AddAdvForm(request.POST)
        Ad(title=request.POST['title'],
            img=request.POST['img'],
            link=request.POST['site'],
            advertiser=Advertiser.objects.get(id=request.POST['ad_id'])).save()
    else:
        form = AddAdvForm()
    return render(request, 'AdAdder.html',
                  {'form': form})
