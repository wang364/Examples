#
# A brief introduction for using xml.etree.ElementTree
# https://docs.python.org/3/library/xml.etree.elementtree.html#
#
import xml.etree.ElementTree as ET

# Import data by reading from a file
tree = ET.parse('country_data.xml')

# Get root element
root = tree.getroot()

# dump() writes an element tree or element structure to sys.stdout
ET.dump(root)

# Get root element's children
for child in root:
    print(child.tag, child.attrib)

# Element.iter() iterate recursively over all the sub-tree below it (its children, their children, and so on).
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

# Element.findall() finds only elements with a tag which are direct children of the current element.
for country in root.findall('country'):
    # Element.find() finds the first child with a particular tag.
    # Element.text accesses the element’s text content.
    rank = country.find('rank').text
    # Element.get() accesses the element’s attributes. 
    name = country.get('name')
    print(name, rank)

##########################################
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    # An Element object may be manipulated by directly changing its fields (such as Element.text)
    rank.text = str(new_rank)
    # Adding and modifying attributes (Element.set() method)
    rank.set('updated', 'yes')

for country in root.findall('country'):
    # using root.findall() to avoid removal during traversal
    rank = int(country.find('rank').text)
    if rank > 50:
        # Element.remove() can remove elements.
        root.remove(country)

# ElementTree.write() writes XML documents to files.
tree.write('output.xml')