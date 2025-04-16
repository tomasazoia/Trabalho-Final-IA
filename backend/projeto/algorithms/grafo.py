grafo = {
    "Aveiro": {"Porto": 68, "Viseu": 95, "Coimbra": 68},
    "Braga": {"Viana do Castelo": 48, "Vila Real": 106, "Porto": 53},
    "Bragança": {"Vila Real": 137, "Guarda": 202},
    "Beja": {"Évora": 78, "Faro": 152, "Setúbal": 142},
    "Castelo Branco": {"Coimbra": 159, "Guarda": 106, "Portalegre": 80},
    "Coimbra": {"Viseu": 96, "Leiria": 67, "Aveiro": 68, "Castelo Branco": 159},
    "Évora": {"Santarém": 117, "Portalegre": 131, "Setúbal": 103, "Beja": 78},
    "Faro": {"Beja": 152},
    "Guarda": {"Viseu": 85 ,"Bragança": 202, "Castelo Branco": 106},
    "Leiria": {"Lisboa": 129, "Santarém": 70, "Leiria": 67},
    "Lisboa": {"Santarém": 78, "Setúbal": 50},
    "Porto": {"Vila Real": 116, "Viseu": 133, "Braga": 53, "Aveiro": 68}, 
    "Vila Real": {"Viseu": 110, "Braga": 106, "Porto": 116, "Bragança": 137},
    "Viana do Castelo": {"Braga": 48},
    "Viseu": {"Porto": 133,"Vila Real": 110, "Guarda": 85,"Coimbra": 96,"Aveiro": 95},
    "Santarém": {"Lisboa": 78, "Leiria": 70, "Évora": 117},
    "Portalegre": {"Castelo Branco": 80, "Évora": 131},
    "Setúbal": {"Lisboa": 50, "Évora": 103, "Beja": 142},
}

heuristica_faro = {
    "Aveiro": 366, "Braga": 454, "Bragança": 487, "Beja": 99,
    "Castelo Branco": 280, "Coimbra": 319, "Évora": 157, "Faro": 0,
    "Guarda": 352, "Leiria": 278, "Lisboa": 195, "Portalegre": 228,
    "Porto": 418, "Santarém": 231, "Setúbal": 168,
    "Viana do Castelo": 473, "Vila Real": 429, "Viseu": 363,
}
