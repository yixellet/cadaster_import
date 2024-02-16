from xml.etree import ElementTree as et

s = et.parse('xsd_parser/schemas/extract_about_property_land_v01/extract_about_property_land_v01.xsd')
for k in s.iter():
    print(k.tag)
    print(k.attrib)
