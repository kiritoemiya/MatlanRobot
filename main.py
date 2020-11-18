import queue 

def buatMap():
    map = []
    map.append(["#","#","#","#","O","#","#","#","#","#","#"])
    map.append(["#","W"," ","#"," "," "," "," "," "," ","#"])
    map.append(["#"," "," ","#"," ","#","#","#","#"," ","#"])
    map.append(["#"," "," ","#"," ","#","Z"," ","#"," ","#"])
    map.append(["#"," "," ","#"," ","#"," "," ","#"," ","#"])
    map.append(["#"," ","#","#"," ","#"," ","#","#"," ","#"])
    map.append(["#"," "," "," "," "," "," "," "," "," ","#"])
    map.append(["#","#","#","#"," ","#","#","#","#","#","#"])
    map.append(["#"," "," ","#"," "," "," "," "," "," ","#"])
    map.append(["#"," "," ","#"," ","#"," "," ","Y"," ","#"])
    map.append(["#","X"," "," "," ","#"," "," "," "," ","#"])
    map.append(["#","#","#","#","#","#","#","#","#","#","#"])

    return map

def cetakMap(map, jalur=""):
    for x, posisi in enumerate(map[0]):
        if posisi == "O":
            mulai = x 
    
    h = mulai 
    v = 0
    posisi = set()              #ubah list ke himpunan

    for gerak in jalur:
        if gerak == "L":
            h = h - 1 
        elif gerak =="R":
            h = h + 1 
        elif gerak =="U":
            v = v - 1 
        elif gerak =="D":
            v = v + 1  

        posisi.add((v,h))
    
    for v, baris in enumerate(map):
        for h, kolom in enumerate(baris):
            if(v, h) in posisi:
                print("+", end=" ")
            elif not (v, h) in posisi:
                print(kolom + " ", end="")
            
        print()

def cek(map, pindah):
    for x, posisi in enumerate(map[0]):             #cek posisi di dictionary pada layer 1
        if posisi == "O":
            mulai = x
    
    h = mulai                   #horizontal 
    v = 0                       #vertikal

    for gerak in pindah:
        if gerak == "L":
            h = h - 1 
        elif gerak =="R":
            h = h + 1 
        elif gerak =="U":
            v = v - 1 
        elif gerak =="D":
            v = v + 1
        
        if not(0 <= h < len(map[0]) and 0 <= v < len(map)) :        #cek keluar map / tidak
            return False
        elif (map[v][h] == "#"):                                    #cek nabrak dinding/tidak
            return False 
    
    return True

def cariApi1(map, pindah):
    for x, posisi in enumerate(map[0]):
        if posisi == "O":
            mulai = x

    h = mulai 
    v = 0

    for gerak in pindah: 
        if gerak == "L":
            h = h - 1 
        elif gerak =="R":
            h = h + 1 
        elif gerak =="U":
            v = v - 1 
        elif gerak =="D":
            v = v + 1  

    if map[v][h] == "W":
        print("Langkah: ", pindah)
        cetakMap(map, pindah)
        return True
    
    return False

def cariApi2(map, pindah):
    for x, posisi in enumerate(map[0]):
        if posisi == "O":
            mulai = x

    h = mulai 
    v = 0

    for gerak in pindah: 
        if gerak == "L":
            h = h - 1 
        elif gerak =="R":
            h = h + 1 
        elif gerak =="U":
            v = v - 1 
        elif gerak =="D":
            v = v + 1  

    if map[v][h] == "X":
        print("Langkah: ", pindah)
        cetakMap(map, pindah)
        return True
    
    return False

def cariApi3(map, pindah):
    for x, posisi in enumerate(map[0]):
        if posisi == "O":
            mulai = x

    h = mulai 
    v = 0

    for gerak in pindah: 
        if gerak == "L":
            h = h - 1 
        elif gerak =="R":
            h = h + 1 
        elif gerak =="U":
            v = v - 1 
        elif gerak =="D":
            v = v + 1  

    if map[v][h] == "Y":
        print("Langkah: ", pindah)
        cetakMap(map, pindah)
        return True
    
    return False

def cariApi4(map, pindah):
    for x, posisi in enumerate(map[0]):
        if posisi == "O":
            mulai = x

    h = mulai 
    v = 0

    for gerak in pindah: 
        if gerak == "L":
            h = h - 1 
        elif gerak =="R":
            h = h + 1 
        elif gerak =="U":
            v = v - 1 
        elif gerak =="D":
            v = v + 1  

    if map[v][h] == "Z":
        print("Langkah: ", pindah)
        cetakMap(map, pindah)
        return True
    
    return False

#main
fifo = queue.Queue()
fifo.put("")
langkah = ""
map = buatMap()

#api1
while not cariApi1(map, langkah):
    langkah = fifo.get()
    for y in ["L","R","U","D"]: 
        pindah = langkah + y
        if cek(map, pindah):
            fifo.put(pindah)

#api2
map = buatMap()
while not cariApi2(map, langkah):
    langkah = fifo.get()
    for y in ["L","R","U","D"]: 
        pindah = langkah + y
        if cek(map, pindah):
            fifo.put(pindah)

#api3
map = buatMap()
while not cariApi3(map, langkah):
    langkah = fifo.get()
    for y in ["L","R","U","D"]: 
        pindah = langkah + y
        if cek(map, pindah):
            fifo.put(pindah)

#api4
map = buatMap()
while not cariApi4(map, langkah):
    langkah = fifo.get()
    for y in ["L","R","U","D"]: 
        pindah = langkah + y
        if cek(map, pindah):
            fifo.put(pindah)

    
#for x in range(0,12) :
#    print(map[x],"\n")          #test cetak Peta