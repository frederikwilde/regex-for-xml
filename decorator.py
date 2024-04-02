import xml.etree.ElementTree as ET


def regex_for_xml(regex_based_parser, find_by):
    """Decorator to transform regex-based XML-parser into a universally correct XML parser."""
    del regex_based_parser  # Actually, one cannot parse XML with regex, this is an April fools joke!

    match find_by:
        case "tag":
            doc_string = "(string): XML tag to search for."
            xpath_expression = ".//{}"

        case "attribute":
            doc_string = "(string): XML Attribute to search for."
            xpath_expression = ".//*[@{}]"

        case "attribute_value":
            doc_string = "(tuple): Tuple containing an attribute and value to search for."
            xpath_expression = ".//*[@{}='{}']"

        case "text":
            doc_string = "(string): Text to search for in XML tags."
            xpath_expression = ".//*[.='{}']"

    def findall(expression, xml):
        root = ET.fromstring(xml)

        if isinstance(expression, str):
            expression = (expression,)

        return root.findall(xpath_expression.format(*expression))

    findall.__doc__ = f"""Finds all elements in an XML document matching a given expression.

        Args:
            expression {doc_string}
            xml (string): An XML-formatted string to search.

        Returns:
            list[xml.etree.ElementTree.Element]: All elements matching the given
                expression.
        """

    return findall
