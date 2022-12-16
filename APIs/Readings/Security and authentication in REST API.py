# Security and authentication in REST API:
#
# Note 1: The core purpose of APIs is to make your data more accessible for apps,
# websites and third party clients to make your data more useful.
#
# Note 2: Web APIs are a security risk for backend serverices. Essentiall,y APIs give
#  third party apps access to your server and database. That's why it's very imporant
# to secure APIs.
#
#  How to Keep APIs Safe and Secure?
#
#   Step 1: Implement SSL certificate on the server (Secure Socket Layer)
#        - SSL makes all the endpoints secure and encrpts all the data that's being send
#        using HTTPs protocol. That's why it's imporant to check the endpoints of
#       the API or server starts with HTTPs
#
#   Step 2: Signed URLs - Signed URLs give a client application limited access to a
# specific resource for a brief period of time. With a signed URL, every time an API
# is called, a particular piece of text called a signature is included with the URL
# Server side code can verify the signature and ensure that the call comes from
# an authentic source.
#       (A) Developers create signed URLs using "HMAC" - "HMAC" is a popular signing
# mechanism used by modern applications. It's easy to use and ensure the authenticity
# and integrity of the message.
#
#   Step 3: Authentication - use "Token-based authentication"  instead of HTTP basic
# authentication when secure APIs Because basic authenticaiton requires users to send
# their username and password in every call. With token-based authentication
# the user sends their user name and password to the sign-in URL, and then recieves a
# unique token in the text form. After that, every API call will include this token
# as a HTTP header. The server side code can check the tocken, extract the information
# hidden in it and match it with an existing user. After this verificaiton, the rest of
# the work is performed on behalf of that matching user.
# To create this token, you can use an "ad hoc policy" from the backend framework
# we're using, or you can use something more industry standard, like JSON Web Token
# or JWT.
#
#   Step 4: HTTP Codes:
#       Next, you need to know that there are a couple of popular HTTP codes involved
# during the authentication process, that you should be aware of.
#   (A) 401 - Means Unauthorized ... it might mean the username and password don't match
#           so the server cannot continue processing the request
#   (B) 403 - Means forbidden (No authority to perform action)
#       ... This means your credentials are valid and you have successfully identified
# yourself but don't have the authority to perform the action.
#
#   Step 5: Cross-Origin Resource Sharing
#       Last is the cross origin resource sharing or CORS policy and firewalls.
# When you design an API, you can accept calls from everywhere, or by configuring
# teh Cores headers, you can only accept calls from some specific domains.
#
#   Step 6: Firewall applicaiton on your server - If you want to make sure that only
# specific IP addresses can access your API, you can use a firewall applicaiton on your
# server
##
