from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from .models import *
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
 

# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('Home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'Registration/signup.html', context)



def Home(request):
  return render(request, 'Home.html')

def index(request):
    person_fitness_form = PersonFitnessForm()
    person = PersonFitness.objects.all()
    return render(request, 'index.html', {
        'person_fitness_form': person_fitness_form,
        'person': person
    })

def about(request):
  return render(request, 'about.html')


#--------------------------------------------------------
def add_personfitness(request, user_id):
	# create the ModelForm using the data in request.POST
  form = PersonFitnessForm (request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_fitnessform = form.save(commit=False)
    new_fitnessform.user_id = user_id
    new_fitnessform.save()
  person = PersonFitness.objects.all()
  return render(request, 'index.html', {'person': person})



 # Full CRUD person fitness form 
 
class personfitnessformCreate(CreateView):
  model = PersonFitness
  fields = '__all__'

class personfitnessformUpdate(UpdateView):
  model = PersonFitness
  fields = '__all__'

# class personfitnessformDelete(DeleteView):
#   model = PersonFitness
#   success_url = 