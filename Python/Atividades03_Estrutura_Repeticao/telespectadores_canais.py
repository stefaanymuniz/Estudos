votos_canal04 = 0
votos_canal05 = 0
votos_canal09 = 0

while True:
    canal_assistido = int(input())
    if canal_assistido == 0:
        break
    elif canal_assistido == 4:
        votos_canal04 += 1
        # continue
    elif canal_assistido == 5:
        votos_canal05 += 1
        # continue
    elif canal_assistido == 9:
        votos_canal09 += 1
        # continue

# Ver forma melhor de fazer:
if votos_canal09 >= votos_canal04 >= votos_canal05:
    print(f'canal 9: {votos_canal09}\
          \ncanal 4: {votos_canal04}\
          \ncanal 5: {votos_canal05}')
elif votos_canal09 >= votos_canal05 >= votos_canal04:
    print(f'canal 9: {votos_canal09}\
          \ncanal 5: {votos_canal05}\
          \ncanal 4: {votos_canal04}')
elif votos_canal05 >= votos_canal09 >= votos_canal04:
    print(f'canal 5: {votos_canal05}\
          \ncanal 9: {votos_canal09}\
          \ncanal 4: {votos_canal04}')
elif votos_canal05 >= votos_canal04 >= votos_canal09:
    print(f'canal 5: {votos_canal05}\
          \ncanal 4: {votos_canal04}\
          \ncanal 9: {votos_canal09}')
elif votos_canal04>= votos_canal05 >= votos_canal09:
    print(f'canal 4: {votos_canal04}\
          \ncanal 5: {votos_canal05}\
          \ncanal 9: {votos_canal09}')
elif votos_canal04>= votos_canal09 >= votos_canal05:
    print(f'canal 4: {votos_canal04}\
          \ncanal 9: {votos_canal09}\
          \ncanal 5: {votos_canal05}')