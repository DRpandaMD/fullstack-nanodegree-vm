# webserver.py a web server written in python
# Michael Zarate
# 13/Dec/2017

import cgi

# for python2 use:
# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# for python3 use:
from http.server import BaseHTTPRequestHandler, HTTPServer


# web handler
class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello!" \
                          "<a href='/hola'>To hola</a>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
                          "<h2>What would you like me to say?</h2> <input name='message'" \
                          "type='text'><input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                # encode to utf-8 is required for python 3
                self.wfile.write(output.encode("utf-8"))
                print(output)

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>&#161Hola! " \
                          "<a href='/hello'>Back to Hello</a>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
                          "<h2>What would you like me to say?</h2> <input name='message'" \
                          "type='text'><input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                # encode to utf-8 is required for python 3
                self.wfile.write(output.encode("utf-8"))
                print(output)

        except IOError:
            self.send_error(404, "File Not Found " % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print("after 301")

            # get data from user
            ctype, pdict = cgi.parse_header(self.headers.getheader("Content-type"))
            print("got header")
            if ctype == "multipart/form-data":
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

                print("data successfully parsed from user")

            output = ""
            output += "<html><body>"
            output += "<h2>Okay, how about this: </h2>"
            output += "<h1> {} </h1>".format(messagecontent[0])

            output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
                      "<h2>What would you like me to say?</h2> <input name='message'" \
                      "type='text'><input type='submit' value='Submit'> </form>"
            output += "</body></html>"

            self.wfile.write(output.encode("utf-8"))
            print(output)

        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(("", port), webserverHandler)
        print("Web server running on port: ", port)
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered, stopping web server")
        server.socket.close()


if __name__ == '__main__':
    main()

