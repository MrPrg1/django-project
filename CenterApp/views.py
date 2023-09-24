from django.shortcuts import render
from django.http import HttpResponse
from .models import SingerModel, MuzicModel

def singerView(request):
    singer = SingerModel.objects.all()
    return render(request, "singer/singer.html", {'singer': singer})


def musicView(request):
    music = MuzicModel.objects.all()
    return render(request, "music/music.html", {'music': music})





    #  try:
    #     p = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404("Poll does not exist")
    # return render(request, "polls/detail.html", {"poll": p})