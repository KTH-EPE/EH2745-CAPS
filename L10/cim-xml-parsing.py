# This short python program is an introduction to reading and parsing CIM-XML files  as part of the 
# EH2745 Computer Applications in power systems course at KTH
# Author: Lars Nordström, larsno@kth.se 
# Date: 2020-03-29
#
#


# First thing we need to do is to import the ElementTree library
import xml.etree.ElementTree as ET

#Next step is to create a tree by parsing the XML file referenced
# We are here using ENTSO-E  model files used in Interoperability testing
tree = ET.parse('MicroGridTestConfiguration_T1_BE_EQ_V2.xml')

#If you have not already, please open up the books.xml file

# After these two steps we now have read the XML file and converted (parsed) 
# the XML data with its tags, attributes and data into a tree stored in memory

# We can access the root of the tree and print it
microgrid = tree.getroot()
print(microgrid)

# To make working with the file easier, it may be useful to store the 
# namespace identifiers in strings and reuse when you search for tags
    
ns = {'cim':'http://iec.ch/TC57/2013/CIM-schema-cim16#',
      'entsoe':'http://entsoe.eu/CIM/SchemaExtension/3/1#',
      'rdf':'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'}

# We create a dictionary  (above) and store the namespace names and their 
# respective URIs in it. We can then reference the namespace like below
# To make pritount more compact, we can replace the namespace URI with a 
# shorter string or even a null-string "".

# Note that in the dictionary, the curly braces '{' are used for the RDF tag
# but not for the cim and entsoe tags. This is a special solution to fix
# a problem of dual use of the curly braces in python dictionaries and the
# XML namespace tags. 

for equipment in microgrid:
    if (ns['cim'] in equipment.tag):
        print (equipment.tag.replace("{"+ns['cim']+"}",""))
        
# As can be seen, a CIM-XML file is very flat - the tree structure is 
# shallow, and most elements exist on the first or second level
# As can also be see, all Element tags are augmented with the namespace
# URI listed at the start of the file
            
# if we want to find all elements with a specific tag in the file:
for breakers in microgrid.findall('cim:Breaker', ns):
    if (ns['cim'] in breakers.tag):
        print (breakers.tag.replace("{"+ns['cim']+"}",""))
    
               
# One important attribute on all equipment is its identifer. All
# elements have an attribute named rdf:ID and the value of this attribute is 
# unique per element. We can find these identifiers and print out a compact
# list as per below

print ("All IDs")
for ids in microgrid:
    print (ids.attrib.get(ns['rdf']+'ID'))

# And finally, joining the two, e.g. we want the ID of all breakers
print ("BusbarSections IDs")
for busbars in microgrid.findall('cim:BusbarSection', ns):
    print (busbars.attrib.get(ns['rdf']+'ID'))
  


