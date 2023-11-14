from django.shortcuts import render
from .models import Bookmark



def index(request):
    Bookmarks = Bookmark.objects.all()
    return render(request, 'index.html', {'Bookmarks': Bookmarks})
