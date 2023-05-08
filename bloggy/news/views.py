from django.shortcuts import render, redirect
from .models import News
from django.urls import reverse
from .forms import NewsForm

def news_page(request):
    news = News.objects.all()
    return render(request=request, template_name="news.html", context={"news": news})


def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request=request, template_name="news_detail.html", context={"news": news})

def news_delete(request, news_id):
   news = News.objects.get(pk=news_id)
   news.delete()
   return redirect(reverse("news:news-page"))


def news_create(request):
    form = NewsForm()
    if request.POST:
        form = NewsForm(request.POST)
        form.is_valid()
        form.save()
        return redirect(reverse("news:news-page"))
    return render(request=request, template_name="news_create.html", context={"form": form})


def news_update(request, news_id):
    news = News.objects.get(pk=news_id)
    form = NewsForm(initial={"headline": news.headline, "body": news.body})
    if request.POST:
        form = NewsForm(request.POST)
        form.is_valid()
        news.headline = form.cleaned_data.get("headline")
        news.body = form.cleaned_data.get("body")
        news.save()
        return redirect(reverse("news:news-page"))

    return render(request=request, template_name="news_update.html",
                   context={"form": form, "news": news})