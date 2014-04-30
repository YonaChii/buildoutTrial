from django.contrib import admin
from polls.models import Question, Option

class ChoiceInline(admin.TabularInline):
    model = Option
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Date information', {'fields': ['date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text','date','is_recent')
    list_filter = ['date']
    search_fields = ['text']
    list_filter = ['date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
