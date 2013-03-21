import mechanize

br = mechanize.Browser()
br.open("http://www.google.com/")

if (br.geturl().find("wifidog") != -1):
    br.select_form("login_form")
    br.form.new_control('text', 'username',{'value':''})
    br.form.fixup()
    br["username"] = "YourEmailHere"
    br["password"] = "YourPasswordHere"
    br.submit()
    print "Logged in to sparkmatrix"
