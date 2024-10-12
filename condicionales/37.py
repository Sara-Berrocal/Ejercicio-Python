def main():
    p, c, f = int(input("Votos Pamela: ")), int(input("Votos Carol: ")), int(input("Votos Fanny: "))
    votos   = {"Pamela": p, "Carol": c, "Fanny": f}
    tvotos  = p+c+f
    votonec = tvotos // 2 + 1

    for candidata, voto in votos.items():
        if voto >= votonec:
            print(f"{candidata} gano la eleccion.")
            return
        
    ranking = sorted(votos.items(), key=lambda x: x[1], reverse=True)
    if ranking[0][1] == ranking [1][1] == ranking[2][1]:
        print("Empate entre las tres, se anula la eleccion.")
    elif ranking[1][1] == ranking[2][1]:
        print("Empate por el segundo lugar, se anula la eleccion.")
    else:
        print(f"Segunda vuelta entre {ranking[0][0]} y {ranking[1][0]}.")

main()