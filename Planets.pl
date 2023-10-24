% Define facts about the planets in our solar system.

planet(mercury, 0.39, 0.24, 4879).

planet(venus, 0.72, 0.62, 12104).

planet(earth, 1.00, 1.00, 12742).

planet(mars, 1.52, 0.11, 6779).

planet(jupiter, 5.20, 317.8, 139822).

planet(saturn, 9.58, 95.2, 116464).

planet(uranus, 19.22, 14.6, 50724).

planet(neptune, 30.05, 17.2, 49244).



% Define a rule to classify planets into terrestrial and gas giants.

terrestrial_planet(Name) :-

    planet(Name, _, Mass, _),

    Mass =< 0.6.



gas_giant(Name) :-

    planet(Name, _, Mass, _),

    Mass > 0.6.



% Define a rule to list the names of all planets.

list_planets(Planets) :-

    findall(Name, planet(Name, _, _, _), Planets).



% Define a rule to get the diameter of a planet by its name.

get_planet_diameter(Name, Diameter) :-

    planet(Name, _, _, Diameter).



% Define a rule to get the distance from the sun of a planet by its name.

get_planet_distance(Name, Distance) :-

    planet(Name, Distance, _, _).



% Define a rule to get the mass of a planet by its name.

get_planet_mass(Name, Mass) :-

    planet(Name, _, Mass, _).
