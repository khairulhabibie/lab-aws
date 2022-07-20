# for and while loop
import random

num = random.randint(1, 10)
print('Game tebak angka!\nkamu hanya ada 3 kali kesempatan\n')
state = 0

while state <= 2:
    try:    
        user_input = int(input('Masukan Nilai Tebakan: '))
        if user_input == num:
            print('Tebakan Benar!')
            break
        elif user_input in range (num+1,11):
            print(f'Tebakan salah, nilai {user_input} lebih besar dari angka yang ditebak'.format(user_input))
            state += 1
        elif user_input in range (0,num):
            print(f'Tebakan benar, nilai {user_input} lebih kecil dari angka yang ditebak'.format(user_input))
            state += 1
        else:
            print('Angka yang anda input keluar dari range')
    except ValueError: 
        print("Hanya menerima input angka")
print('\nGame berakhir')
