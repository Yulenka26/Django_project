from datetime import datetime
from typing import Literal

from ninja import ModelSchema, Schema
from pydantic import EmailStr

from project.blog_app.models import Post


class PostInSchema(ModelSchema):
    author_id: int
    category_id: int
    class Meta:
        model = Post
        fields = ["title", "content"]

class PostOutSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "content", "category", "published", "created_at"]

class FeedbackInSchema(Schema):
    name: str
    email: EmailStr
    subject: Literal["improve", "article", "other"]
    message: str

class FeedbackOutSchema(FeedbackInSchema):
    id: int
    created_at: datetime
