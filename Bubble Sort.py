#bubble sort

def ordenaçao_animes(animes):
    n = len(animes)
    for i in range(n):
        for j in range(0, n-i-1):
            if animes[j][1] < animes[j+1][1]:
                animes[j], animes[j+1] = animes[j+1], animes[j]
    return animes

animes = [("Naruto", 8.5), ("Attack on Titan", 9.2), ("One Piece", 9.0), ("My Hero Academy", 8.8)]
animes_ordem = ordenaçao_animes(animes)

print("Animes ordenados pela classificaçao: ")
for anime in animes_ordem:
    print(f"{anime[0]}: {anime[1]}")
          