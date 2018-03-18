from django.shortcuts import render
from .models import Location, Owner, Stay


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_location = Location.objects.count()
    num_owner = Owner.objects.count()
    num_stay = Stay.objects.count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_location': num_location,
            'num_owner': num_owner,
            'num_stay': num_stay
        },
    )
