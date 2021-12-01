from needed_tools import TypeOb, WordOb

def load_data(classifier, txt, type_name):
    types = classifier.types
    input_words = txt.split()
    words = classifier.words

    # add words if not exist and update total words and type counts:
    for inp_word_name in input_words:
        word_names = [x.name for x in words]
        if inp_word_name not in word_names:
            words.append(WordOb(inp_word_name, len(types)))
            for type_ in types:
                type_.word_counts.append(1)
                type_.total_words += 1

    # add type if not exist:
    types = classifier.types
    type_names = [x.name for x in types]
    if type_name not in type_names:
        types.append(TypeOb(type_name,[1] * len(words), len(words), 1))
        for word in words:
            word.count += 1

    # index of type:
    curType = next(x for x in types if x.name == type_name)
    # update type count:
    curType.num_of_data += 1
    # update word count of type:
    curType.total_words += len(input_words)
    # increment counters of type:
    for i, word in enumerate(words):
        temp = curType.word_counts
        if (type(temp) is list) and (i < len(temp)):
           temp[i] += input_words.count(word.name)

    # update num of words:
    classifier.num_of_data += 1
