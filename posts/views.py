from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'posts/index.html'

    def get_queryset(self):
        return Post.objecst.all()

# def index(request):
#     return render(request, 'posts/index.html')
