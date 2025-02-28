# EX01 Developing a Simple Webserver
## Date:26.10.2024

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
from http.server import HTTPServer,BaseHTTPRequestHandler

content='''

<html>
    <body>
    <title>LENOVO THINKPAD </title>
    <table border="5" bgcolor="cyan" cellpadding="10"> 
    <caption align="center"></caption> 
    <th colspan="7" align="center" bgcolor="aquamarine"> LAPTOP SPECIFICATIONS </th>
     <tr>
        <th>S.NO</th>
        <th>SPECIFICATIONS</th>
        <th>DETAILS</th>
     </tr>
     <tr> 
        <td> 1</td>
        <td> Device ID</td>
        <td> 15EEA3B2-7EF5-4DEC-903D-577382C3C005</td>
        
     </tr>
     <tr>
        <td> 2</td> 
        <td> Product ID</td>
        <td> 00342-42708-95389-AAOEM</td>
        
     </tr>
     <tr>
        <td> 3 </td>
        <td> OS build</td>
        <td> 22631.4317</td>
        
     </tr>
     <tr>
        <td> 4 </td>
        <td> Installed RAM </td>
        <td> 16 GB</td>
     </tr>
     <tr>
        <td> 5 </td>
        <td> Version</td>
        <td> 23H2</td>
     </tr>
     </table>
    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()

## OUTPUT:
![alt text](<Screenshot 2024-10-26 134519.png>)
![alt text](<Screenshot 2024-10-26 134633.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
