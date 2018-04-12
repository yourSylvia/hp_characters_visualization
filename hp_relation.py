import csv
import nltk
import codecs
import time


# nodes - names with count
names = {}
updated_names = {}
# edges
relationships = {}
# name list in a whole chapter
entity_names = []
#  chapter
chapter = []


# Count names occurence in a chapter
def countnames(entity_names):
    for temp in entity_names:
        if any(temp in s for s in name_set):
        # if temp in name_set:
            if temp in names:
                names[temp] += 1

            else:
                names[temp] = 1

    return names


def extract_name_entities(chapter, entity_names):
    # for sent in nltk.sent_tokenize(chapter):
    for sent in chapter:
        # ne_chunk: a classifier-based named entity recognizer
        # pos_tag: processes a sequence of words, and attaches a part of speech tag to each word
        # word_tokenize: tokenize text into words
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):

            if hasattr(chunk, 'label') and chunk.label()=="PERSON":
                name = [child[0] for child in chunk]
                if any("Professor" in w for w in name):
                    name.pop(0)
                    new_name = name
                    entity_names.append(' '.join(new_name))
                elif any("Uncle" in w for w in name):
                    name.pop(0)
                    new_name = name
                    entity_names.append(' '.join(new_name))
                elif any("Aunt" in w for w in name):
                    name.pop(0)
                    new_name = name
                    entity_names.append(' '.join(new_name))
                else:
                    entity_names.append(' '.join(name))

    # print("\nnames in chapter\n", entity_names)
    return entity_names


def hp_relations(chapter, entity_names, updated_names):
    key = list(updated_names.keys())

    for block in chapter:
        for name1 in entity_names:

            if (name1 not in key) or (name1 not in block):
                continue

            for name2 in entity_names:
                if (name2 not in key) or (name2 not in block):
                    continue

                if name1 == name2:
                    continue

                if name1 not in relationships:
                    relationships[name1]={}

                elif name2 not in relationships[name1]:
                    relationships[name1][name2] = 1

                else:
                    relationships[name1][name2] += 1

    return relationships


# Union the same name
def unionname(names):
    for kv in names.items():
        name = kv[0]
        value = kv[1]
        edited = False

        if (name == '') or (len(name) < 3):
            continue
        for dic_new_kv in list(updated_names.items()):
            dic_new_name = dic_new_kv[0]
            dic_new_value = dic_new_kv[1]
            if name in dic_new_name:
                updated_names[dic_new_name] = dic_new_value + value
                edited = True
            elif dic_new_name in name:
                updated_names[name] = value + dic_new_value
                del updated_names[dic_new_name]
                edited = True

        if not edited:
            updated_names[name] = value

    return updated_names


# Save as new csv file
def save_node_and_edge(names, relationships):
    with open('nodes.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key in names:
            writer.writerow([key, names[key]])

    with open('edges.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)

        for key1 in relationships:
            for key2 in relationships[key1]:
                writer.writerow([key1, key2, relationships[key1][key2]])


    print("\nFinish!!!\n")


# --------------------------------------- Read files ---------------------------------------- #
t = time.process_time()

for i in range(1, 8):
    # with codecs.open("data_hp%d.txt" % i, "r") as hp_name:
    #     name_set = hp_name.readlines()
    #     name_set = [j.strip() for j in name_set]
    #     print ("HP_names", name_set, "\n")

    with codecs.open("hp_characters.txt", "r") as hp_name:
        name_set = hp_name.readlines()
        name_set = [j.strip() for j in name_set]
        # print ("HP_names", name_set, "\n")

    with codecs.open("hp%d.txt" % i, "r") as hp:
        hp_content = [j.strip() for j in hp.readlines()]

        print("-------------------------- Book %d --------------------------" %i)
        print("Chapter 1")
        for sen in hp_content:

            if "Chapter" in sen and sen != "Chapter 1":
                print(sen)
                entity_names = extract_name_entities(chapter, entity_names);
                names = countnames(entity_names)
                updated_names = unionname(names)
                relationships = hp_relations(chapter, entity_names, updated_names)

                chapter[:] = []
                entity_names[:] = []

            else:
                chapter.append(sen)

        print("\noccurence of names\n", updated_names)
        print("\nrelationships: ", relationships)


save_node_and_edge(names, relationships)

print("Process in ", time.process_time()-t, " secs")








