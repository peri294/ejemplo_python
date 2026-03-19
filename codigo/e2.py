print("ingrese una cantidad de segundos: ");
segundos = int(input());
minutos = segundos / 60;
horas = minutos / 60;
dias = horas / 24;
segundos = segundos % 60;
print(horas, "horas");
print(minutos, "minutos");
print(segundos, "segundos");