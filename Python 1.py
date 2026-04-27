user_input = input("Masukkan angka positif :")

if user_input.isdigit():
    number = int(user_input)
    if number > 0:
        print(f"Anda memasukkan angka positif yang valid: {number}")
    else:
        print("Angka harus lebih besar dari nol")
else:
    print("Input tidak valid. Masukkan Angka Numerik.")
