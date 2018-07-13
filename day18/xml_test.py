# -*- coding: utf-8 -*-
# Author: hkey
import xml.etree.ElementInclude as ET

tree = ET.parse('test.xml')
root = tree.getroot()
print(root.tag)

