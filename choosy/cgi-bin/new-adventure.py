import cgi
import os
import cgitb
cgitb.enable()


form = cgi.FieldStorage()

path = './adventures/{}'.format(form.getvalue('adventure-title'))
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
              There is already an adventure with that title, try again:<br>
              <input type='text' name='adventure-title'>
              <input type='submit' value='Save Story'>
            </form>
          </div>
        </body>
        </html>
    """)
else:
    os.makedirs(path, exist_ok=True)
    print("""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset='UTF-8'>
          <title>Room Creation</title>
          <link rel='stylesheet' href='/css/style.css'>
        </head>

        <body>
          <div>
            <form action='/cgi-bin/new-room.py' method='post'>
              Adventure was created successfully, now we can create pages<br>
              The first node in an adventure is always titled 'Home'<br>
              Describe the opening node below:<br>
              <textarea name='home-room-description' rows='20' cols='60'></textarea><br>
              <input type='submit' value='Save Description'>
            </form>
          </div>
        </body>
        </html>
    """)
