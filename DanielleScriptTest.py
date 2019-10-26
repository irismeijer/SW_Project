# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:44:21 2019

@author: danie
"""

from xml.dom import minidom

# just the first document
doc = minidom.parse('data/xml/train/webnlg_v2_constrained_Airport_1.xml')

# all entries
entries = doc.getElementsByTagName("entry")

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
