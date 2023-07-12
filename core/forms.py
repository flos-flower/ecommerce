from allauth.account.forms import SignupForm
from django import forms
from .models import Item, Location
from django.utils.translation import gettext_lazy as _
 
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['img', 'title', 'price', 'category', 'description']
        labels = {
            'img': _('Изображение'),
            'title': _('Название'),
            'price': _('Цена'),
            'category': _('Категория'),
            'description': _('Описание'),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        labels = {
            'region': _('Регион'),
            'area': _('Район'),
            'city': _('Город'),
            'street': _('Улица')
        }