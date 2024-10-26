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