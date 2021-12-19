gifts = [
    'A partridge in a pear tree.',
    'Two turtle doves,',
    'Three French hens,',
    'Four calling birds,',
    'Five gold rings,',
    'Six geese a laying,',
    'Seven swans a swimming,',
    'Eight maids a milking,',
    'Nine ladies dancing,',
    'Ten lords a leaping,',
    'Eleven pipers piping,',
    'Twelve drummers drumming,',
]


def verse(day: int) -> str:
    den = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    start = f'On the {den[day-1]} day of Christmas\nMy true love sent to me\n'
    for day in range(day-1, -1, -1):
        start = f'{start}{gifts[day]}\n'
    return start


def whole_song() -> str:
    for n in range(1, 13):
        print(verse(n))
    return
print(whole_song())


def test_verse():
# <editor-fold defaultstate="collapsed" desc="Tests">
    assert verse(1) == "On the first day of Christmas\nMy true love sent to me\nA partridge in a pear tree.\n"
    assert verse(3) == "On the third day of Christmas\nMy true love sent to me\nThree French hens,\nTwo turtle doves,\nA partridge in a pear tree.\n"
# </editor-fold>
