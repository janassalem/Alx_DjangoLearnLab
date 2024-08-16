from django import forms
from django.contrib.auth.models import User
from .models import Book 


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            UserProfile.objects.create(user=user, role=self.cleaned_data['role'])
        return user
class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Ensure that this line correctly references the Book model
        fields = ['title', 'author', 'published_date']



