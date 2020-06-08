
from corenlp import CoreNLP

def main():

	with open("database/data.txt", "r") as f:

		sents = f.read().strip().split("\n")

	keeps = ["COUNTRY", "ORGANIZATION", "PERSON", "MONEY"]

	model = CoreNLP()

	with open("sent.pl", "w") as f:

		words = []

		for i, sent in enumerate(sents, 1):

			for name, ner in model.ner(sent):

				if ner in keeps:

					words.append("sent({}, \"{}\", \"{}\").".format(i, name, ner))

		f.write("{}\n".format("\n".join(words)))

if __name__ == "__main__": main()
