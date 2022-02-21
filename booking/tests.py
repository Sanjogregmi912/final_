
from sqlite3 import register_adapter
from django.urls import reverse,resolve
from django.test import SimpleTestCase, TestCase
from booking import views
from booking.views import bookingfinal
from booking.views import booking_view
from booking.views import booking
from customer.views import homepage,login,registration,dashboard,view
from customer.views import customer_create,customer_edit,customer_delete,customer_update
from games.views import games_view,games_add,games_edit,games_update,games_delete,games_all
from games.views import games_rpg,games_battle,games_board
from user.views import user_view,user_create,user_edit,user_update,user_delete

#----__the testimng of urls in booking__------#
class TestURLS(SimpleTestCase ):
    ##--- the urls in booking ---- #
    def test_case_booking_final(self):
        url = reverse('booking_final')
        self.assertEquals(resolve(url).func,bookingfinal)

    def test_case_booking_view(self):
        url = reverse('booking_view')
        self.assertEquals(resolve(url).func,booking_view)

    def test_booking_new(self):
        url = reverse('booking_new',args=[1])
        self.assertEquals(resolve(url).func,booking)

    #-- urls in customer app #     
    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func,homepage)
    def test_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func,login)
    def test_register(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func,registration)
    def test_dashboard(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func,dashboard)
    def test_view(self):
        url = reverse('view')
        self.assertEquals(resolve(url).func,view)
    def test_customer_create(self):
        url = reverse('customer_create')
        self.assertEquals(resolve(url).func,customer_create)
    def test_customer_edit(self):
        url = reverse('customer_edit',args=[1])
        self.assertEquals(resolve(url).func,customer_edit)
    def test_customer_update(self):
        url = reverse('customer_update',args=[1])
        self.assertEquals(resolve(url).func,customer_update)
    def test_customer_delete(self):
        url = reverse('customer_delete',args=[1])
        self.assertEquals(resolve(url).func,customer_delete)
    #-- urls in games app -- #
    def test_games_view(self):
        url = reverse('games_view')
        self.assertEquals(resolve(url).func,games_view)    
    def test_games_add(self):
        url = reverse('games_add')
        self.assertEquals(resolve(url).func,games_add)      
    def test_games_edit(self):
        url = reverse('games_edit',args=[1])
        self.assertEquals(resolve(url).func,games_edit)  
    def test_games_update(self):
        url = reverse('games_update',args=[1])
        self.assertEquals(resolve(url).func,games_update)                  
    def test_games_delete(self):
        url = reverse('games_delete',args=[1])
        self.assertEquals(resolve(url).func,games_delete) 
    def test_games_all(self):
        url = reverse('games_all')
        self.assertEquals(resolve(url).func,games_all)
    def test_games_rpg(self):
        url = reverse('games_rpg')
        self.assertEquals(resolve(url).func,games_rpg)  
    def test_games_battle(self):
        url = reverse('games_battle')
        self.assertEquals(resolve(url).func,games_battle) 
    def test_games_board(self):
        url = reverse('games_board')
        self.assertEquals(resolve(url).func,games_board)  
     #-- urls from the user app _-- #
    def test_user_view(self):
        url = reverse('user_view')
        self.assertEquals(resolve(url).func,user_view) 
    def test_user_create(self):
        url = reverse('user_create')
        self.assertEquals(resolve(url).func,user_create)
    def test_user_edit(self):
        url = reverse('user_edit',args=[1])
        self.assertEquals(resolve(url).func,user_edit)
    def test_user_update(self):
        url = reverse('user_update',args=[1])
        self.assertEquals(resolve(url).func,user_update)
    def test_user_delete(self):
        url = reverse('user_delete',args=[1])
        self.assertEquals(resolve(url).func,user_delete)                  
    
    