# Forest Waypoint Symbols

Deze repository bevat icoontjes met een bosbeheer thema. Ze zijn geschikt voor gebruik in een Garmin GPS, maar bijvoorbeeld ook voor GIS-programma's. De icoontjes kunnen als 'custom waypoints' op een Garmin GPS apparaat gezet en gebruikt worden. Deze repository bevat de icoontjes in verschillende bestandsformaten die direct in allerlei programma's gebruikt kunnen worden. De Python scripts en andere bestanden zijn daarvoor niet nodig maar helpen bij het genereren van de andere bestandsformaten vanuit de .png versies.

## Overzicht

![overzicht van icoontjes](https://github.com/etiennethomassen/forest-waypoint-symbols/blob/master/grid/grid.png)

## Inhoud repository

De repository bevat de mappen:

- garmin: de bestanden voor de Garmin
- basecamp: de bestanden voor Basecamp
- garmin: de bestanden voor de Garmin
- grid: plaatje met alle symbolen gegenereerd door grid.py
- png: .png bestanden
- pxi: bestanden uit [Pixen](https://pixenapp.com/) waarmee de icoontjes gemaakt zijn
- svg: svg bestanden van dezelfde icoontjes.

Het bestand convert.py is een Python programma dat de bestanden in de map png/ bewerkt en in de mappen _garmin_, _basecamp_ en _svg_ plaatst.

## Bestanden op de GPS plaatsen

De bestanden kunnen op de GPS geplaatst worden door het apparaat met de computer te verbinden en de bestanden in de map _customwaypoints_ te plaatsen (getest met Garmin Oregon 600 en Oregon 700).

## Bestanden in Basecamp gebruiken

Als de bestanden alleen op de GPS staan herkent Basecamp deze niet en verschijnen alleen puntjes op het scherm in plaats van de icoontjes.

De bestanden in de map _basecamp_ moeten naar:

- Windows Vista/7/8 - C:\Users\%USERNAME%\Documents\My Garmin\Custom Waypoint Symbols\
- Windows XP - C:\Documents and Settings\%USERNAME%\My Documents\ My Garmin\Custom Waypoint Symbols\
- Mac OS X - Macintosh HD/Users/%USERNAME%/Library/Application Support/Garmin/Custom Waypoint Symbols/

## convert.py

Het bestand convert.py is een Python programma dat de originele bestanden een achtegrondkleur geeft die de Garmin als doorzichtig weergeeft en daarnaast de juiste namen en nummers toepast voor gebruik op de GPS en in Basecamp. Ook converteert het de .png bestanden naar .svg en plaatst ze in svg/. Python en de PIL module en pixels2svg zijn nodig om het programma te draaien. Zie ook requirements.txt.

## grid.py

Het bestand grid.py maakt een overzichtsplaatje van alle icoontjes

## lijst.csv

Dit bestand geeft een overzicht van de bestandnummers en de oorspronkelijke naam.

## Licentie

[Creative Commons Naamsvermelding 4.0 Internationaal](https://creativecommons.org/licenses/by/4.0/)
