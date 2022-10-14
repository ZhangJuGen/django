from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


class LoginView(View):

    def post(self,request):

        return HttpResponse('666')

    def get(self, request):
        name = request.GET.get('name')
        print(name)
        request.session['name'] = name
        return HttpResponse(name)
