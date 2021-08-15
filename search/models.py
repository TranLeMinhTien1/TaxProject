from django.db import models

# Create your models here.
class Post(models.Model):
    Company = models.CharField(max_length=255, null=True)
    status = models.TextField(max_length=100, null=True)
    address = models.TextField(max_length=100, null=True)
    def __str__(self):
        return self.Company
    class Meta:
        ordering = ['id']

    def MST(self):
        p = Post(Company='CÔNG TY TNHH PHẦN MỀM PVS', status='NNT đang hoạt động (đã được cấp GCN ĐKT)', address='B19.21, Sunrise Cityview, Số 33 Nguyễn Hữu Thọ')
        p.save()