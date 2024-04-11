def new_Structure(names,goals,goals_avoided,assists,diccionario):
    name_list= names.split(", ")
    estadisticas=[]
    for player in range(len(name_list)):
        estadisticas=[goals[player],goals_avoided[player],assists[player]]
        diccionario[name_list[player]]=estadisticas


def get_Player(name_list, estructura, i):
    N = estructura[name_list[i]][0]   # Variable que guarda los goles, es innecesaria pero ayuda a la claridad
    return ('Jugador: ', name_list[i] , ' anoto la cantidad de ', N , ' goles.')


def max_Influence(name_list,estructura):
    min = [-1,'ZZZ']
    for i in range(len(name_list)):
        N = estructura[name_list[i]][0] * 1.5
        N += estructura[name_list[i]][1] * 1.25
        N += estructura[name_list[i]][2]
        if (N > min[0]):
            min = [N,name_list[i]]  
    return (min[1])


def get_Average(name_list,estructura):
    total = 0
    for i in range(len(name_list)):
        total += estructura[name_list[i]][0]
    return total / 25


def get_player_Average(name,estructura):
    return (estructura[name][0]/25)