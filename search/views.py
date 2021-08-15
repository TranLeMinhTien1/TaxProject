from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from .models import Post
from django.template import loader
from django.http import HttpResponse, HttpRequest

#from .mst import MST
# Create your views here.
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class Test(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.chrome('search/chromedriver.exe')

class IndexClass(View):
    def get(self, request):
        return render(request, 'search/index.html')
    
    def send(self, request:HttpRequest):
        p = Post(Company='CÔNG TY TNHH PHẦN MỀM PVS', status='NNT đang hoạt động (đã được cấp GCN ĐKT)', address='B19.21, Sunrise Cityview, Số 33 Nguyễn Hữu Thọ')
        p.save()
        c='CÔNG TY TNHH PHẦN MỀM PVS'
        n ='NNT đang hoạt động (đã được cấp GCN ĐKT)'
        b ='B19.21, Sunrise Cityview'
        #company = request.POST['company']
        #company.save()
        todo= p(company = request.POST['company'])
        todo.save()
        return redirect()
    
    def handle(self, *args, **options):
        models = Post(Company='CÔNG TY TNHH PHẦN MỀM PVS', status='NNT đang hoạt động (đã được cấp GCN ĐKT)', address='B19.21, Sunrise Cityview, Số 33 Nguyễn Hữu Thọ')
        models.save()

        
    
    