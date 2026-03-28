from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline, SearchRank
from django.core.cache import cache
from django.http import HttpResponse
from ninja import NinjaAPI
from slugify import slugify

from project.blog_app.models import Post, Category
from project.feedback_app.models import Feedback
from project.ninja_api.auth_routes import auth_router
from project.ninja_api.schemas import PostOutSchema, PostInSchema, FeedbackOutSchema, FeedbackInSchema, \
    CategoryOutSchema, CategoryInSchema, PostSearchOutSchema

router = NinjaAPI(
    version='1.0.0',
    title='Ninja API BLOG',
    description='Блог на Django Ninja',
)

router.add_router("/auth", auth_router)

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
    cache_key = f"api_post_{post_id}"
    post = cache.get(cache_key)

    if post is None:
        try:
            post = await Post.objects.aget(pk=post_id)
            cache.set(cache_key, post, 60*10)
        except Post.DoesNotExist:
            return router.create_response(request, {"detail":"Статья не найдена"}, status=404)

    return post

@router.post("/posts", response=PostOutSchema)
async def create_post(request, payload: PostInSchema) -> PostOutSchema:
    return await Post.objects.acreate(**payload.model_dump(), slug=slugify(payload.title))

@router.post("/feedback", response=FeedbackOutSchema)
async def create_feedback(request, payload: FeedbackInSchema) -> FeedbackOutSchema:
    return await Feedback.objects.acreate(**payload.model_dump())

@router.get("/categories", response=list[CategoryOutSchema])
async def categories_list(request, search_title: str | None=None) -> list[CategoryOutSchema]:
    qs = Category.objects.all()
    if search_title:
        qs = qs.filter(title__icontains=search_title)

    return [category async for category in qs]

@router.get("/categories/{category_id}", response=CategoryOutSchema)
async def get_category(request, category_id:int) -> CategoryOutSchema | HttpResponse:
    try:
        category = await Category.objects.aget(pk=category_id)
        return category
    except Category.DoesNotExist:
        return router.create_response(request, {"detail":"Категория не найдена"}, status=404)

@router.post("/categories", response=CategoryOutSchema)
async def create_category(request, payload: CategoryInSchema) -> CategoryOutSchema:
    return await Category.objects.acreate(**payload.model_dump(), slug=slugify(payload.title))

@router.delete("/categories/{category_id}")
async def delete_category(request, category_id:int) -> HttpResponse:
    try:
        category = await Category.objects.aget(pk=category_id)
        category.adelete()
        return router.create_response(request, {"detail":"Категория удалена"}, status=200)
    except Category.DoesNotExist:
        return router.create_response(request, {"detail":"Категория не найдена"}, status=404)

@router.get("/post/search", response=list[PostSearchOutSchema])
async def search_posts(request, query: str, published_only: bool = True) -> list[PostSearchOutSchema]:
    vector = SearchVector("title", weight="A", config="russian") + SearchVector("content", weight="B", config="russian") + SearchVector("category__title", weight="C", config="russian")
    search_query = SearchQuery(query, config="russian")
    headline = SearchHeadline("content", search_query, config="russian", max_words=15, min_words=5)
    qs = Post.objects.annotate(rank=SearchRank(vector, search_query), headline=headline).select_related("category")

    if published_only:
        qs = qs.filter(published=True)
    qs = qs.filter(rank__gte=0.1).order_by("-rank")

    results = [
        PostSearchOutSchema(
            id=post.id,
            title=post.title,
            slug=post.slug,
            category=post.category.title,
            headline=post.headline,
            rank=post.rank
        )
        async for post in qs
    ]
    return results
