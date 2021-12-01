import itertools
input = [
    ["aaa aaa aaa", "t1"],
    ["bbb bbb bbb", "t2"],
    ["ccc ccc ccc", "t3"],
    ["ddd ddd ddd", "t3"],
    ["ddd ddd ddd", "t3"]
]

def array_counter(arr):
    unique_words = list(set(arr))
    counter = [(elem,arr.count(elem)) for elem in unique_words]
    return(counter)

def all_words_of_type(input,type):
    arr = [elem[0].split() for elem in input if elem[1]==type]
    all_words = list(itertools.chain(*arr))
    return(all_words)

def histogram_of_type(input,type):
    return array_counter(all_words_of_type(input,type))

def histogrammer(input):
    all_types = [elem[1] for elem in input]
    unique_types = list(set(all_types))
    histogram = [(type,histogram_of_type(input,type)) for type in unique_types]
    return histogram

print(histogrammer(input))
# all_words = list(itertools.chain(*[elem[0].split() for elem in input]))
# print(array_counter(all_words))