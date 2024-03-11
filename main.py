import requests
from fetch_url import country_language_dict
command_message = 'Enter command (1: - help; 2 - lang; 3 - city; 4 - exit): '
help_message = ('Command 2(lang) - Enter the country name to get the language.\n'
                'Command 3(city) - Enter the ip address to get the city.\n'
                'Command 4(exit) - Exit the program.')

def process_lang():
    country_name = input('Enter the country name: ')
    country = country_name.title().replace(" ", "")
    try:
        languages = country_language_dict[country]
        language = ", ".join(lang for lang in languages)
        print(language)
    except KeyError:
        print("Country not found.")

def process_city():
    ip_address = input('Enter the ip address: ')
    try:
        url = f"https://ipapi.co/{ip_address.replace(" ", "")}/json/"
        response = requests.get(url)
        data = response.json()
        print(data['city'])
    except KeyError:
        print("Ip address not found.")

def main():
    while True:
        command = input(command_message)
        if command == '1':
            print(help_message)
        elif command == '2':
            process_lang()
        elif command == '3':
            process_city()
        elif command == '4':
            print('Goodbye')
            break
        else:
            print('Unknown command')

if __name__ == '__main__':
    main()
