% Define the relationships between students, teachers, subjects, and subject codes.

teaches_subject(teacher1, math101).

teaches_subject(teacher2, physics201).

teaches_subject(teacher3, history101).



student_subjects(john, math101).

student_subjects(john, history101).

student_subjects(amy, physics201).

student_subjects(sarah, history101).

student_subjects(sarah, math101).



% Define rules to query and infer relationships.

teaches_teacher(Teacher, Subject) :-

    teaches_subject(Teacher, Subject).



student_teacher(Student, Subject, Teacher) :-

    student_subjects(Student, Subject),

    teaches_teacher(Teacher, Subject).



