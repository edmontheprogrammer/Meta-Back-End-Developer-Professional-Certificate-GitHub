# Types of Testing:
#
# 1. Unit Testing
# 2. Integration Testing
# 3. System Test
# 4. Acceptance Testing
#
#
# White box testing:
#   White box testing is where tester has knowledge of the code design and
#   functionalities.
#
# Black box testing:
#   Black box tests function with no such information. Or Black box testing is a test
#   where the tester has no knowledge of the code design and functionalities
#   (internal information).
#
# Other types of testing:
#
# 1. Functional tests
# 2. Non-functional tests
# 3. Maintenance tests
#
# Functional Tests:
#   Functional tests determine if the features and functionalities are in line with the
# expectations.
#
# Non-functional tests:
#   Non-functional tests are more complex to define and involves metrics such as
#   overall performance and quality of the product.
#
# Maintenance tests:
#   Maintenance tests occurs when the system and its operational environment is
# corrected, changed or extended. But there are also manual and automated testing methods
# that are dependent on the scale of the software.
#
# The most broadly accepted categorization is in terms of the levels of testing as you
# move ahead in the software lifecycle. Let's dive deeper into these levels of testing.
#
# Four Main levels of Testing:
# 1. Unit/ component testing
# 2. Integration testing
# 3. System testing
# 4. Acceptance testing
#
# Note 1: The four types of testing build on each other and have a sequential flow:
#
#   * In Unit testing, the program tests specific individual components by isolating them. The components are low level
# which means they are closer to the actual written code. They often involve the use of automation for continuous
# integration given their small sizes. So you usually write these tests while writing the code. For example, if the code
# is in Python, unit tests can be written with packages such as Pytest, integration testing.
#
#   * Integration testing combines the unit tests and tests the flow of data from one component to another component.
# The keyword here is interface, this means that you test if the data is correctly fetched from a database within the python
# code and if you have sent it to the web page. (Top-dow n approach, Bottom-up approach and sandwich approaches).
# There are different approaches to the integration testing such as "top down approach" and "bottom-up approach".
# Your approach depends on what code level interfaces you attempt first. It builds on the unit testing and a tester deals
# with it.
#
#  * System testing:
#   Next is system testing, which tests all the software you tested against the set requirments and expectations to ensure
# completeness. This includes measurements of the location of deployed components such as reliability, performance,
# security and load balancing. It also measures operability in the working environment such as the platform and operating
# system. This is the most important stage handled by team of testers. It is also the most critical stage as the
# shipping of software to the stakeholders and end user happened after this phase.
#
# * Acceptance testing:
#   The final type of testing is acceptance testing. When the product arrives at this stage, it's generally considered to
# be ready for deployment. It's expected to be bug free and meet the set standards. The stackholders and the select few
# end users are involved in acceptance testing. It normally invovles alpha, beta and regressing testing.
# One way of approaching this is to give pre-written scenarios to the users. You use the results for improvments and
# try to find bug that were missed earlier.
#
#
# All the different testing levels are designed to optimize software at different stages. The key to testing is testing
# early and testing frequently. While each of the testing phases is important, early detection saves time, effort and
# money. As the code gets increasinly complex mistakes become harder to fix. It doesn't necessarily mean that unit testing
# will happen only at the beginning and acceptance at a later stage. There are many testing cycles where these levels are
# approached iteratively. A typical example is the agile model, here you release different versions of the product
# iteratively and you perform acceptance testing every few weeks.  ##
