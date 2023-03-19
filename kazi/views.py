from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate, JobList, Company, JobCategory, BackgroundData
from .forms import CandidateForm, JobListForm, CompanyForm, CreateUserForm, JobCategoryForm, BackgroundDataForm
from django.contrib import messages


# Candidate views
#08/03/2022- Register
def RegisterPage(request):
    form = CreateUserForm()
    asd = "<QueryDict: {'csrfmiddlewaretoken': ['XYSeUxEsvTULLDqO2bKKZPCOySsZBmN6pkRf03ObKT3XaMLLcAb2ShiLtWQ2hLyv'], 'username': ['qwerty'], 'email': ['qwerty@gmail.com'], 'password1': ['qwerty@#asd12'], 'password2': ['qwerty@#asd12'], 'CreateUser': ['Submit Query']}>"
    if request.method == 'POST':
        print(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)

            return redirect('kazi')

    context = {"form": form}
    return render(request, 'accounts/register.html', context)

def LoginPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        if request.POST['btn_check'] == "Signup":
            print(request.POST)
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)

                return redirect('login')
        elif request.POST['btn_check'] == "Login":
            
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                
                login(request, user)
                return redirect('kazi')
            else:
                
                messages.info(request, "Username OR oassword is incorrect")

    context = {}
    return render(request, "accounts/login.html", context)

def LogoutUser(request):
    logout(request)
    return redirect('login')

# signals
@login_required(login_url="login")
def edit_candidate(request):
    candidate = get_object_or_404(Candidate, user=request.user)
    if request.method == 'POST':
        # process form data and save to candidate instance
        candidate.name = request.POST.get('name')
        candidate.email = request.POST.get('email')
        candidate.profession_title = request.POST.get('profession_title')
        # add other fields as needed
        candidate.save()
        return redirect('candidate_profile')
    return render(request, 'edit_candidate.html', {'candidate': candidate})

# cont:
@login_required(login_url="login")
def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

@login_required(login_url="login")
def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, 'candidate_detail.html', {'candidate': candidate})


@login_required(login_url="login")
def candidate_create(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'candidate_create.html', {'form': form})

@login_required(login_url="login")
def candidate_update(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidate_detail', candidate_id=candidate.id)
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'candidate_form.html', {'form': form})

def candidate_delete(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    if request.method == 'POST':
        candidate.delete()
        return redirect('candidate_list')
    context = {'candidate': candidate}
    return render(request, 'candidate_delete.html', context)

'''def candidate_delete(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    candidate.delete()
    return redirect('candidate_list')
'''


# JobList views

@login_required(login_url="login")
def joblist_list(request):
    joblists = JobList.objects.all()
    return render(request, 'job_list.html', {'joblists': joblists})

def joblist_detail(request, joblist_id):
    joblist = get_object_or_404(JobList, pk=joblist_id)
    return render(request, 'joblist_detail.html', {'joblist': joblist})

def joblist_create(request):
    if request.method == 'POST':
        form = JobListForm(request.POST)
        if form.is_valid():
            joblist = form.save()
            return redirect('joblist_detail', joblist_id=joblist.id)
    else:
        form = JobListForm()
    return render(request, 'joblist_form.html', {'form': form})

def joblist_update(request, joblist_id):
    joblist = get_object_or_404(JobList, pk=joblist_id)
    if request.method == 'POST':
        form = JobListForm(request.POST, instance=joblist)
        if form.is_valid():
            form.save()
            return redirect('joblist_detail', joblist_id=joblist.id)
    else:
        form = JobListForm(instance=joblist)
    return render(request, 'joblist_form.html', {'form': form})

def joblist_delete(request, joblist_id):
    joblist = get_object_or_404(JobList, pk=joblist_id)
    joblist.delete()
    return redirect('joblist_list')


# Company views

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'company_detail.html', {'company': company})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)


#basic route
def home(request):
    return render(request, "test/test.html")


def about(request):
    return render(request, "test/about.html")


def contactus(request):
    return render(request, "test/contact.html")

def category(request):
    return render(request, "test/category.html")


def error_404_view(request, exception):

    return render(request, 'test/404.html')
# def register(request):
#     return render(request, 'register.html')