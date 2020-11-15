# ChallengeQuestion_16Nov20

This repository only hosts one file, which solves the question given at this LinkedIn post: https://www.linkedin.com/posts/jayant-sharma-a09447126_interviewquestion-hiring-google-activity-6733007961398009856-F8ha 

The question says:
Given a list of N strings and Q query strings, check for each query string if there is a string from the list which completely is the prefix of this one.
Answer in yes or no for each query.
How would you approach it?

In this piece of code, I have written a basic python program to create a tree of all the prefix-strings (from list N). Then I have used that tree to minimise the amount of time required to check which query-string (from list Q) contains one of the aforementioned strings.
