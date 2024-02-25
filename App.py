import xml.etree.ElementTree as ET
from Info_tab import info_tab

#INPUT DATA
models_list=[
    "NSO_21_PB_AB_AR_OGO_MI_WI_12902_Model branży arch AB_00", 
    "NSO_21_PB_AB_AR_WYP_MI_WI_12903_Model wypo meblowego AB_00"
]

header_dict={
            "xmlns":"http://standards.buildingsmart.org/IDS", 
            "xmlns:xs":"http://www.w3.org/2001/XMLSchema",
            "xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance",
            "xsi:schemaLocation":"http://standards.buildingsmart.org/IDS"   
            }
    

#MAIN IDS
def model_ids(model_name):
    model_name_splited=model_name.split('_')
   #HEADER
    ids=ET.Element("ids", header_dict)
    # #INFO
    info_tab(model_name, ids)

    specifications=ET.SubElement(ids, "specifications")

    # #IFC BUILDING NAME 
    specification=ET.SubElement(specifications, "specification",
                                {
        "name": "IDS1 " +"IfcBuilding Name",
        "ifcVersion":"IFC2X3",
        "description":"Sprawdzenie czy parametr IfcBuildingName jest zgodna z nazwą pliku",
        "minOccurs":"1",
        "maxOccurs":"1"
        })
    applicability=ET.SubElement(specification, "applicability")
    entity=ET.SubElement(applicability, "entity")
    name=ET.SubElement(entity, "name")
    simpleValue=ET.SubElement(name, "simpleValue")
    simpleValue.text ="IFCBUILDING"

    requirements=ET.SubElement(specification, "requirements")
    requirements_attribute=ET.SubElement(requirements, "attribute")
    requirements_attribute_name=ET.SubElement(requirements_attribute, "name")
    requirements_attribute_name_simpleValue=ET.SubElement(requirements_attribute_name, "simpleValue")
    requirements_attribute_name_simpleValue.text="Name"

    requirements_attribute_value=ET.SubElement(requirements_attribute, "value")
    restriction_base=ET.SubElement(requirements_attribute_value,"xs:restriction", {"base":"xs:string"})
    restriction_pattern=ET.SubElement(restriction_base,"xs:pattern", {"value":model_name_splited[3]})
    
    # Convert the XML structure to a string
    tree = ET.ElementTree(ids)
    tree.write("output.xml", encoding="utf-8", xml_declaration=True)
    xml_str = ET.tostring(ids, encoding='utf8').decode('utf8')
    print(xml_str)

model_ids(models_list[0])

