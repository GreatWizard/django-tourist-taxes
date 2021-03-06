from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Resident, Stay
from .forms import StayForm
import datetime


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "stays/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        now = datetime.datetime.now().date()
        locations = Resident.objects.filter(
          user=self.request.user,
          date_end__gte=now,
          date_begin__lte=now
        ).values('location').distinct()
        context['stay_list'] = Stay.objects.filter(
            user=self.request.user,
            is_validated=False,
            location__in=locations
        )
        context['stay_list_validated'] = Stay.objects.filter(
            user=self.request.user,
            is_validated=True,
            location__in=locations
        )
        context['form'] = StayForm()
        return context


@login_required
def validate_all(request):
    if request.method == 'POST':
        now = datetime.datetime.now().date()
        locations = Resident.objects.filter(
            user=request.user,
            date_end__gte=now,
            date_begin__lte=now
        ).values('location').distinct()
        Stay.objects.filter(
            user=request.user,
            is_validated=False,
            location__in=locations
        ).update(is_validated=True)
    return HttpResponseRedirect(reverse('stays'))


@login_required
def post(request):
    if request.method == 'POST':
        form = StayForm(request.POST)
        if form.is_valid():
            pass  # TODO
    return HttpResponseRedirect(reverse('stays'))
