from django.core.paginator import Paginator
from django.conf import settings


def scroll_posts(request, posts):
    paginator = Paginator(posts, settings.CONSTANT)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
