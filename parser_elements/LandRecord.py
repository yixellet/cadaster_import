from xml.etree.ElementTree import Element

from .ParserElements import ParserElements as PE

class LandRecord():
    """
    Инструмент для извлечения информации об отдельном земельном участке
    """

    OBJECT_TYPE = 'lands'

    def __init__(self, root_element: Element) -> None:
        self.root_element = root_element
        self.land_record = {
            'content': self.OBJECT_TYPE
        }
    
    def parse(self):
        """
        record_info
        object
        apartment_building
        cad_links
        params
        address_location
        cad_works
        zones_and_boundaries
        survey_boundaries
        natural_objects
        government_land_supervision
        cost
        object_parts
        restrictions_encumbrances
        contours_location
        special_notes
        """
        self.land_record.update(PE.parse_record_info(self.root_element.find('record_info')))
