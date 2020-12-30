import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ScholarsBank_final.settings')
import django
django.setup()


import pandas as pd
from main.models import University

schools = pd.read_csv("schools.txt",names=("University","Short Name","State"))
schools=schools.values
for school_ in schools:
    uni = University.objects.create(name=school_[0],abbreviation=school_[1],state=school_[2])
    uni.save()