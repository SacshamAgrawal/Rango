from django.shortcuts import render,redirect, get_object_or_404
from .models import Category , Page , UserProfile
from .forms import CategoryForm,PageForm,UserForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from Rango.webhose_search import run_query

def index(request):
	category_list = Category.objects.order_by('-likes')[:15]
	page_list = Page.objects.order_by('-views')[:15]
	context_dict = { 'categories': category_list , 'pages' : page_list }
	
	visitor_cookie_handler(request)
	context_dict['visits']=request.session['visits']

	return render(request,'Rango/index.html',context_dict)

def show_category(request , category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=category_name_slug )
		page=Page.objects.filter(category=category)
		context_dict['pages']=page
		context_dict['category']=category

	except Category.DoesNotExist:
		context_dict['pages']=None
		context_dict['category']=None

	result_list=[]
	query = None
	if request.method == 'POST' :
		query = request.POST['query'].strip()
		if query:
			print("we found ",query)
			result_list = run_query(query)

	context_dict['result_list'] = result_list
	context_dict['query'] = query
	return render(request , 'Rango/category.html' , context_dict)

@login_required
def add_category(request):
	form = CategoryForm()
	if(request.method == 'POST'):
		form = CategoryForm(request.POST);
		if form.is_valid() :
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	context_dict = { 'form': form }
	return render(request,'Rango/add_category.html',context_dict)

@login_required
def add_page(request,category_name_slug):
	try:
		category = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		category = None

	form = PageForm()
	if(request.method == 'POST'):
		form = PageForm(request.POST)
		if form.is_valid() :
			if category:
				page = form.save(commit=False)
				page.category = category 
				page.views = 0
				page.save()
				print("Redirecting\n")
				return redirect(show_category,category_name_slug)
				
		else:
			print(form.errors)

	context_dict = {'form': form , 'category': category}
	return render(request, 'Rango/add_page.html',context_dict)

@login_required
def register_profile(request):
	print("hurray!!")
	form = UserProfileForm()
	if request.method == "POST" : 
		form = UserProfileForm(request.POST,request.FILES)
		if form.is_valid() :
			profile = form.save(commit=False)
			profile.user=request.user
			profile.save()
			print("Profile Saved....")
			return redirect(index)
		else:
			print(form.errors)

	return render(request,'registration/profile_registration.html',{'form':form })

@login_required
def profile(request,username):
	try:
		user=User.objects.get(username=username)
	except User.DoesNotExist:
		redirect('index')

	profile = UserProfile.objects.get_or_create(user=user)[0]
	form = UserProfileForm({'website': profile.website , 'picture':profile.picture })

	if request.method == 'POST' :
		form = UserProfileForm(request.POST , request.FILES , instance = profile )
		if form.is_valid():
			form.save()
			redirect('profile',user.username)
		else:
			print(form.errors)

	context_dict = { 'form' : form , 'profile': profile , 'selecteduser':user }

	return render(request,'Rango/profile.html',context_dict)

def list_profiles(request):
	userprofile_list = UserProfile.objects.all()
	return render(request,'Rango/list_profiles.html', {'userprofile_list':userprofile_list})

def visitor_cookie_handler(request ):
	visits = int(get_server_side_cookie(request,'visits','1'))

	last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
	last_visit_time = datetime.strptime(last_visit_cookie[:-7],
												'%Y-%m-%d %H:%M:%S')	

	if (datetime.now() - last_visit_time).min :
		visits = visits + 1
		request.session['last_visit']= str(datetime.now())
	else:
		request.session['last_visit']= last_visit_cookie

	request.session['visits']=visits

def get_server_side_cookie(request, cookie, default_val=None):
	val = request.session.get(cookie)
	if not val:
		val = default_val
	return val

def track_url(request):
	if request.method == 'GET' :
		if 'page_id' in request.GET :
			page_id = request.GET['page_id']
			try:
				page = get_object_or_404(Page,pk=page_id)
				page.views += 1
				page.save()
				return redirect(page.url)
			except:
				pass
		else:
		 	return redirect(index)


