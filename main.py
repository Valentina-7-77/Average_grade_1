  # Средний балл
  # Установка соответствия между студентами и оценками
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted(students)
new_students = sorted(students)
print(new_students)
print(grades)
print(new_students[0], grades[0])
print(new_students[1], grades[1])
print(new_students[2], grades[2])
print(new_students[3], grades[3])
print(new_students[4], grades[4])
   # Вычисляем средний балл
average_grade_Aaron = sum(grades[0])/len(grades[0])
average_grade_Bilbo = sum(grades[1])/len(grades[1])
average_grade_Johnny = sum(grades[2])/len(grades[2])
average_grade_Khendrik = sum(grades[3])/len(grades[3])
average_grade_Steve = sum(grades[4])/len(grades[4])
   # Выводим значения в консоль
journal = {'Aaron': average_grade_Aaron, 'Bilbo': average_grade_Bilbo, 'Johnny': average_grade_Johnny, 'Khendrik': average_grade_Khendrik,'Steve': average_grade_Steve}
print(journal)

