# REST best practices:
#
# 1. KISS - Keep It Simple Stupid. A single API should do one job and do it well.
#
# 2. Filter, Order and Paginate -  You should always provide a way to filter large result sets and rearrange them
#       in ascending or descending order. Your API should be able to filter results
#       for specific data from a list of data
#
#    When building an API, it is always good to enable it to send results in smaller
#           chunks. When using pagination, you can send results around "10 t0 16"
#   pages per request and allow the client to pick one record. ##
#
#
# 3. Versioning - You should always use versioning for your app to avoid breaking the
#   client's software when working with APIs.
#
#   (A) In general, you should only support two versions of any given resource, or
#           software that uses the API because maintaining multipe versions of
# software can be complex, error prone, and costly.
#   (B) In other words, it's best practice to keep two versions of your software and
#       APIs to make changes more consistant and to avoid breaking your software
#       such as web app when updating the API applications that supports the web app.
#
# 4. Caching - The API should be cachable so that it can reduce the load on your
# database-related API calls. You should always implmeneted caching and send relevant
# HTTP headers in your response. This will minimize the number of calls your client
# makes to your API. This helps with reducing the amount of workload on the database.
#
#  5. Rate Limiting and Monitoring - Rate Limiting limits the numbers of times someone
# can call your API in a period of time like per minute, hour, or day. Some people
# limit calls to their APIs for 30 days.
#
#   (B) Monitoring - You should monitor latency to make sure your clients are getting
# the best possible respond time. It's also important to monitor status and server logs
#
#  Note: It's imporant to keep your API health, performant, and sustainable and you
# can do so by following these best practices: KISS, Filtering and paginate,
# keeping two versions of the software you develop, Caching and
# (Rate Limit and Monitoring)
