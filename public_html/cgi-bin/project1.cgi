#! /bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<title>GET PAGE</title>'
echo '</head>'
echo '<body>'
b=$(echo $QUERY_STRING | cut -d'=' -f2)
echo '<h1>We have copied the HTML contents using cURL! </h1>'
echo 'The webpage we copied: '
echo $b
content = $(/usr/bin/curl -s $b > output.html)
chmod 755 output.html
echo '<form action="http://csun.edu/~dr63126/cgi-bin/output.html">'
echo '<input type="submit" value="Go to our new site" />'
echo '</form>'
echo '</body>'
echo '</html>'

exit 0
