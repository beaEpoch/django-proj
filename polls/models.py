from django.db import models

# Create your models here.
class PhoneCaptcha(models.Model):
    phone = models.CharField(max_length=11, verbose_name="手机号")
    captcha = models.CharField(max_length=6, verbose_name="验证码")
    kind = models.CharField(max_length=6, verbose_name="类型")
    created = models.DateTimeField(null=True, auto_now_add=True, verbose_name="创建时间")

    class Meta:
        ordering = ['-id']
        verbose_name = "phone_captcha"
        verbose_name_plural = "phone_captcha"
        db_table = 'phone_captcha'

    def __str__(self):
        return self.phone