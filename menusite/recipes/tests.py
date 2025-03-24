from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.exceptions import ValidationError
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
        # creating the another recipe ingredients
        self.recipe_ingredient_b = RecipeIngredient.objects.create(
            recipe = self.recipe_a,
            name = 'spinach',
            quantity = 'abukruh',
            unit = 'ounce'
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
        self.assertEqual(qs.count(),2)
        
        
    # test recipe ingredient count for forward
    def test_user_recipe_ingredient_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(),2)
        
    # test recipe ingredient for the specific user
    def test_specific_user_to_level_recipe(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user = user)
        self.assertEqual(qs.count(),2)
        
    # test recipe ingredient for the specific user reverse relation
    def test_specific_user_to_level_recipe_reverse(self):
        user = self.user_a
        recipeingredient_id = list(user.recipe_set.all().values_list('recipeingredient', flat=True))
        qs = RecipeIngredient.objects.filter(id__in=recipeingredient_id)
        self.assertEqual(qs.count(),2)
    
    # test recipe two level relation for the user
    def test_two_level_relation_via_recipe(self):
        user = self.user_a
        ids = user.recipe_set.all().values_list("id",flat=True)
        qs = RecipeIngredient.objects.filter(recipe__id__in=ids)
        self.assertEqual(qs.count(),2)
        
    # test the unit for the validator
    def test_unit_validation(self):
        valid_unit = 'ounce'
        ingredient = RecipeIngredient(
            name = 'New',
            quantity = 10,
            recipe = self.recipe_a,
            unit = valid_unit
            )
        ingredient.full_clean()
            
            
    # test for the validation error
    def test_unit_validation_error(self):
        invalid_unit = 'nda'
        with self.assertRaises(ValidationError):
            ingredient = RecipeIngredient(
                name='New',
                quantity=10,
                recipe=self.recipe_a,
                unit=invalid_unit
            )
            ingredient.full_clean()
            
    # test for the float quantity
    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a.quantity_as_float)
        self.assertIsNone(self.recipe_ingredient_b.quantity_as_float)
        
    