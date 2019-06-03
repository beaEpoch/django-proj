from django.db import models


class Phone(models.Model):
    phone = models.CharField(max_length=11, verbose_name="手机号")
    kind = models.CharField(max_length=6, verbose_name="类型")
    token = models.CharField(max_length=64, verbose_name="token")
    created = models.DateTimeField(null=True, auto_now_add=True, verbose_name="创建时间")

    class Meta:
        ordering = ['-id']
        verbose_name = "phone"
        verbose_name_plural = "phone"
        db_table = 'phone'

    def __str__(self):
        return self.phone


class Captcha(models.Model):
    phone = models.CharField(max_length=11, verbose_name="手机号")
    captcha = models.CharField(max_length=6, verbose_name="验证码")
    created = models.DateTimeField(null=True, auto_now_add=True, verbose_name="创建时间")

    class Meta:
        ordering = ['-id']
        verbose_name = "captcha"
        verbose_name_plural = "captcha"
        db_table = 'captcha'

    def __str__(self):
        return self.captcha