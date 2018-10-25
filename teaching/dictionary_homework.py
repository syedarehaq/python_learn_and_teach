# -*- coding: utf-8 -*-
mexico_cases_male_female_by_state_2015_2017 = {"Aguascalientes":{2015:{"male":0,"female":0},2016:{"male":0,"female":1}, 2017:{"male":0,"female":0}},
"Baja California":{2015:{"male":0,"female":0},2016:{"male":0,"female":0}, 2017:{"male":2,"female":2}},
"Baja California Sur":{2015:{"male":0,"female":0},2016:{"male":3,"female":20}, 2017:{"male":9,"female":15}},
"Campeche":{2015:{"male":0,"female":0},2016:{"male":10,"female":76}, 2017:{"male":0,"female":2}},
"Coahuila":{2015:{"male":0,"female":0},2016:{"male":21,"female":37}, 2017:{"male":37,"female":236}},
"Colima":{2015:{"male":0,"female":0},2016:{"male":25,"female":252}, 2017:{"male":2,"female":1}},
"Chiapas":{2015:{"male":6,"female":4},2016:{"male":98,"female":661}, 2017:{"male":0,"female":4}},
"Chihuahua":{2015:{"male":0,"female":0},2016:{"male":0,"female":0}, 2017:{"male":0,"female":0}},
"Distrito Federal":{2015:{"male":0,"female":0},2016:{"male":0,"female":0}, 2017:{"male":0,"female":0}},
"Durango":{2015:{"male":0,"female":0},2016:{"male":0,"female":0}, 2017:{"male":0,"female":2}},
"Guanajuato":{2015:{"male":0,"female":0},2016:{"male":0,"female":0}, 2017:{"male":0,"female":0}},
"Guerrero":{2015:{"male":0,"female":0},2016:{"male":142,"female":657}, 2017:{"male":5,"female":19}},
"Hidalgo":{2015:{"male":0,"female":0},2016:{"male":19,"female":171}, 2017:{"male":25,"female":60}},
"Jalisco":{2015:{"male":1,"female":0},2016:{"male":17,"female":63}, 2017:{"male":75,"female":260}},
"México":{2015:{"male":0,"female":0},2016:{"male":0,"female":0}, 2017:{"male":12,"female":14}},
"Michoacán":{2015:{"male":0,"female":0},2016:{"male":12,"female":49}, 2017:{"male":1,"female":5}},
"Morelos":{2015:{"male":0,"female":0},2016:{"male":27,"female":242}, 2017:{"male":14,"female":173}},
"Nayarit":{2015:{"male":0,"female":0},2016:{"male":15,"female":24}, 2017:{"male":80,"female":523}},
"Nuevo León":{2015:{"male":2,"female":2},2016:{"male":75,"female":705}, 2017:{"male":5,"female":96}},
"Oaxaca":{2015:{"male":0,"female":0},2016:{"male":94,"female":394}, 2017:{"male":2,"female":3}},
"Puebla":{2015:{"male":0,"female":0},2016:{"male":13,"female":80}, 2017:{"male":14,"female":93}},
"Querétaro":{2015:{"male":0,"female":0},2016:{"male":0,"female":0}, 2017:{"male":4,"female":13}},
"Quintana Roo":{2015:{"male":0,"female":0},2016:{"male":15,"female":348}, 2017:{"male":2,"female":6}},
"San Luis Potosí":{2015:{"male":0,"female":0},2016:{"male":6,"female":25}, 2017:{"male":34,"female":449}},
"Sinaloa":{2015:{"male":0,"female":0},2016:{"male":7,"female":50}, 2017:{"male":24,"female":80}},
"Sonora":{2015:{"male":0,"female":0},2016:{"male":8,"female":16}, 2017:{"male":13,"female":47}},
"Tabasco":{2015:{"male":0,"female":0},2016:{"male":28,"female":277}, 2017:{"male":3,"female":10}},
"Tamaulipas":{2015:{"male":0,"female":0},2016:{"male":13,"female":84}, 2017:{"male":16,"female":620}},
"Tlaxcala":{2015:{"male":0,"female":0},2016:{"male":0,"female":0}, 2017:{"male":0,"female":0}},
"Veracruz":{2015:{"male":0,"female":0},2016:{"male":316,"female":1543}, 2017:{"male":39,"female":94}},
"Yucatán":{2015:{"male":0,"female":0},2016:{"male":108,"female":712}, 2017:{"male":3,"female":12}},
"Zacatecas":{2015:{"male":0,"female":0},2016:{"male":0,"female":1}, 2017:{"male":0,"female":0}}}

## Create a dictionary where for each state we can get the total number of cases there were.

## solution:
mexico_state_level_total_surv_cases_2015_2017 = {mexico_state_name_to_gleam_state_id[state_name]: sum([sum(v.values()) for v in year_male_female_cases.values()]) for state_name, year_male_female_cases in  mexico_cases_male_female_by_state_2015_2017.items()}
