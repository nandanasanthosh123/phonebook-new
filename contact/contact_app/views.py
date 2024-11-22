from django.shortcuts import render,redirect
from .models import Contacts
from django.db import DatabaseError
# Create your views here.

def home(request):
    return render(request,"contact.html")


def addphone(request):
    responseDic = {}

    if request.method == 'POST':
        Name = request.POST.get('name', '').strip()
        Phone = request.POST.get('phone', '').strip()

        # Validate input
        if not Name or not Phone:
            responseDic["key"] = "Name and Phone Number are required."
            return render(request, "contact.html", responseDic)

        # Check if Phone is a valid integer
        try:
            Phone = int(Phone)
        except ValueError:
            responseDic["key"] = "Phone Number must be a valid integer."
            return render(request, "contact.html", responseDic)

        # Check if the contact already exists
        if Contacts.objects.filter(name=Name).exists():
            responseDic["key"] = "Contact already exists."
        else:
            new_contact = Contacts(name=Name, phone=Phone)
            new_contact.save()
            responseDic["key"] = "Phone Number is added."

    return render(request, "contact.html", responseDic)
def display(request):
    phndis=Contacts.objects.all()
    return render(request,"contact.html",{'phn':phndis})


def delete(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        # Try to retrieve the contact
        contact = Contacts.objects.filter(name=name).first()  # Use first() to avoid exceptions
        
        if contact:
            contact.delete()  # Delete the contact
            return redirect('display_contacts')  # Redirect to the display contacts page
        else:
            return render(request, "contact.html", {'key1': "Name not found"})
    else:
        return render(request, "contact.html", {'key1': "Invalid request method."})

def update(request):
    if request.method == 'POST':
        oldname = request.POST.get("oldname")
        newname = request.POST.get('newname')

        # Check if both fields are provided
        if not oldname or not newname:
            return render(request, "contact.html", {'key2': "Both old name and new name must be provided."})

        try:
            updated_count = Contacts.objects.filter(name=oldname).update(name=newname)
            if updated_count > 0:
                return render(request, "contact.html", {'key2': "Contact updated successfully."})
            else:
                return render(request, "contact.html", {'key2': "Old name not found."})
        except DatabaseError as db_error:
            print(f"Database error updating contact: {db_error}")
            return render(request, "contact.html", {'key2': "Database error: Not Updated."})
        except Exception as e:
            print(f"Unexpected error updating contact: {e}")
            return render(request, "contact.html", {'key2': "An unexpected error occurred: Not Updated."})

    # If request method is not POST, render the contact page without any message
    return render(request, "contact.html")