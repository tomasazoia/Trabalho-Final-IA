grafo = {
    "Aveiro": {"Porto": 75, "Viseu": 85, "Coimbra": 65, "Leiria": 115},
    "Viseu": {"Guarda": 85, "Porto": 133, "Aveiro": 85, "Coimbra": 96},
    "Braga": {"Viana do Castelo": 48, "Vila Real": 106, "Porto": 53},
    "Bragança": {"Vila Real": 137, "Guarda": 202},
    "Beja": {"Évora": 78, "Faro": 152, "Setúbal": 142},
    "Castelo Branco": {"Coimbra": 159, "Guarda": 106, "Portalegre": 80, "Évora": 203},
    "Coimbra": {"Viseu": 96, "Leiria": 67, "Aveiro": 65, "Castelo Branco": 159},
    "Évora": {"Lisboa": 133, "Santarém": 117, "Portalegre": 131, "Setúbal": 103, "Beja": 78},
    "Faro": {"Setúbal": 249, "Lisboa": 278, "Beja": 152},
    "Guarda": {"Vila Real": 157, "Viseu": 85, "Castelo Branco": 106, "Bragança": 202},
    "Leiria": {"Lisboa": 129, "Santarém": 70, "Coimbra": 67, "Aveiro": 115},
    "Lisboa": {"Santarém": 78, "Setúbal": 50, "Évora": 133, "Leiria": 129},
    "Porto": {"Viana do Castelo": 71, "Vila Real": 116, "Viseu": 133, "Aveiro": 75, "Braga": 53},
    "Vila Real": {"Viseu": 110, "Porto": 116, "Braga": 106, "Guarda": 157, "Bragança": 137},
    "Santarém": {"Lisboa": 78, "Évora": 117, "Leiria": 70},
    "Setúbal": {"Lisboa": 50, "Évora": 103, "Faro": 249, "Beja": 142},
    "Viana do Castelo": {"Braga": 48, "Porto": 71},
    "Portalegre": {"Castelo Branco": 80, "Évora": 131},
}

heuristica_faro = {
    "Aveiro": 366, "Braga": 454, "Bragança": 487, "Beja": 99,
    "Castelo Branco": 280, "Coimbra": 319, "Évora": 157, "Faro": 0,
    "Guarda": 352, "Leiria": 278, "Lisboa": 195, "Portalegre": 228,
    "Porto": 418, "Santarém": 231, "Setúbal": 168,
    "Viana do Castelo": 473, "Vila Real": 429, "Viseu": 363,
}
