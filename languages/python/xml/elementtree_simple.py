# coding: utf-8
import xml.etree.ElementTree as ET

def main():
    countrydata = """<?xml version="1.0"?>
        <data>
            <country name="Liechtenstein">
                <rank updated="yes">2</rank>
                <year>2008</year>
                <gdppc>141100</gdppc>
                <neighbor name="Austria" direction="E"/>
                <neighbor name="Switzerland" direction="W"/>
            </country>
            <country name="Singapore">
                <rank updated="yes">5</rank>
                <year>2011</year>
                <gdppc>59900</gdppc>
                <neighbor name="Malaysia" direction="N"/>
            </country>
            <country name="Panama">
                <rank updated="yes">69</rank>
                <year>2011</year>
                <gdppc>13600</gdppc>
                <neighbor name="Costa Rica" direction="W"/>
                <neighbor name="Colombia" direction="E"/>
            </country>
        </data>"""

    root = ET.fromstring(countrydata)

    # XPath Test
    year = root.find(".//year")
    print(year)
    print(year.text)


    # Top-level elements
    print(root.findall("."))

    # All 'neighbor' grand-children of 'country' children of the top-level
    # elements
    print(root.findall("./country/neighbor"))

    # Nodes with name='Singapore' that have a 'year' child
    print(root.findall(".//year/..[@name='Singapore']"))

    # 'year' nodes that are children of nodes with name='Singapore'
    print(root.findall(".//*[@name='Singapore']/year"))

    # All 'neighbor' nodes that are the second child of their parent
    print(root.findall(".//neighbor[2]"))

if __name__ == '__main__':
    main()
