import datetime

from django.db import models
from django.utils import timezone


class ManySource(models.Model):
    title = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Demo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    foreign_key = models.ForeignKey(ManySource, null=True, blank=True, related_name='+')
    raw_foreign_key = models.ForeignKey(ManySource, null=True, blank=True, related_name='+')
    radio_fields_horizontal = models.ForeignKey(
        ManySource, null=True, blank=True, related_name='+'
    )
    radio_fields_vertical = models.ForeignKey(ManySource, null=True, blank=True, related_name='+')
    many_to_many = models.ManyToManyField(ManySource, blank=True, related_name='+')
    raw_many_to_many = models.ManyToManyField(ManySource, blank=True, related_name='+')
    filter_horizontal = models.ManyToManyField(ManySource, blank=True, related_name='+')
    filter_vertical = models.ManyToManyField(ManySource, blank=True, related_name='+')

    def __str__(self):
        return self.title


class DateInline(models.Model):
    demo = models.ForeignKey(Demo)
    date_time = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=timezone.now)
    add_inline = models.BooleanField(default=False, help_text='Tick this!')

    def __str__(self):
        return '{}'.format(self.date)


class FileInline(models.Model):
    demo = models.ForeignKey(Demo)
    file_upload = models.FileField(upload_to='uploads')
    clearable_file_upload = models.FileField(upload_to='uploads', blank=True)

    def __str__(self):
        return 'Demo Inline'
