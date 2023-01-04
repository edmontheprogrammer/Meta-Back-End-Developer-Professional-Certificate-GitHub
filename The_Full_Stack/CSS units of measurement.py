# CSS units of measurement:
# 
# A web page, as you know it, is two-dimensional. In other words, it has width and height. There are a number of other ways
# you can express this such as vertical and horizontal, length and breadth, x and y axis and so on. Another propery of a 
# web page is its size which can either be static or dynamic. When you've encountered enough CSS code, you will note a 
# number of different ways in which the values for the same property can be declared using different units of measurement.
# Most of these units of measurement are used to account for the dynamism and dimensionality of a web page. 
# 
# Le'ts examine the most widley used units of measurement. They can broadly be categoriezed as Absolute or Relative units. 
# 
# Absolute units: 
#   Absolute units are constant across different devices and have a fixed size. They are useful for activities like printing
# a page. They are not so suitable when it comes to  the wide variety of devices in use today that have different viewport
# sizes. Because of this, absolute units are used when the size of the web page is known and will remain constant. 
# 
# The table for absolute units can be seen below: 
# 
# Unit          Name                   Comparison 
#   
#  Q      Quater-millimeters             1Q = 1/40th of 1cm     
#  mm        Millimeters                 1mm = 1/10th of 1cm 
#
#  px       Pixels                       1px = 1/96th of 1in
#  
#  * and others 
# 
# 
# Of these, the pixels and centimeters are most frequenctly used for defining properties. 
# 
# 
#  Relative values:
# 
#   When you create a web page, you will almost never have only a single element present inside it. Even in case of 
# containers such as flexboxes and grids, there's usually more than one element present taht rules are applied to. 
# Relative valuess are defined 'in a relation' to the other elements present inside the parent element. Additionally, they 
# are defined 'in a relation' to the viewport or the size of the visible web page. Given the dynamic nature of web pages 
# today and the variable size of devices in use, relative units are the go-to option in many cases. Below is a list of some
# of the important relative units 
# 
# 
# Unit          Description and relativity 
# 
#  em            Font size of the parent where present.
# 
#  %             Denotes a percentage value in relation to its parent element. 
#  vw            1% of the viewport width.
#  vh            1% of the viewport height.
#
#  * and others 
# 
# Many of these units are used in terms of the relative size of fonts. Some units are more suitable depending on the 
# relative context. Like when the dimensions of the viewport are important, it's more appropriate to the "vw" and "vh". 
# In a broader context, the relative units you will see more frequently used are precentage, "em", "vh", and "rem". 
# 
# Much like the absolute and relative units discussed above, certain properties have their own set of acceptable values
# that need to be taken into account. For example, color-based properties such as "backgroundcolor" will have values
# such as hexadecimal, "rgb()", "rgba()", "hsl()" and "hsla()" and so on. Each property should be explored on an 
# individual basis and practicing with the code will help you to decide which of these units of measurement are the most 
# suitable choice.   ##