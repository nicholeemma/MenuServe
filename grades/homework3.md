## Homework 3 Feedback

Commit graded: *41bfaaf518d2abd8bc37a68b0655c5614a946365*

### Incremental development using Git (10.0/10)


### Fulfilling the MenuServe specification (19.0/20)

- **-0** Even though you did a good at implementing all the required features, your website is hard to use when comes to updating data because non of the values are preloaded into the dropdowns so in order update and order or menu item, user have to select those again. I suggest you work on these on your next improvement.

- **-0** Also another point, flow your application is not clear so it is hard to navigate from page to page like from menu management to order selection.

- **-1** Updating menu in the menu management doesn't update the menu on the main page.

### Request routing and configuration in Django (9.9/10)

- **-0.1** You should modularize your django projects by using application-specific `urls.py` files in each application directory, and use your project-wide `urls.py` file to include each application's routes.

### Appropriate use of web application technologies in the Django framework (50.0/50)

- **-0** We suggest adding a [`datetimefield`](https://docs.djangoproject.com/en/1.11/ref/models/fields/#datetimefield) for menuserve timestamps. you may find the `auto_now_add` option helpful.

***

### Total score: 88.9/90

***

Graded by: Enes Palaz (epalaz@andrew.cmu.edu, epalaz)

To view this file with formatting, visit the following page: [https://github.com/cmu-webapps/jiayueya/blob/master/grades/homework3.md](https://github.com/cmu-webapps/jiayueya/blob/master/grades/homework3.md)
