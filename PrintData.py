def print_data(classifier):
    types = classifier.types
    words = classifier.words

    for typeI, type_ in enumerate(types):
        print(type_.name + ":", type_.total_words)
        for wordI, word_count in enumerate(type_.word_counts):
            word = words[wordI]
            print(word.name + ":", word_count, end='    ')
        print()