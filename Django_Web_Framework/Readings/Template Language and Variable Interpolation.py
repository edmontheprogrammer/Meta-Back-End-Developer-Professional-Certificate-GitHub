# Template Language and Variable Interpolation:
#
# In this reading, you will futher explore the templating language and how ti can be used to create markup.
#
# This reading will also showcase the use of variables and how they be dynamically passed in a template to render out
# different content.
#
# Intorduce learneers to the template language with variables, filters and tags.
#
# Template Engine:
#
#   Modern web frameworks use a web template system to merge a data source with static HTML to generate dynamic web pages.
#
# A Web template is an otherwise static HTML script interspersed with placeholder blocks of template language code.
# The template engine takes one set od ata from any souce, such as a database table, substitues in placeholders and tenders
# the generated content to the client browser,
#
# Database ---- Web ---- Template ----> Template Engine ---> Document 1 and Document 2
#
# Web Documents:
#
#   Django's template engine uses its own Django Template Language. The default project template is configured that way.
# However, you may choose to use any other template language such as "jinja2".
#
# Django Template Language has three important compoenets: variables, tags and filters.
#
# Template Variable:
#
#   As you have previously learned, templates are HTML Pages. The "DIRS" attribute of the "TEMPLATES" variable in
# "settings.py" file points to the folder in which the templates are stored. Generally, the templates folder is in the
# project folder.
#
# The easiest way to display a template web age is by callding the "render()" function from within a view function. Its
# three parameters are the HTTP request object, the page itself, and a context dictionary.
# Assuming that the client URL is " http://localhost:8000/myapp/Novak, " the following view function receives the path
# parameters from the URL dispatcher and passes it as context to the template:
#
#   ##
from django.shortcuts import render


def index(request, name):
    context = {'name': name}
    return render(request, 'index.html', context)


# The keys in the context dictionary are available to the template as a variable:
#
#   When put inside double curly brackets, the value is substitued at runtime.
#
# Put the following statment in the body of "index.html" ##
<h2 Welcome {{name}} < /h2 >

# As a result, if the view recieves a Novak as the parameter, "Hello Novak" is rendered.
#
# The value of any key in the context may be a singular object (string, integer), a list or a dictionary.
#
# A certain view passes a "person" dictionary as a context ##
person = {'name': 'Roger', 'profession': 'Teacher'}
return render(request, 'person.html', person)

# Inside the template, you can access teh value assoicated with each key with the dot (".") operator just as the attributes
# of an object are used. For example: ##
Name: {{person.name}}
Profession: {{person.profession}}

# This will render the following output on the browser.
#
#   * Name: Roger
#   * Profession: Teacher
#
# Template Tags:
#
#   Just as there are HTML tags, the Django template language defines several tags. You can think of the tags as keywords
# in a traditional programming language. You place the tags inside "{% tag %}" symbols
#
# The "if" and "for" tags are important because they add processing logic to the web page.
#
# "{% if %}"
#
# With the "if" tag, the template variable is checked against a boolean expression and a block of HTML is rendered
# conditionally.   ##
{% if expression == True % }
HTML block 1
{% else % }
HTML block 2
{% endif % }

# Even though the syntax of "if" and "for" is very similar to Python, Django template language (DTL) doesn't use uniformly
# indented blocks. Hence, for every "if" tag, there is an "endif" tag.
#
# A simple example of Django's "if" tag is as follows:
#
#   The following view passes "{'user': 'admin'}" dictionary as context to the template. ##


def index(request):
    context = {'user': 'admin'}
    return render(request, 'index.html', context)

# The conditional block in the template should be as follows: ##

{% if user == "admin" % }
<h2 > Welcome {{user}} < /h2 >
{% else % }
<h2 > Welcome Guest. You don not have admin access < /h2 >
{% endif % }

# {% for %}:
#
#  You can construct a looping construct inside the template with "{% or %}" and {% endfor %} tags. It is used to traverse
# any Person iterable such as a list, tuple, or string.
#
# In the following example, you pass a list to the template as its context.  ##


def myview(request):
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust']

    return render(request, 'langs.html', {'langs': langs})


# Inside the template, the "for" loop is constructed, much like in Python to render the names of languages as unordered list
#  ##
<h1 > List of Languages < /h1 >
<ul >
    {% for lang in langs % } 
    <li > {{lang}} < /li >
    {% endfor % } 
</ul >

# if the value of a context variable is a dictionary, you can traverse the key-value pairs using the for syntax. ##
{% for key, value in data.items % } 
{{key}}: {{value}}
{% endfor % } 

# DTL has a number of helper variables to used within the loop:
# "forloop.counter": The current iteration of the loop ##

<ul >
    {% for lang in langs % } 
    <li > {{forloop.counter}}: {{lang}} < /li >
    {% endfor % }  
</ul >

# Output:
#   List of Languages: ##
# 1: Python

# 2: Java

# 3: PHP

# 4: Ruby

# 5: Rust

# forloop.revcounter: The number of iterrations from the end of the loop (1-indexed): ##
<ul >
    { % for lang in langs % } 
    <li > {{forloop.revcounter}}: {{lang}} < /li >
    { % endfor % } 

</ul >

# Output:
# List of Languages

# List of Languages

# 5: Python

# 4: Java

# 3: PHP

# 2: Ruby

# 1: Rust


# forloop.first: True if this is the first time through the loop: ##
<ul >
    { % for lang in langs % } 
    <li > {{forloop.first}}: {{lang}} < /li >
    { % endfor % } 
</ul >

# Output:
# List of Languages

# True: Python

# False: Java

# False: PHP

# False: Ruby

# False: Rust


# .....

# {% comment %}
#
# Everything between {% comment %} and {% endcomment %}  is ignored. An optional note may be inserted in the first tag.##
{% comment "Optional note" % }
<p > Commented out text < /p >
{% endcomment % }


# {% block %}:
#
#
# Defines a block that may be overridden by child templates. This tag will be discussed when you learn about template
# inheritance
#
#
# {% csrf_token %}
#
# This tag is used in a form template as protection to prevent Cross Site Request Forgeries (CSRF). This tag generates a
# token on the server-side to make sure to cross-check the incoming requests do not contain the token. If found, they are
# not executed.
#
# {% include %}:
#
#   Loads a template and renders it with the current context. This is a way of "including" other templates within a template.
# The template name can either be a variable or a hard-coded (quoted) string, in either single or double quotes##

{% include "sample.html" % }

# .... ##
