from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Recipe, RecipeIngredient

# Create your tests here.


# creating the user
User = get_user_model()


# Here is the test case for the user
class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='Agh',password='Abhi1998@')
        
    # check the password
    def test_user_pw(self):
        check = self.user_a.check_password(raw_password='Abhi1998@')
        self.assertTrue(check)
        
        
# recipe test case
class RecipeTestCase(TestCase):
    # set up function
    def setUp(self):
        self.user_a = User.objects.create_user(username='Abhi',password='Suraj1998@')
        # creating a model recipe for the user
        self.recipe_a = Recipe.objects.create(
            user = self.user_a,
            name = 'Grilled chicken'
        )
        # creating another recipe for the same user
        self.recipe_b = Recipe.objects.create(
            user = self.user_a,
            name = 'Grilled chicken tacos'
        )
        # creating the recipe ingredients
        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe = self.recipe_a,
            name = 'chicken',
            quantity = '1/2',
            unit = 'kg'
        )
        
    # test user count
    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(),1)
        
    # test user recipe count
    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        self.assertEqual(qs.count(),2)
        
    # test user forward recipe count
    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertTrue(qs.count(),2)
        
    # test recipe ingredient count for reverse 
    def test_user_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
        self.assertEqual(qs.count(),1)
        
        
    # test recipe ingredient count for forward
    def test_user_recipe_ingredient_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(),1)
        
    