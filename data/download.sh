#!/bin/bash
wget -F "http://datigis.comune.fi.it/kml/musei.kmz"
unzip musei.kmz
rm musei.kmz

wget -F "http://datigis.comune.fi.it/kml/luoghi_di_culto_chiesa_cattolica.kmz"

