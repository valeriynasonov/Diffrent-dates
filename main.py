import json
with open("newsafr.json", encoding = "utf-8") as f:
    data = json.load(f)
    list_of_counter = [ ]
    list_of_words_1 = [ ]
    counter_dict = { }
    list_lider_word =[ ]
    count_com = 0
    for v in data["rss"]["channel"]["items"]:
        for key, value in v.items():
            if key == "description":
                list_of_words = value.split(" ")
                for element in list_of_words:
                    lenght_word = len(element)
                    if lenght_word > 6:
                        list_of_words_1.append(element)
                        enter_count = list_of_words_1.count(element)
                        counter_dict[element] = enter_count
                        list_lider_word = list(counter_dict.items())
                        list_lider_word.sort(key = lambda i: i[1])
                        list_lider_word.reverse()
    print(list_lider_word[0:3])








