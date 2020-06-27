5E Character Creator
Shourthanis
Version 1.0.0

-----
Goal
-----
This program is designed more to be used as a way for mainly GMs to quickly make character file with all the important informaion on scores and abilities. It is uesable by players, but it may not have all the options that are traditionally available.
The output file of this program is a word document containing all of the selected information for the generated character, though it is reletively unformatted at this time. It is suggested that after character creation, the character file is opened an cleaned up in what ever fasion you desire before use.

------
Legal
------
Due to copywrites, only the classes, races, backgrounds, and all sub options for these from the 5E SRD are provided. It is possible to add any of these to the program. Instructions will be below.

This program and files are free to use and modify by whomever wants to, just make sure to credit the original creator.

--------------------
Running the Creator
--------------------
Open 5eCharacterCreator.exe

1. Enter the character name. The name entered for the character will be the name of the output file.
2. Select the Level Mode. Set will take the value of the level slider as the charaster level. If the level is set, only class abilities up to that level, and only the spell slots of that level will be put into the output file. If the mode is set to Map, or is left unused, all level abilities and the full spell slot table will bet put into the output file.
3. Select a race from the dropdown. To see the proporties of the selected race, click the Info button next to the box.
-- If the race has a subrace, select one. To see the proorties of the selected subrace, click the Info button next to the box.
4. Enter an age for the character. The appropriate age range for the selected race will be shown. To generate a random age within the expected range, click the Random button next to Generate Age.
5. The average height for the selected race will be given. This can be modified up or down by up to 12 inches using the slider. Below the slider, the Generate button will provide a random height modifier.
6. Input the ability scores for the character using the labeled boxes. Three options to generate a set of random values are provided.
7. Select a class from the dropdown. To se the proporties of the selected class, click the Info button next to the box. If the class is a spellcaster, it will be noted, and the spell slots by level can be seen by clicking the Slots button.
-- If the class has a subclass, select one. To see the proporties of the selected subclass, click the Info button next to the box.
8. Generate the health for the character using one of the three provided options. Roll will randomly generate values based on the selected class hit die, Average will give the average value of the hit die, and Max will give the maximum based on the hit die.
-- If the level is set (step 2), only the health of the selected level will be shown. If the level mode is Map, the healths for all levels will be shown.
9. Select a background from the dropdown. To see the proporties of the selected background, click the Info button.

Note: Steps 1, 2, 3, 7, and 9 may be done in any order.
      Steps 4, and 5 should follow step 3.
      It is advised to complete step 6 after step 3, though it is not strictly necessary.
      Step 8 should follow steps 3, 6, and 7.

10. To enable the character for export to the output file, click the Check button at the bottom of the window. This makes sure that all fields have been filled, in order to prevent any errors.
11. Click the export button. All information will be put into a Word file in the same folder as the program titled with the name of the character.

---------------------------------------
Adding Classes, Races, and Backgrounds
---------------------------------------
To add options to the program, the relevant information can be added to the proviede xcel file (5eCCconfigData.xls).
All data for one option should be on the same line in the appropriate sheet. The top line is only labels for the data and is skipped by the program.
Modifying or adding spell slot data for classes should not be necessary, but if the establised pattern is followed, it should work. This is more complicated than the rest of the data, and is honestly not advised.

Some fields are required by the program. These requirements are given below. Other fields may be left blank if not used.
-Race: Name, minimum age, maximum age, average height, size, base speed
-Subrace: Name, base(race it is a subrace for, case sensitive)
-Class: Name, hit die, skill/saves proficiencies
-Subclass: Name, base(class it is a subclass for, case sensitive)
-Background: Name, feature

After any desired options are added to the excel file, save and close it, and run 5eCCconfigManager.exe. This will transfer the data in the excel file to the three .json files used by the character creator.
