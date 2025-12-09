from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """The home for learning log."""
    return render(request, 'learning_logs/index.html' )

@login_required
def topics(request):
    """Show all the topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    # make sure the topic belongs to current user
    check_topic_owner(topic, request)

    
    entries = topic.entry_set.order_by("-date_added")
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
    
@login_required
def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # Get req from browser give empty form
        # no data submitted create a blank form
        form = TopicForm()
    else:
        # Post data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            
            return redirect('learning_logs:topics')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """add new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)

    
    if request.method != 'POST':
        # Get req from browser give empty form
        # no data submitted create a blank form
        form = EntryForm()
    else:
        # Post data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # create new_entry object without saving it to database
            new_entry = form.save(commit=False)
            # set the entry object’s topic attribute before
            # saving it to the database
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    # Display a blank or invalid form
    context = {'topic': topic,'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """edit a particular entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    check_topic_owner(topic, request)
    
    # for get request , give form to edit
    if request.method != 'POST':
        # prefilled form with existing entry
        form = EntryForm(instance=entry)
        
    else:
        # Post data submitted 
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)        
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
    

def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404
    