def p13():
    student_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    scores = [9, 22, 60, 58, 70, 12, 33, 99, 57, 82]
    grade_a_student_with_score = [(student_names[i], scores[i]) for i in range(len(student_names)) if scores[i] >= 80]
    #Expected Ans -> grade_a_student_with_score = [('h', 99), ('j', 82)]
    return grade_a_student_with_score
print(p13())