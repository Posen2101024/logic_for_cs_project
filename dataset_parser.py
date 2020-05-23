"""
Input file: dataset
Ouput file: parsing

Ouput format: '{sentence}	{exists}' for each line
"""

import numpy as np
import pandas as pd

def main(dataset, parsing):

	with open(parsing, "w") as f:

		for df in pd.read_csv(dataset, header = None, chunksize = 1):

			items = df.values.reshape((-1, ))

			for i in range(3):

				sentence = str(items[i * 2]).strip()
				exists   = str(items[i * 2 + 1]).strip()

				print("\n{}\n{}".format(sentence, exists))

				f.write("{}\t{}\n".format(sentence, exists))

if __name__ == "__main__": 

	dataset = "database/final_project/fin_pairs.csv"

	parsing = "database/data.csv"

	main(dataset, parsing)
