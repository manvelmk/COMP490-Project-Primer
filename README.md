# COMP490-Project-Primer
COMP 490: Individual Primer Project
Overview:
In this project, you are to create a simple web application.  This web application can be written in any programming language of your choice.  However, you must use the simple CGI interface.  I.e., you can’t use the vendor supplied libraries to read access the HTTP Header information.

The functionality of your web application is to be defined by you.  There is a minimal number of features that are required, you are free to add additional features. 
Features:
Your web application must have the following features:
It must respond to the GET verb.
It must have a different response based upon the URI provided to the application.
It must return HTML and appropriate links to any associated CCS sheets or Javascript (I.e., do not inline style or dynamic behavior within your structure).
It must have least one style sheet; it may have dynamic content, but it’s not required.
It must consume information information from the file system.
I.e., your web application must make a call, via the CLI or system call, to the OS to get additional information from the filesystem that is integrated into your output. 
It must consume information from a remote web-server
I.e., your web application must make a call via HTTP to another web-server to get additional information that is integrated into your output.

Conditions:
You may use any programming language, but you must follow the CGI conventions.
You must obtain all information about the request directly from environment variables.
(See ssh://ssh.csun.edu/~steve/webdrive/public_html/cgi-bin/simple.cgi program)
You must handle all URIs within your namespace. 
(See Mod Rewrite Rules)
You must emit both the HTTP header and body.
