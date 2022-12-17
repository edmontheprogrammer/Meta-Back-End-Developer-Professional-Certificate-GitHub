# Consequences of a poorly designed API project
#
# Introduction:
#   Creating a good API project can be challenging. You need to stick to the convetions, write proper error checks in your
# code, perform security checks, and make sure that your APIs are using processing power and bandwidth optimally.
# This is all takes time and proper planning. But what happens if you don't properly plan an execute your APIs?
#
# Let's examine some of the consequences of a poorly designed API project.
#
# Data breach:
#
#       Reasons                                         Consequences
#
# Poor securiy checks in the code,                  The most significant risk of a poorly designed API project is a data
# no authenticaiton or authorization checks         breach. Sensitive data can leak if you don't have proper security
# improper file permission, and not using           checks in your code or if you didn't implement proper permissions for
# SSL  ##                                           the files stored on the server.
#                                                   Also, if you are not using SSL for your API endpoints, attackers can
#                                                   steal user data before it reaches your API web server.
#                                                   Such mistakes can cause severe finanical damage and trust issues.
#
# Fix:
#    Add proper security checks in your code and create a solid authorization layer to prevent unauthorized access to your
# data. Always double-check these sensitive API endpoints before deploying them to production.
#
#
# Data Corruption:
#
#       Reasons                                          Consequuences
#
# Poor security, no authenticaiton          Improper securiy checks and lakc of a solid authorization layer can let any
# or authorization checks, absence of       user with a valid authenticaiton token access sensitive APIs and modify the
# data validation and sanitization of       data unexpectedly. Also, creating resources without proper validation checks
# input data.   ##                          can create malformed data in the database. Such mistakes can cause severe data
#                                           corruption and ata loss beyound repair.
#
# Fix:
#     Bdesides security checks and a solid authorization layer, an API developer must validate and sanitize user data
# before processing and saving it.
#
#
# Wastage of Computing Power and Memory:
#
#     Reasons                                           Consequences
#
#   Unoptimized code, improper business             Poorly written API code can comsume unnecessary computing power and
# logic, lack of data validation, unoptimized       memory with unoptimized code, algorithms and business logic.
# SQL queries or model relationships, lakc of       Unoptimized code, laock of proper database indexing and absence of
# database indexes, and no caching. ##              chacing can cause a hugh load on the database server by running
# #                                                 redudandant SQL queries, which slows the whole system down.
#                                                   Such mistakes can end up increasing the cost of your API infrastructure
# Fix:
#       To avoid this, always spend time optimizing the code and double-checking your database-related code before
# deploying your APIs to production.
#
# Wastage of Bandwidth:
#
#   Reasons                                             Consequences
#
# Absence of necessary caching header               If your API project doesn't follow good API development practices like
# API code, lack of caching policy on the           implementing caching, filtering and pagination can cause your APIs to
# reverse proxy and on the web server, and          deliver unnecessary data more times than what is required.
# lakc of pagination and filtering.   ##            Such mistakes can cause bandwidth wasting and end up charging extra
#                                                   bills in your monthly invoice, as well as poor performance from your
#                                                   API endpoints. Besides, the client applications need to spend more
#                                                   resources and time filtering unnecessary data every time.
#
# Fix:
#       To avoid this, always send proper chacing headers with your API responses and implement filtering and pagination
# features so that the client application can request and recieve only what they need.
#
#
# Bad User experince:
#
#   Reasons                                             Consequences
#
#  Not following the proper naming convention       It creates a bad user experince. The client application developers
# not sending proper HTTP codes, not accepting      must go through extra processing of the API data, extra code to create
# "ACCEPT" headers, and filtering and lack          the final output, and a steeper learning curve to use your API, which
# of proper error checking in code.                 was not necessary if the API was designed by following the standard
#                                                   conventions and best practices.
#
#                                                   Not accepting the "Accept" headers means that the API client is not
#                                                   getting the API output in its required format. That will cause bad
#                                                   experinces because clients need extra time and unnecessary code to
#                                                   process the data on their end. Also, sending wrong HTTP status codes
#                                                   can cause unexpected errors on the client applications and a bad
#                                                   experince for the users who will use those applicaitons.
#
# Fix:
#    To avoid this, always follow the proper naming conveiton and implement data filtering, searching, sorting, searching,
# and pagination features for your API endpoints. Always keep proper error checking in the code and write tests so that
# it doesn't create unexpected 5XX errors on the server side.
#
#
# Breaking Client applicaitons:
#
#       Reasons                         Consequences
#
# Not following the proper      If you don't maintian the proper versioning system for your API project, it can immediately
# version system                break backward compatibilty, and the client applicaiton can stop working instantaneously.
#                               The API can cause failure in teh current client applicaitons because your new API requires
#                               new request data and delivers new responses. So, their old code will not work anymore.
#                               They must refactor it and release a new version of their applicaiton as soon as possible.
#                               Such disruption can cause a bad reputation and financial damage for both the API and
#                               client application developers.
#
# Failure to manage the app:
#
#     Reasons                               Consequences
#
# Keeping everything in one big     Django apps can become big and become unmanageable over time if you keep adding
# Django app, adding all            functionalities in one single app. And then, adding new features or debugging an error
# business logic in the view        will be painful and take extra time and effort. Also, adding all business logic in
#                                   the view file can lead to writing redudant code across multiple classes and
#                                   function-based views. Failure to manage an app over time leads to bad coding, patching
#                                   of errors without test coverage and ultimately, poor performance from the APIs
#
# Fix:
#   Distribute the features and functionalities to multiple smaller Django apps in a decoupled way. Additionally, put some
# business logic in the models which can be reused by the other parts of your API project.
#
# Conclusion:
#       Taking the time to properly desing an API project from the start will save you time and effort over the course of a
# project. The consequences of a poorly designed API affect everyone who uses your API, including the API developers
# and client applicaiton developers.
#
# The knowldge you gained in this reading will hopefully remind you of everything you need to keep in mind to make
# your future API project successful.
#  ##
