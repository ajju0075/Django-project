from django.urls import path
from core import views as core_views


app_name = "core"
urlpatterns = [
    path("", core_views.CatogoryListHomeView.as_view(), name = "home"),
    path("chats/", core_views.ChatsView.as_view(), name = "chats"),
    path("contactus/", core_views.FeedbackCreateView.as_view(), name = "contactus"),


]


