from django.db import models
from django.utils.text import slugify
from users.models import Profile


class University(models.Model):
    name = models.CharField(max_length=100,unique=True)
    state = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(blank=True,null=True)
    
    def __str__(self):
        return "{} ------------ {}".format(self.name.upper(),self.abbreviation)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)


    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Universities'


class Course(models.Model):
    university = models.ForeignKey(University,on_delete=models.CASCADE,related_name='courses')
    name = models.CharField(max_length=100,null=True,blank=True)
    abbreviation = models.CharField(max_length=8)
    slug = models.SlugField(blank=True,null=True)
    
    def __str__(self):
        return "{} {}".format(self.name,self.abbreviation)
    
    def save(self,*args,**kwargs):
        slug_name = str(self.university.name+self.name)
        self.slug = slugify(slug_name)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['name']
    

class Pq(models.Model):
    uploader = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='uploaded_pqs',null=True,blank=True)
    name = models.CharField(max_length=100,unique=True)
    university = models.ForeignKey(University,related_name='pqs',on_delete=models.CASCADE,blank=True,null=True,unique=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True,unique=False)
    file = models.FileField(upload_to='pqs')
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    slug = models.SlugField(blank=True,null=True)

    def __str__(self):
        return "{} file".format(self.name)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['name']


class Material(models.Model):
    uploader = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='uploaded_materials',null=True,blank=True)
    name = models.CharField(max_length=100,unique=True)
    file = models.FileField(upload_to='materials')
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    slug = models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']

CATEGORY = (
    ("GADGET","GADGET"),
    ("CLOTHING","CLOTHING"),
    ("SHOES","SHOES"),
)

class AdvertProduct(models.Model):
    name = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    image1 = models.ImageField(upload_to='products')
    image2 = models.ImageField(upload_to='products')
    seller = models.ForeignKey(Profile,related_name='products',on_delete=models.CASCADE)
    category = models.CharField(max_length=12,choices=CATEGORY)
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_date']

    



