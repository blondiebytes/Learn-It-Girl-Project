
def hi():
	print("Hi there?")
	print("How are you?")


hi()

def hiThere(name):
	print("Hi there " + name + "!")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:
	hiThere(name)
	print("Next girl...")

for i in range(1, 6):
	print(i)

# source myvenv/bin/activate --> activate virtual environment
# pip install django
# django-admin startproject mysite . --> get stuff
# add var STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# to see if it works http://127.0.0.1:8000/

# python manage.py startapp blog --> make application
# add application to settings --> INSTALLED APPS
# add models
# python manage.py makemigrations blog --> creates migration file
# python manage.py migrate blog --> applying changes to database

# admin.site.register(Post) --> makes the model visible on the admin page
# python manage.py runserver --> run server and test

# python manage.py createsuperuser -> create a superuser