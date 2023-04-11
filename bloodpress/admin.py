from django.contrib import admin
from .models import Question, Response


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'user', 'response_text', 'created_at')
    list_filter = ('question', 'user')
    search_fields = ('response_text',)


admin.site.register(Question)
admin.site.register(Response, ResponseAdmin)
