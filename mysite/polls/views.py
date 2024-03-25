from django.shortcuts import render
from polls.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PollListView(ListView):
    model = Poll
    template_name = 'polls/list.html'


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {"object": poll}
        return render(request, self.template_name, context)
