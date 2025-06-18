import os
import random

current_path = os.path.dirname(__file__)


def get_random_images() -> list:

    string_list = []

    dates = os.listdir(f"{current_path}/images_base64_url")

    random_date = dates[random.randint(0,len(dates)-1)]
    print(random_date)
    images_url_path = os.listdir(f'{current_path}/images_base64_url/{random_date}')
    for img_file_name in images_url_path:

        with open(f'{current_path}/images_base64_url/{random_date}/{img_file_name}', 'r') as file:

            content = file.read()
            string_list.append(content)

            file.close()

    string_list.append(random_date)
    
    return string_list


def load_contacts() -> list:
    
    string_list = []

    contacts = os.listdir(f"{current_path}/contacts")

    for contact_img in contacts:

        with open(f"{current_path}/contacts/{contact_img}", 'r') as file:

            content = file.read()

            string_list.append(content)

            file.close()
    os.chdir(current_path)
    return string_list