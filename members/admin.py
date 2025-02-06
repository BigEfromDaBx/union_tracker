from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'status')
    list_filter = ('status', 'state')
    search_fields = ('first_name', 'last_name', 'email', 'phone')

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Name'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('member-report/', self.admin_site.admin_view(self.member_report_view), name='member_report'),
        ]
        return custom_urls + urls

    def member_report_view(self, request):
        active_members = Member.objects.filter(status=True).count()
        inactive_members = Member.objects.filter(status=False).count()
        context = {
            'active_members': active_members,
            'inactive_members': inactive_members,
            'title': 'Member Report',
        }
        return render(request, 'admin/member_report.html', context)

admin.site.register(Member, MemberAdmin)