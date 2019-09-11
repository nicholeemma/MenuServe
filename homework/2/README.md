### Name: Jiayue Yang   Course: 17637 Web Application

## Choose GET method
According to the requirement " This extra data should not be  visible to the user in your UI or in the page URL.", I chose to use POST method.
Because the GET method is insecure and will show the data in the url which the user entered.
POST is a little safer than GET because the parameters are not stored in browser history

Reference: https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests

## Logic of calculation
The same as requirements
Additional:
1. If user enters "9+2=", the calculation will display "9 9 2 11". After that the calculation is over. New entered number will be treated as a new calcualtion. Once pressed "=", the calculation renders the result, calculation is over. A new calculation will start.
2. When the user pressed a "=" in the middle of a series of numbers, the "=" will be ignored.
3. The calculation initially shows "0", if user presses + 6, will render the result of 6.
4. After "2+5=7", 7 is shown. If user pressed +6, it will assume it is 0+6.
5. If the user enter "/0", it will render error. A new second number will be needed to enter, or you can enter new operator. If you enter "=", it will be ignored.
6. If you entered something strange during the calculation, it will render error, all previous information will be cleared. 

## Reference
1. https://www.geeksforgeeks.org/get-post-requests-using-python/
2. https://www.w3schools.com/python/ref_requests_post.asp

