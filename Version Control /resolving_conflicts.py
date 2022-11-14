# Resolving Conflicts: 
# 
# Conflicts will normally occur when you try to merge a branch that may have competing 
# changes. Git will normally try to automatically merge (auto-merge), but in the case 
# of a conflict it will need some confirmation, the competing changes need to be 
# resolved by the end user. This process is called merging or rebasing. 
# 
# The developer must look at the changes on the server and the changes on their local
# and validate which changes should be resolved. 
# 
# A merge conflict example is when two developers are working on their own 
# independent branches. Both developers are working on the same file called 
# "Feature.js". Each of their tasks is to add a new feature to an existing method. 
# Developer 1 has a branch called "feature1" and developer 2 has a branch called 
# "feature2". 
# 
# Developer 1 pushes the code with the changes to the remote repositry. 
# Developer 2 pushes their changes.
# 
# Let's walk through how this would happen in Git. Both developer 1 and 2 checkout the
# main repository on Monday morning. They both have the exact same copy. Both developers
# checkout a new branch - feature 1 and 2
# 
# Developer 1 makes their changes to a file called Feature.js and then commits the 
# changes to the repository for approval via a PR (pull request)
# 
# The PR is reviewed and then merged into the main branch. Meanwhile Developer 2 is 
# starting to code on his feature. Again, they go through the same process as
# Developer 1
# 
# Git lets us know that a merge conflict has occurred and needs to be fixed before it
#  can be pushed to the remote repo. 
# 
# Running git status will also give us the same level of detail: 
# 
# In order to merge, Developer 2 needs to see and compare the changes from Developer 1. 
# It is good practice to first see what branch is causeing the merge issue. 
# Developer 1 runs on the following command.
# 
# We can see from the above that the team conflicting changes occurred in feature 1
# and branch 2. Developer 1 now wants to see the change that is causing the conflict.
# 
# The only difference is the wording in the return statment. Developer 1 added 
# "too much" but developer 2 added "way too much". Everything else is identical so in
# terms of merging and it's a pretty easy fix. Git will show arrows <<<>>> to 
# signify the changes. Developer 1 removes the markers so teh code is ready for being
# submitted: 
# 
# Developer 2 has now fixed a merged conflict and can create their PR to get the code
# merged into the main line.   ##