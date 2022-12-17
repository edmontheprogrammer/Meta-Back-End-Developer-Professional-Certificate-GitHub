# Authentication versus authorization: 
# 
#  Introduction: 
# 
#   You need to secure your APIs because they provide third-party client access to your backend data. If you don't secure 
# your APIs properly, anyone can tamper with the data and access sensitive information. But even if a client is allowed to
# access the data, you need to control who can do what. This is where authentication and authorization come in. You now know
# that although they sound similar, they are not the same. In this reading, you will learn about the difference between 
# authentication and authorization and how you can use it to protect your API endpoints. 
# 
# Authentication: 
#   Authenticaiton is the process of verifying the credentials of a user. Logging into websites with a username and password
# it a typical example of authentication. When the username and password match, the website recognizes the user and sets 
# some cookies in the user's browser. When the user visits another page on that website, the browser sends those cookies
# within the HTTP request header. The website recognizes the cookies as well as server-side session data and therefore 
# doesn't ask for credentials until the user logins out again. 
# 
# So, how does this work? Token-based authentication usually involves two stesp in the API Arhitecture. First, the client
# identifies itself with a username and password. Then the API server gives it a bearer token. From there, the client 
# includes the bearer token with every API call that it places. The API servver verifies it and then allows the client to 
# perform the action or not. This is where authorization comes in, but more on this later. 
# 
# If the credentials are not valid, the client will receive a "401 - Unauthorized" HTTP status code. 
# 
# This is like coming to the office on the first day, submitting all your papers and documents, and then receiving your 
# employee card. After that, only your employee card will be sufficient to get inside. Authentication works just like that!
# 
# The two steps in the API authentication process can be represented by yhe following two diagrams: 
# 
# Authentication process: Getting an access token: 
# 
#  (Client) Username and Password (access token) <----> API Web Server   <---- Database 
# 
# Authenticated API calls: 
# 
# (Client) ---- API call + access token (Response) <---->API Web Server<----> Verified API call (Process Data) --- Database
# 
# Authorization: 
#   
#   However, even with your employee card, you will not be able to access all the rooms or spaces in the office. There are 
# some places that are only accessible to a certain group of people who have been given that privilege. Authorization is 
# exactly like that. Authentication lets you in, authorization lets you act. It checks after authentication if the user has
# the proper privileges to perform some tasks. 
# 
# On the server side, this is typically done by assigning the user to a group or a set of groups. Then, after verifying the 
# token, the code checks if the user belongs to the appropriate group to perfrom that task. It not, the client will recieve
# a "403 - Foribidden" HTTP status code. 
# 
# Client <---> API call + access token (Response) <---> Webb Server <---> check authorization (verified) 
#       <---> Authorization Layer <---> authroized (process data) <---> Database
# 
# This extra authorization layer in the API architecture ensures that only people with proper privileges can access and 
# modify data. An authorization system in an API project is very important because it prevents data corruption and data 
# breaches. 
# 
#   Implementing authorization: 
# 
#   Privileges are the tasks that an API user performs, and they are the building blocks of an authorization layer. First, 
# as an API developer, you identify the required privileges in your project. For example, for a bookshop, there might be the
# following types of privileges: 
# 
#   * Browse the books
#   * Add new books 
#   * Edit books 
#   * Delete books
#   * Place orders 
# 
# There can be many other privileges like this. And not every user will have every privilege. For instance, regular 
# customers are not allowed to add and edit books, even if they are properly authenticated. Only managers are allowed to 
# perform those operations. 
# 
# So, after identifying the privileges, you carefully distribute all these privileges into multiple roles. And then, the 
# authorization check is done in the backend code of each API endpoint that requires a user role check. The developer 
# verifies if the user belongs to the appropriate group or roles, and then makes the decision to allow or deny the action. 
# 
# User Groups in Django: 
#   
#   The Django admin panel comes with excellent support for the user group system. If you log into the admin panel, you will
# find two distinct sections - users and groups. 
# 
# From here, you can create groups or roles like Manager, Edit, Customer, Admin and so on and assign privileges to these 
# groups. If you click on the Add button next to the groups, you will be take  to a screen where you can create new groups. 
# The Django admin panel will list all the necessary privileges based on the models in your project. Here is a screen that
# indicates the available privileges for a bookshop. 
# 
# From here, you can create groups or roles like Manager, Editor, Customer, Admin and so on and assign privileges to these
# groups. If you click on the Add button next to the groups, you will be taken to a screen where you can create new groups. 
# The Django amdin panel will list all the necessary privileges based on the models in your project. Here is a screen that
# indicates the available privileges for a bookshop. On this screen, you can create an Editor role, for instance, and 
# add privileges to it. 
# 
# Or you can create a Customer role that will have different privileges. 
# 
# The Django admin panel allows you to manage groups throughout the project. You can add and remove privileges to groups 
# as the project grows. 
# 
# But creating groups with privileges is not enough. After creating these groups and assigning users to them, you need to 
# write some code in the function or class-based views that determine if authenticated users belong to those groups and 
# then make decisions based on that. But you will learn to do this later in the course. 
# 
# Conclusion:
# 
#   Authenticaiton and authorixation are concepts that differ in function and how they are set up in an API architecture. 
# The knowldge you gained in this reading about users groups, roles and privileges lay the groundwork for all the steps 
# that you will learn later on for setting up a proper security layer in your API projects.   ##