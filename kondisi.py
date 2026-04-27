score = 78

if score >= 90:
    grade = "A"
    feedback = "kerja luar biasa"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
    feedback = "Tetap tingkatkan"
else:
    grade = "F"
    feedback = "Anda perlu belajar keras"
print(f"Nilai : {grade}\nUmpan Balik: {feedback}")
