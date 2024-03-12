import requests, os
from fetch_url import country_language_dict
api_key = os.environ.get("IP_API_KEY")
command_message = 'Enter message (help; LanguageOf <countryName>; IpToCity <IP>; exit): '
help_message = ('Command LanguageOf - Enter the country name to get the language;\n'
                'Command IpToCity - Enter the ip address to get the city;\n'
                'Command exit - Exit the program.')

def process_lang(country_name):
    try:
        languages = country_language_dict[country_name]
        language = ", ".join(lang for lang in languages)
        print(language)
    except KeyError:
        print("Country not found.")

def process_city(ip_address):
    try:
        # url = f"https://api.2ip.ua/geo.json?ip={ip_address}"
        url = f"https://api.ip2location.io/?key={api_key}&ip={ip_address}"
        response = requests.get(url)
        data = response.json()
        print(data['city_name'])
    except KeyError:
        print("Ip address not found.")

def main():
    while True:
        message = input(command_message).strip()
        command_value = message.split(' ', 1)
        command = command_value[0].lower()
        value = command_value[1].title().replace(" ", "") if len(command_value) > 1 else None
        if command == 'help':
            print(help_message)
        elif command == 'languageof':
            process_lang(value)
        elif command == 'iptocity':
            process_city(value)
        elif command == 'exit':
            print('Exiting the program...')
            break
        else:
            print('Unknown command.')

if __name__ == '__main__':
    main()
