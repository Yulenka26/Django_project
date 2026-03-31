from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from project.blog_app.models import Post


@receiver(post_save, sender=Post)
def invalidate_post_cache(sender, instance, **kwargs):
    cache_key = f"api_posts_{instance.id}"
    cache.delete(cache_key)
    try:
        cache.incr("posts_version")
    except ValueError:
        cache.set("posts_version", 1)
