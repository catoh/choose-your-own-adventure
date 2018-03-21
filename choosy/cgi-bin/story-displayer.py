import cgi

form = cgi.FieldStorage()

title = form.getvalue('adventure-title')

adventure_page = """
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset='UTF-8'>
      <title>Story Viewer</title>
      <link rel='stylesheet' href='/css/style.css'>
      <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    </head>

    <body>

      <div id='page-content' class='menu'></div>

      <div id='nav-controls' class='menu'></div>

      <div id='submission-box' class='menu'></div>
      <script>$(function(){{$("#page-content").load('/web/adventures/{0}/{0}.html');}});</script>
    </body>
    </html>
    """.format(title)

# print("""
# <!DOCTYPE html>
# <html>
# <body>
# {}
# </body>
# </html>
# """.format(title))

print(adventure_page)
