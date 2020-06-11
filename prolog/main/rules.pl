
:- table year/2.
:- table word/4.

:- table input/3.
:- table truth/4.

:- dynamic isSolve/1.

truth(YEAR, WORD, NER, POS) :-
	year(NUM, YEAR),
	word(NUM, WORD, NER, POS),
	not(truth(YEAR, WORD, NER, POS)).

solve(YEAR, [NER | NER_LIST], [POS | POS_LIST]) :-
	input(X, NER, POS),
	not(isSolve(YEAR)),
	truth(YEAR, X, NER, POS),
	solve(YEAR, NER_LIST, POS_LIST).

solve(YEAR, [], []) :-
	asserta(isSolve(YEAR)).
