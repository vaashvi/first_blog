from django.contrib.auth.models import User
from django import forms
from .models import order, UserProfile
from django.utils.translation import ugettext_lazy as _

class UserForm(forms.ModelForm):
        username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                    label=_("Username"),
                                    error_messages={'invalid': _("The username must contain only letters,"
                                                                 " numbers and underscores.")})
        email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                 label=_("Email address"))
        password1 = forms.CharField(
            widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
            label=_("Password"))
        password2 = forms.CharField(
            widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
            label=_("Confirm Password"))

        first_name=forms.RegexField(regex=r'^[a-zA-Z]+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                    label=_("first_name"),
                                    error_messages={'invalid': _("The firstname  must contain only letters")})

        last_name = forms.RegexField(regex=r'^[a-zA-Z]+$',widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                      label=_("last_name"),
                                     error_messages={'invalid': _("The lastname  must contain only letters")})
        def clean_username(self):
            try:
                user = User.objects.get(username__iexact=self.cleaned_data['username'])
            except User.DoesNotExist:
                return self.cleaned_data['username']
            raise forms.ValidationError(_("The username already exists. Please try another one."))

        def clean(self):
            if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
                if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                    raise forms.ValidationError(_("The two password fields did not match."))
                if len(self.cleaned_data['password1']) < 8:
                    raise forms.ValidationError(_("Password too short"))


            return self.cleaned_data

        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2','first_name','last_name']



class UserProfileForm(forms.ModelForm):
        contact_no = forms.IntegerField()
        blood_group = forms.CharField(max_length=2)
        address = forms.CharField(widget=forms.Textarea)

        profilepic = forms.ImageField(label='Select a profile image')

        class Meta:
            model = UserProfile
            fields = {'contact_no', 'blood_group', 'address', 'profilepic'}
