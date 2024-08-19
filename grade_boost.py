
def grade_boost(students, letter):
    students = {
    'Elyse': 5,
    'Chris': 20,
    'Mehran': 20,
    'Clinton': 40,
    'Neel': 12
}

    # letter = input("")
    for key in students.keys():
        if letter.upper() in key:
            value = students[key] + 5
            print(value)
    
    print(students)


print(grade_boost({
    'Elyse': 5,
    'Chris': 20,
    'Mehran': 20,
    'Clinton': 40,
    'Neel': 12
}, 'C'))



