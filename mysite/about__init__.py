""" There seems to be an error with django's test functionality if the root directory is a python package"""

### https://forum.djangoproject.com/t/importerror-modulenotfounderror/2324/14
"""
If you’d like to become more confident about what’s happening and revisit the “broken” project, I found something that might explain the issues you’re experiencing.

Look at the second answer in this SO thread, from user ‘Samuel’: https://stackoverflow.com/questions/40206569/django-model-doesnt-declare-an-explicit-app-label 51

He describes that he experienced a similar issue to what you’re getting as long as he had an __init__.py file in his project/root directory. I didn’t catch it first 
in the screenshot in your second post here, but you have the same thing. There’s an __init__.py file right above the db.sqlite3 and manage.py files.

I’m also working my way through the official tutorial (again). I just tried adding a __init__.py file to the root directory and bam, running python manage.py test
produces ‘ImportError: Failed to import test module: official_tutorial.polls’. If I remove (rm __init__.py) the file and run python manage.py test again, 
everything’s back to normal.

I don’t know what exactly Django does in the background which causes this behavior, but apparently it’s really confused by the root directory being turned into a
package (which is what __init__.py does 1).
"""