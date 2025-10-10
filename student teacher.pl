% Facts
student(aksha).
student(ravi).

teacher(sharma).
teacher(kapoor).

subject(cs101, 'AI').
subject(cs102, 'ML').

teaches(sharma, cs101).
teaches(kapoor, cs102).

enrolled(aksha, cs101).
enrolled(ravi, cs102).

% Rule
teacher_of_student(Student, SubCode, Teacher) :-
    enrolled(Student, SubCode),
    teaches(Teacher, SubCode).
