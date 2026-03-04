from django.http import HttpResponse
from ninja import NinjaAPI
from slugify import slugify

from project.blog_app.models import Post
from project.feedback_app.models import Feedback
from project.ninja_api.schemas import PostOutSchema, PostInSchema, FeedbackOutSchema, FeedbackInSchema

router = NinjaAPI(
    version='1.0.0',
    title='Ninja API BLOG',
    description='Блог на Django Ninja',
)

@router.get("/ping")
def ping(request)-> dict[str, bool]:
    return {"pong": True}

@router.get("/posts", response=list[PostOutSchema])
async def posts_list(request, search: str | None=None, category_id: int | None=None) -> list[PostOutSchema]:
    qs = Post.objects.all()
    if search:
        qs = qs.filter(title__icontains=search)

    if category_id:
        qs = qs.filter(category=category_id)

    return [post async for post in qs]

@router.get("/posts/{post_id}", response=PostOutSchema)
async def get_post(request, post_id:int) -> PostOutSchema | HttpResponse:
    try:
        post = await Post.objects.aget(pk=post_id)
        return post
    except Post.DoesNotExist:
        return router.create_response(request, {"detail":"Статья не найдена"}, status=404)

@router.post("/posts", response=PostOutSchema)
async def create_post(request, payload: PostInSchema) -> PostOutSchema:
    return await Post.objects.acreate(**payload.model_dump(), slug=slugify(payload.title))

@router.post("/feedback", response=FeedbackOutSchema)
async def create_feedback(request, payload: FeedbackInSchema) -> FeedbackOutSchema:
    return await Feedback.objects.acreate(**payload.model_dump())
