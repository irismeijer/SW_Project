# SW_Project

This repository is the beginning of the project of translating English RDF-triples to Dutch sentences. 

The xml-data is made available from the WebNLG Challege (http://webnlg.loria.fr/pages/index.html). 
The function split_trip_sent.py loops through the xml files and creates a file containing the triples and the sentences.
The sentences of the train and dev data were translated with the Google Translate Tool and the the test data was translated manually.
The resulting data, that could be found in the data/txt-folder, will be used to run the OpenNMT project (https://github.com/OpenNMT/OpenNMT-py)

The best model that came out of the OpenNMT-system and the predictions for our project can be found in the results_OpenNMT-folder.
