from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django import forms
from . import models
from django.db import transaction


def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        friends = []
        for fr in user_info.friends.all().iterator():
            friends.append(fr)

        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
        posts = []
        all_posts = models.Post.objects.all().order_by('-id')
        for post in all_posts.iterator():
           # if post.owner in user_info.friends.all() or post.owner == user_info:
                post.like_amount = len(post.likes.all())
                post.liked=False
                if user_info in post.likes.all():
                    post.liked = True
                #post.liked = False
                posts.append(post)
                if len(posts) == request.session['post_view']:
                    break


        # TODO Objective 10: check if user has like post, attach as a new attribute to each post

        context = { 'user_info' : user_info
                  , 'posts' : posts,
                  'friends' : friends }
      
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

class UpdateInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["employment", "location", "birthday"]
    def __init__(self, *args, **kwargs):
        super(UpdateInfoForm, self).__init__(*args, **kwargs)
        self.fields['interests'] = forms.CharField(required=False)


def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """

    if request.user.is_authenticated:

        user_info = models.UserInfo.objects.get(user=request.user)
        update_info_form = UpdateInfoForm()
        change_form = PasswordChangeForm(request.user, request.POST)

        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)

            if form.is_valid():

                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('login:login_view')

        else:
            change_form = PasswordChangeForm(request.user)

        
        if request.method == "POST":
            if "employment" in request.POST:
                user_info.employment = request.POST['employment']
                user_info.location = request.POST['location']
                user_info.birthday = request.POST['birthday']
                if request.POST.get("interests") != "":
                    inter_rest = models.Interest(request.POST.get("interests"))
                    inter_rest.save()
                    user_info.interests.add(inter_rest)
                user_info.save()
                

        update_info_form.fields["employment"].initial = user_info.employment
        update_info_form.fields["location"].initial = user_info.location
        update_info_form.fields["birthday"].initial = user_info.birthday

        context = { 'user_info' : user_info,
                    'change_form' : change_form,
                    'update_info_form' : update_info_form }
        return render(request,'account.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        print(user_info.friends.all())
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)
        all_people = []
        all_users = models.UserInfo.objects.all()
        for user in all_users.iterator():
            # if user not in 

            if user == user_info:
                continue
            if user_info not in user.friends.all():
                all_people.append(user)
            if len(all_people) == request.session['ppl_view']:
                break
        # TODO Objective 5: create a list of all friend requests to current user

        friend_requests = []
        all_requests = models.FriendRequest.objects.all()
        for fr_request in all_requests.iterator():
            if fr_request.to_user == user_info:
                friend_requests.append(fr_request)
        context = { 'user_info' : user_info,
                    'all_people' : all_people,
                    'friend_requests' : friend_requests }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    user_info = models.UserInfo.objects.get(user=request.user) 
    if postIDReq is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        postID = postIDReq[5:]

        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field
            post = models.Post.objects.get(id = postID)
            post.likes.add(user_info)
            post.save()
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    user_info = models.UserInfo.objects.get(user=request.user) 
    if postContent is not None:
        if request.user.is_authenticated:

            # TODO Objective 8: Add a new entry to the Post model
            models.Post.objects.create(owner = user_info, content = postContent)
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts dispalyed

        # TODO Objective 9: update how many posts are displayed/returned by messages_view

        # return status='success'
        request.session['post_view'] = request.session['post_view'] + 3
        return HttpResponse()

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people dispalyed

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed

        # return status='success'
        request.session['ppl_view'] = request.session['ppl_view'] + 2
        return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
        username = frID[3:]

        if request.user.is_authenticated:
            from_user = models.UserInfo.objects.get(user = request.user)
            to_user = models.UserInfo.objects.get(user=username)
            models.FriendRequest.objects.create(to_user = to_user, from_user = from_user)
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    if data is not None:
        # TODO Objective 6: parse decision from data
        to_user = models.UserInfo.objects.get(user=request.user)
        if request.user.is_authenticated:

            # TODO Objective 6: delete FriendRequest entry and update friends in both Users

            # return status='success'
            all_requests = models.FriendRequest.objects.all()
            from_username = request.POST.get('username')[2:]
            decision = request.POST.get('username')[0]
            print(from_username)

            from_user = models.UserInfo.objects.get(user=from_username)
            for fr_req in all_requests:

                if fr_req.to_user == to_user and fr_req.from_user == from_user:
                    if (decision == "A"):
                        to_user.friends.add(from_user)
                        from_user.friends.add(to_user)
                    fr_req.delete()
                    break
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
