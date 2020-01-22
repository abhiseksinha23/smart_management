from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'cooperate'
urlpatterns = [
    path('', views.indexview.as_view(), name='index'),
    path('flist/', views.facultieslistview.as_view(), name='faculties_list'),
    re_path(r'^f/(?P<pk>\d+)$', views.facultiesdetailview.as_view(), name='faculties_detail'),
    path('fcreate/',views.facultiescreate.as_view(), name='faculties_create'),
    re_path(r'^f/(?P<pk>\d+)/update/$', views.facultiesupdate.as_view(), name='faculties_update'),
    re_path(r'^f/(?P<pk>\d+)/delete/$', views.facultiesdelete.as_view(), name='faculties_delete'),
    path('rlist/', views.rankerslistview.as_view(), name='rankers_list'),
    re_path(r'^r/(?P<pk>\d+)$', views.rankersdetailview.as_view(), name='rankers_detail'),
    path('rcreate/',views.rankerscreate.as_view(), name='rankers_create'),
    re_path(r'^r/(?P<pk>\d+)/update/$', views.rankersupdate.as_view(), name='rankers_update'),
    re_path(r'^r/(?P<pk>\d+)/delete/$', views.rankersdelete.as_view(), name='rankers_delete'),
    path('clist/', views.centerslistview.as_view(), name='centers_list'),
    re_path(r'^c/(?P<pk>\d+)$', views.centersdetailview.as_view(), name='centers_detail'),
    path('ccreate/',views.centerscreate.as_view(), name='centers_create'),
    re_path(r'^c/(?P<pk>\d+)/update/$', views.centersupdate.as_view(), name='centers_update'),
    re_path(r'^c/(?P<pk>\d+)/delete/$', views.centersdelete.as_view(), name='centers_delete'),
    path('slist/', views.studentslistview.as_view(), name='students_list'),
    re_path(r'^s/(?P<pk>\d+)$', views.studentsdetailview.as_view(), name='students_detail'),
    path('screate/',views.studentscreate.as_view(), name='students_create'),
    re_path(r'^s/(?P<pk>\d+)/update/$', views.studentsupdate.as_view(), name='students_update'),
    re_path(r'^s/(?P<pk>\d+)/delete/$', views.studentsdelete.as_view(), name='students_delete'),
    path('feelist/', views.feelistview.as_view(), name='fee_list'),
    re_path(r'^fee/(?P<pk>\d+)$', views.feedetailview.as_view(), name='fee_detail'),
    path('feecreate/',views.feecreate.as_view(), name='fee_create'),
    re_path(r'^fee/(?P<pk>\d+)/update/$', views.feeupdate.as_view(), name='fee_update'),
    re_path(r'^fee/(?P<pk>\d+)/delete/$', views.feedelete.as_view(), name='fee_delete'),
    path('qlist/', views.quarieslistview.as_view(), name='quaries_list'),
    re_path(r'^q/(?P<pk>\d+)$', views.quariesdetailview.as_view(), name='quaries_detail'),
    path('qcreate/',views.quariescreate.as_view(), name='quaries_create'),
    re_path(r'^q/(?P<pk>\d+)/delete/$', views.quariesdelete.as_view(), name='quaries_delete'),
    path('contact/', views.contactview.as_view(), name='contact'),
    path('ack/', views.ackview.as_view(), name='ack'),
]
