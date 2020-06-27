#5th Edition Character Creator Config Manager
#Shourthanis
#Version 1.0.0

import json
from tkinter import *
import xlrd

classData = [{}]*1

#open excel config file
chart = xlrd.open_workbook("5eCCconfigData.xlsx")

#read races to list of dicts
sheet = chart.sheet_by_index(0)
rows = sheet.nrows
raceData = []
for x in range (0, rows-1):
    raceData.append({})
    raceData[x]['name'] = sheet.cell_value(x+1,0)
    raceData[x]['ageMinimum'] = sheet.cell_value(x+1,7)
    raceData[x]['ageMaximum'] = sheet.cell_value(x+1,8)
    raceData[x]['heightAvg'] = sheet.cell_value(x+1,9)
    raceData[x]['sizeClass'] = sheet.cell_value(x+1,10)
    raceData[x]['speedBase'] = sheet.cell_value(x+1,11)
    if not (sheet.cell_type(x+1, 12) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        raceData[x]['proficiencySkillSave'] = sheet.cell_value(x+1,12)
    if not (sheet.cell_type(x+1, 13) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        raceData[x]['proficiencyArmsArmor'] = sheet.cell_value(x+1,13)
    if not (sheet.cell_type(x+1, 14) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        raceData[x]['proficiencyTools'] = sheet.cell_value(x+1,14)
    if not (sheet.cell_type(x+1, 15) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        raceData[x]['languages'] = sheet.cell_value(x+1,15)
    if not (sheet.cell_type(x+1, 16) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        raceData[x]['extras'] = sheet.cell_value(x+1,16)
    raceData[x]['abilityBonus'] = [0]*6
    for y in range (0, 6):
        if not (sheet.cell_type(x+1, y+1) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
            raceData[x]['abilityBonus'][y] = int(sheet.cell_value(x+1,y+1))
#read subraces to list of races
sheet = chart.sheet_by_index(1)
rows = sheet.nrows
for x in range (0, rows-1):
    for y in range (0, len(raceData)):
        if sheet.cell_value(x+1,1) == raceData[y]['name']:
            if not 'subrace' in raceData[y]: raceData[y]['subrace'] = []
            raceData[y]['subrace'].append({})
            place = len(raceData[y]['subrace'])-1
            raceData[y]['subrace'][place]['name'] = sheet.cell_value(x+1,0)
            if not (sheet.cell_type(x+1, 8) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
                raceData[y]['subrace'][place]['proficiencySkillSave'] = sheet.cell_value(x+1,8)
            if not (sheet.cell_type(x+1, 9) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
                raceData[y]['subrace'][place]['proficiencyArmsArmor'] = sheet.cell_value(x+1,9)
            if not (sheet.cell_type(x+1, 10) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
                raceData[y]['subrace'][place]['proficiencyTools'] = sheet.cell_value(x+1,10)
            if not (sheet.cell_type(x+1, 11) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
                raceData[y]['subrace'][place]['languages'] = sheet.cell_value(x+1,11)
            if not (sheet.cell_type(x+1, 12) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
                raceData[y]['subrace'][place]['extras'] = sheet.cell_value(x+1,12)
            raceData[y]['subrace'][place]['abilityBonus'] = [0]*6
            for z in range (0, 6):
                if not (sheet.cell_type(x+1, z+2) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
                    raceData[y]['subrace'][place]['abilityBonus'][z] = int(sheet.cell_value(x+1,z+2))
with open("Races.json", "w") as outfile:
    json.dump(raceData, outfile, indent=2)

#read classes to list of dicts
sheet = chart.sheet_by_index(2)
rows = sheet.nrows
classData = []
for x in range (0, rows-1):
    classData.append({})
    classData[x]['name'] = sheet.cell_value(x+1,0)
    classData[x]['hitDie'] = int(sheet.cell_value(x+1,1))
    classData[x]['proficiencySkillSave'] = sheet.cell_value(x+1,2)
    if not (sheet.cell_type(x+1, 3) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        classData[x]['proficiencyArmsArmor'] = sheet.cell_value(x+1,3)
    if not (sheet.cell_type(x+1, 4) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        classData[x]['proficiencyTools'] = sheet.cell_value(x+1,4)
    if not (sheet.cell_type(x+1, 5) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        classData[x]['languages'] = sheet.cell_value(x+1,5)
    for y in range (0, 20):
        if not (sheet.cell_type(x+1, 6+y) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
            classData[x][('lvl' + str(y+1))] = sheet.cell_value(x+1,6+y)
#read subclasses to list of classes
sheet = chart.sheet_by_index(3)
rows = sheet.nrows
for x in range (0, rows-1):
    for y in range (0, len(classData)):
        if sheet.cell_value(x+1,1) == classData[y]['name']:
            if not 'subClass' in classData[y]: classData[y]['subClass'] = []
            classData[y]['subClass'].append({})
            place = len(classData[y]['subClass'])-1
            classData[y]['subClass'][place]['name'] = sheet.cell_value(x+1,0)
            for z in range (0, 20):
                if not (sheet.cell_type(x+1, z+2) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
                    classData[y]['subClass'][place][('lvl' + str(z+1))] = sheet.cell_value(x+1,z+2)
#read spell slot data into list of classes
sheet = chart.sheet_by_index(4)
rows = sheet.nrows
group = 1
while group <= rows:
    if not (sheet.cell_type(group, 1) == (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        for y in range (0, len(classData)):
            if sheet.cell_value(group,1) == classData[y]['name']:
                if not (sheet.cell_type(group, 2) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
                    classData[y]['cantripsKnown'] = [0]*20
                    for x in range (0, 20):
                        classData[y]['cantripsKnown'][x] = int(sheet.cell_value(group + x, 2))
                if not (sheet.cell_type(group, 3) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
                    classData[y]['spellsKnown'] = [0]*20
                    for x in range (0, 20):
                        classData[y]['spellsKnown'][x] = int(sheet.cell_value(group + x, 3))
                classData[y]['spellSlots'] = [0]*9
                for z in range (0, 9):
                    classData[y]['spellSlots'][z] = [0]*20
                    for x in range (0, 20):
                        classData[y]['spellSlots'][z][x] = int(sheet.cell_value(group + x, 4 + z))
    group += 21
with open("Classes.json", "w") as outfile:
    json.dump(classData, outfile, indent=2)

#read backgrounds to list of dicts
sheet = chart.sheet_by_index(5)
rows = sheet.nrows
backgroundData = []
for x in range (0, rows-1):
    backgroundData.append({})
    backgroundData[x]['name'] = sheet.cell_value(x+1,0)
    backgroundData[x]['feature'] = sheet.cell_value(x+1,1)
    if not (sheet.cell_type(x+1, 2) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        backgroundData[x]['proficiencySkillSave'] = sheet.cell_value(x+1,2)
    if not (sheet.cell_type(x+1, 3) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        backgroundData[x]['proficiencyArmsArmor'] = sheet.cell_value(x+1,3)
    if not (sheet.cell_type(x+1, 4) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        backgroundData[x]['proficiencyTools'] = sheet.cell_value(x+1,4)
    if not (sheet.cell_type(x+1, 5) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        backgroundData[x]['languages'] = sheet.cell_value(x+1,5)
    if not (sheet.cell_type(x+1, 6) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
        backgroundData[x]['extras'] = sheet.cell_value(x+1,6)
with open("Backgrounds.json", "w") as outfile:
    json.dump(backgroundData, outfile, indent=2, sort_keys=True)
