from django.db import models

a=(('solved','solved'),('un solved','un solved'))


class complaint(models.Model):
    name=models.CharField(max_length=49)
    branch=models.CharField(max_length=30)
    issue=models.CharField(max_length=300)
    status=models.CharField(max_length=90,choices=a,default='un solved')
    def __str__(self):
        return self.name
