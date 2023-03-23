from django.contrib import admin
from .models import Plan

# Register your models here.


# class WordInline(admin.StackedInline):
#     model = Word
#     extra = 1
#
# class TitleAdmin(admin.ModelAdmin):
#     inlines = [WordInline,]
#     list_display = ('title',)
#
# admin.site.register(Title, TitleAdmin)
#
#
# class WordAdmin(admin.ModelAdmin):
#     list_display = ('title', 'text', 'created')
#     readonly_fields = ('title', 'text', 'created')
#     # prepopulated_fields = ('title', 'text')
#
# admin.site.register(Word, WordAdmin)


admin.site.register(Plan)