from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class AnonUsers(models.Model):
    class Meta:
        db_table = 'anonymous_users'
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='name', max_length=100)
    company_id = models.IntegerField(db_column='company_id')
    category_id = models.IntegerField(db_column='category_id')
    anon_user_cost = models.DecimalField(db_column='anon_user_cost',decimal_places=2,max_digits=18)
    anon_user_zipcode = models.CharField(db_column='anon_user_zipcode', max_length=10)
    anon_user_timestamp = models.DateTimeField(db_column='anon_user_timestamp')


class Companies(models.Model):
    class Meta:
        db_table = 'company'
    company_id = models.AutoField(primary_key=True, db_column='company_id')
    company_name = models.CharField(db_column='company_name', max_length=100)


class Categories(models.Model):
    class Meta:
        db_table = 'categories'
    category_id = models.AutoField(primary_key=True, db_column='category_id')
    category_name = models.CharField(db_column='category_name', max_length=100)


class US_Zipcodes(models.Model):
    class Meta:
        db_table='localtable.us_zipcodes'
    zip = models.CharField(db_column='zip', max_length=100)
    city = models.CharField(db_column='city', max_length=100)
    state = models.CharField(db_column='state', max_length=100)
    lat = models.DecimalField(db_column='lat', decimal_places=10,max_digits=18)
    long = models.DecimalField(db_column='long', decimal_places=10,max_digits=18)
    timezone = models.IntegerField(db_column='timezone')
    dst = models.CharField(db_column='dst', max_length=100)




