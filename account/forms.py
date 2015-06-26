from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm

from account.models import Account


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_(u"Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_(u"Password confirmation"), widget=forms.PasswordInput)
    firstname = forms.CharField(label=_(u'First Name'),widget=forms.TextInput)
    lastname = forms.CharField(label=_(u'Last Name'),widget=forms.TextInput)
    class Meta:
        model = Account
        fields = ("email","role","team")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.first_name = self.cleaned_data["firstname"]
        user.last_name = self.cleaned_data["lastname"]

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        exclude = ()

    def clean_password(self):
        return self.initial['password']


class UpdateAccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ('password','follows','last_login')


class CreateAccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ('follows','last_login')

    def save(self, commit=True):
        user = super(CreateAccountForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user