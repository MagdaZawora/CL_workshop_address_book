from django.shortcuts import render
from .models import Person, Address, Phone, Email
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View

def show_all(request):
    contacts = Person.objects.all().order_by('surname')

    return render(request, 'Address_Book/show_all.html', {'title': 'Lista kontaktów', 'contacts': contacts})


def show_person(request, id):
    person = Person.objects.get(id=id)

    my_address = person.address_set.filter()
    my_phone = person.phone_set.filter()
    my_email = person.email_set.filter()

    context = {
        'person': person,
        'addresses': my_address,
        'phones': my_phone,
        'emails': my_email
    }
    return render(request, 'Address_Book/show_person.html', context)

def show_new(request, id):
    person = Person.objects.get(id=id)

    my_address = person.address_set.filter()
    my_phone = person.phone_set.filter()
    my_email = person.email_set.filter()

    context = {
        'person': person,
        'addresses': my_address,
        'phones': my_phone,
        'emails': my_email
    }
    return render(request, 'Address_Book/show_new.html', context)

def add_new(request):

    if request.method == "GET":
        return render(request, 'Address_Book/add_new.html', {'title': 'Dodawanie nowego kontaktu'})

    else:
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        Person.objects.create(name=name, surname=surname)
        return render(request, 'Address_Book/add_new.html', {'title': 'Dodawanie nowego kontaktu'})


def edit_person(request, id):
    person = Person.objects.get(id=id)

    my_address = person.address_set.filter()
    my_phone = person.phone_set.filter()
    my_email = person.email_set.filter()

    context = {
        'person': person,
        'addresses': my_address,
        'phones': my_phone,
        'emails': my_email,
    }

    if request.method == "GET":
        return render(request, 'Address_Book/edit_person.html', context)

    else:
        show_edit = "Dane zostały zmienione."
        person.name = request.POST.get('name')
        person.surname = request.POST.get('surname')
        person.address = request.POST.get('address')
        person.phone = request.POST.get('phone')
        person.email = request.POST.get('email')
        person.update()

        return render(request, 'Address_Book/edit_person.html', {'result': show_edit}, context)
    """
    else:
        address = Address.objects.get(person)
        show_edit = "Dane zostały zmienione."
        person.name = request.POST.get('name')
        person.surname = request.POST.get('surname')
        address.town = request.POST.get('address.town')
        address.street = request.POST.get('address.street')
        address.street_number = request.POST.get('address.street_number')
        address.flat_number = request.POST.get('address.flat_number')
        person.update()
        address.update()
    """


def delete_person(request, id):
    person = Person.objects.get(id=id)
    show_info = 'Kontakt został usunięty.'
    person.delete()
    return HttpResponse(show_info)

