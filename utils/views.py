import csv
import io
from django.forms import ValidationError
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .forms import UniversityCreateForm

@user_passes_test(lambda x:x.is_superuser)
def add_bulk_university(request):
    template = 'utils/add_universities.html'
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            raise ValidationError('Not a csv file!!')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        for row in csv.DictReader(io_string,delimiter=','):
            form = UniversityCreateForm(row)
            if form.is_valid():
                form.save()
            else:
                raise ValidationError('There was an error!')
    return render(request,template)
            
    