from django.shortcuts import render
from django.http import Http404
from polls.models import Poll


def list_view(request):
    context = {'polls': Poll.objects.all()}
    return render(request, 'polls/list.html', context)


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
            poll.save()
        elif request.POST.get("vote") == "No":
            poll.score -= 1
            poll.save()
        else:
            raise Http404

    context = {'poll': poll}
    return render(request, 'polls/detail.html', context)

