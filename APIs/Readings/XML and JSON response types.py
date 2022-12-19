# XML and JSON response types: 
# 
# Introduction: 
# 
#  When it comes to displaying output, an API developer should always allow the client to require the preferred content 
# type, such as JSON, XML. Clients can do this by supplying an additional headers called "Accept" in the request header.
# You learned about this in the reading, HTTP methods, status codes and response types. In this way the client has full 
# flexibility to use the content in the way they want to. In this reading, you'll learn more about the two data formats 
# that you will encouter the most in requests from client, JSON and XML. 
# 
# Request headers: 
#   Client applications need to send "Accept" request headers with every HTTP request to recieve the output in JSON or 
# XML. For example, 
# 
#   Response type                               Request header 
# 
#       JSON                                    Accept: application/json
#       
# 
#       XML                                     Accept: application/xml
#                                               Accept: text/xml
# 
# The client can send an "Accept" header in an HTTP "GET" request and depending on the request header, the same data will
# be displayed differently in JSON and XML. Below is a screenshot of an API request for a JSON response. 
# 
# And here is the same API request but for an XML response.
# 
#   Note 1; Header Response as JSON gives you dictionary with key-value pairs as response 
#   Note 2: Header Response as XML gives you XML document as response
# 
# Data Conversion: 
#   
#   In this course, you will build APIs using Django and Django REST framework, also called DRF. DRF has built-in renderers
# that can convert your data to JSON and repersent it in an interactive, browsable API viewer. There are also third-party
# renderer classes that can convert these data to XML or YAML. You will learn about these features and write actual code 
# later in this course. 
# 
#   JSON versus XML:
# 
# JSON gained popularity because it's very simple and lightweight. And creating JSON data or parsing it is easier than XML. 
# However, XML has its own advantages too. XML is more readable and supports data attributes that are not possible in JSON. 
# And you can represent complex data in XML and still keep it readable. JSON is very popular among JavaScript developers
# because they can instantly read and write JSON data just like a regular object. 
# 
#  The table below compares some of the features of both formats. 
# 
#       JSON                                        XML
# 
#   JSON or JavaScript Object Notation is a     XMNL or Extensible Markup Language is a powerful, tag-based data format 
# lightweight and depedency-free data format    It is similar to HTML. XML data can be fairly complex 
# 
# 
# The size of JSON data is smaller than XML.   XML data is lengthier than JSON and takes up more bandwidth.
# So, it takes less bandwidth
# 
#  JSON data is like keys and values.           XML is completely tag-based, it does not have key-value pairs like JSON
# {                                             <?xml version="1.0" encoding="UTF-8"?>
#   "author": "Jack London",                    <root>
#    "title":    "Seawolf",                             <author> Jack London</author>
#                                                       <title> Seawolf </title>    
# }   ##                                        </root>
#
# 
#   
#  Representing array elements is simpler in    You can still display array elements in XML but its very verbose. 
# JSON. Here's an example:                      <?xml version="1.0"
# {                                               encoding="UTF-8"?>
#   "items": [1, 2, 3, 4, 5]                       <root>
# }                                                     <items> 
#                                                               <element>   1 </element>
# #                                                               <element> 2 </element>
# #                                                               <element> 3 </element>
# #                                                               <element> 4 </element>
# #                                                               <element> 5 </element> ##
#                                                       <items>
#                                                   </root>
# 
#
#   Generating and parsing JSON data is faster      Generating and parsing XML is a complex process, and it usually takes
# than XML and this conversion process requires     more processing power than memory than processing JSON
# less memory and computing power. 
# 
# 
# 
#  There is no way to include comments in JSON data     XML data can include comments
# 
# Conclusion: 
#   It is clear that JSON and XML both have benefits and limitations. Later in ths course, you will learn how to display 
# API output in both formats, but you will mostly use JSON in this course because it's very simple and lightweight. 
#  ##
