segundos_str = input("Por favor, entre com o numero de sgundos que voce deseja converter:")
total_segs = int(segundos_str)

dias = total_segs //86400
segs_restantes1 = total_segs % 86400
horas = segs_restantes1 //3600
segs_restantes = total_segs % 3600
minutos = segs_restantes //60
segs_restantes_final = segs_restantes %60

print(dias, "dias,", horas, "horas,", minutos, "minutos e ", segs_restantes_final, "segundos.")
