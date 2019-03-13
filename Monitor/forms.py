from django import forms
from django.contrib import admin
from ckeditor.widgets import  CKEditorWidget
from Monitor.models import Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'
