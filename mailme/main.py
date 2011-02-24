#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import mail
from django.utils import simplejson as json

# use like this:
# curl-d '{"subject":"some subject", "body":"actual msg body", "to":"someguy@somwhere.net" }' -X POST http://YOUARAPP.com


class MainHandler(webapp.RequestHandler):

    def post(self):
      jsonString = self.request.body
      msg = json.loads(jsonString)      
      
      # change sender to an email that is registered to a admin for this application
      mail.send_mail(sender="ADMIN@YOURAPP.com",
                      to=msg.get('to'),
                      subject=msg.get('subject'),
                      body=msg.get('body'))
      
def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
