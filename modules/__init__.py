def new_Structure(goals,goals_avoided,assists,diccionario,names):
    name_list= names.split(", ")
    for player in range(len(name_list)):
        estadisticas=[goals[player],goals_avoided[player],assists[player]]
        diccionario[name_list[player]]=estadisticas


def get_Player(name_list, estructura, i):
    return ('Jugador: ', name_list[i] , ' anoto la cantidad de ', estructura[name_list[i]][0] , ' goles.')


def max_Influence(estructura):
    points = [(nombre,float (((estadisticas[0]*1.5) + (estadisticas[1]*1.25) + estadisticas[2])/3)) for nombre,estadisticas in estructura.items()]
    return max(points, key= lambda x:(x[1]))[0]


def get_Average(estructura):
    return (sum(tuple(N[0] for N in tuple(estructura.values())))/25)


def get_player_Average(name,estructura):
    return (estructura[name][0]/25)