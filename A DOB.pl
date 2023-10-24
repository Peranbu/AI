Initialize an empty database.

:- dynamic person/2.



% Add a person to the database.

add_person(Name, DOB) :-

    assertz(person(Name, DOB)).



% Retrieve the DOB of a person by their name.

get_dob(Name, DOB) :-

    person(Name, DOB).



% Delete a person from the database.

delete_person(Name) :-

    retract(person(Name, _)).



% List all people in the database.

list_people :-

    findall(Name-DOB, person(Name, DOB), People),

    write('Name - DOB'), nl,

    print_people(People).



print_people([]).

print_people([Name-DOB | Rest]) :-

    write(Name), write(' - '), write(DOB), nl,

    print_people(Rest).
