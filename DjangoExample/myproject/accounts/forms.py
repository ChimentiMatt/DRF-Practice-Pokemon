from django.contrib.auth.forms import UserCreationForm

from .models import Trainer

class SignupForm(UserCreationForm):
    class Meta:
        model = Trainer
        fields = ('email', 'name', 'password1', 'password2')