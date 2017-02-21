from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Members(models.Model):
    user_seq = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=60, unique=True)
    user_nm = models.CharField(max_length=60)
    fst_name = models.CharField(max_length=30)
    lst_name = models.CharField(max_length=40)
    email = models.EmailField()
    del_yn = models.CharField(max_length=1)
    reg_date = models.DateTimeField(auto_now_add=True)
    lst_date = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.user_nm + "(" + self.user_id + ")"

    class Meta:
        db_table = 'tb_member_info'

    pass

# attend memeberr
class Attend(models.Model):
    attd_seq = models.AutoField(primary_key=True)
    attd_type = models.CharField(max_length=4)
    attd_date = models.CharField(max_length=8)
    user = models.ForeignKey(Members, on_delete=models.CASCADE, to_field="user_id")
    lst_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tb_attend_info'

    pass
