from django.conf import settings
from graphene_django import DjangoObjectType
import graphene

from main import models

from django.contrib.auth import get_user_model

User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile

class OrderType(DjangoObjectType):
    class Meta:
        model = models.Order

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag

class TableType(DjangoObjectType):
    class Meta:
        model = models.Table

class EmployeeType(DjangoObjectType):
    class Meta:
        model = models.Employee

class Query(graphene.ObjectType):
    all_posts = graphene.List(OrderType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(OrderType, slug=graphene.String())
    posts_by_author = graphene.List(OrderType, username=graphene.String())
    posts_by_tag = graphene.List(OrderType, tag=graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.Order.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_author_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            models.Order.objects.prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (
            models.Order.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Order.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )

schema = graphene.Schema(query=Query)