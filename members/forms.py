from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    ssn = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '000-00-0000', 'oninput': 'formatSSN(this)'}),
        max_length=11
    )

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'dob', 'address', 'address2', 'city', 'state', 'zip_code', 'phone', 'email', 'ssn', 'status']