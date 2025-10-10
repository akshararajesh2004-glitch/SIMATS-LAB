% Facts: symptom-disease relationships
disease(flu) :- symptom(fever), symptom(headache), symptom(cough), symptom(sore_throat), symptom(fatigue).
disease(common_cold) :- symptom(runny_nose), symptom(sneezing), symptom(sore_throat), symptom(mild_cough).
disease(migraine) :- symptom(headache), symptom(nausea), symptom(sensitivity_to_light).
disease(malaria) :- symptom(fever), symptom(chills), symptom(sweating), symptom(headache).

% Ask about symptoms
ask(S) :-
    write('Do you have the following symptom: '), write(S), write('? (yes/no) '),
    read(Response),
    (Response == yes -> assertz(symptom(S)) ; fail).

diagnose :-
    retractall(symptom(_)),
    (
        (ask(fever) ; true),
        (ask(headache) ; true),
        (ask(cough) ; true),
        (ask(sore_throat) ; true),
        (ask(fatigue) ; true),
        (ask(runny_nose) ; true),
        (ask(sneezing) ; true),
        (ask(mild_cough) ; true),
        (ask(nausea) ; true),
        (ask(sensitivity_to_light) ; true),
        (ask(chills) ; true),
        (ask(sweating) ; true)
    ),
    (disease(Disease) ->
        format('Diagnosis: You may have ~w.', [Disease])
    ;
        write('Diagnosis: No matching disease found.')
    ).
