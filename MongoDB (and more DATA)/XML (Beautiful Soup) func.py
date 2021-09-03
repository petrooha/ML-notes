# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        soup = BeautifulSoup(html, "lxml"))#use the soup
        ev = soup.find(id="__EVENTVALIDATION")#find the key of a dictionary in page source
        data["eventvalidation"] = ev["value"]#assign value
        vs = soup.find(id="__VIEWSTATE")#find key
        data["viewstate"] = vs["value"]#assign
        pass

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,#fixed!!
                          "__VIEWSTATE": viewstate#fixed!!
                    })

    return r.text

#####but before, need to find those variables in the "page source"
#### it would look like this:

<div class="aspNetHidden">
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJNTUyNTIyMzEzDxYOHgdzdHJDb25uBVpQcm92aWRlcj0uTkVUIEZyYW1ld29yayBEYXRhIFByb3ZpZGVyIGZvciBPREJDO0RTTj1FbmRlYXZvdXI7dWlkPXdlYnVzZXI7cHdkPSFXZWJ1c2VyMTIzNDseBU1MaXN0BbMBJ0FUTCcsJ0JXSScsJ0JPUycsJ0NMVCcsJ01EVycsJ09SRCcsJ0RGVycsJ0RFTicsJ0RUVycsJ0ZMTCcsJ0hOTCcsJ0lBSCcsJ0xBUycsJ0xBWCcsJ01JQScsJ01TUCcsJ0pGSycsJ0xHQScsJ0VXUicsJ01DTycsJ1BITCcsJ1BIWCcsJ1BEWCcsJ1NMQycsJ1NBTicsJ1NGTycsJ1NFQScsJ1RQQScsJ0RDQScsJ0lBRCceDEFpcnBvcnRfTmFtZQUfQm9zdG9uL

###BEST PRACTICE FOR DATA SCRAPING:
###1 LOOK AT HOW BROWSER MAKES REQUEST
###2 EMULATE IN CODE
###3 IF STUFF BLOWS UP, LOOK AT YOUR HTTP TRAFFIC
###4 RETURN TO ###1 UNTIL IN WORKS
# more here https://classroom.udacity.com/courses/ud032/lessons/698949179/concepts/7625885380923
