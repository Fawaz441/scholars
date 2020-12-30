import random
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from django.contrib import messages
from django.db.models import Q
from .forms import AdminCourseForm,AdminMaterialForm,AdminPQForm,AdminUniversityForm,StudentPQForm,MaterialForm
from .models import Material,AdvertProduct,University,Course,Pq
from .mixins import SearchMixin
from users.models import Profile

class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        products = AdvertProduct.objects.filter(approved=True)
        # sample = random.sample(set(products),4)
        context['showcase'] = products
        return context


class Universities(SearchMixin,ListView):
    model = University
    template_name = 'main/universities.html'
    paginate_by=20


class UniversityCourses(DetailView):
    model = University
    template_name = 'main/courses.html'
   

def load_courses(request):
    university_id = request.GET.get("university")
    courses = Course.objects.filter(university_id=university_id).order_by('name')
    return render(request,'main/course_dropdown_list.html',{'courses':courses})

class PqsView(DetailView):
    model = Course
    template_name = 'main/pqs.html'



class MaterialsView(SearchMixin,ListView):
    model = Material
    template_name = 'main/materials.html'

   

class CreateMaterial(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    form_class = MaterialForm
    success_url = reverse_lazy('users:dashboard')
    template_name = 'main/material_form.html'

    def create(self,*args,**kwargs):
        messages.info(request,"Successfully created")


class CreatePQ(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    form_class = StudentPQForm
    success_url = reverse_lazy('users:dashboard')
    template_name = 'main/pq_form.html'

    def create(self,*args,**kwargs):
        messages.info(request,"Successfully created")


class Adverts(ListView):
    model = AdvertProduct
    template_name = 'main/adverts.html'

    def get_queryset(self,*args,**kwargs):
        queryset = super().get_queryset(*args,**kwargs) 
        return queryset.order_by('price')


# Admin views
@user_passes_test(lambda x:x.is_superuser)
def admin_view(request):
    pq_form = AdminPQForm()
    material_form = AdminMaterialForm()
    university_form = AdminUniversityForm()
    course_form = AdminCourseForm()
    if request.method == "POST":
        if 'pq_btn' in request.POST:
            pq_form = AdminPQForm(request.POST,request.FILES)
            if pq_form.is_valid():
                pq_form.save()
        if 'material_btn' in request.POST:
            material_form = AdminMaterialForm(request.POST,request.FILES)
            if material_form.is_valid():
                material_form.save()
        if 'university_btn' in request.POST:
            university_form = AdminUniversityForm(request.POST)
            if university_form.is_valid():
                university_form.save()
        if 'course_btn' in request.POST:
            course_form = AdminCourseForm(request.POST)
            if course_form.is_valid():
                course_form.save()
    universities = University.objects.all()
    unapproved_adverts = AdvertProduct.objects.filter(approved=False).order_by('-created_date')
    unapproved_materials = Material.objects.filter(approved=False)
    unapproved_pqs = Pq.objects.filter(approved=False)
    materials = Material.objects.filter(approved=True)
    students = Profile.objects.count()
    context = {
        'pq_form':pq_form,
        'material_form':material_form,
        'university_form':university_form,
        'course_form':course_form,
        'universities':universities,
        'materials':materials,
        'student_count':students,
        'new_adverts':unapproved_adverts,
        'new_materials':unapproved_materials,
        'new_pqs':unapproved_pqs,
    }
    return render(request,'users/admin_dashboard.html',context)


# Approving stuff
def approve_advert(request,slug):
    advert = get_object_or_404(AdvertProduct,slug=slug)
    advert.approved = True
    advert.save()
    messages.success(request,"Approved {}".format(advert.name))
    return redirect("users:boss2")

def approve_pq(request,slug):
    pq = get_object_or_404(Pq,slug=slug)
    pq.approved = True
    pq.save()
    messages.success(request,"Approved {}".format(pq.name))
    return redirect("users:boss2")

def approve_material(request,slug):
    material = get_object_or_404(Material,slug=slug)
    material.approved = True
    material.save()
    messages.success(request,"Approved {}".format(material.name))
    return redirect("users:boss2")


# Deleting stuff
def delete_advert(request,slug):
    advert = get_object_or_404(AdvertProduct,slug=slug)
    name = advert.name
    advert.delete()
    messages.success(request,"Deleted {}".format(name))
    return redirect("users:boss2")

def delete_pq(request,slug):
    pq = get_object_or_404(Pq,slug=slug)
    name = pq.name
    pq.delete()
    messages.success(request,"Deleted {}".format(name))
    return redirect("users:boss2")

def delete_material(request,slug):
    material = get_object_or_404(Material,slug=slug)
    name = material.name
    material.delete()
    messages.success(request,"Deleted {}".format(name))
    return redirect("users:boss2")


