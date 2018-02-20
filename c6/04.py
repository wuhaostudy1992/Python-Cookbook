from xml.etree.ElementTree import iterparse
from collections import Counter

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    print(path_parts)
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)
    
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            #print(event, elem)
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            #print(tag_stack)
            print(elem_stack)
            if tag_stack == path_parts:
                #print(tag_stack)
                yield elem
                print(elem_stack, 'This is what I am confused: (before)')
                #to delete the previous yield element
                elem_stack[-2].remove(elem)
                print(elem_stack, 'This is what I am confused: (after)')
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

potholes_by_zip = Counter()
data = parse_and_remove('xmldata.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)
