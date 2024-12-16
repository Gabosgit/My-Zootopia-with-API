"""
    Obtaining animal types and information by giving an animal name
"""
from data_fetcher import fetch_data


def load_html_template(file_path):
  """ Loads the html template file """
  with open(file_path, "r") as html_file:
      text_data = html_file.read()
      return text_data
template_html = load_html_template('animals_template.html')


def serialize_info_animals(list_animal_types):
    """ Serializes data to be written in html format. Return de html in a variable 'output'"""
    output = str()
    for animal_type in list_animal_types:
        print(animal_type)
        output += f'<li class="cards__item">\n'
        output += f'\t<div class="card__title">{animal_type["name"]}</div>\n'

        output += f'\t<h3>Locations:</h3>\n'
        output += f'\t<ul class="card__text info_list">\n'
        locations = animal_type['locations']
        for location in locations:
            output += f'\t\t<li>{location}</li>\n'
        output += f'\t</ul>\n'

        output += f'\t<h3>Characteristics:</h3>\n'
        output += f'\t<ul class="card__text info_list">\n'
        characteristics = animal_type['characteristics']
        for key, value in characteristics.items():
            output += f'\t\t<li><strong>{key}:</strong> {value}</li>\n'
        output += f'\t</ul>\n'
        output += f'</li>\n\n'

    return output


def write_new_html(file_path, html_data):
    """ Write a html file replacing a html string with html serialized data """
    new_html_template = template_html.replace('__REPLACE_ANIMALS_INFO__', html_data)
    with open(file_path, "w") as new_html:
        new_html.write(new_html_template)
    print("An 'animals.html' file was generated with the information of the animals with the selected skin type.")


def main():
    """ The user enters an animal name in the terminal.
        The animal information is obtained from the API.
        The obtained data is serialized to write it in html.
        A html file is generated to display the data in a browser.
    """
    animal_name = input('Enter a name of an animal: ')
    list_animal_types = fetch_data(animal_name)
    html_data = serialize_info_animals(list_animal_types)
    write_new_html('animals.html', html_data)


if __name__ == '__main__':
    main()
