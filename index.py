from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

SWAPI_URL = 'https://swapi.py4e.com/api/'
categories = ["people", "planets", "vehicles", "starships", "films", "species"]

def name_strip(name_list):
    print(name_list)
    list_of_names = []
    for film in name_list:
        name_call = requests.get(film)
        name_data = json.loads(name_call.content)
        try:
            name_title = name_data["name"]
        except KeyError:
            name_title = name_data["title"]
        else:
            name_title = name_data["name"]
        list_of_names.append(name_title)
    return list_of_names


@app.route('/', methods=['GET', 'POST'])
def swapi_search():
    display_info = 'Nothing to display yet!'
    if request.method == 'GET':
        category = request.args.get('info_categories')
        category_index = request.args.get('index')
        response = requests.get(f"{SWAPI_URL}{category}/{category_index}")
        if response:
            info = json.loads(response.content)
            match category:
                case "people":
                    """This is just for homeworld because homeworld breaks trying to use the name stripper function."""
                    home = json.loads(requests.get(info["homeworld"]).content)

                    name = f'Name: {info["name"]}'
                    height = f'Height: {info["height"]}'
                    weight = f'Weight: {info["mass"]}'
                    hair_colour = f'Hair colour: {info["hair_color"]}'
                    eye_colour = f'Eye colour: {info["eye_color"]}'
                    birth_year = f'Birth year: {info["birth_year"]}'
                    gender = f'Gender: {info["gender"]}'
                    homeworld = f'Homeworld: {home["name"]}'
                    films = f'Films: {", ".join(name_strip(info["films"]))}'
                    species = f'Species: {", ".join(name_strip(info["species"]))}'
                    vehicles = f'Vehicles: {", ".join(name_strip(info["vehicles"]))}'
                    starships = f'Starships: {", ".join(name_strip(info["starships"]))}'

                    display_info = [name, height, weight, hair_colour, eye_colour, birth_year, gender, homeworld, films, species, vehicles, starships]
                    pass
                case "planets":
                    name = f'Name: {info["name"]}'
                    rotation = f'Rotation period: {info["rotation_period"]}'
                    orbital = f'Orbital rotation: {info["orbital_period"]}'
                    diameter = f'Diameter: {info["diameter"]}'
                    climate = f'Climate: {info["climate"]}'
                    gravity = f'Gravity: {info["gravity"]}'
                    terrain = f'Terrain: {info["terrain"]}'
                    surface_water = f'Surface water: {info["surface_water"]}'
                    population = f'Population: {info["population"]}'
                    residents = f'Residents: {", ".join(name_strip(info["residents"]))}'
                    films = f'Films: {", ".join(name_strip(info["films"]))}'

                    display_info = [name, rotation, orbital, diameter, climate, gravity, terrain, surface_water, population, residents, films]
                    pass
                case "vehicles":
                    name = f'Name: {info["name"]}'
                    model = f'Model: {info["model"]}'
                    manufacturer = f'Manufacturer: {info["manufacturer"]}'
                    cost_in_credits = f'Cost in credits: {info["cost_in_credits"]}'
                    length = f'Length: {info["length"]}'
                    max_atmosphering_speed = f'Max atmosphering speed: {info["max_atmosphering_speed"]}'
                    crew = f'Crew: {info["crew"]}'
                    passengers = f'Passengers: {info["passengers"]}'
                    cargo_capacity = f'Cargo capacity: {info["cargo_capacity"]}'
                    consumables = f'Consumables: {info["consumables"]}'
                    vehicle_class = f'Vehicle class: {info["vehicle_class"]}'
                    pilots = f'Pilots: {", ".join(name_strip(info["pilots"]))}'
                    films = f'Films: {", ".join(name_strip(info["films"]))}'

                    display_info = [name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, vehicle_class, pilots, films]
                    pass
                case "starships":
                    name = f'Name: {info["name"]}'
                    model = f'Model: {info["model"]}'
                    manufacturer = f'Manufacturer: {info["manufacturer"]}'
                    cost_in_credits = f'Cost in credits: {info["cost_in_credits"]}'
                    length = f'Length: {info["length"]}'
                    max_atmosphering_speed = f'Max atmosphering speed: {info["max_atmosphering_speed"]}'
                    crew = f'Crew: {info["crew"]}'
                    passengers = f'Passengers: {info["passengers"]}'
                    cargo_capacity = f'Cargo capacity: {info["cargo_capacity"]}'
                    consumables = f'Consumables: {info["consumables"]}'
                    hyperdrive_rating = f'Hyperdrive rating: {info["hyperdrive_rating"]}'
                    starship_class = f'Starship class: {info["starship_class"]}'
                    pilots = f'Pilots: {", ".join(name_strip(info["pilots"]))}'
                    films = f'Films: {", ".join(name_strip(info["films"]))}'

                    display_info = [name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, hyperdrive_rating, starship_class, pilots, films]
                    pass
                case "films":
                    title = f'Title: {info["title"]}'
                    episode_id = f'Episode: {info["episode_id"]}'
                    opening_crawl = f'Opening crawl: {info["opening_crawl"]}'
                    director = f'Director: {info["director"]}'
                    producer = f'Producer: {info["producer"]}'
                    release_date = f'Release date: {info["release_date"]}'
                    characters = f'Characters: {", ".join(name_strip(info["characters"]))}'
                    planets = f'Planets: {", ".join(name_strip(info["planets"]))}'
                    starships = f'starships: {", ".join(name_strip(info["starships"]))}'
                    vehicles = f'Vehicles: {", ".join(name_strip(info["vehicles"]))}'
                    species = f'Species: {", ".join(name_strip(info["species"]))}'

                    display_info = [title, episode_id, opening_crawl, director, producer, release_date, characters, planets, starships, vehicles, species]
                    pass
                case "species":
                    home = json.loads(requests.get(info["homeworld"]).content)

                    name = f'Name: {info["name"]}'
                    classification = f'Classification: {info["classification"]}'
                    designation = f'Designation: {info["designation"]}'
                    average_height = f'Average height: {info["average_height"]}'
                    skin_colors = f'Skin colour: {info["skin_colors"]}'
                    hair_colours = f'Hair colours: {info["hair_colors"]}'
                    eye_colours = f'Eye colour: {info["eye_colors"]}'
                    average_lifespan = f'Average lifespan: {info["average_lifespan"]}'
                    homeworld = f'Homeworld: {home["name"]}'
                    language = f'Language: {info["language"]}'
                    people = f'People: {", ".join(name_strip(info["people"]))}'
                    films = f'Films: {", ".join(name_strip(info["films"]))}'

                    display_info = [name, classification, designation, average_height, skin_colors, hair_colours, eye_colours, average_lifespan, language, people, films]
                    pass
                case _:
                    pass

        context = {
            'display_info': display_info
        }

    return render_template("index.html", **context)




if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)