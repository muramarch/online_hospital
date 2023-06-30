from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from apps.accounts.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'phone', 'password1', 'password2']

    # Hii ni kwaajili ya kuondoa yale maelekezo yanayotokea kwenye kuandika Password
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        for field_name in ('name', 'username', 'email', 'phone', 'password1', 'password2'):
            self.fields[field_name].help_text = ''
            
            
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'email', 'phone']

