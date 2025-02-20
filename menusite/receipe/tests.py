from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Receipi , ReceipiIngredient
from django.core.exceptions import ValidationError
# Create your tests here.


User = get_user_model()


# setting the test case for the user
class UserTest(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('test',password='abc123@')
        
    # first test case for the password check
    def test_check_pw(self):
        checked = self.user_a.check_password('abc123@')
        self.assertTrue(checked)
        
        
        
        

#  setting up for the Receipe model
class ReceipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('test',password='abc123@')
        self.receipi_a = Receipi.objects.create(
            name = 'Chicken tandoor',
            user = self.user_a
        )
        self.receipi_b = Receipi.objects.create(
            name = 'Chicken gravy',
            user = self.user_a
        )
        self.receipi_ingredient_a = ReceipiIngredient.objects.create(
            receipi = self.receipi_a,
            name = 'Chicken',
            quantity = '1/2',
            unit = 'kg'
        )
        
    # first case for the test count
    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(),1)
        
        
    #  second case for the test count for the setting receipe
    def test_receipi_reverse_count(self):
        user = self.user_a
        qs = user.receipi_set.all()
        self.assertEqual(qs.count(),2)
    
    # 3rd case for the test forward count for the receipe
    def test_receipe_forward_count(self):
        user = self.user_a
        qs = Receipi.objects.filter(user=user)
        self.assertEqual(qs.count(),2)
        
    # 4th case for the reverse test receipi ingridient
    def test_receipi_ingridient_reverse_count(self):
        receipe = self.receipi_a
        qs = receipe.receipiingredient_set.all()
        self.assertEqual(qs.count(),1)
        
    # 5th test case for the forward test for the receipi ingredent
    def test_receipi_ingridient_count(self):
        receipi = self.receipi_a
        qs = ReceipiIngredient.objects.filter(receipi=receipi)
        self.assertEqual(qs.count(),1)
        
    # 6 th test case for user to receipi count
    def test_user_to_receipi_count(self):
        user = self.user_a
        qs = ReceipiIngredient.objects.filter(receipi__user=user)
        self.assertEqual(qs.count(),1)
        
        
    # 7 th test case for user to show the reverse relation
    def test_user_to_recceipi_reverse_count(self):
        user = self.user_a
        receipi_ingridient_ids = list(user.receipi_set.all().values_list('receipiingredient',flat=True))
        qs = ReceipiIngredient.objects.filter(id__in=receipi_ingridient_ids)
        self.assertEqual(qs.count(),1)
        
    # test case for the clean validation for the unit

    def test_case_for_validation(self):
        valid_unit = 'gram'
        ingredient = ReceipiIngredient(
            name='New',
            receipi=self.receipi_a,
            quantity=10,
            unit = valid_unit
        )
        ingredient.full_clean()

        
    #  test case for validation for unit
    def test_case_for_validation_error(self):
        invalid_unit = 'nda'
        with self.assertRaises(ValidationError):
            ingredient = ReceipiIngredient(
                name='New',
                receipi = self.receipi_a,
                quantity = 10,
                unit = invalid_unit
            )
            ingredient.full_clean()
            
            
    
        
        
        
    
        
        
