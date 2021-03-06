from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import time, decimal, json, sys
from django.db import connection
from django.core import serializers

from .models import AnonUsers, Categories, Companies, US_Zipcodes
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
            sql =  "INSERT INTO localtable.anonymous_users (name, company_id, category_id, anon_user_cost, anon_user_zipcode, anon_user_timestamp) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (request.POST["name"],companyId[0][0],categoryId[0][0],request.POST["price"],request.POST["zipcode"],time.strftime('%Y-%m-%d %H:%M:%S')))

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

    # Calculate the average for the user entered zipcode and category
    total_cost = calculate_average(category, zipcode)

    # fetch the lat and long of the current zipcode entered by the anonymous user
    cursor.execute('SELECT * FROM localtable.us_zipcodes WHERE zip = %s', [zipcode])
    entered_zipcode = cursor.fetchall()
    print " entered_zipcode: " + str(entered_zipcode)
    sys.stdout.flush()
    my_state = entered_zipcode[0][2]
    latitude = entered_zipcode[0][3]
    longitude = entered_zipcode[0][4]

    # Apply 'radius' formula to find zipcodes around our original point
    upper_lat = latitude + decimal.Decimal(0.0085)
    lower_lat = latitude - decimal.Decimal(0.15)

    lower_long = longitude - decimal.Decimal(0.25)
    upper_long = longitude + decimal.Decimal(0.055)

    print "upper lat: " + str(upper_lat) + " lower lat: " + str(lower_lat) + " lower_long: " + str(lower_long) + " upper long: " + str(upper_long) + " my state: " + str(my_state)
    sys.stdout.flush()

    # data = US_Zipcodes.objects.filter(lat__lt=upper_lat, lat__gt=lower_lat,
    #                                                                 long__gt=lower_long, long__lt=upper_long,
    #                                                                 state__exact=my_state)
    cursor.execute('SELECT * FROM localtable.us_zipcodes WHERE lat < %s '
                   'and lat > %s and long > %s and long < %s and state = %s', [upper_lat, lower_lat, lower_long, upper_long, my_state])
    data = cursor.fetchall()

    print " data1: " + str(data)
    sys.stdout.flush()


    # turn the tuple into json

    data = {"zip"  : [x[0] for x in data],
            "city"      : [x[1] for x in data],
            "state"     : [x[2] for x in data],
            "lat"       : [str(x[3]) for x in data],
            "long"      : [str(x[4]) for x in data],
            "timezone"  : [x[5] for x in data],
            "dst"       : [x[6] for x in data],
            "id"        : [x[7] for x in data]}




    # Calculate the averages of the surrounding zipcodes
    radius_locations = []
    for zipcode in data['zip']:
        radius_locations.append(str(format(calculate_average(category, zipcode), '.2f')))
        #zipcode_averages.append(averages_dict)

    #radius_locations = zipcode_averages

    print "radius locations: " + str(radius_locations) + " data2: " + str(data) + " total cost: " + str(total_cost)
    sys.stdout.flush()
    data = json.dumps(data)

    return render(request, 'search_results.html', {'average': str(format(total_cost, '.2f')),

                                                   'radius_locations': radius_locations,
                                                   "obj_as_json": data})


def calculate_average(category, zipcode):
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM localtable.anonymous_users '
                                   'WHERE category_id = %s and anon_user_zipcode = %s',
                   [category, str(zipcode.replace(" ", ""))])
    users = cursor.fetchall()

    total_cost = 0
    number_of_users = 0
    for user in users:
        total_cost += user[4]
        number_of_users += 1

    if number_of_users > 0:
            total_cost = total_cost / number_of_users

    else:
            total_cost = 0


    print("total cost: " + str(total_cost))

    return total_cost






