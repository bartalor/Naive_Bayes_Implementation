class TypeOb:
    def __init__(self, name, word_counts, total_words, num_of_data):
        self.name = name
        self.word_counts = word_counts
        self.total_words = total_words
        self.num_of_data = num_of_data

class WordOb:
    def __init__(self, name, count):
        self.name = name
        self.count = count
