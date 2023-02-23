from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User


# Create your views here.
class UsersIndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })
