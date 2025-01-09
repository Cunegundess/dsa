from typing import List


def filter_cities(cities_list: List[str], prefixes_list: List[str]):
    results: List[str] = []

    for c in cities_list:
        city_split = c.split(" ")
        city_first_term = city_split[0]

        for p in prefixes_list:
            if p in city_first_term:
                results.append(c)

    return results


cities = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Salvador",
    "Fortaleza",
    "Curitiba",
    "Manaus",
    "Brasília",
    "Recife",
    "Porto Alegre",
    "Belém",
    "Goiânia",
    "Campinas",
    "São Luís",
    "Maceió",
    "Natal",
    "João Pessoa",
    "Cuiabá",
    "Aracaju",
    "Teresina",
]

prefixes = [
    "São",
    "Rio",
    "Belo",
    "Salva",
    "Fort",
    "Cur",
    "Man",
    "Bra",
    "Rec",
    "Port",
    "Bel",
    "Goi",
    "Camp",
    "João",
    "Natal",
    "Arac",
    "Cui",
    "Teres",
    "Flor",
    "Vit",
]

print(filter_cities(cities, prefixes))
