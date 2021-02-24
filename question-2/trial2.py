#!/usr/bin/python
import mysql.connector
import webbrowser


conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="123456",
    database="customers_db"
    )

if conn:
    print("Connected Successfully")
else:
    print("Connected Successfully")

select_cus_tab = "SELECT * FROM Customer_tab"
cursor = conn.cursor()
cursor.execute(select_cus_tab)
result = cursor.fetchall()

p =[]

tbl = "<tr><td>Id</td><td>Name</td><td>Sector</td><td>Industry</td><td>Phone</td><td>Email</td><td>Gender</td><td>Date_Birth</td></tr>"
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)

    b = "<td>%s</td>"%row[1]
    p.append(b)

    c = "<td>%s</td>  "%row[2]
    p.append(c)

    d = "<td>%s</td>"%row[3]
    p.append(d)

    e = "<td>%s</td>"%row[4]
    p.append(e)

    f = "<td>%s</td>"%row[5]
    p.append(f)

    g = "<td>%s</td>"%row[6]
    p.append(g)

    h = "<td>%s</td></tr>"%row[7]
    p.append(h)


p = [i.replace("'", '') for i in p]
#for e in p:
    #if e == p[0] or e == p[-1]:
     #   continue
    #else:
     #   p = p.replace('"', "")


#html template
contents = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="html; charset=utf-8"
http-equiv="content-type">
<link rel="stylesheet" href="./style.css">
<title>Customer Dashboard</title>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN"
    crossorigin="anonymous">
     <link rel="stylesheet" href="style.css">
</head>

<body>


<nav class="navigation">
      <ul>
        <li>
          <a href="#">
            <span class="icon"><i class="fa fa-home" aria-hidden="true"></i></span>
            <span class="title">Home</span>
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon"><i class="fa fa-users" aria-hidden="true"></i></span>
            <span class="title">customers</span>
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon"><i class="fa fa-user" aria-hidden="true"></i></span>
            <span class="title">Profile</span>
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon"><i class="fa fa-industry" aria-hidden="true"></i></i></span>
            <span class="title">Industries</span>
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
            <span class="title">Contacts</span>
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon"><i class="fa fa-sign-out" aria-hidden="true"></i></span>
            <span class="title">Signout</span>
          </a>
        </li>
      </ul>
    </nav>

<div class="logo">
<img src="https://content.codecademy.com/courses/web-101/unit-9/htmlcss1-img_logo-shiptoit.png" >
</div>

<table>
%s
</table>

</body>
<html>
'''%(p)


#opening web_browser
filename = 'webbrowser.html'
def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)
webbrowser.open(filename)

#closing connection
if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")
