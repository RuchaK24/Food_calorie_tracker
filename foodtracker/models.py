# A user can have many food logs, a food log can have many foods, a food can have many images, a food
# can have many food logs, a food can have many food categories, a food category can have many foods
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'


# The FoodCategory class is a model that has a category_name field that is a CharField with a max
# length of 50
class FoodCategory(models.Model):
    category_name = models.CharField(max_length=50)
# `FoodCategory` is a class that inherits from `models.Model` and has a `name` field that is a
# `CharField` with a max length of `255`

   # The Meta class is a class within a class. It's used to set some additional properties of the
   # class
    class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

    def __str__(self):
        """
        The __str__ function is a special function in Python classes. It is similar to the toString()
        function in Java. It is used to represent the object of the class in the form of a string
        :return: The category name.
        """
        return f'{self.category_name}'

    @property
        """
        It returns the number of foods that belong to a category
        :return: The number of foods in the category.
        """
    def count_food_by_category(self):
        return Food.objects.filter(category=self).count()

# The Food class is a model that has a food_name, quantity, calories, fat, carbohydrates, protein, and
# category

class Food(models.Model):
    food_name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=100.00)
    calories = models.IntegerField(default=0)
    fat = models.DecimalField(max_digits=7, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=7, decimal_places=2)
    protein = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='food_category')

    def __str__(self):
        """
        The __str__ method is a special method that is called when you use the print() function on an
        object
        :return: The food name and the category of the food.
        """
        return f'{self.food_name} - category: {self.category}'

# The Image class is a model that has a foreign key to the Food class, and an image field
# The Image class is a model that has a foreign key to the Food class, and an image field

class Image(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='get_images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        """
        The __str__ function is a special function that is called when you print an object
        :return: The image file name.
        """
        return f'{self.image}'


# A FoodLog is a record of a user consuming a food
class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  # Creating a foreign key to the Food class.
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

    def __str__(self):
        return f'{self.user.username} - {self.food_consumed.food_name}'


class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    entry_date = models.DateField()

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weight'

    def __str__(self):
        return f'{self.user.username} - {self.weight} kg on {self.entry_date}'