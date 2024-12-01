from django import template

register = template.Library()

@register.filter
def to_arabic(num):
    ar_num = '۰١٢٣٤٥٦٧٨٩'
    en_num = '0123456789'

    table = str.maketrans(en_num, ar_num)
    num = str(num)
    return num.translate(table)