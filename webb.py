from http.server import HTTPServer, BaseHTTPRequestHandler

content =  '''<html>
<head>
<h1>EXPERIMENT NUMBER 1</h1>
<h2>roll number:25014181</h2>
<h2>Name: LOGESHWARI N</h2>
<title>TABLE</title>
<style>
  table{
    border:2px solid black;
    boder-collapse:collapse;
    width: 60%;}
  th ,td {
    border: 1px solid black;
    padding: 8px;
    text-align: center;}
  th{
    background-color: "cyan";}
</style>
</head>
<body>
   <table>
     <tr>
     <th>s.no</th>
     <th>Name</th>
     <th>sem 1</th>
     <th>sem 2</th>
     <th>percentage</th>
     </tr>
     <tr>
     <td>1</td>
     <td>Mithra</td>
     <td>98</td>
     <td>88</td>
     <td>93%</td>
     </tr>
     <tr>
     <td>2</td>
     <td>John</td>
     <td>78</td>
     <td>99</td>
     <td>88.5%</td>
     </tr>
     <tr>
     <td>3</td>
     <td>Ranjini</td>
     <td>87</td>
     <td>79</td>
     <td>83%</td>
     </tr>
     <tr>
     <td>4</td>
     <td>Monisha</td>
     <td>99</td>
     <td>95</td>
     <td>97%</td>
     </tr>
     <tr>
     <td>5</td>
     <td>Sidhu</td>
     <td>76</td>
     <td>77</td>
     <td>76.5%</td>
     </tr>
   </table>
</body>

</html>'''

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
