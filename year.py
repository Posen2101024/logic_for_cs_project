
def main():

	with open("database/date.txt", "r") as f:

		dates = [line.split() for line in f.read().strip().split("\n")]
		dates = [[x, y[:4]] for x, y in dates if 1800 <= int(y[:4]) <= 2100]

	with open("year.pl", "w") as f:

		for x, y in dates:

			f.write('year({}, {}).\n'.format(x, y))

if __name__ == "__main__": main()
