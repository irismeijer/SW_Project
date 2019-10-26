# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:44:21 2019

@author: danie
"""

from xml.dom import minidom

# create doc file
print("This is a word document")

# parse all documents

doc = minidom.parse('data/xml/train/webnlg_v2_constrained_Airport_1.xml')
print("xml 1")

entries = doc.getElementsByTagName("entry")

# test
otriple = entries[0].getElementsByTagName("otriple")[0]
print("otriple", otriple.firstChild.data)


for entry in entries:
    print("entry", entry.getAttribute("eid"))
    otriples = entry.getElementsByTagName("otriple")
    mtriples = entry.getElementsByTagName("mtriple")
    sentences = entry.getElementsByTagName("lex")
    for otriple in otriples:
        for lex in sentences:
            print("otriple", otriples.index(otriple), otriple.firstChild.data)
            print("sentence", sentences.index(lex), lex.firstChild.data)
    for mtriple in mtriples:
        for lex in sentences:
            print("mtriple", mtriples.index(mtriple), mtriple.firstChild.data)
            print("sentence", sentences.index(lex), lex.firstChild.data)
    # just one for now so break
    break
