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

heuristica_aveiro = {
    "Aveiro": 0, "Braga": 95, "Bragança": 220, "Beja": 320,
    "Castelo Branco": 190, "Coimbra": 65, "Évora": 260, "Faro": 366,
    "Guarda": 120, "Leiria": 90, "Lisboa": 220, "Portalegre": 200,
    "Porto": 68, "Santarém": 180, "Setúbal": 240,
    "Viana do Castelo": 120, "Vila Real": 140, "Viseu": 95,
}

heuristica_braga = {
    "Aveiro": 95, "Braga": 0, "Bragança": 180, "Beja": 370,
    "Castelo Branco": 240, "Coimbra": 150, "Évora": 310, "Faro": 454,
    "Guarda": 170, "Leiria": 160, "Lisboa": 300, "Portalegre": 260,
    "Porto": 53, "Santarém": 250, "Setúbal": 310,
    "Viana do Castelo": 48, "Vila Real": 106, "Viseu": 140,
}

heuristica_braganca = {
    "Aveiro": 220, "Braga": 180, "Bragança": 0, "Beja": 450,
    "Castelo Branco": 280, "Coimbra": 240, "Évora": 390, "Faro": 487,
    "Guarda": 202, "Leiria": 250, "Lisboa": 380, "Portalegre": 300,
    "Porto": 190, "Santarém": 340, "Setúbal": 400,
    "Viana do Castelo": 220, "Vila Real": 137, "Viseu": 210,
}

heuristica_beja = {
    "Aveiro": 320, "Braga": 370, "Bragança": 450, "Beja": 0,
    "Castelo Branco": 230, "Coimbra": 290, "Évora": 78, "Faro": 99,
    "Guarda": 310, "Leiria": 220, "Lisboa": 150, "Portalegre": 210,
    "Porto": 370, "Santarém": 170, "Setúbal": 142,
    "Viana do Castelo": 400, "Vila Real": 380, "Viseu": 320,
}

heuristica_coimbra = {
    "Aveiro": 65, "Braga": 150, "Bragança": 240, "Beja": 290,
    "Castelo Branco": 159, "Coimbra": 0, "Évora": 220, "Faro": 319,
    "Guarda": 140, "Leiria": 67, "Lisboa": 200, "Portalegre": 180,
    "Porto": 120, "Santarém": 160, "Setúbal": 220,
    "Viana do Castelo": 180, "Vila Real": 160, "Viseu": 96,
}

heuristica_porto = {
    "Aveiro": 68, "Braga": 53, "Bragança": 190, "Beja": 370,
    "Castelo Branco": 240, "Coimbra": 120, "Évora": 310, "Faro": 418,
    "Guarda": 170, "Leiria": 160, "Lisboa": 300, "Portalegre": 260,
    "Porto": 0, "Santarém": 250, "Setúbal": 310,
    "Viana do Castelo": 48, "Vila Real": 116, "Viseu": 133,
}

heuristica_castelo_branco = {
    "Aveiro": 190, "Braga": 240, "Bragança": 280, "Beja": 230,
    "Castelo Branco": 0, "Coimbra": 159, "Évora": 180, "Faro": 280,
    "Guarda": 106, "Leiria": 120, "Lisboa": 220, "Portalegre": 80,
    "Porto": 240, "Santarém": 160, "Setúbal": 200,
    "Viana do Castelo": 260, "Vila Real": 190, "Viseu": 140,
}

heuristica_evora = {
    "Aveiro": 260, "Braga": 310, "Bragança": 390, "Beja": 78,
    "Castelo Branco": 180, "Coimbra": 220, "Évora": 0, "Faro": 157,
    "Guarda": 240, "Leiria": 180, "Lisboa": 130, "Portalegre": 131,
    "Porto": 310, "Santarém": 117, "Setúbal": 103,
    "Viana do Castelo": 340, "Vila Real": 300, "Viseu": 220,
}

heuristica_guarda = {
    "Aveiro": 120, "Braga": 170, "Bragança": 202, "Beja": 310,
    "Castelo Branco": 106, "Coimbra": 140, "Évora": 240, "Faro": 352,
    "Guarda": 0, "Leiria": 150, "Lisboa": 250, "Portalegre": 180,
    "Porto": 170, "Santarém": 200, "Setúbal": 260,
    "Viana do Castelo": 200, "Vila Real": 110, "Viseu": 85,
}

heuristica_leiria = {
    "Aveiro": 90, "Braga": 160, "Bragança": 250, "Beja": 220,
    "Castelo Branco": 120, "Coimbra": 67, "Évora": 180, "Faro": 278,
    "Guarda": 150, "Leiria": 0, "Lisboa": 129, "Portalegre": 150,
    "Porto": 160, "Santarém": 70, "Setúbal": 150,
    "Viana do Castelo": 190, "Vila Real": 180, "Viseu": 120,
}

heuristica_lisboa = {
    "Aveiro": 220, "Braga": 300, "Bragança": 380, "Beja": 150,
    "Castelo Branco": 220, "Coimbra": 200, "Évora": 130, "Faro": 195,
    "Guarda": 250, "Leiria": 129, "Lisboa": 0, "Portalegre": 180,
    "Porto": 300, "Santarém": 78, "Setúbal": 50,
    "Viana do Castelo": 330, "Vila Real": 290, "Viseu": 220,
}

heuristica_portalegre = {
    "Aveiro": 200, "Braga": 260, "Bragança": 300, "Beja": 210,
    "Castelo Branco": 80, "Coimbra": 180, "Évora": 131, "Faro": 228,
    "Guarda": 180, "Leiria": 150, "Lisboa": 180, "Portalegre": 0,
    "Porto": 260, "Santarém": 140, "Setúbal": 190,
    "Viana do Castelo": 280, "Vila Real": 220, "Viseu": 160,
}

heuristica_setubal = {
    "Aveiro": 240, "Braga": 310, "Bragança": 400, "Beja": 142,
    "Castelo Branco": 200, "Coimbra": 220, "Évora": 103, "Faro": 168,
    "Guarda": 260, "Leiria": 150, "Lisboa": 50, "Portalegre": 190,
    "Porto": 310, "Santarém": 120, "Setúbal": 0,
    "Viana do Castelo": 350, "Vila Real": 310, "Viseu": 240,
}

heuristica_santarem = {
    "Aveiro": 180, "Braga": 250, "Bragança": 340, "Beja": 170,
    "Castelo Branco": 160, "Coimbra": 160, "Évora": 117, "Faro": 231,
    "Guarda": 200, "Leiria": 70, "Lisboa": 78, "Portalegre": 140,
    "Porto": 250, "Santarém": 0, "Setúbal": 120,
    "Viana do Castelo": 290, "Vila Real": 250, "Viseu": 180,
}

heuristica_viana_do_castelo = {
    "Aveiro": 120, "Braga": 48, "Bragança": 220, "Beja": 400,
    "Castelo Branco": 260, "Coimbra": 180, "Évora": 340, "Faro": 473,
    "Guarda": 200, "Leiria": 190, "Lisboa": 330, "Portalegre": 280,
    "Porto": 48, "Santarém": 290, "Setúbal": 350,
    "Viana do Castelo": 0, "Vila Real": 150, "Viseu": 180,
}

heuristica_vila_real = {
    "Aveiro": 140, "Braga": 106, "Bragança": 137, "Beja": 380,
    "Castelo Branco": 190, "Coimbra": 160, "Évora": 300, "Faro": 429,
    "Guarda": 110, "Leiria": 180, "Lisboa": 290, "Portalegre": 220,
    "Porto": 116, "Santarém": 250, "Setúbal": 310,
    "Viana do Castelo": 150, "Vila Real": 0, "Viseu": 110,
}

heuristica_viseu = {
    "Aveiro": 95, "Braga": 140, "Bragança": 210, "Beja": 320,
    "Castelo Branco": 140, "Coimbra": 96, "Évora": 220, "Faro": 363,
    "Guarda": 85, "Leiria": 120, "Lisboa": 220, "Portalegre": 160,
    "Porto": 133, "Santarém": 180, "Setúbal": 240,
    "Viana do Castelo": 180, "Vila Real": 110, "Viseu": 0,
}

todas_heuristicas = {
    "Faro": heuristica_faro,
    "Aveiro": heuristica_aveiro,
    "Braga": heuristica_braga,
    "Bragança": heuristica_braganca,
    "Beja": heuristica_beja,
    "Castelo Branco": heuristica_castelo_branco,
    "Coimbra": heuristica_coimbra,
    "Évora": heuristica_evora,
    "Guarda": heuristica_guarda,
    "Leiria": heuristica_leiria,
    "Lisboa": heuristica_lisboa,
    "Portalegre": heuristica_portalegre,
    "Setúbal": heuristica_setubal,
    "Santarém": heuristica_santarem,
    "Viana do Castelo": heuristica_viana_do_castelo,
    "Vila Real": heuristica_vila_real,
    "Viseu": heuristica_viseu,
    "Porto": heuristica_porto
}
