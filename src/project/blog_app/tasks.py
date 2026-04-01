from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F

from project.blog_app.models import Post


@shared_task
def notify_new_post(post_id: int, post_title: str, post_url: str):
    admin_email = settings.DEFAULT_FROM_EMAIL
    send_mail(
        subject=f"Новая статья: {post_title}",
        message=(
            f"Вышла нова статья в блоге\n\n"
            f"Название: {post_title}\n"
            f"Ссылка на статью: {post_url}"
        ),
        from_email=admin_email,
        recipient_list=[admin_email],
        fail_silently=False,
    )
    return f"Уведомление о посте {post_id} отправлено на {admin_email}"


@shared_task
def increment_views_count(post_id: int):
    Post.objects.filter(id=post_id).update(views_count=F("views_count") + 1)
    return f"Просмотр поста {post_id} засчитан"
