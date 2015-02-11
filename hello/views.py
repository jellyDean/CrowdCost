from django.shortcuts import render
from django.http import HttpResponseRedirect
import time, decimal, json
from django.db import connection

from .models import AnonUsers, Categories, Companies
from .forms import UserInput


# Create your views here.
def index(request):
    # if this is POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserInput(request.POST)

        # check whether it's valid:
        if form.is_valid():
            cursor = connection.cursor()

            cursor.execute('SELECT company_id FROM company WHERE company_name= %s', [request.POST["provider"]])
            companyId = cursor.fetchall()

            cursor.execute('SELECT category_id FROM categories WHERE category_name= %s', [request.POST["category"]])
            categoryId = cursor.fetchall()

            # process the data in form.cleaned_data as required
            # redirect to a new page
            new_user = AnonUsers(name=request.POST["name"],company_id=companyId[0][0],category_id=categoryId[0][0],anon_user_cost=request.POST["price"],
                                 anon_user_zipcode=request.POST["zipcode"], anon_user_timestamp=time.strftime('%Y-%m-%d %H:%M:%S'))
            new_user.save()

            request.session["category"] = categoryId[0][0]
            request.session["zipcode"] = request.POST["zipcode"]
            return HttpResponseRedirect('/search_results/',categoryId,companyId)

    # if a GET request, create a new blank form
    else:
        form = UserInput()
        form.fields['category'].choices = [('CABLE','CABLE'),('PHONE','PHONE'),('WEDDINGS','WEDDINGS')]
        form.fields['provider'].choices = [('TWC','TWC'),('VERIZON','VERIZON'),('WEDDINGS','WEDDINGS')]

    return render(request, 'index.html', {'form': form})


def search_results(request):
    category = str(request.session.get('category', False))
    zipcode = str(request.session.get('zipcode', False))
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM localtable.anonymous_users '
                                   'WHERE category_id = %s and anon_user_zipcode = %s', [category, zipcode])
    users = cursor.fetchall()

    total_cost = 0
    number_of_users = 0
    for user in users:
        total_cost += user[4]
        number_of_users += 1
        print(user[4])

    total_cost = total_cost / number_of_users

    # fetch the lat and long of the current zipcode entered by the anonymous user
    cursor.execute('SELECT * FROM localtable.us_zipcodes WHERE zip = %s', [zipcode])
    entered_zipcode = cursor.fetchall()
    state = entered_zipcode[0][2]
    latitude = entered_zipcode[0][3]
    longitude = entered_zipcode[0][4]

    upper_lat = latitude + decimal.Decimal(0.0085)
    lower_lat = latitude - decimal.Decimal(0.10)

    lower_long = longitude - decimal.Decimal(0.25)
    upper_long = longitude + decimal.Decimal(0.055)

    cursor.execute('SELECT * FROM localtable.us_zipcodes '
                   'WHERE (lat < %s and lat > %s) '
                   'and (long > %s and long < %s) and state = %s;', [upper_lat, lower_lat, lower_long, upper_long, state])
    radius_locations = cursor.fetchall()
    return render(request, 'search_results.html', {'users': users, 'average': str(format(total_cost, '.2f')),
                                                   'userCount': str(number_of_users),
                                                   'radius_locations': radius_locations,
                                                   "obj_as_json": json.dumps(radius_locations)})






