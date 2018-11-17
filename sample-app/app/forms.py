# coding=utf-8

from __future__ import unicode_literals

from django import forms
from app.models import AppModel

# from gradient_colorfield.fields import GradientColorWidget, GradientColorField


class AppForm(forms.ModelForm):
    # header_background = forms.CharField(label='Header Background', max_length=20, widget=GradientColorWidget(),
    #                                     initial='linear-gradient(to bottom, #00f260 0%, #0575e6 100%)',
    #                                     )
    # footer_background = forms.CharField(label='Footer Background', max_length=20, widget=GradientColorWidget(),
    #                                     initial='linear-gradient(to bottom, #00f260 0%, #0575e6 100%)')

    class Meta:
        model = AppModel
        fields = ['header_background', 'footer_background']
