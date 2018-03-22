marks_person = {
    "Akanksh": [7.56, 8.08, 7.43, 7.29, 3.92],
    "Shiraz": [7.83, 6.67, 7.86, 6.357, 6.38],
    "Nithin": [8.83, 9.33, 9, 8.71, 7.61],
    "Mohak": [7.67, 7.75, 8, 8.2, 7.19]
}
marks = marks_person["Shiraz"]
total_marks = 24 + 24 + 28 + 28 + 26
agg_marks = ((24 * marks[0]) + (24 * marks[1]) + (28 * marks[2]) +
             (28 * marks[3]) + (26 * marks[4])) / total_marks
print(agg_marks)
avg_marks = 7
rest_sem_total = 26

marks_needed = avg_marks * (total_marks + rest_sem_total) - (
    agg_marks * total_marks)
print(marks_needed / rest_sem_total)
