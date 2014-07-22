#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs

import datetime

html_body="""
<html><body>
foo=%s <br>
neko=%s
</body></html>"""

import cgi
form=cgi.FieldStorage()

print "Content-type: text/html\n"
print html_body % (form.getvalue('foo','N/A'), form.getvalue('neko', 'N/A')) # エラー処理できる
#print html_body % form['foo'].value
