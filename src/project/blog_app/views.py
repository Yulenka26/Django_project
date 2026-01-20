from django.http import HttpResponse
from project.blog_app.models import Post, Category
from django.shortcuts import get_object_or_404


def index(request):
    return HttpResponse("<h1>Hello Blog!</h1>")

def post_list(request):
    posts = Post.objects.filter(published=True)
    response_content = "<h1>Список статей</h1> <ul>"
    for post in posts:
        response_content += f"<li><a href='/post/{post.slug}'>{post.title}</a>{post.created_at}</li>"
    response_content += "</ul>"
    return HttpResponse(response_content)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    content = f'''
    <h1>{post.title}</h1>
    <p>Автор: {post.author.username}</p>
    <div>Содержание: {post.content}</div>
    <hr>
    <a href="/post_list/">Назад к списку статей</a>
    '''
    return HttpResponse(content)

def categories_list(request):
    categories = Category.objects.all()
    response_content = "<h1>Список категорий</h1> <ul>"
    for category in categories:
        response_content += f"<li><a href='/categories/{category.id}'>{category.title}</a></li>"
    response_content += "</ul>"
    return HttpResponse(response_content)

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category, published=True)
    response_content = f"<h1>{category.title}</h1> <ul>"
    for post in posts:
        response_content += f"<li><a href='/post/{post.slug}'>{post.title}</a></li>"
    response_content += """
    </ul>
    <p>
        <a href="/post_list/">Назад к списку статей</a><br>
        <a href="/categories/">Назад к списку категорий</a>
    </p>
    """
    return HttpResponse(response_content)
