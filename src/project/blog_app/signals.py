from django.db.models.signals import post_save
from django.dispatch import receiver

from project.blog_app.models import Post


@receiver(post_save, sender=Post)
def on_post_published(sender, instance, created, **kwargs):
    if not created or not instance.published:
        return

    post_url = f"http://127.0.0.1:8000/post/{instance.slug}/"

    from project.blog_app.tasks import notify_new_post

    notify_new_post.delay(
        post_id=instance.id, post_title=instance.title, post_url=post_url
    )
