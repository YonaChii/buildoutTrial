from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Question, Option

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'poll_list'

    def get_queryset(self):
        return Question.objects.order_by('-date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'poll'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    context_object_name = 'poll'

def vote(request, q_id):
    p = get_object_or_404(Question, pk=q_id)
    try:
        selected_choice = p.option_set.get(pk=request.POST['choice'])
    except (KeyError, Option.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
