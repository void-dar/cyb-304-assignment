import xml.etree.ElementTree as ET

# Parse XML string
with open("students.xml", "r") as file:
    data = file.read()
root = ET.fromstring(data)
print(root.find('name').text) # Ada

