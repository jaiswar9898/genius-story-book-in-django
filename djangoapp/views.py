from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
import requests
import re
from datetime import datetime
import os
from .models import Story,Category

def story_list(request,category_slug=None):
    category = None 
    categories=Category.objects.all()
    story = Story.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        story=story.filter(category=category)
    return render(request,'story/story_list.html',{'categories':categories,
                                                   'story':story,
                                                   'category':category,
                                                   })