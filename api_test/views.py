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
    """
       展示项目
       :param request:
       :return: 成功返回creat ok
       """
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

@require_http_methods(["GET"])
def show_FuncSuite(request):
    """
       展示模块
       :param request:
       :return: 成功返回creat ok
       """
    list_suite = []
    response = {}
    try:

        name = request.GET.get('name')
        if len(name.strip()) == 0:
            suites = TestSuite.objects.filter().values('suite_id','name','project_id__project_id','project_id__name')
           # suites = TestSuite.objects.filter()
        else:
            suites = TestSuite.objects.filter(name__contains=name.strip()).values('suite_id','name','project_id__project_id','project_id__name')
            # suites = TestSuite.objects.filter()
        for suite in suites:
            item = {}
            item['name'] = suite['name']
            item['suite_id'] = suite['suite_id']
            item['project_id__project_id'] = suite['project_id__project_id']
            item['project_id__name'] = suite['project_id__name']
            list_suite.append(item)
        response['list'] = list_suite
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@csrf_exempt
def add_suite(request):
    """
    增加一个模块
    :param request:
    :return: 成功返回creat ok
    """
    if request.method == 'POST':
        response = {}
        project_id = request.POST['pk']
        name = request.POST['name']

        try:
            with transaction.atomic():
                TestSuite.objects.create(name=name, project_id_id=project_id)
                response['msg'] = 'success'
                response['error_num'] = 0
        except Exception as e:
            print (e)
            response['msg'] = str(e)
            response['error_num'] = 1
        return JsonResponse(response)



@csrf_exempt
def edit_suite(request):
    """
    修改一个模块
    :param request:
    :return: 成功返回creat ok
    """
    if request.method == 'POST':
        response = {}
        suite_id = request.POST['suite_id']
        project_id = request.POST['project_id']
        name = request.POST['name']

        try:
            with transaction.atomic():
                tp = TestSuite.objects.get(suite_id=suite_id)
                tp.project_id_id = project_id
                tp.name = name
                tp.save()
                response['msg'] = 'success'
                response['error_num'] = 0
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error_num'] = 1
        return JsonResponse(response)


@csrf_exempt
def del_suite(request):
    if request.method == 'GET':
        response = {}
        try:

            suite_id = request.GET.get('suite_id')
            if suite_id!= None :
                TestSuite.objects.get(suite_id=suite_id).delete()
                response['msg'] = 'success'
                response['error_num'] = 0
        except  Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
        return JsonResponse(response)