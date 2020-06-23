from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView

from OPSApp.forms import StudentOTRForm, puploadForm, happroveform
from OPSApp.models import User, Student, pupload, Guide, Hod
from .choices import semester_choice,ptype_choice

def index(request):
    ns=Student.objects.all().count()
    pr=pupload.objects.all().count()
    fa=Guide.objects.all().count()
    hod=Hod.objects.all().count()
    pupload2 = pupload.objects.all()
    guides=Guide.objects.all()
    paginator = Paginator(pupload2, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context={'ns':ns,'guides':guides,'pr':pr,'fa':fa,'hod':hod,'paged_listings':paged_listings,
    }

    return render(request,'index.html',context)

def register(request):
    if request.method=='POST':
        # messages.error(request,'Testing Error Message')
        # Registerd User
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # return
            if User.objects.filter(username=username).exists():
                messages.error(request,'The Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(username=email).exists():
                    messages.error(request, 'The Email is already used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                    # auth.login(request,user)
                    # messages.success(request,'You are Now Logged in')
                    # return redirect('index')
                    user.save();
                    messages.success(request,'Registration Sucessfull Now Login' )
                    return redirect('login')#login


        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('welcome')#change
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

@login_required
def welcome(request):
    if request.user.is_guide:
        return render(request, 'guide.html')
    if request.user.is_student:
        return render(request, 'student.html')
    if request.user.is_hod:
        return render(request, 'hod.html')
    return redirect('studentotr')

class StudentOTR(CreateView):
    template_name = 'studentotr.html'
    model= Student
    form_class = StudentOTRForm
    success_url = '/login/'


class CreateProjectView(LoginRequiredMixin,CreateView):
    template_name = 'projectupload.html'
    model = pupload
    fields = ['ptitle','pdescription','guide','hod',
              'pphoto','pabstract','ptype',

              'plive','pshare','pdate','ereport',
              'photo_1', 'photo_2', 'photo_3', 'photo_4'
              ]
    def form_valid(self, form):
        form.instance.user = Student.objects.get(user=self.request.user)
        return super(CreateProjectView, self).form_valid(form)

# class gstatusview(CreateView):
#     template_name = 'gproject_view.html'
#     model = gstatus
#     fields = ['user','pstatus','comments','about','rating'
#
#               ]
#     def form_valid(self, form):
#         form.instance.id = Student.objects.get(user=self.request.user)
#         return super(gstatusview, self).form_valid(form)

# def gstatusview(request):
#     context = {}
#
#
#     form = gstatusviewForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context['form'] = form
#     return render(request,'gstatus.html',context)



def projectlist(request):
    context = {}
    context['pupload'] = pupload.objects.filter(user__user__username__iexact=request.user.username)
    return render(request, "student.html", context)

def gprojectlist(request):
    context = {}
    context['pupload'] = pupload.objects.filter(guide__user__username__iexact=request.user.username)
    return render(request, "guide.html", context)

def hprojectlist(request):
    context = {}
    context['pupload'] = pupload.objects.filter(hod__user__username__iexact=request.user.username)
    return render(request, "hod.html", context)

def project_view(request,pk):
    context ={}
    context['stu'] = pupload.objects.get(pk=pk)

    return render(request, "project_view.html", context)


def project_status(request,pk):
    context ={}
    context['stu'] = pupload.objects.get(pk=pk)

    return render(request, "project_status.html", context)

def gproject_view(request,pk):
    context ={}
    context['stu'] = pupload.objects.get(pk=pk)

    return render(request, "gproject_view.html", context)



def updateproject(request,pk):

    obj = get_object_or_404(pupload,pk=pk)
    form = puploadForm(request.POST or None,request.FILES or None,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,'You successfully updated')
        context = {'form': form}
        return render(request,'student.html',context)
    else:
        context = {'form': form,
                   'error': 'The form was not updated successfully. Please enter in a title and content'}
        return render(request,"updateproject.html",context)

# def approveproject(request,pk):
#
#     obj = get_object_or_404(pupload,pk=pk)
#     form = gapproveroject(request.POST or None,request.FILES or None,instance=obj)
#     if form.is_valid():
#         form.save()
#         messages.success(request,'You successfully updated')
#         context = {'form': form}
#         return render(request,'approveproject.html',context)
#     else:
#         context = {'form': form,
#                    'error': 'The form was not updated successfully. Please enter in a title and content'}
#         return render(request,"approveproject.html",context)

class approveproject(UpdateView):
    template_name = 'approveproject.html'
    model = pupload
    fields = [
        'gustatus','gucomments','rating'
    ]
    success_url = '/projectlist'

class happroveproject(UpdateView):
    template_name = 'happroveproject.html'
    model = pupload
    fields = [
        'hostatus','hocomments'
    ]
    success_url = '/projects'




# def happroveproject(request, pk):
#     # dictionary for initial data with
#     # field names as keys
#     context = {}
#
#     # fetch the object related to passed id
#     obj = get_object_or_404(pupload, pk=pk)
#
#     # pass the object as instance in form
#     form = happroveform(request.POST or None, instance=obj)
#
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/" + id)
#
#         # add form dictionary to context
#     context["form"] = form
#
#     return render(request, "happroveproject.html", context)
#


def projectdelete(request,pk):
    context={}
    obj = get_object_or_404(pupload,pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect("userprojectlist")
    return render(request, "projectdelete.html", context)

def gprojectdelete(request,pk):
    context={}
    obj = get_object_or_404(pupload,pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect("gprojectlist")
    return render(request, "gprojectdelete.html", context)

def searchproject(request):
    pupload2=pupload.objects.filter(gustatus__exact='Accept',hostatus__iexact='Accept')
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            pupload2=pupload2.filter(user__batch__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            pupload2 = pupload2.filter(user__user__username__icontains=city)

    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            pupload2 = pupload2.filter(ptitle__icontains=title)

    if 'semester' in request.GET:
        semester =request.GET['semester']
        if semester:
            pupload2 = pupload2.filter(user__semester__iexact=semester)

    if 'ptype' in request.GET:
        ptype =request.GET['ptype']
        if ptype:
            pupload2 = pupload2.filter(ptype__iexact=ptype)

    if 'gname' in request.GET:
        gname = request.GET['gname']
        if gname:
            pupload2 = pupload2.filter(guide__user__first_name__icontains=gname )

    context={
        'semester_choice':semester_choice,
        'ptype_choice':ptype_choice,
        'listings':pupload2,
        'values': request.GET
    }
    return render(request,'_projects.html',context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now Loged Out')
        return redirect('index')
