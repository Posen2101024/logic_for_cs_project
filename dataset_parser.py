"""

Input file:
	dataset

Ouput file:
	parsing

Ouput form:

	'Whole sentence'
	'Parsed pairs'
	'Cause of the whole sentence'
	'Parsed pairs'
	'Effect of the whole sentence'
	'Parsed pairs'

	with sep = \t for each line

"""

import numpy as np
import pandas as pd

def main(dataset, parsing):

	with open(parsing, "w") as f:

		for df in pd.read_csv(dataset, header = None, chunksize = 1):

			items = df.values.reshape((-1, ))

			write = []

			for i in range(3):

				sentence = str(items[i * 2]).strip()
				sentence = sentence[len('{"sentence":"'):-len('"}')]

				exists = str(items[i * 2 + 1]).strip()
				exists = " ".join(exists.split()[1:])

				write.append(sentence)
				write.append(exists)

				print("\n\n{}\n\n{}".format(sentence, exists))

			f.write("{}\n".format("\t".join(write)))

if __name__ == "__main__": 

	dataset = "database/final_project/fin_pairs.csv"

	parsing = "database/data.csv"

	main(dataset, parsing)
