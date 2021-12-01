from typing import List
from LoadData import load_data
from Classify import classify
from PrintData import print_data
from needed_tools import TypeOb, WordOb

class Classifier:
    types: List[TypeOb] = []
    words: List[WordOb] = []
    num_of_data = 0

    def load_data(self, txt, type):
        load_data(self, txt, type)

    def classify(self, txt):
        return classify(self, txt)

    def print_data(self):
        print_data(self)



clasif = Classifier()
clasif.load_data("aaa aaa", "type1")
clasif.load_data("bbb bbb", "type2")
clasif.load_data("ccc ccc", "type3")
print(clasif.classify("ccc"))
