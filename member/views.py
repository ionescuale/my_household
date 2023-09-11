from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView


# Create your views here.

class MemberCreateView(CreateView):
    pass

class MemberListView(ListView):
    pass

class MemberDeleteView(DeleteView):
    pass

class MemberUpdateView(UpdateView):
    pass