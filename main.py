import xml.etree.ElementTree as ET
import glob


def main():
    # initialising dictionary
    trip_sent = {}

    # looping through all files of a path
    for path in glob.glob("data/xml/train/*"):
        # parsing the data of xml file
        tree = ET.parse(path)
        # loops through every entry in xml file
        for entry in tree.iter('entry'):
            sentences = []
            # loops through every tripleset in a entry
            for tripleset in entry:
                # add all sentences of an entry too a list
                if tripleset.tag == "lex":
                    sentences.append(tripleset.text)
                # add the triple with the corresponding sentences to the dictionary
                for triple in tripleset:
                    trip_sent[triple.text] = sentences

    triples_file = open("triples_train.txt", "w")
    sentence_file = open("sentences_train.txt", "w")

    for key, value in trip_sent.items():
        for el in value:
            triples_file.write(key)
            triples_file.write("\n")
            sentence_file.write(el)
            sentence_file.write("\n")

    #
    print("WRITING TO FILE WORKED")
    triples_file.close()
    sentence_file.close()


if __name__ == "__main__":
    main()