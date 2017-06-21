from django.contrib import admin

from .models import DateInline, Demo, FileInline, ManySource


@admin.register(ManySource)
class ManySourceAdmin(admin.ModelAdmin):
    pass


@admin.register(DateInline)
class DateAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'


class DateInlineAdmin(admin.StackedInline):
    model = DateInline
    extra = 1


class FileInlineAdmin(admin.TabularInline):
    model = FileInline
    extra = 1


@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_editable = ('title',)
    raw_id_fields = ('raw_foreign_key', 'raw_many_to_many')
    radio_fields = {
        'radio_fields_vertical': admin.VERTICAL,
        'radio_fields_horizontal': admin.HORIZONTAL,
    }
    filter_horizontal = ('filter_horizontal',)
    filter_vertical = ('filter_vertical',)
    save_on_top = True
    save_as = True
    prepopulated_fields = {
        'slug': ('title',),
    }
    inlines = [DateInlineAdmin, FileInlineAdmin]
