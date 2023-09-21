from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from userextend.forms import UserForm, UserProfileForm
from userextend.models import History


# Create your views here.

class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter password'})


#
# class UserCreateView(CreateView):
#     template_name = 'userextend/pages_register.html'
#     model = User
#     form_class = UserProfileForm
#     success_url = reverse_lazy('pages-login')
#
#     def form_valid(self, form):
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.first_name = new_user.first_name.title()
#             new_user.last_name = new_user.last_name.title()
#             new_user.username = new_user.username.lower()
#
#             new_user.save()
#
#             # History
#             get_message = (f'Userul a fost adaugat cu succes Username: {new_user.username}, email: {new_user.email}, '
#                            f'first name:{new_user.first_name}, last name: {new_user.last_name}')
#
#             History.objects.create(message=get_message, created_at=datetime.now(), active=True)
#
#         return redirect('pages-login')


# @login_required

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.instance.user = user
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect("/login")
        else:
            return render(request, 'userextend/pages_register.html', {
                'user_form': UserForm(),
                'profile_form': UserProfileForm()
            })
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render(request, 'userextend/pages_register.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


class UserDetailedView(DetailView):
    template_name = 'userextend/users_profile.html'
    model = User
