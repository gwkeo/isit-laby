import xml.dom.minidom as minidom
import requests

def get_currencies():
    result = []
    url = 'https://www.cbr.ru/scripts/XML_valFull.asp?'
    r = requests.get(url)
    dom = minidom.parseString(r.text)
    dom.normalize()
    node = dom.getElementsByTagName('Item')
    for i in node:
        code_nodes = i.getElementsByTagName('ISO_Char_Code')
        if code_nodes and code_nodes[0].childNodes:
            id = i.getAttribute('ID')
            code = code_nodes[0].childNodes[0].nodeValue
            result.append((id, code))
    return result

def get_currency_value(id):
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.get(url)
    dom = minidom.parseString(r.text)
    node = dom.getElementsByTagName('Valute')
    for i in node:
        if i.getAttribute('ID') == id:
            return i.getElementsByTagName('Value')[0].childNodes[0].nodeValue
    return 0

def get_currency_value_with_interval(id, start, end):
    url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={start}&date_req2={end}&VAL_NM_RQ={id}'
    print(url)
    r = requests.get(url)
    try:
        dom = minidom.parseString(r.text)
    except(e):
        return None
    dom.normalize()
    nodes = dom.getElementsByTagName('Record')
    values = [i.getElementsByTagName('Value')[0].firstChild.nodeValue for i in nodes]
    values = [float(i.replace(',', '.')) for i in values]
    return values