# All selectors and their specificity
#
# As you build a website, the complexity of the code might increase to such a point that more than one CSS fule is applied
# to the same element. Or, you might accidentally add more than one rule over the same element. This results in conflicts
# as ony one rule can be applied to a specific property. For example, the color of a certain p tag can either be blue or
# white, but not both. CSS engines use something called specificity to resolve these conflicts. Specificity is the ranking
# or score that helps CSS determine the final rule that will be applied to a given element.
#
# This reading will help you grasp how the element with the 'highest' specificity is selected by CSS. But before you read
# on, it is important to note that these rules only apply in cases where conflicts arise for the properties.
#
# Specificity hierarchy:
#
#   CSS has a set of rules that it uses to 'score' or assign a certain weight to selectors and this creates a specificity
# hierarchy. Based on the weights, there are four categories in this hierarchy:
#
#   * Inline styles
#   * IDs
#   * Classes, attributes and pseudo-classes
#   * Elements and pseudo-elements
#
# Inline styles:
#   Inline styles are attached to the elements within your HTML code with the 'style' attribute. Inline styles have the
# highest specificity. That means that rules that are defined as inline styles will be applied irrespective of other rules.
#
# For example, take these two rules that create a conflict in color styling for a p tag:  ##
#  <p style=“color: white;”> 
#    p{color: blue} 
#
# The p tag will be colored  white because it is declared inside the inline tag.
#
# IDs:
#   Next in the hierarchy are IDs and by now you know that they are represented by '#'. For example, #div
#
# Classes, attributes and psuedo-classes
#
#  Classes, and the attributes inside the selectors come next with what is called the pseudo-classes that you will soon
# learn more about.
#
# For example,
#
#   .my-class
#
#   '["attribute"]
#
#   div:hover
#
#   Elements and pesudo-elements
#
# Finally, elements and something you call pesudo-elements have the lowest position in the specificty hierachy. You will
# learn more about pesudo-elements later in this lesson.
#
# Calculating scores:
#
#   But by now you might wonder how is specificty calculated?
#
#   CSS uses the hierachical model internally to calculate the specificity of the selectors used on a web page. But often
# as the size of CSS code increases, developers unavvoidably face rule conflicts. In these cases, developers use the
# specificity hierachy to calculate the precdence of CSS rules and to control the outcome of their web pages.
#
# Let's explore a practical example of how to determine the score of a few selectors.
#
# #hello {} will be 0100
#
# div {} will be 0001 and
#
# div p.foo {} will be 0012
#
# In the order stated above, the four categories will be assigned values 1000, 100, 10 and 1 with the element selectors
# having the lowest value of 1. These scores will be calculated respectively for each element present inside the selector.
# The total score for these elements is then calculated and the one withe the highest value has the higest specificity.
#
# Let's exmplore a couple of examples for clarity. Take note that the properties and values are not included in these
# examples to keep the focus on the selectors only.
#
# Example 1:
#
#   p{}
#   div p {}
#   div p.foo {}
#
#   p => 1 element => 0 0 0 1 => Score: 1
#
#   div p => 2 elements => 0 0 0 2 => Score: 2
#
#   div p.foo{} => elements and 1 class selector => 0 0 1 2 => Score: 12
#
#   The third case has a total of 12 for the p tag and so has the highest specificity. The rules for the other two cases
# are then overridden and the rules inside the third case are applied.  ##
