from urllib import response
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from customer.models import Customer
from django.contrib.auth.models import User


# the testing of the crude operation used #
class Testviews(TestCase):
    ## from customer views test ## 
    def test_customer_view(self):
        user=User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client= Client()
        logged_in=client.login(username="testcase",password="123")
        url = reverse('view')
        response = client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"customers/view.html")
    def test_customer_create(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase",password="123")
        url = reverse('customer_create')
        response = client.post(url,{
            'name':"test",
            'email':"emailtest",
            'phone' : "test phone",
     
        })
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/view')

        ## from booking views test ## 

    def test_booking_view(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase",password="123")
        url = reverse('booking_view')
        response = client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'booking/booking_view.html')


        # views from the games app ## 

    def test_games_view(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase", password="123")
        url=reverse('games_view')
        response = client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"games/view.html")

    def test_game_add(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase",password="123")
        url = reverse('games_add')
        response = client.post(url,{
            'name':"testgamename",
            'price':"testprice",
            'type' : "testtype",
            'image' : 'testimage',
     
        })
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/games/games_view',)

        ## view from the user app ## 
    def test_user_view(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase",password="123")
        url = reverse('user_view')
        response = client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'user/view.html')
    def test_user_add(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase",password="123")
        url = reverse('user_create')
        response = client.post(url,{
         'username' :'testUsername',
         'email' : "test email",
         'password':'test password'
     
        })
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/user_view')