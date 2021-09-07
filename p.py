#!/usr/bin/python3.6


print("content-type: text/html")
print()

import cgi 
import subprocess

form = cgi.FieldStorage()
cmd = "sudo" + " " + form.getvalue("x") 
op=subprocess.getoutput(cmd)
print(op)
