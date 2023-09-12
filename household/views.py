from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView

from household.forms import HouseholdForm
from household.models import Household


# Create your views here.
def index(request):
    context = {}
    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))


class HouseholdCreateView(LoginRequiredMixin, CreateView):
    template_name = 'household/create_household.html'
    model = Household
    form_class = HouseholdForm
    success_url = reverse_lazy('index')


class HouseholdListView(LoginRequiredMixin, ListView):
    model = Household
    context_object_name = 'households'  # Household.objects.all()
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Household.objects.filter(active=True)


class HouseholdDetailedView(LoginRequiredMixin, DetailView):
    pass

class HouseholdDeleteView(LoginRequiredMixin, DeleteView):
    pass
