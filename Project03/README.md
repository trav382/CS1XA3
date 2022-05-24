# CS 1XA3 Project03 - Social Media Website



## Usage
To run Project 03 you need to have **Anaconda** installed.
Please refer to [here](https://docs.anaconda.com/anaconda/install/)  to **Install Anaconda** 

### Running Locally 
- Make sure the **conda environment** is activated
```
	conda activate djangoenv
```
- Then run the server by running 
```
	python manage.py runserver localhost:8000
```
**Make** **sure** you run this in the directory with the manage.py file.
Going to **localhost:8000/e/mooret12/** will take you to the signup/login page.

###  Running on the Server
- Make sure the **conda environment** is activated
```
	conda activate djangoenv
```
- Then run the server by running 
```
	python manage.py runserver localhost:10069
```
Going to **https://mac1xa3.ca/e/mooret12/**  will then take you to the signup/login page.


### Log in and use the app

I made an account for using the app and testing its features
Username: TA
Password: django10
However every user has the password "django10" and you can use any account.
List of other Usernames: 
- Claire
- Delaney
- Drake
- John
- Justin
- Travis 

## Objective 01 - Sign up Page
**Description:**
- This feature is displayed in signup.djhtml which is rendered by signup_view
```python
def  signup_view(request):

	form = UserCreationForm()

	failed = request.session.get('create_failed',False)

	context = { 'create_form' : form , 'create_failed' : failed}

	return render(request,'signup.djhtml',context)
```
It uses a built-in form from Django that creates a user, from the given username and password.
## Objective 02 - User Info
**Description:** 
- This feature displays information of the user currently logged in, such as their Employment, Location, Birthday, and Interests.
- For example,
```
{{user_info.location}}
```
This code in social_base.djhtml will display the location of the User. This information is displayed in the left column of e/mooret12/social/*
*= messages, people, and account
## Objective 03 - Password Change/Update Info

**Description:** 
- For the password change another built-in form was used (PasswordChangeForm)
- For the update information a Form class was created 
```python
class UpdateInfoForm(forms.ModelForm):

	class Meta:

	model = models.UserInfo

	fields = ["employment", "location", "birthday"]
```
This form allows Users to change their UserInfo Fields, and the PasswordChangeForm allows Users to change their password
## Objective 04 - Displaying People List
**Description**:
- This feature displays all users who are not friends of the current user and friend requests
```python
for user in all_users.iterator():

	if user == user_info:

		continue

	if user_info not in user.friends.all():

		all_people.append(user)
```
This code looped through all users, and checked to see if they were friends with the logged in user. The ones who are not friends were put in a list and then put in people.djhtml to be displayed 
```
{% for user in all_people%}
	<h4>{{user.user}}</h4><br>
{%endfor%}
```
## Objective 05 - Sending Friend Requests

```python
def friend_request_view(request):
```
**Description:** This function will handle a POST request from clicking the Friend Request button in people.djhtml.

**Exceptions:**
Will return a HttpResponseNotFound error if the function is called without frID in POST

## Objective 06 - Accepting / Declining Friend Requests
```python
def accept_decline_view(request):
```
**Description:** 
- Handles POST Request recieved from accepting or declining a friend request in people.djhtml (sent by people.js)
- Deletes corresponding FriendRequest entry and adds to users friends relation if accepted

**Exceptions**:
-  Will return a HttpResponseNotFound error if the function is called without decision in POST

From accept_decline_view:
```python
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
```
 - This code loops through all the Friend Requests. It checks if The User decided to add the other User.  
 - If the User did accept the decision will == "A" and they will become  friends. 
- The request is deleted regardless if they choose accept or decline.
## Objective 07 - Displaying Friends
```
{% for friend in friends%}
	<span>{{friend.user}}</span>
{%endfor%}
```
 - This Objective required a loop to display the User's friends in  **messages.djhtml**.
 - friends was already defined in messages_view and contained a list of the User's friends.

## Objective 8 - Submitting Posts
```javascript
function submitPost(event) {

	var post_text = $("#post-text").text();

	let url = post_submit_url;

	let json_data = {

	'postContent' : post_text,

	}

	$.post(url,

	json_data, moreResponse);
```
**Description:**
- This function sends contents of post-text via AJAX Post to post_submit_view

From post_submit_view:
```python
postContent = request.POST.get('postContent')
user_info = models.UserInfo.objects.get(user=request.user)

if postContent is not None:

	if request.user.is_authenticated:
		
		models.Post.objects.create(owner = user_info, content = postContent)

	return HttpResponse()
	
	else:
		return redirect('login:login_view')

return HttpResponseNotFound()
```
**Description:**
- Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry to the Post Model

**Exceptions**:
- Will call HttpResponseNotFound error if post_submit_view is called without postContent in POST

## Objective 9/10 
```python
def  messages_view(request):

posts = []

all_posts = models.Post.objects.all().order_by('-id')

	for post in all_posts.iterator():

		post.like_amount = len(post.likes.all())

		post.liked=False

		if user_info in post.likes.all():

			post.liked = True
			
		posts.append(post)

			if len(posts) == request.session['post_view']:
				break
```
**Description:**
- Displays all posts and also allows user to make new posts and like posts
- The code loops through all posts, ordered by newest to oldest.
- It checks to see if the user liked the post. If they have liked it the like button will be disabled as ```post.liked``` becomes True

**Exceptions:**
- If the User is not Authenticated the function will redirect to the login page.

```
{% for post in posts %}
	{% load static %}

	<span class="w3-right w3-opacity">{{post.timestamp}}</span>

	<h4 class="post-user">{{post.owner.user}}</h4><br>

	<h3>{{post.content}}</h3>
{% endfor %}
```
For Loop for Displaying Posts 
