# This short python program is an introduction to reading and parsing XML files
# It has been written as an introduction to XML parsing as part of the 
# EH2745 Computer APplications in power systems course at KTH
# Author: Lars Nordström, larsno@kth.se 
# Date: 2020-03-25
#
#
# While working with this file, make sure to also open the books.xml file to make
# referencing to the XML structure easier.
#
# In the comments throughtout the file, you find questions and exercises to
# complete - in some cases you need to add code of your own.


# First thing we need to do is to import the ElementTree library
import xml.etree.ElementTree as ET

#Next step is to create a tree by parsing the XML file referenced
# We are here using a sample XML file provided by Microsoft that containts
# records of books
tree = ET.parse('books.xml')

#If you have not already, please open up the books.xml file

# After these two steps we now have read the XML file and converted (parsed) 
# the XML data with its tags, attributes and data into a tree stored in memory

# We can access the root of the tree and print it
root = tree.getroot()
print(root)

# Any attributes associated with the root element?
print (root.attrib)


# We can list the elements immediately below the root by iterating
# through the children of the root, printing information as we go along
# In this first loop, we retrieve the tag of the children as well as 
# any attributes


for child in root:
    print (child.tag, child.attrib)


# To find all tags that exist  in the document and store them in a list
    
tags = []
for child in root.iter():
    if child.tag not in tags:
        tags.append(child.tag)
print (tags)

# To print all titles of all books
for ti in root.iter('title'):
    print (ti.text)


# To find a specific piece of text from one specific child in the three
# Text in the first book's second child (=title)
print (root[0][1].text)


# Print all booktitles and their authors.

for b in root.findall('book'):
    name = b.find('title')
    print(name.text)
    for a in b.findall('author'):
        print(' |-->', a.text)


        
#
    
