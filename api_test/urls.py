from django.conf.urls import url, include
from .views import *

urlpatterns = [
    # url(r'add_book', add_book, ),
    # url(r'show_books', show_books, ),
    url(r'add_book$', add_book, ),
    url(r'show_books$', show_books, ),
    url(r'add_project$', add_project, ),
    url(r'show_projects$', show_projects, ),
    url(r'del_projects$', del_projects, ),
    url(r'edit_project$', edit_project, ),
    url(r'show_FuncSuite$', show_FuncSuite, ),
    url(r'add_suite$', add_suite, ),
    url(r'edit_suite$', edit_suite, ),
    url(r'del_suite$', del_suite, ),


]