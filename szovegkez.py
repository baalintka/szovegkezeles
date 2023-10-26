def szepnap():
    szoveg:str = "Szép nap van!"

    print(szoveg[0])

    print(szoveg[1])
    print(len(szoveg))
    print(szoveg[:3])
    print("utolso", szoveg[len(szoveg)-1])

    i:int=0

    while i <len(szoveg):
        print(szoveg[i])
        i+=1

def szovegkezelesek():
    szoveg: str = "Ez egy teszt szöveg"
    print(szoveg.upper())
    if szoveg.find("teszt")=="-1":
        print("nincsen benne")
    else:
        print("van benne")

    print(str(szoveg.index("s"))+". helyen van")
    szoveg.title()
    szoveg.replace("teszt","proba")

def szovegvissza(szoveg:str):
    hossz=len(szoveg) #5
    v=0
    while hossz-1 > v :
        print(hossz)
        print(szoveg[hossz],end="")
        hossz-=1

def a_beutik_szama(szoveg:str):
    szamlalo=0
    i=0
    while i < len(szoveg):
        if szoveg[i] == "a":
            szamlalo+=1
        i+=1
    print(szamlalo)