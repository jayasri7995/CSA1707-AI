% Foods and their properties
food(apple, [low_sugar, fruit]).
food(banana, [high_sugar, fruit]).
food(broccoli, [vegetable, low_sodium]).
food(chicken, [high_protein, low_sodium]).
food(bread, [carb, gluten]).
food(milk, [dairy]).

% Disease restrictions
disease(diabetes, high_sugar).
disease(hypertension, high_sodium).
disease(celiac, gluten).
disease(lactose_intolerance, dairy).

% Food allowed if it does not have the forbidden property
allowed(Food, Disease) :-
    food(Food, Props),
    disease(Disease, Bad),
    \+ member(Bad, Props).

% Get all allowed foods for a disease
allowed_foods(Disease, Foods) :-
    findall(F, allowed(F, Disease), Foods).
