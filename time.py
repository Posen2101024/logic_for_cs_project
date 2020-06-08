
from corenlp import CoreNLP

def main():

	with open("database/data.txt", "r") as f:

		sents = f.read().strip().split("\n")

	keeps = ["COUNTRY", "ORGANIZATION", "PERSON", "MONEY"]

	model = CoreNLP()

	with open("time.pl", "w") as f:

		dic = {}

		for sent in sents:

			items = model.ner(sent)

			times = []

			for word, ner in items:

				if ner == "DATE":

					for num in "".join([c if "0" <= c <= "9" else "." for c in word]).split("."):

						if num != "" and 1800 <= int(num) <= 2100:

							times.append(num)

			for word, ner in items:

				for time in times:

					if ner in keeps:

						if not time in dic:

							dic[time] = []

						dic[time].append((word, ner))

		for time in dic:

			for word, ner in set(dic[time]):

				f.write("time_({}, \"{}\", \"{}\").\n".format(time, word, ner))

if __name__ == "__main__": main()
