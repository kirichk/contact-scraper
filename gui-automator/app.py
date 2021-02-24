import pyautogui
import time
import platform
from settings import platform_settings



# text_to_send = pyautogui.prompt(text='Введите текст для рассылки сообщений',
#                       title='Ввод текста',
#                       default='Привет')

def get_names_from_vcf():
    with open('Contacts-A.vcf', mode='r') as vcf:
        data = vcf.read().split('\n')
        result = []
        for item in data:
            if item[:2] == 'FN':
                result.append(item.split(':')[1])
        return result


def sending_funnel(contacts: list):
    print('Program started, you have 5 seconds to open Viber on a fullscreen')
    time.sleep(5)
    for contact in contacts:
        pyautogui.click(SEARCH_FIELD_X, SEARCH_FIELD_Y)
        for letter in contact:
            pyautogui.press(letter)
        time.sleep(2)
        if pyautogui.locateOnScreen(image='windows.png',
                                     region=(TOP_LEFT_CONTACT_FIELD_X,
                                               TOP_LEFT_CONTACT_FIELD_Y,
                                               CONTACT_FIELD_WEIGHT,
                                               CONTACT_FIELD_HEIGHT),
                                     confidence=0.5):
            time.sleep(2)
            pyautogui.click(SEARCH_RESULT_FIELD_X, SEARCH_RESULT_FIELD_Y)
            time.sleep(1)
            pyautogui.click(MESSAGE_FIELD_X, MESSAGE_FIELD_Y)
            pyautogui.write('Test')
            time.sleep(1)
            pyautogui.moveTo(SEND_FIELD_X, SEND_FIELD_Y)
            time.sleep(10)
        else:
            pyautogui.click(CROSS_BUTTON_X, CROSS_BUTTON_Y)
            time.sleep(2)


if __name__ == '__main__':
    locals().update(platform_settings())
    contacts = get_names_from_vcf()
    sending_funnel(contacts)
