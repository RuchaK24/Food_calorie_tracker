from django import forms

from .models import Food, Image


# The FoodForm class is a ModelForm class that inherits from the ModelForm class in the forms module. 
# 
# The Meta class is a nested class that tells the FoodForm class which model to use and which fields
# to use. 
# 
# The __init__ method is a special method that is called when the class is instantiated. 
# 
# The super method is used to call the __init__ method of the parent class. 
# 
# The for loop iterates through each visible field in the form and adds a class attribute to the
# field's widget. 
# 
# The class attribute is used to apply Bootstrap styling to the form. 
# 
# The form is rendered in the template using the following code:
class FoodForm(forms.ModelForm):
    '''
    A ModelForm class for adding a new food item
    '''
    class Meta:
        model = Food
        fields = ['food_name', 'quantity', 'calories', 'fat', 'carbohydrates', 'protein', 'category']

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ImageForm(forms.ModelForm):
    '''
    A ModelForm class for adding an image to the food item
    '''
    class Meta:
        model = Image
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.visible_fields()[0].field.widget.attrs['class'] = 'form-control'