% file: simple_kb.pl

% facts
parent(alice, bob).
parent(bob, carol).
parent(bob, david).
male(bob).
female(alice).
female(carol).
female(david).

% rules
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
