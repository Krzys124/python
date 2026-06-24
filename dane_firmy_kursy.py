firmy = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7","Firma 8"]
Kurs_akcji_wczoraj = [16.48, 25.24,57.23,37.92,99.59,94.39,91.56,100.0]  
Kurs_akcji_dzis    = [16.71,25.64 ,57.11, 38.16, 99.14, 94.52, 91.11,110.0]

gdzie_jestem=__name__

if gdzie_jestem=="__main__":

    ile_firm=len(firmy)
    print(f"do analizy jest: {ile_firm} firma/firm.")
    print(gdzie_jestem)