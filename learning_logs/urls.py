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
    # Page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # PAge for adding new topic entry
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry')
    
]