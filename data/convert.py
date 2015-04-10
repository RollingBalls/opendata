#!/usr/bin/env python
import xml.etree.ElementTree as ET
import re

def parsekml1(fn):
    ns = {
        "kml": "http://www.opengis.net/kml/2.2",
    }
    tree = ET.parse(open(fn))
    root = tree.getroot()
    for pm in root[0].findall("kml:Placemark", ns):
        desc = pm.find("kml:description", ns).text
        nome = re.compile(r"NOME.*?span class.*?>(.*?)</span").search(desc, re.MULTILINE).group(1)
        try:
            telefono = re.compile(r"TELEFONO.*?span class.*?>(.*?)</span").search(desc, re.MULTILINE).group(1)
        except:
            telefono = ""
        try:
            indirizzo = re.compile(r"INDIRIZZO.*?span class.*?>(.*?)</span").search(desc, re.MULTILINE).group(1)
        except:
            indirizzo = ""

        point = pm.find("kml:Point", ns)
        coord = point.find("kml:coordinates", ns)
        lon,lat = coord.text.split(",")
        lon = lon.replace(".", ",")
        lat = lat.replace(".", ",")

        print "%s\t%s\t%s\t%s\t%s" % (nome.title(), lon, lat, indirizzo, telefono)

def parsekml2(fn):
    ns = {
        "kml": "http://www.opengis.net/kml/2.2",
    }
    tree = ET.parse(open(fn))
    root = tree.getroot()
    for pm in root[0][0].findall("kml:Placemark", ns):
        name = pm.find("kml:name", ns).text
        desc = pm.find("kml:description", ns).text
        point = pm.find("kml:Point", ns)
        coord = point.find("kml:coordinates", ns)
        coords = coord.text.split(",")

        try:
            indirizzo = re.compile(r"Accesso da:.*?span.*?>(.*?)</span").search(desc, re.MULTILINE).group(1)
        except:
            indirizzo = ""
        try:
            telefono = re.compile(r"Tel:.*?span.*?>(.*?)</span").search(desc, re.MULTILINE).group(1)
        except:
            telefono = ""

        lon = coords[0].replace(".", ",")
        lat = coords[1].replace(".", ",")
        print "%s\t%s\t%s\t%s\t%s" % (name.title().encode("utf-8"), lon, lat, indirizzo.encode("utf-8"), telefono.encode("utf-8"))

# parsekml1("turismo-musei.kml")
parsekml2("luoghi_di_culto_chiesa_cattolica.kml")
