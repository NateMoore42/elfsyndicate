from django import forms
from character.models import *
from items.models import *
from django.utils.translation import ugettext_lazy as _

class CharEditForm(forms.Form):
    error_css_class = 'error'
    class Meta:
        model = Character
        fields = ('level', 'hp', 'c_class', 'alignment',
                  'dexterity', 'strength', 'constitution', 'age',
                  'charisma', 'wisdom', 'intelligence', 'language',
                  'height', 'weight')

class InvEditForm(forms.Form):
    error_css_class = 'error'

    currency_amount = forms.IntegerField()
    vehicles = forms.ModelMultipleChoiceField(
                                        queryset=Vehicles.objects.all())
    m_items = forms.ModelMultipleChoiceField(
                                        queryset=MountItems.objects.all())
    instruments = forms.ModelMultipleChoiceField(
                                        queryset=Instruments.objects.all())
    weapons = forms.ModelMultipleChoiceField(queryset=Weapon.objects.all())
    mounts = forms.ModelMultipleChoiceField(queryset=Mounts.objects.all())
    tools = forms.ModelMultipleChoiceField(queryset=Tools.objects.all())
    kits = forms.ModelMultipleChoiceField(queryset=Kits.objects.all())
    sets = forms.ModelMultipleChoiceField(queryset=Sets.objects.all())
    copper = forms.IntegerField()
    silver = forms.IntegerField()
    electrum = forms.IntegerField()
    gold = forms.IntegerField()
    platinum = forms.IntegerField()

    class Meta:
        model = Inventory
        fields = ('weapons', 'mounts', 'tools', 'kits',
                  'sets', 'instruments', 'm_items', 'vehicles',
                  'copper', 'silver', 'electrum', 'gold', 'platinum')
