import pyautogui
import sys
import time
import platform
import pyperclip
import keyboard
from settings import platform_settings


text = 'Привет! Мы рады приветствовать тебя в группе по трудоустройству моряков — TOPCREW. Подписывайся прямо сейчас.'\
'\nhttps://invite.viber.com/?g2=AQBrdQUS4O%2FWW0zpmfDWOkwGAl0bi4HPZ4VwEtaB%2Bn50BN1JDFKu5%2B7lFn0Ng8HX'\
'\nМы поможем тебе найти работу в море абсолютно бесплатно! Это реальный шанс трудоустройства. Мы представляем крупнейшие крюинги по всему миру.'\
'\nХочешь получать вакансии только по своему профилю? Используй нашего бесплатного бота для поиска вакансий  — TOPCREW. '
text_link = 'viber://pa?chatURI=TopCrew'


def paste(text: str):
    buffer = pyperclip.paste()
    pyperclip.copy(text)
    keyboard.press_and_release('ctrl + v')
    pyperclip.copy(buffer)


def get_names_from_vcf():
    with open('contacts.vcf', mode='r') as vcf:
        data = vcf.read().split('\n')
        result = []
        for item in data:
            if item[:2] == 'FN':
                result.append(item.split(':')[1])
        return result


def sending_funnel(contacts: list):
    print('Program started, you have 10 seconds to open Viber on a fullscreen')
    time.sleep(10)
    for contact in contacts:
        pyautogui.click(SEARCH_FIELD_X, SEARCH_FIELD_Y)
        for letter in contact:
            if keyboard.is_pressed('Esc'):
                sys.exit()
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
            pyperclip.copy(text)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            if keyboard.is_pressed('Esc'):
                sys.exit()
            pyautogui.click(SEND_FIELD_X, SEND_FIELD_Y)
            pyautogui.click(SEND_FIELD_LONGER_X, SEND_FIELD_LONGER_Y)
            pyperclip.copy(text_link)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            if keyboard.is_pressed('Esc'):
                sys.exit()
            pyautogui.click(SEND_FIELD_X, SEND_FIELD_Y)
            pyautogui.click(SEND_FIELD_LONGER_X, SEND_FIELD_LONGER_Y)
            time.sleep(5)
            pyautogui.click(CROSS_BUTTON_X, CROSS_BUTTON_Y)
        else:
            if keyboard.is_pressed('Esc'):
                sys.exit()
            pyautogui.click(CROSS_BUTTON_X, CROSS_BUTTON_Y)
            time.sleep(2)


if __name__ == '__main__':
    locals().update(platform_settings())
    contacts = get_names_from_vcf()
    sending_funnel(contacts)
