# Input types:
#
#  You already learned about the input HTML tag and how the type property determines the data your users can type in.
# This cheat sheet should be a reference to decide what type best suits your use case. Most of the inputs go hand in hand
# with the labels tag for best accessibility practices.
#
# Button:
#   This displays a clickable button and it's mostly used in HTML forms to activate a script when clicked.
#
#    <input type="button" value="Click me" onclick="msg()" />
#
# Keep in mind, you can also define buttons with the "<button>" tag, with the added benefit of being able to place content
# like text or images inside the tag.  ##
#
# <button onclick="alert('Are you sure you want to continue?')">
#     <img src="https://yourserver.com/button_img.jpg"
#         alt="Submit the form" height="64" width="64">
#  </button>
#
# Checkbox:
#
#   Defines a check box allowing single values to be selected or deselected. They are used to lset a user select one or
# more options from a limited number of choices. ##
#
# <input type="checkbox" id="dog" name="dog" value="Dog">
# <label for="dog">I like dogs</label>
# <input type="checkbox" id="cat" name="cat" value="Cat">
# <label for="cat">I like cats</label>
#
# Radio:
#
# Displays a radio button, allowing only a single value to be selected out of multiple choices. They are normally presented
# in a radio group, which are collections of radio buttons describing a set of related options that share the same "name"
# attribute. ##
# <input type="radio" id="light" name="theme" value="Light">
# <label for="light">Light</label>
# <input type="radio" id="dark" name="theme" value="Dark">
# <label for="dark">Dark</label>
#
#
# Submit:
#
#  Displays a submit button for submitting all values from an HTML form to a form-handler, typically a server. The
# form-handler is specificed in the form's action attribute.
#
# <form action="myserver.com" method="POST">
#   …
# <input type="submit" value="Submit" />
# </form>
#
# Text:
#
#   Defines a basic single-line text field that a user can enter text into.  ##
# <label for="fname">First name:</label>
# <input type="text" id="fname" name="fname">
#
#
# Password:
#   Defines a single-text field whose valuse is obscured, suited for sensitive information like passwords.
# <label for="pwd">Password:</label>
# <input type="password" id="pwd" name="pwd">
#
# Date:
#   Displays a control for entering a date (year, month, and day) with no time. ##
# <label for="dob">Date of birth:</label>
# <input type="date" id="dob" name="date of birth">
#
# Datetime-local:
#
#   Defines a control for entering a date and time, including the year, month and day, as well as the time in hours and
#   minutes
# <label for="birthdaytime">Birthday (date and time):</label>
# <input type="datetime-local" id="birthdaytime" name="birthdaytime">
#
# Email:
#   Defines a field for an email address. It's similar to plain text input, with the addition that it validates
# automatically when submitted to the server.
# <label for="email">Enter your email:</label>
# <input type="email" id="email" name="email">
#
# File:
#   Displays a control that lets the user selecte and upload a file from their computer. To define the types of files
# permissible you can use the "accept" attribute. Also, to enable multiple files to be selected, add the "multiple"
# attribute.
# <label for="myfile">Select a file:</label>
# <input type="file" id="myfile" name="myfile">
#
# Hidden:
#   Defines a control that is not displayed but whose value is still submitted to the server ##
# <input type="hidden" id="custId" name="custId" value="3487">
#
# Image:
#   Defines an image as a graphical submit button. You should use the "str" attribute to point to the locaiton of your image
# file.  ##
# <input type="image"src="submit_img.png" alt="Submit" width="48" height="48">
#
# Number:
#   Defines a control for entering a number. You can use attribute to specify restructions, such as min and max values
# allowed, the number intervals or a default value.
# <input type="number" id="quantity" name="quantity" min="1" max="5">
#
# Range:
#   Displays a range widget for specifying a number between two values. The precise value, however, is not considered
# important. This is typically represented using a slider or dial control. To define the range of acceptable values, use
# the "min" and "max" properties. ##
# <label for="volume">Volume:</label>
# <input type="range" id="volume" name="volume" min="0" max="10">
#
# Reset:
#   Displays a button that resets the contents of the form to their default values.
#   <input type="reset">
#
# Searh:
#   Defines a text field for entering a search query. These are functionally identical to text inputs, but may be styled
# differently depending on the browser.
# <label for="gsearch">Search in Google:</label>
# <input type="search" id="gsearch" name="gsearch">
#
# Time:
#   Displays a control for entering a time value in hours and minutes, with no time zone.
# ##
# <label for="appt">Select a time:</label>
# <input type="time" id="appt" name="appt">
#
# Tel:
#   Defines a control for entering a telephone number. Browsers that do not support "tel" fall back to standard text input.
# You can optionally use the "pattern" field to perform validation  ##
# <label for="phone">Enter your phone number:</label>
# <input type="tel" id="phone" name="phone" pattern="[+]{1}[0-9]{11,14}">
#
# Url:
#   Displays a field for entering a text URL. It works similary to a text input, but perform automatic validaiton before
# being sumbitted to the server.  ##
# <label for="homepage">Add your homepage:</label>
# <input type="url" id="homepage" name="homepage">
#
# Week:
#   Defines a control for entering a date consisting of a week-year number and a year, with no time zone. Keep in mind that
# this is a newer type that is not supported by all browsers. ##
# <label for="week">Select a week:</label>
# <input type="week" id="week" name="week">
#
#
# Month:
#   Displays a control for entering a month and year, with no time zone. Keep in mind that this is a newer type that is not
# supported by all browsers. ##
# <label for="bdaymonth">Birthday (month and year):</label>
# <input type="month" id="bdaymonth" name="bdaymonth" min="1930-01" value="2000-01">
#
# Note 1: HTTP "POST" request is more secure than HTTP "GET" request, but the data can
# still be read by a third-party under HTTP "POST" request. Therefore, HTTPS is used to
# encyption and make that data more secure.
