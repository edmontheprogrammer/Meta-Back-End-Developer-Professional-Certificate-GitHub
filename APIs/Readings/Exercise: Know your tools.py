# Exercise: Know your tools:
#
#   Introduction:
#
#   In this exercise, you are going to use the REST API client "Isomnia" to make HTTP Requests so make sure you've install
# it on your computer. You will also use the Request and Response Service "httpbin.org". Httpbin.org is an open-source web
# service that allows you to make HTTP calls without any additional installations or depedencies.
#
# You will be exploring the different functionalities available in Insomnia such as
#   * Creating a "GET" request
#   * Creating a "POST" request with Form Data
#   * Creating a "POST" request with JSON Data
#
# To get started, open "Insomina" on your local device and navigate to the tab labeled "DEBUG".
#
# "Create a GET request":
#
#   Open the "https://httpbin.org/" website and click on "HTTP Methods". A menu with different HTTP methods will expand
# which you can add to your endpoints.
#
# Step 1:
#   In Insomnia, click on the "+" icon on the left-hand side of the screen and select "HTTP Request" from the drop-down
# menu.
#
# Step 2:
#   Double-click the request to change its title to "GET request using Insomnia".
#
# Step 3:
#   Click on the "GET" dropdown to see a list of available options and re-select "GET".
# Update the URL endpoint with the value: "https://httpbin.org/get"
# Press the "Send" button and notice the JSON output.
#
# Step 4:
#   From the "Body" drop-down option, select "Multipart Form".
#
# Add the following values under "New name" and " New value":
#
#   * New name: title
#   * New value: Lord of the Rings
#
# Press the "Send" button once again and observe the changes.
# Notice that the value of "Content-Length" has been updated to include the changes.
#
# Step 5:
#   Update a form entry with the following details:
#
#       * New name: author
#       * New value: JRR Tolkien
#
# Press the "Send" button once again. Notice that "Content-Length" has further been updated
#
# Step 6:
#
#   You can "Filter" your output using the Filter response body at the section in the bottom right-hand side of "Isomnia"
#
# Add the following filter inside it:
#
# "$.origin"
#
#  It should update the "Preview" as indicated  in the screenshot below.
#
# [
#   "76.197.210.235"
# ]
#
# Step 7:
#
#   Modify the filter incrementally as below which should produce the respective outputs.
#
# "$.headers"
#
# "$.headers.Content-Type"
#
# Note: The dot operator is used here to explore the contents of the JSON output. Also notice the value of the Content-Type
# is "form-data" because you select Multipart form.
#
# Clear the contents of the "Filter response body"
#
# Step 8:
#   Now deselect the option for the name "" and re-create the "GET" request.
#
# Notice the change in the "Content-Length" again.
#
# Aditional Step:
#
#   Now that you know the steps to create a "GET" request in Insomnia, you can explore different configuration settings by 
# following the steps to get more accustomed to the tool.
# 
# Create a POST request with Form Data: 
# 
#   Step 1: Keeping the contents of the form data in the same, update the request type to POST and update URL endpoint to:
# https://httpbin.org/post 
# 
# 
# Notice that the contents of the form are updated inside the output for the "POST" request. 
# 
# Step 2: 
#   Explore the other tabs under the output such as "Headers", "Cookies" and "Timeline". 
# 
# Step 3: 
#   Since you have modified the same HTTP request, update the changes for the title of the request in the left-hand section
# to "POST request using "Insomnia". 
# 
# Create a POST request with JSON Data. 
# 
# Step 1: 
#   Now further create another HTTP Request like the one at the beginning by pressing the "+" and selecting "HTTP Request"
# 
# Step 2: 
#   Update the request type to "POST" and the request label as: 
# 
#   "POST request using JSON object" 
# 
# Note: The labels are for reference and indepdendent of the request type. 
#       Past the same URL endpoint that you used ealier in the URL "text-box":
# 
# "https://httpbin.org/post" 
# 
# Step 3: 
#   Under the "Body" dropdown option, select "JSON" as the text input.
# 
# A text input area should appear as below. 
# 
# Step 4: 
#   Enter the following content inside the text input area:
# 
# {
#   "title": "Lord of the Rings", 
#   "author": "JRR Tolkien", 
#   "published": {
#                   "year": 1954, 
#                   "month": "july", 
#                   "day": 29 
#               } ##
# } 
# 
# 
# Press the "Send" buttton 
# 
# The output for the JSON input should appear as below:  
# 
# Notice the contents entered as JSON object in both the "data" and "json" field inside the JSON output.
# 
# Step 5: 
#   5.1: Add  the following line to Filter response body:
# 
#       "$.json.published.year"
# 
# The output will be as follows: 
# 
#       [
#           1954   
#       ] 
# 
# 5.2 Modify the "Filter response body" as follow:
#   
#   "$[json][published][day]"
# 
# The output will be as follows: 
# 
#   [
#       29
#   ] 
# 
# 
# Concluding Thoughts:
# 
#   There are several configuration options inside Insomnia. While using a REST API client it is good to explore these. 
# You can also get help from other free and open-source API services that provide options to make API calls to access 
# public data. ##
