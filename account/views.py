from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully.')
            else:
                return HttpResponse('Disabled account.')
        else:
            return HttpResponse('Invalid login.')
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'account/login.html', context)

def dashboard(request):
    context = {
        'section': 'dashboard'
    }
    return render(request, 'account/dashboard.html', context)

class Dashboard(TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'dashboard'
        return context
