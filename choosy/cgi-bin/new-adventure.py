#!C:\Users\Mimir\AppData\Local\Programs\Python\Python36\python.exe

import cgi
import os
import cgitb
cgitb.enable()




form = cgi.FieldStorage()

title = form.getvalue('adventure-title')
description = form.getvalue('adventure-description')

path = 'web/adventures/' + title
adventure_location = path + '/' + title + '.html'


if os.path.isdir(path):

    print("""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset='UTF-8'>
          <title>Adventure Creation</title>
          <link rel='stylesheet' href='/css/style.css'>
        </head>
        <body>
          <div>
            <form action='/cgi-bin/new-adventure.py' method='post'>

              There is already an adventure with that title, try again:<br><br>

              Adventure title:<br>
              <input type='text' name='adventure-title'><br><br>

              Adventure description:<br>
              <textarea name='adventure-description'></textarea><br><br>

              <input type='submit' value='Save Adventure'>
            </form>
          </div>
        </body>
        </html>
    """)

else:

    os.makedirs(path, exist_ok=True)

    homepage = """
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset='UTF-8'>
          <title>{}</title>
          <link rel='stylesheet' href='/css/style.css'>
        </head>
        <body>
          <div>
            {}
          </div>
        </body>
        </html>
    """.format(title, description)

    with open(adventure_location, 'w') as adventure_home_page:

        adventure_home_page.write(homepage)


    print("""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset='UTF-8'>
          <meta http-equiv='refresh' content='1; url=/{}'
          <title>Room Creation</title>
          <link rel='stylesheet' href='/css/style.css'>
        </head>
        <body>
          <div>
            Adventure created successfully, redirecting...
          </div>
        </body>
        </html>
    """.format(adventure_location))
