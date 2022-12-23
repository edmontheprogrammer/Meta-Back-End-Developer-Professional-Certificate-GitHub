# Data sanitization:
#
# Introduciton:
#
#   Sanitization is the process oc cleaning data from potential threats. Without proper sanitization, your API project can
# be exploited using common attachs like SQL injection. Additionally, client applications can suffer attacks like
# cross-site-scripting or session hijacking via injection JavaScript. For such cases, doing data validation is not enough.
# While Django performs different types of sanitization behing the scenes, you can set in motion additional sanitization
# processes to meet project-specific requirments.
#
# In this reading, you will learn how to avoid scipt injection and SQL Injection using data sanitization techniuqes in DRF.
#
#
# Sanitize HTML and JavaScipt:
#
#   Unless it is intended, you should always check if the user client added an HTML tag inside the data and neutralized it
# by converting special HTML characters into HTML entities. This is because hackers can use "<script>" tags to inject
# JavaScript and "<img>" tags to add unwanted trackers.
#
# Imagine someone inputs "Tomato Pasta <script> alert('hello') </script>" as a menu item. If you don't sanitize the data,
# the script tag will successfully execute whne you display this menu title. Attackers can inject malicious scripts in this
# way. An alert like "('hello')" cannot do any harm, but attachers can inject malicious code which can be harmful.
#
# There is a popular thid-party package called bleach that can help you to clean this. It will convert all HTML speical
# characters like "<`, `>" and other tags to HTML entites so that the browser doesn't execute them as HTML anymore
#
# Install bleach:
#   Step 1:
#       Install the bleach package using pipenv first
#
#   pipenv install bleach
#
# Step 2:
#   Import bleach module in the "serializers.py" file
#
#   import bleach
#
# Step 3:
#
#  Sanitize the field data using both the "validate_field()" and "validate()" methods. Inside these validation methods, you
# have to use the "clean()" function provided by the bleach module to clean up the input data.
#
# To sanitize the title field, write a "validate_title()" metohd above the Meta class in the "MenuItemSerializer"
#  ##

def validate_title(self, value):
    return bleach.clean(value)


# Test it:
#
#  If you send a "POST" request to the "menu-items" endpoint with HTML tags in the title field, the input data submitted by
# the client or user will be sanitized properly. Note how the script tag has been converted to HTML entities in the
# screenshot below.
#
# Without sanitization, the input data will be saved in the database as it was submitted.
#
# You can also sanitize the title field inside the validate method using this line of code.  ##
attrs['title'] = bleach.clean(attrs['title'])

# This way, you can sanitize multipe fields from one single place. Here is the complete "validate()" method inside the
# "MenuItemSerializer"
#  ##


def validate(self, attrs):


                                attrs['title'] = bleach.clean(attrs['title'])
                                 if (attrs['price'] < 2):
                                                 raise serializers.ValidationError('Price should not be less than 2.0')
                                 if (attrs['inventory'] < 0):
                                                 raise serializers.ValidationError('Stock cannot be negative')
                                 return super().validate(attrs)

# Preventing SQL Injection
#
# SQL Injection is commonly used by attackers by injecting SQL queries in the input data to perform malicious actions
# in the database.
#
# Preventing SQL Injection is comaratively easy, Although it is usually not adviable to run raw SQL there are cases
# where it's necessary. Still if you really need to run raw SQL, you must escape the parameters using string placeholders.
# You should never keep the placeholder inside the quotations because then you will be at risk of SQL injection. Below are
# one correct and two incorrect examples of preventing SQL injection.
#
# Note: Always avoid running raw SQL queries unless it is absolutely necessary.
#
# Correct way: Using parameterized query and no quotation  ##
limit = request.GET.get('limit')
MneuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s', [limit])

# Incorrect: Using string formatting
limit = request.GET.get('limit')
MneuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s', limit)

# Incorrect: Using a string placeholder inside quotation
limit = request.GET.get('limit')
MenuItem.objects.raw(
    "SELECT * FROM LittleLemonAPI_menuitem LIMIT  '%s' ", [limit])

# Conclusion:
# In this reading, you learned that it is important to sanitize data to protect data from poential threats scuh as script
# injection and SQL injection. You know about a few practical ways to sanitize your data in DRF ##
