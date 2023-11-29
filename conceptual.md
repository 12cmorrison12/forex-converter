### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is used for backend development

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

one is the get() method, another is to use the try-except block.

- What is a unit test?
a test that tests a block or code that is usually just a single function or method

- What is an integration test?
these test how different combinations of methods/functions work together 

- What is the role of web application framework, like Flask?
to make developing web applications easier and quicker, using built in servers and a debugger

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?


- How do you collect data from a URL placeholder parameter using Flask?
by creating a corresponding function with the name as an argument and using a placeholder url in the url

- How do you collect data from the query string using Flask?
you can access the query string property of the request object

- How do you collect data from the body of the request using Flask?
you can use request.data

- What is a cookie and what kinds of things are they commonly used for?
cookies are like saved data on a website that remembers information from your last visit. it makes it easier to visit the site again and they're commonly used for 
putting in data to make your next visit easier.

- What is the session object in Flask?
it's a dictionary object taht is used to keep track of the session data and usually contains a key-value pair

- What does Flask's `jsonify()` do?
it turns response objects into json so that the browser can read it
