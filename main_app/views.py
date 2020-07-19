from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import todos
import requests


class home(View):
    base_url = 'https://owlbot.info/api/v4/dictionary/'
    __access_token = '04c41b70794ea41af8a903381d2cbb96614c12ad'

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

    def post(self, request, *args, **kwargs):
        url = self.base_url + request.POST['search_query']
        response = requests.get(
            url, headers={'Authorization': 'Token %s' % self.__access_token})
        response = response.json()
        return render(request, 'home.html', {'definition': response})


class todo(View):

    def get(self, request, *args, **kwargs):
        context = {}
        if('delete' in kwargs):
            todos.objects.get(slugg_id=kwargs['delete']).delete()
            return HttpResponseRedirect('/todo')
        elif('id' in kwargs):
            if(todos.objects.filter(slugg_id=kwargs['id']).exists() == False):
                return HttpResponseRedirect('/todo')
            context.update(
                {'todo_entry': todos.objects.get(slugg_id=kwargs['id'])})

        context.update({'todos': todos.objects.all()})
        return render(request, 'todo.html', context=context)

    def post(self, request, *args, **kwargs):
        if(request.POST['id']):
            todos.objects.filter(slugg_id=request.POST['id']).update(
                title=request.POST['title'], todo_content=request.POST['body'])
        elif(request.POST['title']):
            todos.objects.create(
                title=request.POST['title'], todo_content=request.POST['body'])
        else:
            return HttpResponseRedirect('/todo')
        all_todos = todos.objects.all()
        return render(request, 'todo.html', {'todos': all_todos})
