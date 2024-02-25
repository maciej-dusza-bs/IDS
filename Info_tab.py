import xml.etree.ElementTree as ET
import datetime

def info_tab(model_name, ids):

    # INFO TAB
    # model_name_splited=model_name.split("_")
    info = ET.SubElement(ids, "info")
    
    title = ET.SubElement(info, "title")
    title.text = "NSO Wrocław IDS-1, sprawdzenie modelu"+model_name
    
    copyright = ET.SubElement(info, "copyright")
    copyright.text = "md.bimsolutions@gmail.com"

    version = ET.SubElement(info, "version")
    version.text = "1.0 - sprawdzenie PB"

    description = ET.SubElement(info, "description")
    description.text = "Lvel 1 - Sprawdzenie wykonywane dla każdego modelu"

    author = ET.SubElement(info, "author")
    author.text = "md.bimsolutions@gmai.com"

    date = ET.SubElement(info, "date")
    date.text = str(datetime.date.today())

    purpose = ET.SubElement(info, "purpose")
    purpose.text = "Sprawdzenie nadania poprawnie danych o budynku oraz przedrostkach symboli komponentów powiązanych z branżą."
