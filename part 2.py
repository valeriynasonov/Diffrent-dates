import xml.etree.ElementTree as ET
list_of_counter = [ ]
list_of_words_1 = [ ]
counter_dict = { }
list_lider_word =[ ]
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
news_xml = root.findall("channel/item")
for news in news_xml:
    a = news.find("title").text
    list_of_words = a.split(" ")
    for element in list_of_words:
        lenght_word = len(element)
        if lenght_word > 6:
            list_of_words_1.append(element)
            enter_count = list_of_words_1.count(element)
            counter_dict[element] = enter_count
            list_lider_word = list(counter_dict.items())
            list_lider_word.sort(key=lambda i: i[1])
            list_lider_word.reverse()
print(list_lider_word[0:3])

