# EX01 Developing a Simple Webserver

# Date:19-09-2025
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler

content =  """
from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TCP/IP Protocol suite</title>
    <style>
        body {
            font-family: arial, sans-serif;
            background:#78df0a;
            margin: 0;
            padding: 20px;
            text-align: center;
        }
        h2 {
            margin-bottom:10px;
        }
        .container {
            display: flex;
            justify-content: center;
            gap: 30px;
        }
        .model, .protocol {
            border: 2px solid #7323a2;
            border-radius:5px;
            margin: 10px 0;
            padding: 10px;
            background:#99ffb4;
            width:300px;
        }
        .layer{
            background:#42187a;
            border: 10px solid #000;
            border-radius:10px 0;
            padding: 10px;
            font-weight: bold;
        }
        .protocol-section{
            margin:10 px;
            padding: 8px;
        }
        .protocol-section h3{
            margin:5px 0;
            font-size:16px;
        }
        .box{
            display: inline-block;
            background:#042a51;
            color:#e50822;
            padding: 6px, 10px;
            margin: 4px;
            border-radius: 5px;
            font-size: 14px;
        }
        .transport.box {background: #336600;}
        .internet.box {background: #333399;}
        .network.box {background: #cc3300;}
    </style>
</head>
<body>
    <h2>TCP/IP Protol suite</h2>
       <div class="container">
        <div class="model">
            <h3>TCP/IP Model</h3>
            <div class="layer">Application layer</div>
            <div class="layer">Transoport layer</div>
            <div class="layer">Internet layer</div>
            <div class="layer"> Network interface layer</div>
        </div>
        <div class="protocol"><h3>TCP/IP Protocol suite</h3>
            <div class="protocol-section application">
                <div class="box">HTTP</div>
                <div class="box">FTP</div>
                <div class="box">TFTP</div>
                <div class="box">DNS</div>
                <div class="box">DHCP</div>
                <div class="box">SMTP</div>
                <div class="box">Telnet</div>
            </div>
            <div class="protocol-section transport">
                <div class="box">TCP</div>
                <div class="box">UDP</div>
            </div>
            <div class="protocol-section internet">
                <div class="box">IP</div>
            </div>
            <div class="protocol-section network">
                <div class="box">Ethernet</div>
                <div class="box">Token Ring</div>
                <div class="box">Frame Relay</div>
                <div class="box">ATM</div>
            </div>
        </div>
    </div>
</body>
</html>
'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()
```

# OUTPUT:
 
![alt text](<Screenshot 2025-09-19 183151.png>)
![alt text](<Screenshot 2025-09-19 183151.png>)


# RESULT:
The program for implementing simple webserver is executed successfully.
