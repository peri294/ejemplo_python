print("ingrese una cantidad de segundos: ");
segundos = int(input());
horas = segundos // 3600;
minutos = (segundos % 3600) // 60;
segundos = segundos % 60;
print("horas: ", horas, "minutos: ", minutos, "segundos: ", segundos);