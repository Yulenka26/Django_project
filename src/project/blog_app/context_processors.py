from project.blog_app.models import Category


def categories_processor(request):
    return {
        'nav_categories': Category.objects.all()
    }
