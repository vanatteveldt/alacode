from django.forms import ModelForm
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, TemplateView

from coding.models import Code


class CodingForm(ModelForm):
    class Meta:
        model = Code
        exclude = ['id']

class CodingView(FormView):
    form_class = CodingForm
    template_name = "coding/coding.html"