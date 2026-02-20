from project.blog_app.models import Category
from project.blog_app.models import Post
from project.users_app.models import Profile


def categories_processor(request):
    return {
        'nav_categories': Category.objects.all()
    }

def blog_stats(request):
    return {
        "nav_post_count": Post.objects.filter(published=True).count(),
        "nav_user_count": Profile.objects.count()
    }
