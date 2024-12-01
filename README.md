## PDF Invoice generator

https://shihas.stackschools.com


deployment:

```
<VirtualHost *:80>
	ServerName shihas.stackschools.com
    WSGIDaemonProcess shihasapp python-home=/var/www/shihas/env python-path=/var/www/shihas/
	WSGIProcessGroup shihasapp
	WSGIScriptAlias / /var/www/shihas/mysite/wsgi.py
	ErrorLog /var/www/shihas/media/error.log
	CustomLog /var/www/shihas/media/access.log combined
</VirtualHost>
```