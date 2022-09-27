from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
                # Apply login_required() as a decorator to the topics() view
                # function by prepending login_required with the @ symbol.
                # As a result, Python knows to run the code in login_required()
                # before the code in topics(). The code in login_required()
                # checks whether a user is logged in, and Django runs the code
                # in topics() only if they are. If the user isn’t logged in,
                # they’re redirected to the login page.
from django.http import Http404     # if the user requests a topic they shouldn’t see
from .models import Topic, Entry    #import the model associated with the data we need
from .forms import TopicForm, EntryForm
# Write your views here.

def index(request):
    """The home page for the learning log"""
    return render(request,'learning_logs/index.html')
                                    #When a URL request matches the pattern we just defined, Django looks
                                    #for a function called index() in the views.py file. Django then passes the
                                    #request object to this view function. 
@login_required()
def topics(request):                                 #The topics() function needs one parameter: the request object Django received from the server
    """Shows all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')   #query the database by asking for the Topic objects, sorted by the date_added attribute. We store query in "topics"
        #(above) The query Topic.objects .filter(owner=request.user) tells Django to retrieve only the Topic objects from the database whose owner attribute matches the current user
    context = {"topics": topics}                    #A context is a dictionary in which the keys are names we’ll use in the template to access the data, and the values are the data we need to send to the template. In this case, there’s one key-value pair, which contains the set of topics we’ll display on the page.
    return render(request, 'learning_logs/topics.html', context)

@login_required()
def topic(request, topic_id):                       #2nd parameter is the expression /<int:topic_id>/ from urls.py
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)          #as previously tested in django shell, use get() to retrieve the topic_id
    if topic.owner != request.user:                 #If the current user doesn’t own the requested topic,
        raise Http404                               # we raise the Http404 exception
    entries = topic.entry_set.order_by('-date_added') #get entries associated with this topic and order them
    context = {'topic': topic, 'entries': entries}  #store in a dictionary
    return render(request, 'learning_logs/topic.html', context) #send 'context' to the template topic.html

@login_required()
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':                    #test whether the request is GET or POST
        form = TopicForm()                          #No data submitted, create a blank form.
    else:                                           #make an instance of TopicForm v, assign it to the variable form, and send the form to the template in the context dictionary
        # POST data submitted; process data
        form = TopicForm(data=request.POST)         #pass it the data entered by the user, stored in request.POST. 
        if form.is_valid():                         #checks that all required fields have been filled in (all fields in a form are required by default) and that the data entered matches the field types expected
            new_topic = form.save(commit=False)     #call form.save(), we pass the commit=False argument because we need to modify the new topic before saving it to the database
            new_topic.owner = request.user          # call form.save(), we pass the commit=False argument because we need to modify the new topic before saving it to the database
            new_topic.save()                        #If everything is valid, we can call save(), writing the data from the form to the database
            return redirect('learning_logs:topics') #redirect the user’s browser to the topics page, where the user should see the topic they just entered in the list of topics
    #display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required()
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)          #need the topic to render the page and process the form’s data; topic_id gets the correct topic object here

    if request.method != 'POST':
        form = EntryForm()                          #No data submitted, create a blank form
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)     #set the entry object’s topic attribute before saving it to the database. When we call save(), we include the argument commit=False to tell Django to create a new entry object and assign it to new_entry without saving it to the database yet. 
            new_entry.topic = topic                 #set the topic attribute of new_entry to the topic we pulled from the database at the beginning of the function
            new_entry.save()                        #call save() with no arguments, saving the entry to the database with the correct associated topic
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required()
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)          #entry object that the user wants to edit and the topic associated with this entry.
    topic = entry.topic
    if topic.owner != request.user:                 #This protects the "edit_entry" page
        raise Http404                               #no one can use the URL to gain access to someone else’s entries

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry
        form = EntryForm(instance=entry)
        #In the if block, which runs for a GET request, we make
        # an instance of EntryForm with the argument instance=entry
    else:
        # POST date submitted, process data
        form = EntryForm(instance=entry, data=request.POST)
        # (above) When processing a POST request, we pass the
        # instance=entry argument and the data=request.POST argument
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
            #(above)redirect to the topic page, where the user should
            # see the updated version of the entry they edited

    context =  {
        'entry': entry,
        'topic': topic,
        'form': form
            }
    return render(request, 'learning_logs/edit_entry.html',context)
