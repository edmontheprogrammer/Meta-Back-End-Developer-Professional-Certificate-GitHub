from django import forms
from django.forms.widgets import NumberInput


# Note 1: This is an example that allows users to choose an option from a list of
# predefined choices in a list. Then the list items can be used in the form ##
FAVORITE_DISH = [
    ('italian', 'Italian'),
    ('greek', 'Greek'),
    ('turkish', 'Turkish'),
]


class DemoForm(forms.Form):
    name = forms.CharField()
    name_filed_option_two = forms.CharField(widget=forms.Textarea)
    name_filed_option_three_limiting_textarea_size = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}))
    email = forms.EmailField(label='enter an email address')
    # Getting a date such as day/month/year from the user
    reservation_date = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'}))
    # Using the "FAVORITE_DISH" list that contains a list of tuple elements in the form
    # "choices=FAVORITE_DISH" gives you a dropdown list to choose from
    favorite_dish_option_1 = forms.ChoiceField(choices=FAVORITE_DISH)
    # Displays all the list items as a radio button
    favorite_dish_option_2 = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_DISH)
