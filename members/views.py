from django.shortcuts import render, get_object_or_404
from .models import Member

def home(request):
    return render(request, 'index.html')

def member_list(request):
    members = Member.objects.all()  # Fetch all members from the database
    return render(request, 'members.html', {'members': members})

def member_detail(request, id):
    member = get_object_or_404(Member, id=id)  # Fetch a single member by ID
    return render(request, 'member_detail.html', {'member': member})