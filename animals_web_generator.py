"""
"""
from data_fetcher import fetch_data

def load_html_template(file_path):
  """ Loads the html template file """
  with open(file_path, "r") as html_file:
      text_data = html_file.read()
      return text_data
template_html = load_html_template('animals_template.html')

def write_new_html(file_path, html_data):
    """ Write a html file replacing a html string with html serialized data """
    new_html_template = template_html.replace('__REPLACE_ANIMALS_INFO__', html_data)
    with open(file_path, "w") as new_html:
        new_html.write(new_html_template)
    print("An 'animals.html' file was generated with the information of the animals with the selected skin type.")


def main():
    animal_name = input('Enter a name of an animal: ')
    animals_data = fetch_data(animal_name)
    print(animals_data)

if __name__ == '__main__':
    main()
