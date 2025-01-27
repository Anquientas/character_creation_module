"""
Стартовый модуль игры.
Здесь вводится имя персонажа, его игровой класс и проводятся его тренировки.
"""
from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Функция вычисления наносимого урона."""
    if char_class == 'warrior':
        damage: int = 5 + randint(3, 5)
    elif char_class == 'mage':
        damage: int = 5 + randint(5, 10)
    elif char_class == 'healer':
        damage: int = 5 + randint(-3, -1)
    return (f'{char_name} нанёс урон противнику равный {damage}')


def defence(char_name: str, char_class: str) -> str:
    """Функция вычисления блокируемого урона."""
    if char_class == 'warrior':
        block: int = 10 + randint(5, 10)
    elif char_class == 'mage':
        block: int = 10 + randint(-2, 2)
    elif char_class == 'healer':
        block: int = 10 + randint(2, 5)
    return (f'{char_name} блокировал {block} урона')


def special(char_name: str, char_class: str) -> str:
    """Функция определения специального скила и его характеристик."""
    if char_class == 'warrior':
        number: int = 80 + 25
        skill: str = f'«Выносливость {number}»'
    elif char_class == 'mage':
        number: int = 5 + 40
        skill: str = f'«Атака {number}»'
    elif char_class == 'healer':
        number: int = 10 + 30
        skill: str = f'«Защита {number}»'
    return (f'{char_name} применил специальное умение {skill}')


def start_training(char_name: str, char_class: str) -> str:
    """Функция тренировки персонажа."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    elif char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    elif char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        elif cmd == 'defence':
            print(defence(char_name, char_class))
        elif cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Функция именования и выбора игрового класса персонажа."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        elif char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        elif char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
