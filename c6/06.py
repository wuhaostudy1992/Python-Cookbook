from xml.etree.ElementTree import parse, Element

doc = parse('xmldata6.xml')
root = doc.getroot()

if root.find('haha'):
    root.remove(root.find('haha'))
    
print(root.getchildren().index(root.find('nm')))

e = Element('NewNode')
e.text = 'This is a new node'
root.insert(2, e)
doc.write('xmldata6.xml', xml_declaration=True)
