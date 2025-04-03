def suite_somme() :
    U = 5
    S = U
    for i in range (0,101) :
        U = U * 7
        S = S + U
    return(S)