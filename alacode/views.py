from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
import openpyxl
import csv

from django.urls import reverse
from django.views.generic import FormView, CreateView
from django.forms import ModelForm, HiddenInput

from alacode.models import Code, Tweet


class CodingForm(ModelForm):
    class Meta:
        model = Code
        exclude = ['id']
        widgets = {'user': HiddenInput(), 'tweet': HiddenInput()}


class CodingView(LoginRequiredMixin, CreateView):
    login_url = '/login/'

    form_class = CodingForm
    template_name = 'alacode/coding.html'


    def get_tweet(self):
        self.coded = {c.tweet_id for c in Code.objects.filter(user=self.request.user)}
        self.ncoded = len(self.coded)
        tweets = Tweet.objects.exclude(pk__in=self.coded)
        self.total = tweets.count()
        if self.total == 0:
            self.total+=1
            self.perc = 10 + int(self.ncoded / self.total*90)
            self.total-=1
        else:
            self.perc = 10 + int(self.ncoded / self.total * 90)
        return tweets[0]

    def get_initial(self):
        initial = super().get_initial()
        self.tweet = self.get_tweet()
        initial['tweet'] = self.tweet
        initial['user'] = self.request.user
        return initial

    def get_success_url(self):
        return reverse("alacode:index")






