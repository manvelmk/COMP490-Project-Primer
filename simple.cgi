#! /bin/bash

###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The MIME type of associated with the option body of the HTTP request.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.  
# HTTP_USER_AGENT:   Information about the browser/client that made requested.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. The most common methods are GET and POST.
# REQUEST_URI:       The URI of the request
# SERVER_PROTOCOL:   Currently HTTP/1.1
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address
# SERVER_PORT:       The port of the server

echo "Content-type: text/html"
echo ""

echo "PATH=$PATH"
echo "         Current working directory: "
pwd
echo "____"
echo "Script Located at:"
echo $SCRIPT_FILENAME
echo "_____"
echo $HTTP_USER_AGENT
echo "_____"
echo $REQUEST_METHOD
echo "_____"
date
echo "_____"

#cat simple.html

if [ -n "${QUERY_STRING}" ] ; then 
   echo $QUERY_STRING
   #Display the query string if one exists
   cat ${QUERY_STRING}
   #Display the contents of the query string if it is a file in same directory
fi

#/usr/bin/curl http://www.csun.edu/engineering-computer-science/computer-science
/usr/bin/curl $QUERY_STRING
#curl the query string if it is a http address to display as a embeded page

# Read the body -- if it is a post
while read _post_line ; do
  echo ${_post_line} ";loop"
done 
echo $_post_line


exit 0
