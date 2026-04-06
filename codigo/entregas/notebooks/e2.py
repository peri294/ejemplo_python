playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

minutos = 0
segundos = 0
minMax = -1
segMax = -1
segMin = 61
minMin = 61
for cancion in playlist:
    tiempo = cancion['duration'].split(':')
    minutos += int(tiempo[0])
    segundos += int(tiempo[1])
    if (int(tiempo[0]) > minMax):
        minMax = int(tiempo[0])
        segMax = int(tiempo[1])
        cancionMax = cancion['title']
    elif(int(tiempo[0]) == minMax and int(tiempo[1]) > segMax):
        segMax = int(tiempo[1])
        cancionMax = cancion['title']
    elif(int(tiempo[0])<minMin):
        minMin = int(tiempo[0])
        segMin = int(tiempo[1])
        cancionMin = cancion['title']
    elif(int(tiempo[0]==minMin and int(tiempo[1])<segMin)):
        segMin = int(tiempo[1])
        cancionMin = cancion['title']

resto = segundos // 60
minutos+=resto
segundos = segundos % 60
print('minutos: ',minutos,' segundos: ',segundos)
print('Canción más larga: ',cancionMax, minMax,':',segMax)
print('Canción más corta: ',cancionMin, minMin,':',segMin)
