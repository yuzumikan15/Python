#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs

def output_html (o):
	print >> o, "<html>"
	print >> o, "<head>"
	print >> o, '<meta http-equiv="Content-Type" content="text/html; charset=utf8" />'
	print >> o, "</head>"
	print >> o, "<body>"
  print >> o, "<h1>出力結果</h1>"
  print >> o, "</body>"
  print >> o, "</html>"

from BaseHTTPServer import *
 
class MyHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    output_html(self.wfile)
 
HTTPServer(('', 8700), MyHandler).serve_forever()
