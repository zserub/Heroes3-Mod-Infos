# 9. MISCELLANEOUS

## STARTING RESOURCES & BONUSES

The amount of resources and gold that all players start with depends on the chosen difficulty level (NOT
the difficulty level of the map itself, which has no effect on gameplay). The higher the difficulty, the
fewer resources that human players begin with and the more that all AI players begin with, as so:

	HUMAN PLAYER	Wood	Ore	Merc	Sulf	Crys	Gems	Gold
	----------------------------------------------------------------------
	Easy		278170	278178	278174	27817C	278180	278184	278188
	Normal		27818C	278194	278190	278198	27819C	2781A0	2781A4
	Hard		2781A8	2781B0	2781AC	2781B4	2781B8	2781BC	2781C0
	Expert		2781C4	2781CC	2781C8	2781D0	2781D4	2781D8	2781DC
	Impossiburu	2781E0	2781E8	2781E4	2781EC	2781F0	2781F4	2781F8

	AI PLAYER	Wood	Ore	Merc	Sulf	Crys	Gems	Gold
	----------------------------------------------------------------------
	Easy		2781FC	278204	278200	278208	27820C	278210	278214
	Normal		278218	27821C	278220	278224	278228	27822C	278230
	Hard		278234	27823C	278238	278240	278244	278248	27824C
	Expert		278250	278258	278254	27825C	278260	278264	278268
	Impossiburu	27826C	278274	278270	278278	27827C	278280	278284

-----------------------------------------------------------------------------------------

As for the starting bonuses, the random treasure artifact is usually the clear winner since the gold and
resource bonuses are so insignificant. Let's look at the gold bonus first: a paltry 500~1000 extra gold
to start out with. We start by getting a random value between 5 (0C0002) and 10 (0BFFFD), which we then
multiply by 25 (0C000B~10) and then double twice (0C0016 = 02), effectively multiplying it by 100.
Bearing this in mind, you can easily raise the bonus by adjusting the values at 0C0002 and 0BFFFD.

If you wish to set the starting gold bonus to a static value, we can simplify the code somewhat:

      ------------	-------------------------------------------------------------------------
      0BFFFC~C0005	; STARTING GOLD BONUS TO A STATIC VALUE
      ------------	-------------------------------------------------------------------------
      8B 45 14	mov eax,[ebp+14]	; (displaced code)
      BA C4 09 00 00	mov edx,09C4		; EDX = gold bonus (09C4 = 2,500)
      EB 11		jmp 4C0017		; (0C0006~16 is free space)

>The starting resource bonuses depend on the chosen faction and are set via a DWORD pointer table:

| Town        | Address   | Resources                    |
|-------------|-----------|------------------------------|
| Castle      | 0C01B4    | AF FF 4B 00 (Wood & Ore)     |
| Rampart     | 0C01B8    | D6 FF 4B 00 (Crystal)        |
| Tower       | 0C01BC    | E1 FF 4B 00 (Gems)           |
| Inferno     | 0C01C0    | EC FF 4B 00 (Mercury)        |
| Necropolis  | 0C01C4    | AF FF 4B 00 (Wood & Ore)     |
| Dungeon     | 0C01C8    | F4 FF 4B 00 (Sulfur)         |
| Stronghold  | 0C01CC    | AF FF 4B 00 (Wood & Ore)     |
| Fortress    | 0C01D0    | AF FF 4B 00 (Wood & Ore)     |
| Conflux     | 0C01D4    | EC FF 4B 00 (Mercury)        |


If desired, you can have the rare resource bonuses also include wood and ore bonuses by changing 0BFFDC
to EB D1 90 90 90 (Crystals), 0BFFE7 to EB C6 90 90 90 (Gems), 0BFFF2 to EB BB (Mercury), and 0BFFFA to
EB B3 (Sulfur). If you wish to just get rid of the wood and ore bonus, it will free up 0BFFAF~D5.

Note that you'll also need to edit ScnrStar.def from the h3sprite.lod archive to reflect any changes you
make to this table. Rather than having its own image, Conflux is set to use the same graphic as Inferno
at 18E062, 182BD5, 1698E5. You can change this value to that of another faction or, to give Conflux a
unique resource bonus (see below), change them to 0B and add a new image to the end of ScnrStar.def.

      ---------	-------------------------------------------------------------------------
      0BFFAF~C5	; CONFLUX RESOURCE BONUS TO RANDOM RARE RESOURCE (OVERWRITES WOOD & ORE)
      ---------	-------------------------------------------------------------------------
      50		push eax		; store EAX
      6A 01		push 01			; minimum = 1 (Rampart)
      6A 04		push 04			; maximum = 4 (Necropolis)
      5A		pop edx			; ""
      59		pop ecx			; ""
      E8 05C80400	call 50C7C0		; (EAX = min~max)
      83 F8 04	cmp eax,04		; Necropolis?
      75 01		jne 4BFFC1		; if no -> ECX = faction to copy
      40		inc eax			; Necropolis -> Dungeon
      8B C8		mov ecx,eax		; ECX = faction to copy
      58		pop eax			; retrieve EAX
      EB E2		jmp 4BFFA8		; -> [resource bonus] (0BFFC6~D5 is free space)

      0C01D4 > AF ; sets Conflux bonus exit pointer to above routine (former Wood & Ore bonus)

The minimum and maximum values for the resource bonuses are specified at the following addresses:

			   WOOD & ORE      RARE RESOURCES
			----------------	----------------
			0BFFB5 (Min: 05)	0BFF8C (Min: 03)
			0BFFB0 (Max: 0A)	0BFF87 (Max: 06)

Again, if we want to set the starting bonuses to static values, the code gets much simpler:

      ---------	-------------------------------------------------------------------------
      0BFFAF~B3	; STARTING WOOD & ORE RESOURCE BONUS TO STATIC VALUE
      ---------	-------------------------------------------------------------------------
      6A XX		push XX			; EAX = resource bonus
      58		pop eax			; ""
      EB 0A		jmp 4BFFBE		; (0BFFB4~D is free space)

      --------	-------------------------------------------------------------------------
      0BFF86~A	; STARTING RARE RESOURCE BONUS TO STATIC VALUE
      --------	-------------------------------------------------------------------------
      6A XX		push XX			; EAX = resource bonus
      58		pop eax			; ""
      EB 0A		jmp 4BFF95		; (0BFF8B~94 is free space)

>the odds of each player's starting town having its second-level built are set at 1C1062.

---------------------------------------------------------------------------------------------------------

## INTERFACE IMPROVEMENTS

There are several things we can do to improve the game cosmetically, such as the spellbook overhaul from
earlier. One of the very first things you may notice when electing to start a new (non-campaign) game is
that the "new game" screen defaults to a functionless background that requires you to click on a button
to pull up the list of maps rather than simply defaulting to that list. To set the list of maps as the
default page, change 17C92F to 75 and 17C92C to 66. Further, since there's no reason to ever pull this
background up in the first place, we can disable toggling to it with repeated button clicks by changing
180D54 (map list), 1801A1 (random map), and 181424 (advanced options) all to EB.

We can further improve the behavior of this screen to better fit how players will use it. Specifically,
"advanced options" is an important part of the game setup and so calling it that and making it a small,
out-of-the-way button is not a good design choice. What we can do about this is make double-clicking a
map bring you to the advanced options screen instead of simply beginning the game. Next, we'll make the
"back" button return you to the map selection screen you came from (standard or random) instead of the
main menu when clicked from the advanced options screen. Finally, the only reason to click "Begin" from
the map selection screen without going to advanced options is to play with all random settings, but this
doesn't work because the game will default you to the first human-playable color instead of choosing one
at random. We can fix this by randomizing the human player's color (in addition to everything else) if
"Begin" is clicked from the map selection screen instead of from the advanced options screen.

All of the above edits except for the double-click change will require some free space. The space we'll
be using in the below examples will come from removing the "map size" text next to the size filters on
the standard map selection screen. We'll also look at how to remove the filters themselves in addition
to the above changes and simply have a large "choose a standard map" header in their place.

      ---------	-------------------------------------------------------------------------
      187623~31	; DOUBLE-CLICKING A MAP CALLS ADVANCED OPTIONS INSTEAD OF STARTING GAME
      ---------	-------------------------------------------------------------------------
      E8 A89DFFFF	call 5813D0		; call "advanced options" screen
      E9 BEF9FFFF	jmp 586FEB		; ""
      90 90 90 90 90	nop			; -

      18761B = 90 01 ; timeframe for double-click (400ms)

      ----------	-------------------------------------------------------------------------
      1848AA~90F	; RANDOMIZE COLOR FROM MAP SELECTION SCREEN (OVERWRITES MAP SIZE TEXT)
      ----------	-------------------------------------------------------------------------
      8B 35 24FE6900	mov esi,[69FE24]	; shifted code
      89 75 F4	mov [ebp-0C],esi	; ""
      E9 87000000	jmp 58493F		; frees space: 1848B8~93E

      80BB7C03000001	cmp byte [ebx+37C],01	; did we click "Begin" from advanced options?
      74 4A		je 58490B		; if yes -> [begin game]

      A1 38956900	mov eax,[699538]	; EAX = main index
      8D B8 6CF80100	lea edi,[eax+1F86C]	; EDI = map data
      31 C0		xor eax,eax		; EAX = 0
      31 D2		xor edx,edx		; EDX = 0
      81 C7 A0000000	add edi,A0		; EDI = team 1
      57		push edi		; store EDI

      80 3F 01	cmp byte [edi],01	; is this team human-playable?
      75 01		jne 5848DD		; if no -> EAX +1
      42		inc edx			; EDX +1 (total number of human-playable teams)
      40		inc eax			; EAX +1
      83 C7 44	add edi,44		; EDI = next team
      83 F8 07	cmp eax,07		; have we checked all 8 teams?
      7E F1		jle 5848D7		; if no -> human-playable?

      6A 01		push 01			; ECX = 1
      59		pop ecx			; ""
      E8 D27EF8FF	call 50C7C0		; EAX = ECX~EDX
      5F		pop edi			; EDI = team 1
      31 C9		xor ecx,ecx		; ECX = 0
      31 D2		xor edx,edx		; EDX = 0

      80 3F 01	cmp byte [edi],01	; is this team human-playable?
      75 01		jne 5848F9		; if no -> EDX +1
      41		inc ecx			; ECX +1
      42		inc edx			; EDX +1
      83 C7 44	add edi,44		; EDI = next team
      39 C1		cmp ecx,eax		; have we found the (EAX)th human-playable team?
      75 F2		jne 5848F3		; if no -> human-playable?

      4A		dec edx			; EDX -1 (this is our randomly-selected team)
      8D BB 64100000	lea edi,[ebx+1064]	; EDI = player index
      89 57 70 	mov [edi+70],edx	; update human player's team
      E9 7B200000	jmp 58698B		; -> [begin game] (184910~3E is free space)

      187AE4 > B8 48	; update jump pointer

      ---------	-------------------------------------------------------------------------
      184910~2E	; BACK TO MAP SELECTION FROM ADVANCED OPTIONS (OVERWRITES MAP SIZE TEXT)
      ---------	-------------------------------------------------------------------------
      80BB7C03000001	cmp byte [ebx+37C],01	; was "Back" clicked from advanced options?
      0F85 22200000	jne 58693F		; if no -> [Main Menu]
      80BB7F03000001	cmp byte [ebx+37F],01	; random map?
      0F84 F0260000	je 58701A		; if yes -> [Random Map Selection]
      E9 DB260000	jmp 58700A		; -> [Standard Maps] (18492F~3E is free space)

      187AE8 > 10 49	; update jump pointer

As for removing the map filters entirely, we'll need to get our hands a little dirtier with some graphic
editing. The first task is to dummy out the buttons (ScALBut.def, ScSMBut.def, ScMDBut.def, ScLGBut.def,
and ScXLBut.def from h3sprite.lod) by fully covering each individual image with the transparent (cyan)
color. The more difficult task is to edit ScSelBck.bmp from "_HD3_Data\Common" to increase the size of
the small text window (like in the advanced options screen) to accommodate the new, larger header text.
Once that's been done, we'll head back into the .exe file and make the following changes:

      187ACC > B0	; disables "S" filter
      187AD0 > B0	; disables "M" filter
      187AD4 > B0	; disables "L" filter
      187AD8 > B0	; disables "XL" filter
      187ADC > B0	; disables "All" filter	(187994~AF is free space)

      17A481 > 240B66	; large header font
      17A487 > 3C	; Y position
      17A490 > 1E	; X position

By default, the standard map selection menu will load sorted primarily by map version, then by map name.
We can change the default primary sort column at 183320 with the following values:

			00 = Map Name
			01 = Map Size
			02 = Map Version (original setting)
			03 = # of Players
			04 = Victory Condition
			05 = Loss Condition

-----------------------------------------------------------------------------------------

There's also the credits button, which we can disable by setting 0F0630~1 to BF EE (for left click) and
0FBFFE~004 to 31 C0 E9 58 01 00 00. This may seem more nitpicky, but the main reason we're doing this is
to free up some space (0EF7AD~82C) for a few other things. HD Mod converts the "fort" icon on the lower
left of the town screen to a shortcut which allows you to recruit from all of that town's dwellings at
once rather than needing to go to each one individually. Using the space we just freed up, let's convert
the icon next to it (the town icon) into a shortcut to the build menu, thus putting the two most common
things you'll be doing in any town you visit in one place that's the same regardless of what type it is.

      ---------	-------------------------------------------------------------------------
      1D386A~F	; ADD SHORTCUT BUTTON TO TOWN HALL
      ---------	-------------------------------------------------------------------------
      E9 3EBFF1FF	jmp 4EF7AD		; -> free space (credits)
      90		nop			; -

      ---------	-------------------------------------------------------------------------
      0EF7AD~C9	; (EXPANDED SPACE - OVERWRITES CREDITS)
      ---------	-------------------------------------------------------------------------
      83 C0 F6	add eax,-0A		; displaced code
      83 F8 02	cmp eax,02		; left click?
      75 0D		jne 4EF7C2		; if no -> right click?

      817E089E000000	cmp [esi+08],9E		; clicked on town hall icon?
      0F84 A4410E00	je 5D3966		; if yes -> [build menu]

      83 F8 04 	cmp eax,04		; right click?
      E9 A6400E00	jmp 5D3870		; return (0EF7CA~82C is free space)

Next, let's look at few minor annoyances alongside a legitimate display bug. There are four war machine
slots on the hero screen, three of which (2~4) are grouped together with a fourth (1) off to the side.
One would expect the odd slot out to be reserved for the one war machine which every hero comes with and
can never take off, except it isn't. We can change this by setting both 0DE114 and 1AFA9A to 0D, 0D8BDF
to 95, and then editing ArTraits.txt to stick the catapult in slot 1 instead of 4. To keep everything in
a sensible order, we then move the ballista, ammo cart, and tent to slots 2, 3, and 4, respectively.

Secondly, there's the kingdom overview screen. It displays the artifacts equipped by your heroes in a
particularly nonsensical order: Helm, Cloak, Neck, Weapon, Shield, Armor, L Ring, R Ring, Legs. It also
fails to display the contents of the fifth Miscellaneous slot entirely since that slot was added by the
SoD expansion and this screen was never updated to compensate. The below code will change the equipped
artifact display order to be more intuitive (Weapon, Shield, Helm, Armor, Cloak, Legs, Neck, L/R Rings),
as well as display the fifth Miscellaneous slot in place of war machine 1.

      ------		-------------------------------------------------------------------------
      51E439		; KINGDOM OVERVIEW ARTIFACT REARRANGEMENT
      ------		-------------------------------------------------------------------------
      E8 8C13FDFF	call 4EF7CA		; -> free space (credits)
      90 90		nop			; -

      ------		-------------------------------------------------------------------------
      51F56D		; KINGDOM OVERVIEW ARTIFACT REARRANGEMENT (RIGHT CLICK)
      ------		-------------------------------------------------------------------------
      E8 6502FDFF	call 4EF7D7		; -> free space (credits)
      90 90		nop			; -

      ----------	-------------------------------------------------------------------------
      4EF7CA~82C	; (EXPANDED SPACE - OVERWRITES CREDITS)
      ----------	-------------------------------------------------------------------------
      E8 15000000	call 4EF7E4		; swap positions
      8BBCD02D010000	mov edi,[eax+edx*8+12D]	; displaced code
      C3		ret			; return

      E8 08000000	call 004EF7E4		; swap positions
      8B84D62D010000	mov eax,[esi+edx*8+12D]	; displaced code
      C3		ret			; return

      83 FA 00	cmp edx,00		; Helm -> Weapon (+3)
      74 35		je 4EF81E		; ""
      83 FA 01	cmp edx,01		; Cloak -> Shield (+3)
      74 30		je 4EF81E		; ""
      83 FA 02	cmp edx,02		; Neck -> Helm (-2)
      74 31		je 4EF824		; ""
      83 FA 03	cmp edx,03		; Weapon -> Armor (+2)
      74 27		je 4EF81F		; ""
      83 FA 04	cmp edx,04		; Shield -> Cloak (-3)
      74 26		je 4EF823		; ""
      83 FA 05	cmp edx,05		; Armor -> Legs (+3)
      74 1C		je 4EF81E		; ""
      83 FA 06	cmp edx,06		; L Ring -> Neck (-4)
      74 1B		je 4EF822		; ""
      83 FA 07	cmp edx,07		; R Ring -> L Ring (-1)
      74 19		je 4EF825		; ""
      83 FA 08	cmp edx,08		; Legs -> L Ring (-1)
      74 14		je 4EF825		; ""
      83 FA 0D	cmp edx,0D		; War Machine 1 -> Misc (+5)
      74 06		je 4EF81C		; ""
      83 FA 11	cmp edx,11		; Spell Book -> War Machine 1 (-4)
      74 07		je 4EF822
      C3		ret			; return

      42		inc edx			; +5
      42		inc edx			; +4
      42		inc edx			; +3
      42		inc edx			; +2
      42		inc edx			; +1
      C3		ret			; return

      4A		dec edx			; -4
      4A		dec edx			; -3
      4A		dec edx			; -2
      4A		dec edx			; -1
      C3		ret			; return
      90		nop			; -

We replace war machine 1 instead of 4 (the catapult) as an aesthetic choice: we want the one war machine
that's different from the other three to be in the place on the hero screen that's set apart from them.
We learned earlier how to make Catapults buyable from town blacksmiths instead of coming pre-equipped on
all heroes, which will allow you to arrange the slots of war machines in ArTraits.txt as desired. If you
aren't interested in that and wish only to move the pre-equipped catapult to slot 1, set 0D8BDF to 95.

That said, while there's no reason to display the catapult on the Kingdom Overview screen if every hero
comes pre-equipped with one, there is some validity to it if we they're buyable. To that end, we replace
the spell book on the far right side of the Kingdom Overview screen with war machine 1. Regardless of if
you've changed mage guilds to sell spells individually, there's little reason in having might heroes not
start out with a spell book. Even so, it's still easily the least important thing to show here.

-----------------------------------------------------------------------------------------

Finally, let's tackle what is in my opinion the most obnoxious and pervasive display issue of all: the
fact that the two "common" resources (wood & ore) are not properly grouped together on the main display.
The free space we'll be using will come from removing something else I don't much care for: the cycling
display on the hero/town status window on the bottom right of the main adventure screen. Setting 009F46
to EB 53 will cause it to continue displaying the hero/town status when clicked and free up 009F48~9A.

      --------	-------------------------------------------------------------------------
      1591A7~D	; SWAP ORE AND MERCURY VALUES ON MAIN INTERFACE
      --------	-------------------------------------------------------------------------
      E8 9C0DEBFF	call 409F48		; -> free space (hero/town status window)
      90 90		nop			; -

      ---------	-------------------------------------------------------------------------
      009F48~6B	; (EXPANDED SPACE - OVERWRITES HERO/TOWN STATUS WINDOW)
      ---------	-------------------------------------------------------------------------
      83 F8 01	cmp eax,01		; Slot 2?
      74 0E		je 409F5B		; if yes -> ECX = ore value

      83 F8 02	cmp eax,02		; Slot 3?
      74 12		je 409F64		; if yes -> ECX = mercury value

      8B8C839C000000	mov ecx,[ebx+eax*4+9C]	; ECX = resource value (everything else)
      EB 10		jmp 409F6B		; -> return

      8B8C83A0000000	mov ecx,[ebx+eax*4+A0]	; ECX = ore value
      EB 07		jmp 409F6B		; -> return

      8B8C8398000000	mov ecx,[ebx+eax*4+98]	; ECX = mercury value
      C3		ret			; return

      --------	-------------------------------------------------------------------------
      11F0D2~6	; SWAP ORE AND MERCURY MINE COUNT ON KINGDOM OVERVIEW
      --------	-------------------------------------------------------------------------
      E8 95AEEEFF	call 409F6C		; -> free space (status window)

      ---------	-------------------------------------------------------------------------
      009F6C~7D	; (EXPANDED SPACE - OVERWRITES HERO/TOWN STATUS WINDOW)
      ---------	-------------------------------------------------------------------------
      8A 5D E6	mov bl,[ebp-1A]		; BL = mercury lab count
      8A 7D E5	mov bh,[ebp-1B]		; BH = ore put count
      88 7D E6	mov [ebp-1A],bh		; mercury lab -> ore pit
      88 5D E5	mov [ebp-1B],bl		; ore pit -> mercury lab
      BB 28746900	mov ebx,00697428	; (displaced code)
      C3		ret			; return

      --------	-------------------------------------------------------------------------
      121A49~F	; SWAP ORE AND MERCURY MINE HOVER TEXT ON KINGDOM OVERVIEW
      --------	-------------------------------------------------------------------------
      E8 3085EEFF	call 409F7E		; -> free space
      90 90		nop			; -

      ---------	-------------------------------------------------------------------------
      009F7E~92	; (EXPANDED SPACE - OVERWRITES HERO/TOWN STATUS WINDOW)
      ---------	-------------------------------------------------------------------------
      83 F8 1E	cmp eax,1E		; Slot 2?
      74 07		je 409F8A		; if yes -> (mercury lab -> ore pit)
      83 F8 1F 	cmp eax,1F		; Slot 3?
      75 03		jne 409F8B		; if no -> EDI = mine graphic

      48		dec eax			; (ore pit -> mercury lab)
      48		dec eax			; ""
      40		inc eax			; (mercury lab -> ore pit)

      8B3C85C4746A00	mov edi,[eax*4+6A74C4]	; EDI = mine graphic
      C3		ret			; return (009F93~A is free space)

To finish the swap, we'll also need to make several edits to some other files. We'll need to swap the
positions of mercury and ore in both GenrlTxt.txt and Help.txt (but NOT MineNames.txt or ResTypes.txt).
We'll also need to swap the order of the two mine graphics in OvMines.def. Finally, we'll need to edit
the following resource bar graphics in "_HD3_Data\Common" to swap the positions of mercury and ore:

			aresbar_l.bmp		HD_kRes4.bmp
			aresbar2_l.bmp		HD_kResB.bmp

---------------------------------------------------------------------------------------------------------

## PLAYER COLORS

To change player colors, you'll need to swap ALL of the pointers listed below:

      28A324:	00 C2 68 00 = PRRED.pcx			28A334:	CC C1 68 00 = PRORANGE.pcx
      28A328:	F4 C1 68 00 = PRBLUE.pcx		28A338:	BC C1 68 00 = PRPURPLE.pcx
      28A32C:	E8 C1 68 00 = PRTAN.pcx			28A33C:	B0 C1 68 00 = PRTEAL.pcx
      28A330:	DC C1 68 00 = PRGREEN.pcx		28A340:	A4 C1 68 00 = PRROSE.pcx

      25F610:	50 FE 65 00 = ABF01L.def (Red)		25F630:	F0 FD 65 00 = ABF02L.def (Red)
      25F614:	44 FE 65 00 = ABF01G.def (Blue)		25F634:	E4 FD 65 00 = ABF02G.def (Blue)
      25F618:	38 FE 65 00 = ABF01R.def (Tan)		25F638:	D8 FD 65 00 = ABF02R.def (Tan)
      25F61C:	2C FE 65 00 = ABF01D.def (Green)	25F63C:	CC FD 65 00 = ABF02D.def (Green)
      25F620:	20 FE 65 00 = ABF01B.def (Orange)	25F640:	C0 FD 65 00 = ABF02B.def (Orange)
      25F624:	14 FE 65 00 = ABF01P.def (Purple)	25F644:	B4 FD 65 00 = ABF02P.def (Purple)
      25F628:	08 FE 65 00 = ABF01W.def (Teal)		25F648:	A8 FD 65 00 = ABF02W.def (Teal)
      25F62C:	FC FD 65 00 = ABF01K.def (Pink)		25F64C:	9C FD 65 00 = ABF02K.def (Pink)

      25F650:	90 FD 65 00 = ABF03L.def (Red)		25F5F0:	B0 FE 65 00 = AF00.def (Red)
      25F654:	84 FD 65 00 = ABF03G.def (Blue)		25F5F4:	A4 FE 65 00 = AF01.def (Blue)
      25F658:	78 FD 65 00 = ABF03R.def (Tan)		25F5F8:	98 FE 65 00 = AF02.def (Tan)
      25F65C:	6C FD 65 00 = ABF03D.def (Green)	25F5FC:	8C FE 65 00 = AF03.def (Green)
      25F660:	60 FD 65 00 = ABF03B.def (Orange)	25F600:	80 FE 65 00 = AF04.def (Orange)
      25F664:	54 FD 65 00 = ABF03P.def (Purple)	25F604:	74 FE 65 00 = AF05.def (Purple)
      25F668:	48 FD 65 00 = ABF03W.def (Teal)		25F608:	68 FE 65 00 = AF06.def (Teal)
      25F66C:	3C FD 65 00 = ABF03K.def (Pink)		25F60C:	5C FE 65 00 = AF07.def (Pink)

	    241AF0: 72 62 79 67 6F 70 74 73 = rbygopts (ADOP*PNL.pcx)
	    2831F8: 72 62 79 67 6F 70 74 73 = rbygopts (ADOPFLG*.pcx)
	    283600: 52 42 59 47 4F 50 54 53 = RBYGOPTS (AOFLGB*.def, ADOPB2*.def)

			            H3MAPED.EXE
			------------------------------------
			13F954	AC D0 58 00 = AF00.def (Red)
			13F958	A0 D0 58 00 = AF01.def (Blue)
			13F95C	94 D0 58 00 = AF02.def (Tan)
			13F960	88 D0 58 00 = AF03.def (Green)
			13F964	7C D0 58 00 = AF04.def (Orange)
			13F968	70 D0 58 00 = AF05.def (Purple)
			13F96C	64 D0 58 00 = AF06.def (Teal)
			13F970	58 D0 58 00 = AF07.def (Pink)

    You'll also need to edit the Game.pal and Players.pal files from h3bitmap.lod:

		 GAME.PAL				PLAYERS.PAL
	--------------------------		---------------------------
	000118 = FF 00 00 00 (red)		000018~097 = Player 1 (red)
	00011C = 32 50 FF 00 (blue)		000098~117 = Player 2 (blue)
	000120 = 9E 76 56 00 (tan)		000118~197 = Player 3 (tan)
	000124 = 40 96 2A 00 (green)		000198~217 = Player 4 (green)
	000128 = FF 80 00 00 (orange)		000218~297 = Player 5 (orange)
	00012C = 88 2F A3 00 (purple)		000298~317 = Player 6 (purple)
	000130 = 09 9B A1 00 (teal)		000318~397 = Player 7 (teal)
	000134 = C0 78 88 00 (pink)		000398~417 = Player 8 (pink)


    Finally, you'll need to edit the following image archives from h3sprite.lod:

		    • AGemLL.def    • AGemLR.def    • AGemUL.def
		    • AGemUR.def    • Crest58.def   • VwSymbol.def

---------------------------------------------------------------------------------------------------------

## SOUND EFFECTS

Editing sound effects is mostly a simple matter of replacing the relevant sound file in Heroes3.snd with
whatever new sound you'd like. The main point of difficulty will often be figuring out which sound file
to replace since many of them have unintuitive/flat-out wrong names. Here's a helpful list:

| Sound File       | Used By                                         |
|-------------------|-------------------------------------------------|
| BuildTwn          | New building, recruit hero                      |
| CaveHead          | Subterranean Gate, Quest/Border Guard, Keymaster |
| Chat              | Chat message/cheat code                         |
| Chest             | Treasure chests                                 |
| Climax            | (copy of Morale - replace both)                 |
| Danger            | Whirlpool, Siren                                 |
| Dragon            | Dragon Utopia                                   |
| Expernce          | (copy of Luck - replace both)                   |
| Faerie            | Magic Well/Spring, School of Magic               |
| Gazebo            | Learning Stone, Witch Hut, Tree of Wisdom, Axis of Power |
| Genie             | Water Wheels, Windmills, Wagon, Floatsam         |
| GetProtection     | Garden of Revelation, Sanctuary                 |
| Graveyard         | Crypt, Warrior Tomb                             |
| Lighthouse        | Redwood Observatory/Pillar, Lighthouse, Cover of Darkness, Cartographer |
| Luck              | Idol/Fountain of Fortune, Fairy Ring, Swan Pond, Mystical Garden |
| Military          | External dwellings, Hill Fort, Garrison, School of War |
| Morale            | Fountain of Youth, Watering Hole, Oasis, Rally Flag |
| Mystery           | Thieves' Den, Altar of Sacrifice, Corpse, Pyramid |
| Nomad             | Mercenary Camp, Marletto Tower, Arena            |
| NwHeroLv          | Level up                                        |
| Obelisk           | Obelisks                                        |
| Quest             | Seer's Hut                                      |
| Rogue             | Creature Banks (except Crypt/Dragon Utopia), Prison |
| Store             | Tavern, Stables, Shipyard, War Machine Factory, Trading Post, Black Market, Freelancer's Guild, Sign, Message in a Bottle |
| SysMsg            | It's your turn (multiplayer)                    |
| Temple            | Shrines, Temples                                |
| Treasure          | Artifacts, Shipwreck Survivor                   |
| Decay             | Implosion                                       |
| Fireblst          | Inferno                                         |
| Sacbreth          | Destroy Undead                                  |
| Spontcomb         | Fireball                                        |
| Muckmire          | Slow                                            |
| Tailwind          | Haste                                           |
| Tuffskin          | Stoneskin                                       |
| Regener           | Regeneration, First Aid Tent                    |
| Resurect          | Resurrection, Animate Dead, Rebirth              |


>not sure: Scholar, Hut of the Magi, Pandora's Box

Replacing sound files, of course, isn't necessary if all you want to do is switch to a different sound
that's already in the game. I suggest changing treasure chests and loose artifacts to the much-shorter
level-up sound (0AB294 > F8 9C for chests and 0AB374 > F8 9C for artifacts) since they often tend to be
found in large clusters. Something else that I enjoy is replacing the "Quest" sound file with the iconic
quest chime from the mainline games, which I then also use for the "level up" screen (0DAC97~8 > 78 77)
as well as the "new building/recruit a hero" sound (68C434~F > 51 75 65 73 74 2E 77 61 76 00 00 00).

---------------------------------------------------------------------------------------------------------

## SCORING

Your score upon completing a map is calculated according to the following formula:

	Base Score = 200 - ((days + 10) / (towns + 5)) + grail/genocide bonuses [25]
		Final Score = Base score * (player difficulty multiplier)

The parameters of this formula can be edited at the following addresses (edit all three for each):

			0F4535, 0F45BA, 0F46BB = C8 (base 200)
			0F450D, 0F4594, 0F468F = 0A (days - 10)
			0F4507, 0F458E, 0F4689 = 05 (towns - 5)
			0F4523, 0F45A8, 0F46A9 = 19 (grail bonus)
			0F45B6, 0F4531, 0F46B7 = 19 (genocide bonus)

For the player difficulty, there are two tables: one with DWORD pointers for the actual calculation and
one with values used for the text display in the game setup screen:

	            Easy: 27F5B4 = CD CC 4C 3F (0.8), 283490 = 50 (80%)
	          Normal: 27F5B8 = 00 00 80 3F (1.0), 283494 = 64 (100%)
	            Hard: 27F5BC = 66 66 A6 3F (1.3), 283498 = 82 (130%)
	          Expert: 27F5C0 = CD CC CC 3F (1.6), 28349C = A0 (160%)
	  Hurt Me, Daddy: 27F5C4 = 00 00 00 40 (2.0), 2834A0 = C8 (200%)

Finally, your ranking is assigned based on the DWORD values in a table starting at 27F1FC. The first two
bytes are a threshold (27F1FC = 04 00, or 4 points) representing the maximum score that will be assigned
this ranking while the third byte is the ID of the unit (27F1FE = 2A, or Imp). Byte 4 is always 00.

-----------------------------------------------------------------------------------------

I have a few problems with the game's original formula. First is that due to the division in particular,
there tends to be little variation in scores regardless of performance, with player difficulty being the
only major contributing factor. Second is that the map difficulty setting isn't considered at all. Third
is that a bonus for defeating every opponent is kind of stupid since A) that's already the goal of most
maps and B) probably not something you want to encourage on maps where it isn't. Bearing that in mind, I
came up with a new formula that, while still very close to the original, addresses these problems:

	Base Score = (Handicap Level [1~5] * 75) + (Map Size [1~4] * 25)
      Final Score = (Base Score) - (Days)(*) + (Map Difficulty [1~5] * Obelisks * (Grail [0~1]+1))

			  *(For team maps, double this value)

As with the original formula, this one is written around a score of 400 or higher as being an excellent
performance, but is much quicker to assign lower scores for sub-par outings. It's also a bit more fair
across maps of different sizes due to using size as main factor rather than the number of towns as a
minor one, and the inclusion of map difficulty and number of obelisks as factors can be used to balance
scores among maps of the same size. Finally, it now more simply subtracts 1 point per day taken to win.

      ---------	-------------------------------------------------------------------------
      0F4681~E8	; NEW SCORING FORMULA
      ---------	-------------------------------------------------------------------------
      8B 3D 38956900	mov edi,[699538]	; EDI = map index
      31 C9		xor ecx,ecx		; ECX = 0
      8A 8F 84F80100	mov cl,[edi+1F884]	; CL = map size (24/48/6C/90)
      6B C9 08	imul ecx,ecx,08		; CL * 8
      0FBE CD		movsx ecx,ch		; ECX = map size (1~4)
      6B C9 19	imul ecx,ecx,19		; ECX * 25

      0FBE97D8F60100	movsx edx,[edi+1F6D8]	; EDX = player difficulty (0~4)
      42		inc edx			; EDX + 1 (1~5)
      6B D2 4B	imul edx,edx,4B		; EDX * 75
      01 D1		add ecx,edx		; ECX + EDX
      89 4D E4	mov [ebp-1C],ecx	; store base score

      80BF78F8010000	cmp byte [edi+1F878],00	; Allied map?
      74 02		je 4F46B3		; If no -> base score - days taken
      01 F6		add esi,esi		; days taken (ESI) * 2
      29 F1		sub ecx,esi		; Base score (ECX) - days taken

      E8 86AC1800	call 67F340		; EBX = obelisks found
      A1 5C956900	mov eax,[69955C]	; EAX = grail? [-1/1]
      3C 01		cmp al,01		; Did we find the grail?
      7C 02		jl 4F46C5		; if no -> EAX = map difficulty
      01 DB		add ebx,ebx		; EBX * 2

      8A 97 71F80100	mov dl,[edi+1F871]	; EDX = map difficulty (0~4)
      42		inc edx			; EDX +1 (1~5)
      0FAF DA		imul ebx,edx		; Bonus = obelisks/grail (EBX) * difficulty
      01 D9		add ecx,ebx		; base score - days (ECX) + bonus (EBX)
      83 F9 00	cmp ecx,00		; is final score score less than zero?
      7D 02		jnl 4F46D8		; if no -> store final score
      31 C9		xor ecx,ecx		; final score = 0

      89 4D E0	mov [ebp-20],ecx	; store final score
      DB 45 E0	fild dword [ebp-20]	; cleanup
      D9 5D E0	fstp dword [ebp-20]	; ""
      D9 45 E0 	fld dword [ebp-20]	; ""
      9090909090	nop			; -

      ---------	-------------------------------------------------------------------------
      18457C~8F	; DISPLAY BASE SCORE ON GAME SETUP SCREEN
      ---------	-------------------------------------------------------------------------
      8A 46 18	mov al,[esi+18]		; EAX = map size (24/48/6C/90)
      6B C0 08	imul eax,08		; EAX * 8
      0FBE C4		movsx eax,ah		; EAX = map size (1~4)
      E8 06EF0F00	call 683490		; -> free space (original text table)
      8D 95 78FDFFFF	lea edx,[ebp-288]	; (shifted code)

      ---------	-------------------------------------------------------------------------
      167C4A~5D	; DISPLAY BASE SCORE ON SCENARIO INFO SCREEN
      ---------	-------------------------------------------------------------------------
      8A 47 18	mov al,[edi+18]		; EAX = map size (24/48/6C/90)
      6B C0 08	imul eax,08		; EAX * 8
      0FBE C4		movsx eax,ah		; EAX = map size (1~4)
      E8 38B81100	call 683490		; -> free space (original text table)
      8D 95 7CFDFFFF	lea edx,[ebp-284]	; (shifted code)

      ---------	-------------------------------------------------------------------------
      283490~A3	; (INLINE EDIT - OVERWRITES ORIGINAL SCORE FORMULA)
      ---------	-------------------------------------------------------------------------
      0FBE8AD8F60100	movsx ecx,[edx+1F6D8]	; ECX = player difficulty (0~4)
      41		inc ecx			; ECX +1 (1~5)
      6B C9 4B	imul ecx,ecx,4B		; ECX * 75
      6B C0 19 	imul eax,eax,19		; EAX * 25
      01 C1		add ecx,eax		; ECX + EAX
      C3		ret			; return
      90 90 90	nop			; -

      283237 > 00	; remove percentage sign from base score on game setup screen

This will free up space in several locations. Since the difficulty multiplier table is no longer used,
27F5B4~C7 will now be free (283490~A3 is used for the rewrite). More substantially, an entire subroutine
(0F44B4~53F) is no longer called. This just leaves the routine starting at 0F4540, which I believe to be
the routine for campaign scoring. Assuming it is, the routine at 0F45E6 will also need to be edited.

Like the kingdom overview screen, the rankings table was never updated for the SoD expansion. And so, as
one final parting gift to my gentle readers, here's a revised table that's a bit more accurate:

      ----------	-------------------------------------------------------------------------
      27F1FC~33F	; NEW SCORE RANKINGS
      ----------	-------------------------------------------------------------------------
      04 00 8B 00	;   0-4   = Peasant
      09 00 68 00	;   5-9   = Serpent Fly
      0E 00 76 00	;  10-14  = Pixie
      13 00 1C 00	;  15-19  = Gremlin
      18 00 38 00	;  20-24  = Skeleton
      1D 00 54 00	;  25-29  = Goblin
      22 00 2A 00	;  30-34  = Imp
      27 00 46 00	;  35-39  = Troglodyte
      2C 00 8A 00	;  40-44  = Halfling
      31 00 0E 00	;  45-49  = Centaur
      36 00 00 00	;  50-54  = Pikeman
      3B 00 3A 00	;  55-59  = Zombie
      40 00 8F 00	;  60-64  = Rogue
      45 00 02 00	;  65-69  = Archer
      4A 00 10 00	;  70-74  = Dwarf
      4F 00 48 00	;  75-79  = Harpy
      54 00 8C 00	;  80-84  = Boar
      59 00 56 00	;  85-89  = Wolf Rider
      5E 00 1E 00	;  90-94  = Stone Gargoyle
      63 00 64 00	;  95-99  = Lizardman
      68 00 2C 00	; 100-104 = Gog
      6D 00 58 00	; 105-109 = Orc
      72 00 3C 00	; 110-114 = Wight
      77 00 12 00	; 115-119 = Wood Elf
      7C 00 4A 00	; 120-124 = Beholder
      81 00 62 00	; 125-129 = Gnoll
      86 00 20 00	; 130-134 = Stone Golem
      8B 00 8E 00	; 135-139 = Nomad
      90 00 2E 00	; 140-144 = Hell Hound
      95 00 8D 00	; 145-149 = Mummy
      9A 00 04 00	; 150-154 = Griffin
      9F 00 6A 00	; 155-159 = Basilisk
      A4 00 22 00	; 160-164 = Mage
      A9 00 4C 00	; 165-169 = Medusa
      AE 00 3E 00	; 170-174 = Vampire
      B3 00 14 00	; 175-179 = Pegasus
      B8 00 30 00	; 180-184 = Demon
      BD 00 5A 00	; 185-199 = Ogre
      C2 00 06 00	; 190-194 = Swordsman
      C7 00 89 00	; 195-199 = Sharpshooter
      CC 00 90 00	; 200-204 = Troll
      D1 00 08 00	; 205-209 = Monk
      D6 00 40 00	; 210-214 = Lich
      DB 00 5C 00	; 215-219 = Roc
      E0 00 24 00	; 220-224 = Genie
      E5 00 16 00	; 225-229 = Dendroid
      EA 00 74 00	; 230-234 = Gold Golem
      EF 00 4E 00	; 235-239 = Minotaur
      F4 00 32 00	; 240-244 = Fiend
      F9 00 66 00	; 245-249 = Gorgon
      FE 00 88 00	; 250-254 = Enchanter
      03 01 78 00	; 255-259 = Psychic Elemental
      08 01 26 00	; 260-264 = Naga
      0D 01 5E 00	; 265-269 = Cyclops
      12 01 75 00	; 270-274 = Diamond Golem
      17 01 79 00	; 275-279 = Magic Elemental
      1C 01 34 00	; 280-284 = Efreet
      21 01 50 00	; 285-289 = Manticore
      26 01 18 00	; 290-294 = Unicorn
      2B 01 6C 00	; 295-299 = Wyvern
      30 01 0A 00	; 300-304 = Cavalier
      35 01 42 00	; 305-309 = Black Knight
      3A 01 6E 00	; 310-314 = Hydra
      3F 01 60 00	; 315-319 = Behemoth
      44 01 44 00	; 320-324 = Bone Dragon
      49 01 82 00	; 325-329 = Firebird
      4E 01 1A 00	; 330-334 = Green Dragon
      53 01 36 00	; 335-339 = Devil
      58 01 52 00	; 345-349 = Red Dragon
      5D 01 28 00	; 340-344 = Giant
      62 01 0C 00	; 350-354 = Angel
      67 01 6F 00	; 355-359 = Chaos Hydra
      6C 01 61 00	; 360-364 = Ancient Behemoth
      71 01 45 00	; 365-369 = Ghost Dragon
      76 01 83 00	; 370-374 = Phoenix
      7B 01 1B 00	; 375-379 = Gold Dragon
      80 01 37 00	; 380-384 = Archdevil
      85 01 53 00	; 385-389 = Black Dragon
      8A 01 29 00	; 390-394 = Titan
      8F 01 0D 00	; 395-399 = Archangel
      FF 7F 84 00	; 400+    = Azure Dragon (27F340~D3 is free space)

-----------------------------------------------------------------------------------------

Slowest map scroll setting disables automatic map scroll:
419543 > 75 05 E9 02020000

Disable (incorrect) hero right-click info if there is no starting hero:
182749~E > E9 25060000 90

"N" keyboard shortcut to show correct text (New Game instead of Quit Game)
0092E2 > 18

No confirmation on exiting game:
0F83D3 > EB 3E	(0F83D5~412 is free)

; Combat speed settings

      23CF7C	00 00 80 3F (1.00) ->	00 00 00 3F (0.50)
      23CF80	AE 47 21 3F (0.63) ->	33 33 B3 3E (0.35)
      23CF84	CD CC CC 3E (0.40) ->	CD CC CC 3D (0.10)

Hero movement speed settings:

23D6E0 = 32
23D6E4 > 28
23D6E8 > 24

23D6CC > 0A
23D6D0 > 10
23D6D4 > 18