from django.urls import  path
from . import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.BoardListView.as_view(), name = "index"),
    path('boards/<int:pk>/', views.TopicListView.as_view(), name = "board_topics"),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('signup/', accounts_views.signup, name='signup'),
    path('boards/<int:pk>/topics/<int:topic_pk>/',  views.PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    
]
