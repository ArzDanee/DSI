from django import forms
from django.contrib import admin
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }

# Register your models here.
admin.site.register(Post)