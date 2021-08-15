from django.core.management.base import BaseCommand
from django.db import models
from .models import Post
#from .mst import MST
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        models = Post(Company='CÔNG TY TNHH PHẦN MỀM PVS', status='NNT đang hoạt động (đã được cấp GCN ĐKT)', address='B19.21, Sunrise Cityview, Số 33 Nguyễn Hữu Thọ')
        models.save()
