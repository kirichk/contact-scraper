import pyautogui
import time
import platform
import keyboard
from settings import platform_settings


text1 = 'Привет! Мы рады приветствовать тебя в группе по трудоустройству моряков — '
text2 = 'TOPCREW. '
text3 = 'Подписывайся прямо сейчас.'
text4 = '\nhttps://invite.viber.com/?g2=AQBrdQUS4O%2FWW0zpmfDWOkwGAl0bi4HPZ4VwEtaB%2Bn50BN1JDFKu5%2B7lFn0Ng8HX'
text5 = '\nМы поможем тебе найти работу в море абсолютно бесплатно! Это реальный шанс трудоустройства. Мы представляем крупнейшие крюинги по всему миру.'\
'Хочешь получать вакансии только по своему профилю? Используй нашего бесплатного бота для поиска вакансий  — '
text6 = 'TOPCREW. \nhttps://www.viber.com/topcrew'

def get_names_from_vcf():
    with open('Contact-A(2).vcf', mode='r') as vcf:
        data = vcf.read().split('\n')
        result = []
        for item in data:
            if item[:2] == 'FN':
                result.append(item.split(':')[1])
        return result


def sending_funnel(contacts: list):
    print('Program started, you have 5 seconds to open Viber on a fullscreen')
    time.sleep(10)
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
            pyautogui.hotkey('shift', 'alt')
            pyautogui.hotkey('shift', 'alt')
            pyautogui.write(text1)
            pyautogui.hotkey('shift', 'alt')
            pyautogui.hotkey('shift', 'alt')
            pyautogui.write(text2)
            pyautogui.hotkey('shift', 'alt')
            pyautogui.hotkey('shift', 'alt')
            pyautogui.write(text3)
            pyautogui.hotkey('shift', 'alt')
            pyautogui.hotkey('shift', 'alt')
            pyautogui.write(text4)
            pyautogui.hotkey('shift', 'alt')
            pyautogui.hotkey('shift', 'alt')
            pyautogui.write(text5)
            pyautogui.hotkey('shift', 'alt')
            pyautogui.hotkey('shift', 'alt')
            pyautogui.write(text6)
            time.sleep(1)
            if keyboard.is_pressed('Esc'):
                break
            pyautogui.moveTo(SEND_FIELD_X, SEND_FIELD_Y)
            time.sleep(5)
        else:
            pyautogui.click(CROSS_BUTTON_X, CROSS_BUTTON_Y)
            time.sleep(2)


if __name__ == '__main__':
    locals().update(platform_settings())
    contacts = get_names_from_vcf()
    sending_funnel(contacts)
