input("find", "O", "VBD").
input("U.S.", "COUNTRY", "NNP").
input("health", "O", "NN").
input("care", "O", "NN").
input("spend", "O", "NN").
input("be", "O", "VB").
input("$", "MONEY", "$").
input("3.9", "MONEY", "CD").
input("trillion", "MONEY", "CD").
input("Medicare", "ORGANIZATION", "NNP").
input("2019", "DATE", "CD").
input("compare", "O", "VBN").
input("$", "MONEY", "$").
input("3.8", "MONEY", "CD").
input("trillion", "MONEY", "CD").
input("status", "O", "NN").
input("quo", "O", "NN").
goal :-
	solve(YEAR, ["DATE", "O", "COUNTRY", "O", "MONEY", "MONEY", "ORGANIZATION", "O", "O"], ["CD", "NN", "NNP", "VB", "CD", "$", "NNP", "VBD", "VBN"]),
	print(YEAR), nl, fail.
