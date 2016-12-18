from django.forms import ModelForm, TextInput

from django.contrib.auth.models import User

class RegisterForm(ModelForm):

    """This handles the user registeration form """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {'username': TextInput(attrs={
            'placeholder': 'Your unique username',
            'autocomplete': 'off',
            'class': 'form-control'
        }),
          'first_name': TextInput(attrs={
                'placeholder': 'Your Name',
                'autocomplete': 'off',
                'class': 'form-control'
            }),
            'last_name': TextInput(attrs={
                'placeholder': 'Last Name',
                'autocomplete': 'off',
                'class': 'form-control'}),
            'email': TextInput(attrs={
                'placeholder': 'Enter Email Address',
                'autocomplete': 'off',
                'class': 'form-control'
            }),
        }

    # password_conf = forms.CharField(max_length=100,
    #                                 widget=forms.PasswordInput(attrs={
    #                                     'placeholder': 'Verify secret password',
    #                                     'class': 'form-control',
    #                                 }))

    # def clean_username(self):
    #     try:
    #         User.objects.get(username=self.cleaned_data['username'])
    #     except User.DoesNotExist:
    #         return self.cleaned_data['username']
    #     raise forms.ValidationError(
    #         "This user already exist, please choose another username")

    # def clean_email(self):
    #     try:
    #         User.objects.get(email=self.cleaned_data['email'])
    #     except User.DoesNotExist:
    #         return self.cleaned_data['email']
    #     raise forms.ValidationError(
    #         "This email already exist in the database, please use another email address")

    # def clean(self):
    #     if 'password' in self.cleaned_data and 'password_conf' in self.cleaned_data:
    #         if self.cleaned_data['password'] != self.cleaned_data['password_conf']:
    #             raise forms.ValidationError(
    #                 "You must type in the same password each time")
    #     return self.cleaned_data

    # def save(self):
    #     new_user = User.objects.create_user(
    #         username=self.cleaned_data['username'],
    #         email=self.cleaned_data['email'],
    #         password=self.cleaned_data['password'],
    #         first_name=self.cleaned_data['first_name'],
    #         last_name=self.cleaned_data['last_name'],
    #     )
    #     return new_user