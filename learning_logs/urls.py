"""Define url patterns for learning log"""

from django.urls import path

from . import views

app_name = 'learning_logs'

# list of individual pages that can be rewuested from this app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # page that shows all the topics
    path('topics/', views.topics, name='topics'),
    # Detail page for single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]