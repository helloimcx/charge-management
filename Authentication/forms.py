from django.contrib.auth.forms import UserCreationForm
from .models import Phone


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Phone
        fields = ("phone",)