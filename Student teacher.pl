teacher(aashrit, maths).
teacher(bhanu, ai).
teacher(smitha,networks).
teacher(naveen,english ).
student(abhi,smitha,123).
student(jyothi,bhanu,163).
student(gangi,smitha,123).
student(bala,naveen,193).

find_teacher(Teacher_name,Subject):-
    teacher(Teacher_name,Subject).
find_student(stu_name,Teacher_name,Code):-
    student(stu_name,Teacher_name,Code).
