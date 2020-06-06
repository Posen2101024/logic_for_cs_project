
test1 :- 

	person_(X), print(X), nl, fail.

test2 :- 

	(person_("Trump") -> (X = true); X = false), print(X), nl, fail.

test3 :- 

	(person_("Posen") -> (X = true); X = false), print(X), nl, fail.
