import os
import sys
root = os.path.dirname(__file__) + '/'

sys.path.insert(0,root)
sys.path.append(os.path.join(root, '..'))
os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
