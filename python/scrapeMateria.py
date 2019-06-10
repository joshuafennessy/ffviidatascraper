    #package imports
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from json import dumps

#import custom functions
from projectFunctions import *
from Materia import *

def parseMateriaDetails(m, resp):
    #start by selecting all of the correct DIV tags
    divs = resp.find_all("div", class_="card")
    materiaDetails = ''

    done = False

    for div in divs:
        if not done:
            #look at the links in the div and check for the materia name
            divLinks = div.select('a')
            for link in divLinks:
                #print('{0}|{1}'.format(link['name'], m.Name))
                try:
                    if m.Name == link['name']:
                        #Found One!
                        materiaDetails = div
                        details = materiaDetails.select('dd')
                        materiaDescription = details[0].get_text()
                        materiaLocation = details[1].get_text()

                        m.Description = materiaDescription
                        m.Location = materiaLocation

                        done = True
                except:
                    i = 1

    #print(materiaDetails)

"""
 The first objective is to retrieve a list of all materia from the 
 landing page. For each materia in this list, make a request to the child
 page and scrape data from there.
"""

mainMateriaURL = "https://jegged.com/Games/Final-Fantasy-VII/Materia/Full-List.html"

mainMateriaListContent = simple_get(mainMateriaURL)
bsMainMaterial = BeautifulSoup(mainMateriaListContent, 'html.parser')

#loop thorough the Materia list on this page and start collecting attributes
for link in bsMainMaterial.find_all("a", class_="iconwrap"):
    try:
        materiaName = link['href'][::-1].split("/")[0].split("#")[0][::-1]
        materiaType = link['href'][::-1].split("/")[0].split("#")[1][::-1].replace('.html', '')

        #create a new instance object to be consumed via JSON later
        m = Materia(materiaName, materiaType)
        m.URL = 'https://jegged.com' + link['href']

        #get the response for the materia details
        detailResp = BeautifulSoup(simple_get(m.URL), 'html.parser')

        #check out the output
        parseMateriaDetails(m, detailResp)
        print(m.__dict__)

    except Exception as e:
        print(e)
