# Project structure and API routes:
#
# Introduciton:
#
#   This reading is an overview of the scope of the project, all the necessary endpoints, and notes that you will have to
# implment in the final project. This reading will help to successfully complete the project so read it carefully and
# reference it while developing your API project to help you keep on track.
#
# Scope:
#   You will create a fully functioning API project for the Little Lemon restaurant so that the client application
# developers can use the APIs to develop web and web and mobile applications. People with different roles will be able to
# browse, add and edit menu ites, place orders, browse orders, assign delivery crew to orders and finally deliver
# the orders.
#
# The next section will walk you through the required endpoints with an authorization level and other helpful notes.
# Your task is to create these endpoints by following the instructions.
#
# Structure:
#
#   You will create one single Django app called LittleLemonAPI and implement all API endpoints in it. Use pipenv to manage
# the dependecies in the virtual enviornment. Review the video about "Creating a Django Project using pipenv".
#
#   Function or class-based views:
#
#   You can use function or class-based views or both in this project. Follow the proper API naming convention throughout
# the project. Review the video about "Function - and class-based views" as well as the video about "Naming Convention".
#
# User Groups:
#
#   Create the following two user groups and then create some random users and assign them to these groups from the Django
# admin panel.
#
#   * Manager
#   * Delivery Crew
#
# Users not assigned to a group will be considered customers. Review the video about User roles.
#
# Error check and proper status codes:
#
#   You are required to display error messages with appropriate HTTP status codes for specific errors. These include when
# someone requests a non-existing item, makes unauthorized API requests, or sends invalid data to a "POST", "PUT" or
# "PATCH" request. Here is a full list.
#
#  HTTP Status Code        Reason
#
#  200 - OK                For all succesful "GET", "PUT", "PATCH" and "DELETE" calls
#  201 - Created           For all successful "POST" requests
#  403 - Unauthorized      If authorization fails for the current user token
#  401 - Forbidden         If the user authenticaiton fails
#  400 - Bad request       If validation fails for "POST", "PUT", "PATCH" and "DELETE" calls
#  404 - Not found         If the request was made for a non-existing resource
#
#
#  API endpoints:
#
#   Here are all the required API routes for this project grouped into several categories.
#
# User registration and token generation endpoints:
#
#   You can use Djoser in your project to automatically create the following endpoints and functionalities for you.
#
#   Endpoint                Role                                         Method    Purpose
#
#   /api/users              No role required                             POST     Creates a new user with name, email and password
#  /api/users/users/me/     Anyone with a valid user token               GET      Displays only the current user
# /token/login/             Anyone with a valid username and password    POST     Generates access tokens that can be used in other API calls in ths proejct
#
#
#
# When you include Djoser endpoints, Djoser will create other useful endpoints as discueed in the Introduction to Djoser
# library for better authenticaiton video.
#
#  Menu-items endpoints:
#
#   * Implement all the menu-items endpoints here.
#
#
# User group management endpoints:
#
#   * Implement all the user group management endpoints here.
#
#
# Cart managment endpoints:
#
#   * Implement all the cart managment endpoints here.
#
# Order managment endpoints:
#
#   * Implement all the order managment endpoints here.
#
# Additional step:
#
#   Implement proper filtering, pagination and sorting capabilities for "/api/menu-items" and "/api/orders endpoints".
# Review the videos about "Filtering and searching" and "Pagination" as well as the reading
# "More on filtering and pagination".
#
# Throttling:
#   Finally, apply some throttling for the authenticated users and anonymous or unathenticated users. Review the video
# "Setting up API throttling" and the reading "API throttling for class-based views" for guidance.
#
# Conclusion:
#
#   Now that you have a better idea of the scope of this project with essential API endpoints, it's time to start coding.
#   Good luck!    ##
