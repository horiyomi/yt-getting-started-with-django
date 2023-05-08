from django.urls import path 
from .views import news_page, news_detail, news_delete, news_create, news_update

app_name = "news"

urlpatterns = [
    path("", news_page, name="news-page"), 
    path("<int:news_id>/detail", news_detail, name="news-detail"),
    path("<int:news_id>/delete", news_delete, name="news-delete"), 
    path("create", news_create, name="news-create"),
    path("<int:news_id>/update", news_update, name="news-update")
]