import xml.etree.ElementTree as ET


def find_xml_strings(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    heading_list = []

    def search_and_collect(element, accumulated_title=''):
        current_sec_type = None
        # Handle 'sec' elements and capture 'sec-type' attribute
        if element.tag == 'sec':
            # Extract title if present
            title_elements = [sub_element.text for sub_element in element if sub_element.tag == 'title' and sub_element.text]
            if title_elements:
                accumulated_title = ' > '.join([accumulated_title] + ['sec'] + title_elements) if accumulated_title else title_elements[0]  
            # Capture 'sec-type' if it exists
            current_sec_type = element.attrib.get('sec-type')
            # Assure that the title tags appear after the <sec> tag
            current_title = f"{accumulated_title}" if accumulated_title else element.tag
        else:
            # Construct the hierarchical title for all other elements
            current_title = f"{accumulated_title} > {element.tag}" if accumulated_title else element.tag
        # Append to list
        heading_list.append((element.tag, current_title, current_sec_type))
        # Recursively process child elements
        for child in element:
            search_and_collect(child, current_title)
    search_and_collect(root)

    return heading_list

