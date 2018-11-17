# coding=utf-8

from __future__ import unicode_literals

from django.views import generic
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

from app.forms import AppForm
from app.models import AppModel


class AppIndex(generic.TemplateView, FormMixin):
    """
    Endpoint for Index
    """
    template_name = 'index.html'
    form_class = AppForm
    success_url = reverse_lazy('sample-app:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Index'
        context['color'] = AppModel.objects.filter(id=1).first()
        color = context['color']
        context['form'] = AppForm(initial={
            'header_background': color.header_background,
            'footer_background': color.footer_background
        })
        return context

    def post(self, request):
        form = AppForm(request.POST, instance=AppModel(id=1))
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        return render(request, self.template_name, {'form': form})
