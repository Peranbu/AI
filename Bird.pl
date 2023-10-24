can_fly(crow).
can_fly(sparrow).
can_fly(eagle).
cannot_fly(penguin).
cannot_fly(ostrich).
fly(X) :- can_fly(X).
fly(X) :- \+ cannot_fly(X).
