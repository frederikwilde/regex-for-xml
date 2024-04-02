# Universal regex-based XML parsing
**Release date: April 1, 2024**

Many experts claim (see answers to this [question](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags) on StackOverflow) that one cannot universally and robustly parse XML using regex.
But as of today (April 1, 2024), using the power of [Python decorators](https://www.youtube.com/watch?v=sEAz0kIRuVA), I am introducing a robust
way of transforming regex-based XML parsers into universal, robust XML parsers.

## Example
Here is a cute little example of a function that uses `re.findall` to find matching patterns
in an XML string.
To make this robust, we attach the `regex_for_xml` decorator and specify by which property we want to
search for elements.
Here we use `find_by="tag"` to search the XML document for elements of a given tag.

```Python
import re
from functools import partial
from decorator import regex_for_xml


@partial(regex_for_xml, find_by="tag")
def findall(pattern, xml):
    """My cool regex-based XML parser."""
    matches = re.findall(pattern, xml)
    return matches
```

The resulting `findall` function has an informative doc-string and returns all matching elements in a list:

```Python
xml_string = """<?xml version="1.0"?>
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

findall('gdppc', xml_string)
# [<Element 'gdppc' at 0x10a252980>, <Element 'gdppc' at 0x10a2521b0>, <Element 'gdppc' at 0x10a253ba0>]
```
_(Example XML data taken from the [Python Docs](https://docs.python.org/3/library/xml.etree.elementtree.html))_

## What the heck?
This is an April fools joke. If you like have a look at the links above, I find them quite entertaining.
That being said, you should probably use a dedicated XML parser and avoid regex parsing if you can.
