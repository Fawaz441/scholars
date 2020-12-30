from django import forms
from .models import University,Course,Pq,Material,AdvertProduct


class AdminUniversityForm(forms.ModelForm):
    class Meta:
        fields = ["name","state","abbreviation"]
        model = University


class AdminCourseForm(forms.ModelForm):
    class Meta:
        fields = ["university","name","abbreviation"]
        model = Course

class StudentPQForm(forms.ModelForm):
    class Meta:
        fields = ["name","university","course","file"]
        model = Pq

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["course"].queryset = Course.objects.none()

        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['course'].queryset = Course.objects.filter(university_id=university_id).order_by('name')
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.course_set.order_by('name')

class AdminPQForm(forms.ModelForm):
    class Meta:
        fields = ["name","university","course","file","approved"]
        model = Pq

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["name","file"]

class AdminMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["name","file","approved"]



# Adverts for Products
CATEGORY = (
    ("GADGET","GADGET"),
    ("CLOTHING","CLOTHING"),
    ("SHOES","SHOES"),
)
class AdvertProductForm(forms.ModelForm):
    class Meta:
        fields = ["name","price","image1","image2","category"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["category"].choices = CATEGORY






