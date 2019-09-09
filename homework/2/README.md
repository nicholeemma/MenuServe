To turn in homework 2, create files (and subdirectories if needed) in
this directory, add and commit those files to your cloned repository,
and push your commit to your bare repository on GitHub.

Add any general notes or instructions for the TAs to this README file.
The TAs will read this file before evaluating your work.

##Choose GET method
According to the requirement " This extra data should not be  visible to the user in your UI or in the page URL.", I chose to use POST method.
Because the GET method is insecure and will show the data in the url which the user entered.
POST is a little safer than GET because the parameters are not stored in browser history

Reference: https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests

##Logic of calculation
The same as requirements
Additional:
1. If user enters "9+2=", the calculation will display "9 9 2 11". Now the calculation is over. New entered number will be treated as a new calcualtion. Once pressed "=", the calculation rendered the result, calculation is over.
2. When the user pressed a "=" in the middle of a series of numbers, the "=" will be ignored.
3. A new calcution will be started until a number entered.

##Reference
1. https://www.geeksforgeeks.org/get-post-requests-using-python/
2. https://www.w3schools.com/python/ref_requests_post.asp

