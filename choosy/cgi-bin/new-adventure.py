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


    with open('web/adventure-list.html', 'a') as adventure_list:
        link = "<form action='/cgi-bin/story-displayer.py'><input type='submit' name='adventure-title' value='{}'></form>\n".format(title)
        adventure_list.write(link)

    homepage = description

    with open(adventure_location, 'w') as adventure_home_page:

        adventure_home_page.write(homepage)

    # with open('web/adventure-list.html', 'a') as adventure_list:
    #
    #     adventure_list.write("<a href='web/adventures'")

    print("""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset='UTF-8'>
          <meta http-equiv='refresh' content='1; url=/index.html'
          <title>Room Creation</title>
          <link rel='stylesheet' href='/css/style.css'>
        </head>
        <body>
          <div>
            Adventure created successfully, redirecting...
          </div>
        </body>
        </html>
    """)
