from django.shortcuts import render
from django.http import Http404
from django.views.generic import View

# Create your views here.
posts = [
    {
        'id': i,
        'title': '{0}{1}'.format('Order №', i),
        'description': 'The description for {} order'.format(i),
        'text': 'Message for You.'.format(i)
    } for i in range(1, 7)
    ]

posts_dict = {val.get('id'): val for val in posts}

def main(request):
    return render(request, 'home.html', {
        'posts': posts
    })


class PostView(View):
    def get(self, request, id):
        post = posts_dict.get(int(id))

        if post is None:
            raise Http404

        return render(request, 'post.html', {
            'post': post
        })
