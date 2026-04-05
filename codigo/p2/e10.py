rounds = [
{
'theme': 'Entrada',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Santiago': {'judge_1': 6, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 8},
}
},
{
'theme': 'Plato principal',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Mateo': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Camila': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Lucía': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
}
},
{
'theme': 'Postre',
'scores': {
'Valentina': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Mateo': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Santiago': {'judge_1': 7, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
}
},
{
'theme': 'Cocina internacional',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 9,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Santiago': {'judge_1': 8, 'judge_2': 9,
'judge_3': 7},
'Lucía': {'judge_1': 7, 'judge_2': 7,
'judge_3': 8},
}
},
{
'theme': 'Final libre',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 8,
'judge_3': 9},
'Mateo': {'judge_1': 8, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 7, 'judge_2': 7,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 7},
}
}
]
estadisticas = {}
for participantes in rounds[0]["scores"]:
    estadisticas[participantes] ={
        "total": 0,
        "rondas ganadas": 0,
        "mejor ronda": 0
    }
for round in rounds:
    print(f"\n -- ronda: {round['theme']} --")
    puntaje_ronda = {} #temporal

    for participantes,jueces in round['scores'].items():
        puntajeTotal = sum(jueces.values())
        puntaje_ronda[participantes] = puntajeTotal
        #actualiza los datos
        estadisticas[participantes]["total"] += puntajeTotal
        estadisticas[participantes]["mejor ronda"] = max(estadisticas[participantes]["mejor ronda"], puntajeTotal)
        #determina el ganador de la ronda
        ganador = max(puntaje_ronda, key=puntaje_ronda.get)
        estadisticas[ganador]["rondas ganadas"] += 1
        print(f"ganado de la ronda: {ganador}")
        orden = sorted(puntaje_ronda.items(),key=lambda x: x[1], reverse=True)
        print("posiciones:")
        for nombre,puntos in orden:
            print(f"{nombre}: {puntos}")

print("\n tabla final.. \n")

for jugador in estadisticas:
    estadisticas[jugador]["promedio"] = estadisticas[jugador]["total"] / len(rounds)

ordenFinal = sorted(estadisticas.items(), key=lambda x: x[1]["total"], reverse=True)
for nombre,datos in ordenFinal:
    print(f"{nombre} | total: {datos["total"]} | "
    f"rondas ganadas: {datos["rondas ganadas"]} | "
    f"mejor ronda: {datos["mejor ronda"]} | "
    f"promedio: {datos["promedio"]:.2f}")
