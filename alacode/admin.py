from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from alacode.models import Tweet, Code


class TweetAdmin(ImportExportModelAdmin):
    fields = ('tweet', 'url')
    pass
admin.site.register(Tweet, TweetAdmin)


class CodeAdmin(ImportExportModelAdmin):
    fields = ('tweet', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12')
admin.site.register(Code, CodeAdmin)
