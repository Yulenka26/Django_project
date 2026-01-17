from django.http import HttpResponse

from project.blog_app.models import Post
from django.shortcuts import get_object_or_404


def index(request):
    return HttpResponse("<h1>Hello Blog!</h1>")

def post_list(request):
    posts = Post.objects.filter(published=True)
    response_content = "<h1>Список статей</h1> <ul>"
    for post in posts:
        response_content += f"<li><a href='/post/{post.id}'>{post.title}</a>{post.created_at}</li>"
    response_content += "</ul>"
    return HttpResponse(response_content)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    content = f'''
    <h1>{post.title}</h1>
    <p>Автор: {post.author.username}</p>
    <div>Содержание: {post.content}</div>
    <hr>
    <a href="/post_list/">Назад к списку статей</a>
    '''
    return HttpResponse(content)
