def classify(classifier, txt):
    types = classifier.types
    input_words = txt.split()
    scores = [0] * len(types)
    word_names = [x.name for x in classifier.words]
    relevant_input_words = \
        [x for x in input_words if x in word_names]
    for typeI, type_ in enumerate(types):
        cur_score = type_.num_of_data/classifier.num_of_data
        for cur_inp_word_name in relevant_input_words:
            wordI = word_names.index(cur_inp_word_name)
            cur_score *= (type_.word_counts[wordI] / type_.total_words)
        scores[typeI] = cur_score

    result_typeI = scores.index(max(scores))
    classification = types[result_typeI].name
    return classification



