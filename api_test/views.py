from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from api_test.models import TestSuite, TestCase, TestProject
from django.db import transaction
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt

from .models import Book


@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)





@csrf_exempt
def add_project(request):
    """
    增加一个项目
    :param request:
    :return: 成功返回creat ok
    """
    if request.method == 'POST':
        response = {}
        project_name = request.POST['projectName']
        baseUrl = request.POST['url']

        try:
            with transaction.atomic():
                TestProject.objects.create(name=project_name, url=baseUrl)
                response['msg'] = 'success'
                response['error_num'] = 0
        except Exception as e:
            print (e)
            response['msg'] = str(e)
            response['error_num'] = 1
        return JsonResponse(response)


@csrf_exempt
def edit_project(request):
    """
    修改一个项目
    :param request:
    :return: 成功返回creat ok
    """
    if request.method == 'POST':
        response = {}
        pk = request.POST['pk']
        project_name = request.POST['projectName']
        baseUrl = request.POST['url']

        try:
            with transaction.atomic():
                tp = TestProject.objects.get(project_id=pk)
                tp.url = baseUrl
                tp.name = project_name
                tp.save()
                response['msg'] = 'success'
                response['error_num'] = 0
        except Exception as e:
            print (e)
            response['msg'] = str(e)
            response['error_num'] = 1
        return JsonResponse(response)

@require_http_methods(["GET"])
def show_projects(request):
    response = {}
    try:

        project_name = request.GET.get('name')
        if len(project_name.strip()) == 0:
            projects = TestProject.objects.filter()
        else:
            projects = TestProject.objects.filter(name__contains=project_name.strip())
        response['list'] = json.loads(serializers.serialize("json", projects))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@csrf_exempt
def del_projects(request):
    if request.method == 'GET':
        response = {}
        try:

            pk = request.GET.get('pk')
            print(pk)
            if pk!= None :
                TestProject.objects.get(pk=pk).delete()
                response['msg'] = 'success'
                response['error_num'] = 0
        except  Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
        return JsonResponse(response)

