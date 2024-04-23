def chiffer_rsa(message_clair:str, e:int, n:int):
    liste_message_clair=[]
    liste_ord_message_clair = []
    ascii_message_clair = ""
    for i in range(len(message_clair)):
        lettre = message_clair[i]
        liste_message_clair.append(lettre)
    #print(liste_message_clair)
    for i in range(len(liste_message_clair)):
        liste_ord_message_clair.append(ord(liste_message_clair[i]))
    #print(liste_ord_message_clair)
    for i in range(len(liste_ord_message_clair)):
        ascii_message_clair = ascii_message_clair + str(liste_ord_message_clair[i])
    #print(ascii_message_clair)
    m = int(ascii_message_clair)
    c = (m**e) % n
    return c

def dechiffer_rsa(message_chiffre:int, d:int, n:int):
    c = message_chiffre
    message_clair_ord = 1
    for i in range(d):
        message_clair_ord = (message_clair_ord*c)%n
    return message_clair_ord

def creation_kpr(e, f):
    d = 1
    while True:
        if e*d%f == 1:
            return d
        else:
            d=d+1

def nbr_ord_message_clair(nbr_ord_message_clair):
    message_clair = ""
    liste_ord_message_clair=[]
    nbr_ord_message_clair = str(nbr_ord_message_clair)
    for i in range(len(nbr_ord_message_clair)):
        lettre_ord = nbr_ord_message_clair[i]
        liste_ord_message_clair.append(lettre_ord)
    a = len(nbr_ord_message_clair)/2
    for i in range(int(a)):
        chiffre_1 = liste_ord_message_clair[0]
        chiffre_2 = liste_ord_message_clair[1]
        del(liste_ord_message_clair[0])
        del(liste_ord_message_clair[0])
        nbr = str(chiffre_1)+str(chiffre_2)
        lettre = chr(int(nbr))
        message_clair = message_clair + str(lettre)
    return message_clair

def resfinal(nb):
    message_clair = ""
    nb = str(nb)
    for i in range(len(nb//2)):
        asci = nb[2*i:2*(i+1)]
        lettre = chr(int(asci))
        message_clair = message_clair + lettre
    return message_clair



try:
    p = 6991
    q = 7529
    n = p*q
    f = (p-1)*(q-1)
    e = 23
    d = creation_kpr(e, f)
    print("p = "+str(p))
    print("q = "+str(q))
    print("n = "+str(n))
    print("f = "+str(f))
    print("e = "+str(e))
    print("\nOn choisit e = " +str(e)+" (premier avec f = "+str(f)+") comme exposant de chiffrement")
    print("l'exposant de déchiffrement est d = " +str(d)+", l'inverse de " +str(e)+" modulo "+str(f)+" (en effet ed = " +str(e)+" × "+str(d)+" ≡ 1 mod "+str(f)+").")
    print("\nLa clé publique d'Alice est (n, e) = ("+str(n)+", "+str(e)+"), et sa clé privée est (n, d) = ("+str(n)+", "+str(d)+").")
    message_clair = "RSA"
    message_chiffre = chiffer_rsa(message_clair, e, n)
    print("\nmessage_chiffre   = "+str(message_chiffre))
    message_clair_ord = dechiffer_rsa(message_chiffre, d, n)
    print("message_clair_ord = "+str(message_clair_ord))
    message_clair = nbr_ord_message_clair(message_clair_ord)
    print("message_clair     = "+ str(message_clair))
except:
    print("Une erreur c'est produite...")