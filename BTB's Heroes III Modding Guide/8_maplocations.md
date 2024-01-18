# 8. Map Locations

## EXTERNAL DWELLINGS

There's a table beginning at 23D570 which specifies the unit ID produced by each external dwelling; this
table goes in the order of the dwelling IDs - which starts out as the sort-of alphabetical order of the
units they generate before saying "fuck it" and giving up halfway through - and also doesn't include the
Golem Factory or the combo package Elemental Conflux. Note that "random" map dwellings will look at the
unit which is produced to determine the dwelling's level, so you can swap, say, the Graveyard and Cursed
Temple and both will continue to be properly called in random functions.

| Code    | Structure                  | Code    | Structure               | Code    | Structure               |
|---------|----------------------------|---------|-------------------------|---------|-------------------------|
| 23D570  | Basilisk Pit               | 23D610  | Hell Hole               | 23D574  | Behemoth Crag           |
| 23D614  | Dragon Cave                | 23D578  | Pillar of Eyes          | 23D618  | Cliff Nest              |
| 23D57C  | Hall of Darkness           | 23D61C  | Workshop                | 23D580  | Dragon Vault            |
| 23D620  | Cloud Temple               | 23D584  | Training Grounds        | 23D624  | Dendroid Arches         |
| 23D588  | Centaur Stables            | 23D628  | Warren                  | 23D58C  | Air Elemental Conflux   |
| 23D62C  | Water Elemental Conflux    | 23D590  | Portal of Glory         | 23D630  | Tomb of Souls           |
| 23D594  | Cyclops Cave               | 23D634  | Wyvern Nest             | 23D598  | Forsaken Palace         |
| 23D638  | Enchanted Spring           | 23D59C  | Serpent Fly Hive        | 23D63C  | Unicorn Glade           |
| 23D5A0  | Dwarf Cottage              | 23D640  | Mausoleum               | 23D5A4  | Earth Elemental Conflux |
| 23D644  | Estate                     | 23D5A8  | Fire Lake               | 23D648  | Cursed Temple           |
| 23D5AC  | Homestead                  | 23D64C  | Graveyard               | 23D5B0  | Fire Elemental Conflux  |
| 23D650  | Guardhouse                 | 23D5B4  | Parapet                 | 23D654  | Archers' Tower           |
| 23D658  | Barracks                   | 23D5B8  | Altar of Wishes         | 23D65C  | Magic Lantern           |
| 23D660  | Altar of Thought            | 23D5BC | Wolf Pen                | 23D664  | Pyre                    |
| 23D668  | Frozen Cliffs              | 23D5C0  | Gnoll Hut               | 23D66C  | Crystal Cavern          |
| 23D670  | Magic Forest               | 23D5D4  | Griffin Tower           | 23D674  | Sulfurous Lair          |
| 23D678  | Enchanter's Hollow         | 23D5D8  | Harpy Loft              | 23D67C  | Treetop Tower            |
| 23D5DC  | Kennels                    | 23D680  | Unicorn Glade            | 23D5E0  | Hydra Pond              |
| 23D684  | Altar of Air               | 23D5E4  | Imp Crucible            | 23D688  | Altar of Earth           |
| 23D68C  | Altar of Fire               | 23D5EC | Mage Tower              | 23D690  | Altar of Water          |
| 23D694  | Thatched Hut               | 23D5F4  | Chapel of Stilled Voices | 23D5F8  | Labyrinth               |
| 23D698  | Hovel                      | 23D5FC  | Monastery               | 23D69C  | Boar Glen                |
| 23D6A0  | Tomb of Curses              | 23D600 | Golden Pavilion         | 23D604  | Demon Gate               |
| 23D6A4  | Nomad Tent                 | 23D608  | Ogre Fort               | 23D6A8  | Rogue Cavern            |
| 23D6AC  | Troll Bridge               |


-----------------------------------------------------------------------------------------

	External dwellings can be made to accumulate units rather than capping:

		   Guards Accumulate: 0B8771 > 90 90 90 90 90
		    Units Accumulate: 0B87A1 > 01

0B87BB specifies the highest-level dwelling (04 = level 4) that is not guarded; set it to
00 for every dwelling to be guarded or 07 for none of them to be. The number of guards is
set by a command at 0B87C3~5 (8D 0C 49), which triples the ECX register (the base growth
value of the unit) in a roundabout way. We can easily assume more control over this by
replacing it with a multiply command: 6B C9 XX, where X is the desired multiple.

	External lv.1 dwellings to charge gold: 0A197C & 0AB813: 09 > 00

-----------------------------------------------------------------------------------------

	  Refugee Camps specifically ban six units at the following addresses:

		Sharpshooters	0C902B		Enchanters	0C903A
		----------------------		----------------------
		Azure Dragons	0C8FEF		Faerie Dragons	0C900D
		Crystal Dragons	0C8FFE		Rust Dragons	0C901C

---------------------------------------------------------------------------------------------------------

## CREATURE BANKS

Creature banks are mostly editable in CrBanks.txt: there are four possible outcomes for each, with their
odds adjustable to your liking. You can also change the quantity (but not type) of units fought, as well
as the rewards or gold, resources, and/or artifacts. The "upgrade%" value is kind of broken; it's the
chances of getting upgraded versions of the units fought, but only applies to the bottom-left stack for
some reason. It's better to change this by directly editing the units to be fought.

You'll need to edit the .exe to change either the units you fight or any awarded. It's possible to add
unit rewards to any bank that originally doesn't have one by editing the below addresses; you can also
add up to four types of guards (total) for banks which only have one by moving "FF FF FF FF" ahead by 4,
8, or 12 bytes and then specifying more IDs (4 bytes each) in the resulting space.

| CREATURE BANK       | FIGHT              | REWARD      |
|--------------------|--------------------|-------------|
| Cyclops Stockpile  | 2702A0 (Cyclopses) | 27037C (-) |
| Dwarven Treasury   | 2702B4 (Dwarves)   | 270380 (-) |
| Griffin Conservatory | 2702C8 (Griffins) | 270384 (Angels) |
| Imp Cache          | 2702DC (Imps)      | 270388 (-) |
| Medusa Store       | 2702F0 (Medusas)   | 27038C (-) |
| Naga Bank          | 270304 (Nagas)     | 270390 (-) |
| Dragonfly Hive     | 270318 (Dragonflies) | 270394 (Wyverns) |
| Shipwreck          | 27032C (Wights)    | 270398 (-) |
| Derelict Ship      | 270340 (Water Dudes) | 27039C (-) |
| Crypt              | 270354 (Skeletons) | 2703A0 (-) |
|                    | 270358 (Walking Dead) | ------ |
|                    | 27035C (Wights)    | ------ |
|                    | 270360 (Vampires)  | ------ |
| Dragon Utopia      | 270368 (Green Dragons) | 2703A4 (-) |
|                    | 27036C (Red Dragons) | ------ |
|                    | 270370 (Gold Dragons) | ------ |
|                    | 270374 (Black Dragons) | ------ |

     If editing the units in a bank, be sure to update the AI column [total AI value of units/50])

-----------------------------------------------------------------------------------------

Although technically not a creature bank, Pyramids more or less act like one and so will also be covered
here. The parameters for the units to be fought are specified at the following addresses:

	    0A3FA7 = 75 (Diamond Golems)    0A3FAF = 74 (Gold Golems)
	    0A3FA5 = 14 (20 units)          0A3FB6 = 28 (40 units)
	    0A3FA3 = 02 (# of stacks)       (# of stacks depends on army strength)

Disappointingly, Pyramids contain no actual mummies. Unfortunately, the unit ID for Mummies is 8D, which
as we learned earlier will require more space for a long push. Thankfully, there's a completely needless
luck penalty for visiting an already-looted Pyramid just nearby that we can axe to make that space:


	------		-------------------------------------------------------------------------
	0A3FA6		; PYRAMIDS TO HAVE MUMMIES INSTEAD OF DIAMOND GOLEMS
	------		-------------------------------------------------------------------------
	EB DC		jmp 4A3F84		; -> free space (empty Pyramid luck penalty)

	------		-------------------------------------------------------------------------
	0A3F82~8F	; (EXPANDED SPACE - OVERWRITES EMPTY PYRAMID LUCK PENALTY)
	------		-------------------------------------------------------------------------
	EB 0C		jmp 4A3F90		; frees space: 0A3F84~F
	68 8D000000	push 8D			; 8D = Mummies
	EB 1D		jmp 4A3FA8		; -> [continue]
	90 90 90 90 90	nop			; -
      
Finally, a fifth-level spell is a rather odd choice of reward. There's a lot of options we can go with
here, but in the end I decided on cold, hard cash. This will overwrite/invalidate the earlier edit for
Pyramids to skip checking the visiting hero's Wisdom and free up a lot of space in the process.
      
	---------	-------------------------------------------------------------------------
	0A4024~4B	; PYRAMIDS TO GOLD REWARD
	---------	-------------------------------------------------------------------------
	09 D1		or ecx,edx		 ; (shifted code)
	89 08		mov [eax],ecx		 ; ""
	0FBE 47 22	movsx eax,[edi+22]	 ; EAX = visiting hero's owner
	6B C0 2D	imul eax,2D		 ; EAX = data range
	8B 35 38956900	mov esi,[699538]	 ; ESI = main index
	8D84C6D00A0200	lea eax,[esi+eax*8+20AD0]; EAX = player data
	BE 10270000	mov esi,61A8		 ; ESI = 25,000 (gold reward)
	01 B0 B4000000	add [eax+B4],esi	 ; update player's gold
	E9 AB000000	jmp 4A40F7		 ; -> [continue] (0A404C~F6 is free space)

	0A410C > 06	; dialogue box GFX to gold

---------------------------------------------------------------------------------------------------------

## MAGIC SPRINGS, TAVERNS, & THIEVES' DENS

We already discussed how to remove the "mana doubling" effect from the Mana Vortex earlier (or, at least
how to move it to something else that's harder to build) for being too powerful, and if you agreed with
that then you'll probably want to do the same thing with Magic Springs. With just a few edits, we can
change Magic Springs to have the same effect as Magic Wells by calling the same routine:

		0A9296 > 45	; magic spring -> magic well routine
		0A9299 > 4D	; ""
		0A929B > 50	; ""
		0A929D > 51	; ""
		0A92A1 > FB A0	; ""

This change will free a substantial amount of space 0A31FD~39F, which we can use in part to rewrite the
tavern code to allow different heroes to appear in taverns on the map than in the ones in your towns, as
well as preventing heroes who escape from battle on Sundays from being lost on the week rollover. While
the specific free space we use is never an issue, it's actually important in this case since it's not
just free code space we need: we're also stealing the Magic Spring SRAM space in the player data block.

	---------	-------------------------------------------------------------------------
	0C8131~54	; CHECK FOR RETREATED/SURRENDERED HERO BEFORE WEEKLY TAVERN FILL
	---------	-------------------------------------------------------------------------
	8B 1D 38956900	mov ebx,[699538]	; EBX = map index
	E8 C1B0FDFF	call 4A31FD		; -> free space (magic spring)
	89 45 E8	mov [ebp-18],eax	; (shifted code)
	89 45 EC	mov [ebp-14],eax	; ""
	89 5D F0	mov [ebp-10],ebx	; ""
	EB 03		jmp 4C814A		; ""
	8B 75 08	mov esi,[ebp+08]	; ""
	8B 44 9A 28	mov eax,[edx+ebx*4+28]	; ""
	85 C0		test eax,eax		; ""
	E8 CDB0FDFF	call 4A3222		; -> free space (magic spring)

	4C834B > F8	; adjusted jump

	----------	-------------------------------------------------------------------------
	0A31FD~22B	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	----------	-------------------------------------------------------------------------
	80BB40F6010001	cmp byte [ebx+1F640],01	; week 1?
	75 09		jne 4A320F		; if no -> EBX = tavern slot 1

	80BB42F6010001	cmp byte [ebx+1F642],01	; month 1?
	74 0D		je 4A321C		; if yes -> EBX = 0 (fill all four slots)

	8B 5A 28	mov ebx,[edx+28]	; EBX = tavern slot 1
	3B 5A 2C	cmp ebx,[edx+2C]	; does EBX = tavern slot 2?
	75 05		jne 4A321C		; if no -> EBX = 0 (fill all four slots)
	31 DB		xor ebx,ebx		; EBX = 1 (do not overwrite first slot)
	43		inc ebx			; ""
	EB 02		jmp 4A321E		; -> (displaced code)
	31 DB		xor ebx,ebx		; EBX = 0
	89 55 F4	mov [ebp-0C],edx	; (displaced code)
	C3		ret			; return

	89 1D B0AA6A00	mov [6AAAB0],ebx	; ~~~I forget why I do this
	6A 0B		push 0B			; (displaced code)
	59		pop ecx			; ""
	C3		ret			; return

	---------	-------------------------------------------------------------------------
	0C827F~85	; WEEKLY TAVERN FILL TO USE MAGIC SPRING SRAM
	---------	-------------------------------------------------------------------------
	E8 A8AFFDFF	call 4A322C		; -> free space (magic spring)
	90 90		nop			; -

	---------	-------------------------------------------------------------------------
	0A322C~3F	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	---------	-------------------------------------------------------------------------
	88841ABC000000	mov [edx+ebx+BC],al	; move hero to magic spring SRAM
	83 FB 02	cmp ebx,02		; is this one of the first two heroes?
	7D 04		jge 4A323C		; if no -> (displaced code)
	89 74 9A 28	mov [edx+ebx*4+28],esi	; move hero into tavern
	83 FE FF	cmp esi,-01		; (displaced code)
	C3		ret			; return

	0C8345 > 04	; fill 4 slots instead of 2

	------		-------------------------------------------------------------------------
	0BB2F7		; EQUAL CLASS ODDS FOR EXTERNAL TAVERNS
	------		-------------------------------------------------------------------------
	E8 447FFEFF	call 4A3240		; -> free space

	---------	-------------------------------------------------------------------------
	0A3240~55	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	---------	-------------------------------------------------------------------------
	85 FF		test edi,edi		; odds greater than 0?
	74 0C		je 4A3250		; if no -> (displaced code)
	833DB0AA6A0002	cmp dword [6AAAB0],02	; external tavern?
	7C 03		jl 4A3253		; if no -> (displaced code)
	31 FF		xor edi,edi		; EDI = 1 (equal odds)
	47		inc edi			; ""
	83 C0 40	add eax,40		; (displaced code)
	89 39		mov [ecx],edi		; ""
	C3		ret			; return

	1D8299: 01 > 02	; flag when entering external tavern

	--------	-------------------------------------------------------------------------
	1D83F4~D	; CHECK TAVERN TYPE WHEN ENTERING AND LOAD APPROPRIATE HEROES
	--------	-------------------------------------------------------------------------
	E8 5DAEECFF	call 4A3256		; -> free space (magic spring)
	8D 4D D0	lea ecx,[ebp-30]	; (displaced code)
	90		nop			; -
	90		nop			; -

	---------	-------------------------------------------------------------------------
	0A3256~99	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	---------	-------------------------------------------------------------------------
	31 C9		xor ecx,ecx		; ECX = 0
	833DB0AA6A0002	cmp [6AAAB0],02		; external tavern?
	7C 14		jl 4A3275		; if no -> CX = internal heroes

	668B8BBE000000	mov cx,[ebx+BE]		; CX = external heroes
	80 F9 FF	cmp cl,-01		; is first external slot empty?
	74 08		je 4A3275		; if yes -> internal heroes
	88 4B 28	mov [ebx+28],cl		; fill tavern slot 1
	88 6B 2C	mov [ebx+2C],ch		; fill tavern slot 2
	EB 09		jmp 4A327E		; -> ECX = 0

	668B8BBC000000	mov cx,[ebx+BC]		; CX = internal heroes
	EB EF		jmp 4A326D		; -> fill tavern

	31 C9		xor ecx,ecx		; ECX = 0
	49		dec ecx			; ECX = FFFFFFFF
	80 7B 28 FF	cmp byte [ebx+28],-01	; is tavern slot 1 FF (no hero?)
	75 03		jne 4A328A		; if no -> next slot
	89 4B 28	mov [ebx+28],ecx	; tavern slot 1 = FFFFFFFF
	80 7B 2C FF	cmp byte [ebx+2C],-01	; is tavern slot 2 FF (no hero?)
	75 03		jne 4A3293		; if no -> (displaced code)
	89 4B 2C	mov [ebx+2C],ecx	; tavern slot 2 = FFFFFFFF
	6A 04		push 04			; (displaced code)
	59		pop ecx			; ""
	89 4D D8	mov [ebp-28],ecx	; ""
	C3		ret			; return

	--------	-------------------------------------------------------------------------
	0C8374~F	; UNSET "TEMP" FLAG FOR AI PLAYERS (AI CAN'T USE EXTERNAL TAVERNS)
	--------	-------------------------------------------------------------------------
	8D9CC7D00A0200 lea ebx,[edi+eax*8+20AD0]; prepare EBX to check for AI player
	E8 1AAFFDFF	call 4A329A		; -> free space (magic spring)

	---------	-------------------------------------------------------------------------
	0A329A~AE	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	---------	-------------------------------------------------------------------------
	80BBE100000001	cmp byte [ebx+E1],01	; AI player?
	74 08		je 4A32AB		; if no -> (displaced code)
	31 C9		xor ecx,ecx		; ECX = 0
	89 0D B0AA6A00	mov [6AAAB0],ecx	; tavern flag = 0 (internal)
	6A 12		push 12			; (displaced code)
	59		pop ecx			; ""
	C3		ret			; return

	------		-------------------------------------------------------------------------
	0C83BB		; REFILLING A TAVERN SLOT AFTER HIRING A HERO
	------		-------------------------------------------------------------------------
	E8 EFAEFDFF	call 4A32AF		; -> free space (magic spring)
	90 90		nop			; -

	---------	-------------------------------------------------------------------------
	0A32AF~CF	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	---------	-------------------------------------------------------------------------
	89 74 93 28	mov [ebx+edx*4+28],esi	; (displaced code)
	833DB0AA6A0002	cmp dword [6AAAB0],02	; external tavern?
	7D 09		jge 4A32C5		; if yes -> fill external tavern slot
	88841ABC000000	mov [edx+ebx+BC],al	; fill internal tavern slot
	EB 07		jmp 4A32CC		; -> (displaced code)
	88841ABE000000	mov [edx+ebx+BE],al	; fill external tavern slot
	83 FE FF	cmp esi,-01		; (displaced code)
	C3		ret			; return

	0DA42F > 31 C0	; escaped heroes always go into slot 1 (frees space: 0DA431~A)

	---------	-------------------------------------------------------------------------
	0DA4A0~B6	; RETREAT AND SURRENDER
	---------	-------------------------------------------------------------------------
	0F BE 56 22	movsx edx,[esi+22]	; EDX = player ID
	6B D2 2D	imul edx,edx,2D		; EDX = data range
	6B D2 08	imul edx,edx,08		; ""
	E8 218EFCFF	call 4A32D0		; -> free space (magic spring)
	90		nop			;
	888C3A8C0B0200	mov [edx+edi+20B8C],cl	; fill new tavern index 1 or 2

	---------	-------------------------------------------------------------------------
	0A32D0~E3	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	---------	-------------------------------------------------------------------------
	8B 4E 1A	mov ecx,[esi+1A]	; ECX = escaped hero ID
	01 C2		add edx,eax		; (~~~unnecessary? EAX is always 0 now)
	898C3AF80A0200	mov [edx+edi+20AF8],ecx	; move hero ID to both tavern slots
	898C3AFC0A0200	mov [edx+edi+20AFC],ecx	; ""
	C3		ret			; return

	----------	-------------------------------------------------------------------------
	0C86E4~72A	; PROPERLY REMOVE HEROES FROM TAVERNS EACH WEEK
	----------	-------------------------------------------------------------------------
	8D B8 8C0B0200	lea edi,[eax+20B8C]	; EDI = magic spring SRAM (new tavern index)
	89 7D F4	mov [ebp-0C],edi	; store tavern index
	E8 F2ABFDFF	call 4A32E4		; -> free space (magic spring)
	89 4D F0	mov [ebp-10],ecx	; store slot count

	8A 0F		mov cl,[edi]		; CL = hero ID in current tavern slot
	85 C9		test ecx,ecx		; is slot empty?
	7C 24		jl 4C871F		; if yes ->

	8B 5D FC	mov ebx,[ebp-04]	; EBX = ??? (+4DF18 = hero status table)
	51		push ecx		; push Hero ID
	8B CB		mov ecx,ebx		; ECX = EBX
	E8 CA90F6FF	call 4317D0		; EAX = hero data
  F7800501000000000200	test [eax+105],20000	; does hero have "in tavern" flag set? (~~~necessary?)
	75 0D		jne 4C871F		; if no -> EAX = slot count
	6A FF		push -01		; AL = FF
	58		pop eax			; ""
	88841A18DF0400	mov [edx+ebx+4DF18],al	; hero goes back into pool
	88 07		mov [edi],al		; empty tavern slot
	90		nop 			; -

	8B 45 F0	mov eax,[ebp-10]	; EAX = slot count
	47		inc edi			; EDI + 1 (next slot)
	31 C9		xor ecx,ecx		; ECX = 0 (needed to check next slot properly)
	48		dec eax			; EAX - 1
	89 45 F0	mov [ebp-10],eax	; store slot count
	75 CA		jne 4C86F5		; if slot count not -> CL = hero ID

	---------	-------------------------------------------------------------------------
	0A32E4~FA	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	---------	-------------------------------------------------------------------------
	8B 8F 70FFFFFF	mov ecx,[edi-90]	; ECX = tavern slot 1
	3B 8F 6CFFFFFF	cmp ecx,[edi-94]	; does ECX = tavern slot 2?
	74 04		je 4A32F6		; if yes -> fill 3 slots
	6A 04		push 04			; slot count = 4
	EB 03		jmp 4A32F9		; -> ECX = slot count
	6A 03		push 03			; slot count = 3
	47		inc edi			; skip first tavern slot
	59		pop ecx			; ECX = slot count
	C3		ret			; return

There's a bit going on here so it's worth explaining what we're doing. The two heroes in each player's
tavern are stored as two DWORD (4-byte) values in the player's SRAM/data block. Since we only need a
single byte for hero ID's, we can fit four of them (two internal tavern heroes and two external tavern
heroes) in the 4 bytes that used to be where the player data stored the flag for having visited a magic
spring. When we go into a tavern, we check if it's internal or external and then copy the appropriate
heroes from those four bytes over into the original tavern hero slots. The only thing that these SRAM
slots are used for is the display heroes in taverns; all other management is done to the new slot.

Bearing the above in mind, whenever a hero escapes from battle (retreat or surrender), we put that hero
into both of the original tavern slots - this is our cue to not replace the first of the four heroes in
the new SRAM slot. Thus, an escaped hero will remain available indefinitely until the player enters any
tavern, which will overwrite the original two slots and thus unset the "do not replace the first hero"
flag. For the sake of not making this code any longer than it already is, we make escaped heroes always
overwrite the first internal tavern slot rather than one of the two internal slots chosen at random.

A final feature of this new code is that it gives external taverns the same appearance probability for
all classes which can appear in that player's tavern. In other words, while their internal taverns might
be weighted heavily toward having heroes from their starting faction (as specified in HcTraits.txt) with
a smaller chance of heroes from an allied faction (i.e. Druids or Wizards for a Castle player), external
taverns will have equal weighting for all classes that can possibly appear while still disallowing ones
that are set to not appear at all (i.e. evil heroes for a Castle player).

----------------------------------------------------------------------------------------

Unlike taverns, thieves' dens on the adventure map actually do provide a benefit that the ones in your
towns don't, at least until you have five or more of them. That said, it's still usually not worth the
trip to visit them, so they can use anything we can throw at them to make them more useful. To keep in
line with their theme, let's have them also apply advanced Visions to visiting heroes for the turn.

	------		------------------------------------------------------------------------
	0A9E86		; EXTERNAL THIEVES' DENS GIVE HEROES EXPERT VISIONS FOR REST OF TURN
	------		------------------------------------------------------------------------
	E8 D671FFFF	call 4A1061		; -> free space (Idol even day)

	--------	------------------------------------------------------------------------
	0A1061~E	; (EXPANDED SPACE - OVERWRITES EVEN DAY IDOL CHECK)
	--------	------------------------------------------------------------------------
	6A 02		push 02			; EDX = 2 (advanced level)
	5A		pop edx			; ""
	8B 4D 08	mov ecx,[ebp+08]	; ECX = hero data
	89 91 29010000	mov [ecx+129],edx	; set hero's Visions level to advanced
	4A		dec edx			; EDX = 1 (displaced code)
	C3		ret			; return

---------------------------------------------------------------------------------------------------------

## LUCK/MORALE & MOVEMENT MODIFIERS

If you've edited the formulas for luck and morale (see the "Skills" section above), you'll probably also
want to edit the map locations which affect them. As you're probably familiar with by this point, you'll
have a much easier time lowering or removing bonuses than adding or increasing them mainly because any
bonus of +1 is usually coded as an INC command, which is shorter than an ADD. However, the INC commands
used by all map locations are only to the low byte of the relevant registers; this is unnecessary since
there's no reason you can't just increment the entire register, and more importantly allows us to change
any +1 bonus to a +2 with no extra space required (FE Cx -> 4x 4x).

>(Remember to update AdvEvent.txt with any changes you make below!)

#### TEMPLE (WEEKDAYS)

| Address  | Value | Description  |
|----------|-------|--------------|
| 0A5F10   | 1A    | Morale       |
| 0A5F29   | ""    |              |
| 0A5F1F   | FE C1 | (INC)        |
| 0A5F45   | 0E    | MoraleUp     |

#### TEMPLE (SUNDAYS)

| Address  | Value | Description  |
|----------|-------|--------------|
| 0A5EDC   | 1A    | Morale       |
| 0A5EF6   | ""    |              |
| 0A5EED   | +2    |              |
| 0A5F0C   | 0E    | MoraleUp     |



To skip the Temple check for Sunday, set 0A5EDA from 75 to EB; to have it always give +2
morale, NOP out the jump instead (75 34 -> 90 90). Skipping the Sunday check frees up
space from 0A5EDC~F0F; skipping weekdays instead frees up 0A5F10~3C.

#### IDOL (WEEKDAYS)

| Address  | Value | Description  |
|----------|-------|--------------|
| 0A102A   | 1B    | Luck         |
| 0A103A   | ""    |              |
| 0A1036   | FE C1 | (INC)        |
| 0A101A   | 0B    | LuckUp       |
| 0A1073   | 1A    | Morale       |
| 0A1086   | ""    |              |
| 0A107F   | FE C1 | (INC)        |
| 0A1063   | 0E    | MoraleUp     |

#### IDOL (SUNDAYS)

| Address  | Value | Description  |
|----------|-------|--------------|
| 0A0FC6   | 1B    | Luck         |
| 0A0FDC   | ""    |              |
| 0A0FD8   | FE C2 | (INC)        |
| 0A0FB6   | 0B    | LuckUp       |
| 0A0FCC   | 1A    | Morale       |
| 0A0FE2   | ""    |              |
| 0A0FDA   | FE C1 | (INC)        |
| 0A0FAC   | 0E    | MoraleUp     |

#### RALLY FLAG

| Address  | Value | Description          |
|----------|-------|----------------------|
| 0A41FE   | 1A    | Morale               |
| 0A4214   | ""    |                      |
| 0A4210   | FE C0 | (INC)                |
| 0A41A6   | 0E    | MoraleUp             |
| 0A4204   | 1B    | Luck                 |
| 0A4225   | ""    |                      |
| 0A4212   | FE C2 | (INC)                |
| 0A419C   | 0B    | LuckUp               |
| 0A421A   | +400  | movement (additional)|

To skip the Idol checks for Sundays and even days (so always +1 luck), go to 0A0F80 and
write 8A 45 10 EB 74; this will free up two portions of space (0A0F85~F8 and 0A1042~8B).
To always give +1 to both (creating one contiguous block of free space: 0A0FF2~108B),
instead NOP out the jump at 0A0F90 (75 60 -> 90 90).

#### FOUNTAIN OF FORTUNE

| Address  | Value  | Description          |
|----------|--------|----------------------|
| 0A21F3   | 1B     | Luck                 |
| 0A2201   | ""     |                      |
| 0A21FD   | 02 C8  | (Add "X")            |
| 0A2146   | 0B     | LuckUp               |
| 0A214A   | 0D     | LuckDown             |

#### SWAN POND

| Address  | Value  | Description          |
|----------|--------|----------------------|
| 0A88C1   | 1B     | Luck                 |
| 0A88D6   | ""     |                      |
| 0A88CA   | 02     | +2                   |
| 0A88FA   | 0B     | LuckUp               |
| 0A88CB   | Movement to 0 |              |

To have the Fountain of Fortune always give +1 luck, change 0A21FD to FE C1 (INC), write
EB 29 to 0A2177 (this frees up space from 0A2179 to 0A21A1), NOP out the jump at 0A2143
(7E 04 -> 90 90), and change 0A21AC to 08 to force the correct bit for right-click info.

The remove the "movement to 0" effect from Swan Ponds, NOP out the instruction at 0A88CB:

		    (C7 47 4D 00 00 00 00 -> 90 90 90 90 90 90 90)

#### WATERING HOLE

| Address  | Value | Description          |
|----------|-------|----------------------|
| 0A7BDA   | 1A    | Morale               |
| 0A7BF1   | ""    |                      |
| 0A7BE4   | FE C0 | (INC)                |
| 0A7B87   | 0E    | MoraleUp             |
| 0A7BF6   | +400  | movement (additional)|

#### FOUNTAIN OF YOUTH

| Address  | Value | Description          |
|----------|-------|----------------------|
| 0A232C   | 1A    | Morale               |
| 0A2343   | ""    |                      |
| 0A2336   | FE C0 | (INC)                |
| 0A22D9   | 0E    | MoraleUp             |
| 0A2348   | +400  | movement (additional)|

#### OASIS

| Address  | Value | Description          |
|----------|-------|----------------------|
| 0A39F0   | 1A    | Morale               |
| 0A3A04   | ""    |                      |
| 0A3A00   | FE C3 | (INC)                |
| 0A3982   | 0E    | MoraleUp             |
| 0A39F5   | +800  | movement (additional)|

You may wish to remove the morale bonuses from these objects and have them simply act as
movement enhancers; this is a simple matter of NOPing the INC commands (FE C# -> 90 90)
and then changing 0E (this is the "Morale Up" graphic in the text box) to FF.

#### BUOY

| Address  | Value | Description  |
|----------|-------|--------------|
| 0A85BE   | 1A    | Morale       |
| 0A85CE   | ""    |              |
| 0A85C6   | FE C2 | (INC)        |
| 0A863A   | 0E    | MoraleUp     |

#### MERMAID

| Address  | Value | Description  |
|----------|-------|--------------|
| 0A93DA   | 1B    | Luck         |
| 0A93E2   | ""    |              |
| 0A93E0   | FE C0 | (INC)        |
| 0A937A   | 0B    | LuckUp       |

These two are particularly weird; buoys would make far more sense as movement enhancers
while mermaids, given how much more effort it takes to get to them, would be better off
boosting both luck and morale. There is example code below for both of these changes.

#### PYRAMID

| Address  | Value | Description   |
|----------|-------|---------------|
| 0A3F84   | 1B    | Luck          |
| 0A3F8C   | ""    |               |
| 0A3F89   | (DEC*)| (DEC*)        |
| 0A3F51   | 0D    | LuckDown      |
| 0A3F5B   | 0D "" |               |

#### SHIPS & CRYPTS

| Address  | Value | Description     |
|----------|-------|-----------------|
| 0AC23A   | 1A    | Morale          |
| 0AC242   | ""    |                 |
| 0AC23E   | FE C8 | (DEC)           |
| 0AC213   | 10    | MoraleDown      |
| 0AC213   | 10 "" |                 |

#### WARRIOR TOMB

| Address  | Value | Description     |
|----------|-------|-----------------|
| 0A7A2C   | 1A    | Morale          |
| 0A7A34   | ""    |                 |
| 0A7A31   | FD    | (-3)            |
| 0A79E1   | 10    | MoraleDown      |
| 0A79EC   | ""    |                 |
| 0A79F6   | ""    |                 |

The DEC (-1) command for Pyramids is unusually long (FE 88 87 1B 01 00) since it's
editing an address in memory rather than a value in one of the registers; it would be
longer still were it a greater change than +/-1, so it's not a free pass on space.

Crypts, Shipwrecks, and Derelict Ships share the same code block to apply their morale
penalties, but are otherwise completely independent of each other in that they are able
to stack and will report individually in the right-click text. And on that note...

----------------------------------------------------------------------------------------

That takes care of everything except the right-click text, which as we know now is an entirely separate
pain in the ass to deal with. Removing a bonus (like morale from Watering Holes) is a simple matter of
changing the conditional jump following the check for it (74 XX) to a standard one (EB XX). Lowering a
bonus (or penalty) is similarly very easy; the only note in that regard is a very strange optimization
attempt that the game makes with luck bonuses by setting ESI to 02 at the very beginning of the routine
(0DCF72 = BE [02] 00 00 00) and then adding/subtracting ESI to (or from) EBP-10 (the running luck bonus)
instead of a static value. In those cases, you'll need to replace the entire command with an INC or DEC.

Where things start getting annoying is with increasing bonuses or adding new ones. Increasing a +1 luck
bonus to +2 is thankfully easy due to the ESI setting above, but morale won't have that luxury. Ideally,
anything you add will come from somewhere else: the Mermaid code further below, for example, hijacks the
Fountain of Youth right-click check for its new morale bonus. Further complicating matters is that the
check code is unoptimized; the table below provides an optimal version of each check so that any swaps
can be made completely inline (i.e. using the Bouy right-click check for Mermaids, instead).

| ADDRESS | OBJECT FLAG        | CHECK CODE                  | OPTIMIZED CHECK        |
|---------|--------------------|-----------------------------|------------------------|
| 0DC7F7  | Bouy               | F6 83 05010000 04          | -                      |
| 0DCF6C  | Swan Pond          | 8A 83 05010000 (*) A8 08  | F6 83 05010000 08     |
| 0DCF9A  | Idol of Fortune (Luck) | F6 83 05010000 10       | -                      |
| 0DCFC2  | Fountain of Fortune (-1) | F6 83 05010000 20     | -                      |
| 0DC8F1  | Watering Hole      | F6 83 05010000 40          | -                      |
| 0DC81F  | Oasis              | F6 83 05010000 80          | -                      |
| 0DC847  | Temple (+1)        | 8B 83 05010000 F6 C4 01    | F6 83 06010000 01     |
| 0DC8C7  | Shipwreck          | 8B 83 05010000 F6 C4 02    | F6 83 06010000 02     |
| 0DC89D  | Crypt              | 8B 83 05010000 F6 C4 04    | F6 83 06010000 04     |
| 0DC919  | Derelect Ship      | 8B 83 05010000 F6 C4 08    | F6 83 06010000 08     |
| 0DD0EC  | Pyramid            | 8B 83 05010000 F6 C4 10    | F6 83 06010000 10     |
| 0DD116  | Fairy Ring          | 8B 83 05010000 F6 C4 20   | F6 83 06010000 20     |
| 0DC96E  | Fountain of Youth   | 8B 83 05010000 F6 C4 40   | F6 83 06010000 40     |
| 0DD140  | Mermaid             | 8B 83 05010000 F6 C4 80   | F6 83 06010000 80     |
| 0DD16A  | Rally Flag (luck)   | F7 83 05010000 00000100   | F6 83 07010000 01     |
| 0DC943  | Rally Flag (morale) | F7 83 05010000 00000100   | F6 83 07010000 01     |
| 0DC998  | Warrior Tomb        | F7 83 05010000 00002000   | F6 83 07010000 20     |
| 0DC7CC  | Idol of Fortune (Morale) | F7 83 05010000 00000002 | F6 83 08010000 02     |
| 0DC871  | Temple (+2)         | F7 83 05010000 00000004   | F6 83 08010000 04     |
| 0DD00A  | Fountain of Fortune (+1) | F7 83 05010000 00000008 | F6 83 08010000 08     |
| 0DD055  | Fountain of Fortune (+2) | F7 83 05010000 00000010 | F6 83 08010000 10     |
| 0DD0A0  | Fountain of Fortune (+3) | F7 83 05010000 00000020 | F6 83 08010000 20     |


>*Swan Pond's check is interrupted by the above-mentioned command to set ESI to 2

| ADDRESS | OBJECT FLAG            | CODE               |
|---------|------------------------|--------------------|
| 0DC81C  | Bouy                   | FF 45 F0 (INC)    |
| 0DCF97  | Swan Pond              | 01 75 F0 (ADD ESI)|
| 0DCFBF  | Idol of Fortune (Luck) | FF 45 F0 (INC)    |
| 0DD007  | Fountain of Fortune (-1)| FF 4D F0 (DEC)    |
| 0DC916  | Watering Hole          | FF 45 F0 (INC)    |
| 0DC844  | Oasis                  | FF 45 F0 (INC)    |
| 0DC86E  | Temple (+1)            | FF 45 F0 (INC)    |
| 0DC8EE  | Shipwreck              | FF 4D F0 (DEC)    |
| 0DC8C4  | Crypt                  | FF 4D F0 (DEC)    |
| 0DC940  | Derelect Ship          | FF 4D F0 (DEC)    |
| 0DD113  | Pyramid                | 29 75 F0 (SUB ESI)|
| 0DD13D  | Fairy Ring             | FF 45 F0 (INC)    |
| 0DC995  | Fountain of Youth      | FF 45 F0 (INC)    |
| 0DD167  | Mermaid                | FF 45 F0 (INC)    |
| 0DD192  | Rally Flag (Luck)      | FF 45 F0 (INC)    |
| 0DC96B  | Rally Flag (Morale)    | FF 45 F0 (INC)    |
| 0DC9C0  | Warrior Tomb           | 83 6D F0 03 (ADD 03)|
| 0DC7F4  | Idol of Fortune (Morale)| FF 45 F0 (INC)   |
| 0DC899  | Temple (+2)            | 83 45 F0 02 (ADD 02)|
| 0DD007  | Fountain of Fortune (+1)| FF 45 F0 (INC)   |
| 0DD09D  | Fountain of Fortune (+2)| 01 75 F0 (ADD ESI)|
| 0DD0E8  | Fountain of Fortune (+3)| 83 45 F0 03 (ADD 03)|


>(Don't forget to update ArrayTxt.txt with any changes you make!)

-----------------------------------------------------------------------------------------

	------		-------------------------------------------------------------------------
	0A93E2		; MERMAIDS TO +1 MORALE & LUCK
	------		-------------------------------------------------------------------------
	E9 F5CAFFFF	jmp 4A5EDC		; -> free space
	90		nop			; -

	---------	-------------------------------------------------------------------------
	0A5EDC~F4	; (OVERWRITES TEMPLE DAY 7 CHECK)
	---------	-------------------------------------------------------------------------
	88 87 1B010000	mov [edi+11B],al	; update hero Luck
	8A 87 1A010000	mov al,[edi+11A]	; AL = hero Morale
	FE C0		inc al			; AL +1
	88 87 1A010000	mov [edi+11A],al	; update hero Morale
	E9 F3340000	jmp 4A93E8		; return to original code

	0A9371 > 0E	; adds "MoraleUp" graphic to textbox
	4DC7F9 > 06	; hijack right click check from Bouy
	4DC7FD > 80	; ""

	-----------------------------------------------------------------------------------------

	------		-------------------------------------------------------------------------
	0A85BE		; BOUYS TO +MOVEMENT (INSTEAD OF +MORALE)
	------		-------------------------------------------------------------------------
	0C 04		or al,04		; AL = sets "Bouy" flag (04)
	89 81 05010000	mov [ecx+105],eax	; update hero data
	8B 51 49	mov edx,[ecx+49]	; EDX = maximum hero movement
	E9 27D9FFFF	jmp 0A5EF5		; -> free space
	89 51 49	mov [ecx+49],edx	; update hero movement
	89 71 4D	mov [ecx+4D],esi	; ""

	---------	-------------------------------------------------------------------------
	0A5EF5~05	; (OVERWRITES TEMPLE DAY 7 CHECK)
	---------	-------------------------------------------------------------------------
	8B 71 4D	mov esi,[ecx+4D]	; EDX = current hero movement
	B8 58020000	mov eax,00000258	; EAX = movement bonus (58 02 = 600)
	01 C2		add edx,eax		; Add EAX to EDX
	01 C6		add esi,eax		; Add EAX to ESI
	E9 C8260000	jmp 0A85CE		; return (0A5F06~F is free space)

	0A863B > FF	; removes "MoraleUp" graphic from textbox
	0DC7FE > EB	; skips right click check for morale bonus (not needed w/ Mermaid hack)

-----------------------------------------------------------------------------------------

Lastly, if you've gone the route of removing morale bonuses from map locations which also boost movement
to focus solely on that aspect, you may wish to have them be visitable at least once per day instead of
requiring the hero to win a battle first. The instruction at 0C7D9F (81 E7 FE FF FD FF) clears two flags
on all active heroes at the beginning of their respective turns: Magic Well and (for some reason) "hero
is in a tavern". We can adjust this to also clear the flags for other map locations, as well:

	    81 E7 3EBFFDFF = Oasis, Watering Hole, & Fountain of Youth
	    81 E7 3ABFFDFF = Oasis, Watering Hole, Fountain of Youth, & Bouy

-----------------------------------------------------------------------------------------

Also on the subject of movement-boosting map objects are Lighthouses and Stables, both of which can be
easily edited in Movement.txt without any bullshit. Speaking of bullshit, something of an easter egg in
the original game is that external stables on the map will upgrade any Cavaliers you have to Champions
free of charge. Cute, but kinda broken and it probably needs to go. Let's get rid of it:

	---------	-------------------------------------------------------------------------
	4A5D6B~70	; EXTERNAL STABLES DO NOT UPGRADE CAVALIERS
	---------	-------------------------------------------------------------------------
	E9 8B000000	jmp 4A5DFB		; -> (shortened code; see below)
	90		nop			; -

	----------	-------------------------------------------------------------------------
	0A5DFB~E10	; ""
	----------	-------------------------------------------------------------------------
	8A 45 10	mov al,[ebp+10]		; EAX = AI flag
	84 C0		test al,al		; AI player?
	0F85 73FFFFFF	jne 4A5D79		; if no -> [no upgrade]
	6A 0B		push 0B			; (upgrade cavaliers)
	6A 0A		push 0A			; ""
	8B CE		mov ecx,esi		; ""
	E9 60FFFFFF	jmp 4A5D71		; -> [continue] (0A5E11~58 is free space)

As you can see, we leave in an exception for AI players which allows them to still get the upgrade. This
is because the AI is expecting the result of upgraded Cavaliers and will get "stuck" stepping on and off
of the Stables tile if it doesn't get it. It's something that I may or may not look into dealing with in
a more elegant fashion in the future, but it's a low-priority fix at most.

---------------------------------------------------------------------------------------------------------

## WATER WHEELS & WINDMILLS

These are being discussed together since they're both bread and butter map locations that provide steady
weekly benefits that could both stand to be just a little bit better. Let's start off with Water Wheels,
which provide 500 gold on the first week of the game and then 1,000 every week thereafter. The example
below will change that amount to 500 times the week number, which resets at the beginning of each month.
Thus: 500 gold on week 1, 1,000 gold on week 2, 1,500 gold on week 3, and 2,000 gold on week 4.

	---------	-------------------------------------------------------------------------
	0A7A69~74	; WATER WHEELS TO GIVE 500 GOLD * WEEK
	---------	-------------------------------------------------------------------------
	84 C0		test al,al		; already been visited this week?
	75 D5		jne 4A7A42		; if no -> free space
	90 90		nop			; -
	8D 04 80	lea eax,[eax+eax*4]	; EAX * 5
	6B C0 64	imul eax,eax,64		; EAX * 100

	--------	-------------------------------------------------------------------------
	0A7A42~F	; (EXPANDED SPACE - UNUSED IN ORIGINAL CODE)
	--------	-------------------------------------------------------------------------
	8B 35 38956900	mov esi,[699538]	; ESI = main index
	8A 86 40F60100	mov al,[esi+1F640]	; EAX = week number
	EB 1F		jmp 4A7A6F		; -> return

-----------------------------------------------------------------------------------------

Next is Windmills, which are most notably annoying in that they can potentially provide ore even though
they're ostensibly intended purely as a source of magical resources. The reason this occurs is quickly
apparent if you glance at the resource index (or the game's interface): ore comes after mercury when it
should come before it so that both resource types are grouped together in the code, and clearly nobody
felt like putting in an exception (or, y'know, fucking fixing it). Thankfully, a little bit of the 'ol
"push/pop" optmization in the randomization subroutines can free up enough space for an inline fix.

>(Yes, I said subroutines, plural - there are two of them for some reason)

	---------	-------------------------------------------------------------------------
	0C1D00~1F	; WINDMILLS TO ONLY GIVE RARE RESOURCES (WEEK ONE)
	---------	-------------------------------------------------------------------------
	6A 03		push 03			; minimum quantity = 3
	6A 05		push 05			; maximum quantity = 5
	5A		pop edx			; ""
	59		pop ecx			; ""
	E8 B5AA0400     call 50C7C0		; (EAX = min~max)
	8B F8		mov edi,eax		; EDI = quantity
	6A 02		push 02			; minimum type = 2 (Ore)
	6A 05		push 05			; maximum type = 5 (Gems)
	5A 		pop edx			; ""
	59		pop ecx			; ""
	E8 A8AA0400	call 50C7C0		; (EAX = min~max)
	83 F8 02	cmp eax,02		; Ore?
	75 03		jne 4C1D20		; if no -> [exit]
	48		dec eax			; EAX = 1 (Mercury)
	90 90		nop			; -

	---------	-------------------------------------------------------------------------
	0C8926~45	; WINDMILLS TO ONLY GIVE RARE RESOURCES (SUBSEQUENT WEEKS)
	---------	-------------------------------------------------------------------------
	6A 03		push 03			; minimum quantity = 3
	6A 05		push 05			; maximum quantity = 5
	5A		pop edx			; ""
	59		pop ecx			; ""
	E8 8F3E0400	call 50C7C0		; (EAX = min~max)
	8B F8		mov edi,eax		; EDI = quantity
	6A 02		push 02			; minimum type = 2 (Ore)
	6A 05		push 05			; maximum type = 5 (Gems)
	5A		pop edx			; ""
	59		pop ecx			; ""
	E8 823E0400	call 50C7C0		; (EAX = min~max)
	83 F8 02	cmp eax,02		; Ore?
	75 05		jne 4C8946		; if no -> [exit]
	48		dec eax			; EAX = 1 (Mercury)
	90 90 		nop			; -

>(As for the resource positioning on the interface, we'll look at fixing that later on)

---------------------------------------------------------------------------------------------------------

## STAT BOOSTERS

Schools of War and Magic are functionally near-identical to the four "free" +1 stat boosters, trading a
choice of attribute for a tuition fee. Let's look into making them a little more effective:

#### School of War

| Address  | Code                    | Description               |
|----------|-------------------------|---------------------------|
| 0A786C   | FE C0 > 04 XX           | -                         |
| 0A77C3   | XX                      | -                         |
| 0A77CD   | XX                      | -                         |
| 0A774F   | E8 03 (1,000 gold)      | 1,000 gold income        |
| 0A788F   | 18 FC (-1,000 gold)     | -1,000 gold expenditure  |

#### School of Magic

| Address  | Code                    | Description               |
|----------|-------------------------|---------------------------|
| 0A31CD   | FE C3 > 80 C3 XX        | -                         |
| 0A316A   | XX                      | -                         |
| 0A3174   | XX                      | -                         |
| 0A30EF   | E8 03 (1,000 gold)      | 1,000 gold income        |
| 0A31F3   | 18 FC (-1,000 gold)     | -1,000 gold expenditure  |

Schools of Magic are slightly more complicated because they use EBX to increment the chosen stat instead
of EAX, meaning that the ADD opcode is 1 byte longer than INC (+1). If you're just looking to raise the
bonus to +2, then 43 43 (INC EBX twice) will accomplish that with no dramas. For anything more, there's
some unused space at the end of the Magic School routine that will allow us to shift everything down by
one byte, after which we'll just need to adjust a few jumps and we're good to go:

	0A31C0:	-- -- -- -- -- -- -- -- -- -- -- -- -- 80 C3 XX	    0A31B9: 3C > 3D
	0A31D0:	B8 01 00 00 00 88 9C 3E 76 04 00 00 8B 09 8B 57	    0A3194: 61 > 62
	0A31E0:	77 D3 E0 0B D0 89 57 77 A1 FC CC 69 00 81 80 B4	    0A30FC: F6 > F7
	0A31F0:	00 00 00 18 FC FF FF 5F 5E 5B 5D C2 10 00 90 90	    0A3073: 7F > 80

-----------------------------------------------------------------------------------------

More curious are Arenas and Libraries of Enlightenment - one would expect them to be mirror counterparts
to each other, with the former giving +2 to both Attack and Defense (instead of just one) and the latter
raising both Knowledge and Spell Power (instead of all four primary stats), both with the requirement of
a level "X" hero. There is a somewhat-hidden feature which will lower the level requirement by two for
each level in Diplomacy, which we can remove if desired by setting 0A2F52 and 12946F to 8D 02 90, but we
can do better than that. Instead, let's have it require a combined Magic and Knowledge stat of 10:

	---------	-------------------------------------------------------------------------
	0A2F47~54	; LIBRARY REQUIRES 10 (MAGIC + KNOWLEDGE) INSTEAD OF LEVEL/DIPLOMACY
	---------	-------------------------------------------------------------------------
	31 C0		xor eax,eax		; EAX = 0
	8A 86 78040000	mov al,[esi+478]	; EAX = hero's Magic Power
	02 86 79040000	add al,[esi+479]	; EAX + hero's Knowledge

	---------	-------------------------------------------------------------------------
	129464~71	; "" (AI)
	---------	-------------------------------------------------------------------------
	31 C0		xor eax,eax		; EAX = 0
	8A 83 78040000	mov al,[ebx+478]	; EAX = hero's Magic Power
	02 83 79040000	add al,[ebx+479]	; EAX + hero's Knowledge

>(The required value of 10, regardless of whether the above code is used, is set at 0A2F57 and 129474)

Now, let's move on to the Library only raising two attributes. Note that, as an added bonus, this will
allow us to graphically display the attributes in the resulting message box rather than just plain text.

		0A2F6B > 53 90			0A2F6F > 53 90
		0A2F77 > 02 (+2)		0A2F81 > 02 (+2)
		0A2F79 > 21 (Spell Power)	0A2F83 > 22 (Knowledge)

	---------	-------------------------------------------------------------------------
	0A2F92~A1	; LIBRARY TO BOOST MAGIC AND KNOWLEDGE ONLY
	---------	-------------------------------------------------------------------------
	80867804000002	add byte [esi+478],02	; +2 Magic
	80867904000002	add byte [esi+479],02	; +2 Knowledge
	EB 1A		jmp 4A2FCC		; (4A2FA2~CB is free space)

-----------------------------------------------------------------------------------------

			And now let's change up arenas...

	09E460 > 91	; adjusted jump (AI on a revisit... for some reason?)
	09E49D > 3D	; skip textbox and requirements for AI
	09E49E > EB 5B	; human players jump to ATK+DEF check
	09E4D2 > 01	; standard confirm box (no multiple choice)

	---------	-------------------------------------------------------------------------
	09E4DB~FA	; ARENA TO BOOST ATTACK AND DEFNESE
	---------	-------------------------------------------------------------------------
	80877604000002	add byte [edi+476],02	; +2 Attack
	80877704000002	add byte [edi+477],02	; +2 Defense
	8B 55 0C	mov edx,[ebp+0C]	; EDX = object data
	52		push edx		; push to set "visited" flag for hero
	8B CF		mov ecx,edi		; ECX = hero data
	E8 5C710400	call 4E5650		; set "visited" flag
	5B		pop ebx			; ""
	5F		pop edi			; ""
	5E		pop esi			; ""
	5D		pop ebp			; ""
	C2 0C00		ret 000C		; return

	----------	-------------------------------------------------------------------------
	09E4FB~527	; ARENA REQUIRES 10 (ATTACK + DEFENSE)
	----------	-------------------------------------------------------------------------
	8A 87 76040000	mov al,[edi+476]	; AL = hero's Attack
	02 87 77040000	add al,[edi+477]	; AL + hero's Defense
	3C 0A		cmp al,0A		; is Attack + Defense 10?
	7C 04		jl 49E50F		; if less -> (fail)
	6A FF		push -01		; (displaced code)
	EB 91		jmp 49E4A0		; return

	58		pop eax			; (fail) remove 4 bytes from stack
	B9 045D6A00	mov ecx,6A5D04		; ArrayTxt, line 246
	8B 09		mov ecx,[ecx]		; (set up textbox)
	6A 00		push 00			; ""
	6A FF		push -01		; ""
	6A 00		push 00			; ""
	6A FF		push -01		; ""
	6A 00		push 00			; ""
	6A FF		push -01		; ""
	E9 0C4B0000	jmp 4A3034		; -> [continue] (09E528~5F is free space)

As with Libraries, we check for a combined Attack + Defense score here instead of level. If you want to
use level instead, write 8A 47 55 90 90 90 90 90 90 90 90 90 in place of the first two instructions in
the above code. For the rejection dialogue box, we use line 246 from ArrayTxt ("Extra Quick", the first
free line after our Wisdom edits from earlier). The remainder of the free lines can be called thusly:

	08 5D 6A 00: 247 (Very Quick)	    18 5D 6A 00: 251 (Extra Fast)
	0C 5D 6A 00: 248 (Ultra Quick)	    1C 5D 6A 00: 252 (Very Fast)
	10 5D 6A 00: 249 (Super Quick)	    20 5D 6A 00: 253 (Ultra Fast)
	14 5D 6A 00: 250 (Fast)		    24 5D 6A 00: 254 (Super Fast)

to be done: right-click info box for Arenas
bug-ish: AI ignores requirements

---------------------------------------------------------------------------------------------------------

## EXPERIENCE & LEVEL-UP OBJECTS

Learning Stones should be a simple edit but unfortunately are not since they loads the experience bonus
as a floating value for some reason rather than an integer. Specifically, it multiplies a floating value
of 1 by 1000 (0A6001 = F0E46300). We've seen enough of these by now to know how they work, but none of
them have been values even remotely close to this high. Thus, if you want to change it, you'll need to
create your own floating value somewhere else and point to it.

Trees of Wisdom are thankfully much easier to edit. When the map loads, each tree is randomly set to one
of three options: 2000 gold, 10 gems, or free. If desired, we can force one of these options like so:

    0C1B3C > 6A (XX) 58 90 90 ; always free (00) / always gold (01) / always gems (02)

    0A6430 > E9 90 01 00 00 ; always free (frees space: 0A6435~5C4)
    0A6430 > E9 D7 00 00 00 ; always gold (frees space: 0A6435~50B, 0A65C5~F7)
    0A6430 > EB 1D          ; always gems (frees space: 0A6432~4E, 0A650C~F7)

Further, the values and required resources for both of the non-free options are easily customizable:

		           GEMS                    GOLD
		           ----                    ----
		    A6456: B0 = Gems(*)    0A6514: B4 = Gold(*)
		    A6502: B0 = Gems(*)    0A65BB: B4 = Gold(*)
		    A64E8: 05 = Gems       0A65A5: 06 = Gold
		    A64E6: 0A = 10         0A6519: D0 07 = 2000
		    A645F: 0A = 10         0A65A0: D0 07 = 2000
		    A6506: F6 = -10        0A65BF: 30 F8 = -2000

>(*Other resources: Wood = 9C, A0 = Mercury, A4 = Ore, A8 = Sulfur, AC = Crystal)

-----------------------------------------------------------------------------------------

Altars of Sacrifice provide static values for artifacts according to their level as follows:

				ARTIFACT VALUES
			-------------------------------
			(Lv.1) 15FECA = E8030000 (1000)
			(Lv.2) 15FED3 = DC050000 (1500)
			(Lv.3) 15FEDC = B80B0000 (3000)
			(Lv.4) 15FEE5 = 70170000 (6000)

For units, it provides 1/8 of their AI value. For a simple edit, you can double this to 1/4 by changing
164EE1 and 1630D2 from 4 to 3. More drastically, we can change it to 1/3 of the unit's gold value:

	---------	-------------------------------------------------------------------------
	1630C5~D5	; ALTAR OF SACRIFICE UNIT EXPERIENCE TO 1/3 OF ITS GOLD VALUE
	---------	-------------------------------------------------------------------------
	8B 4C 90 38	mov ecx,[eax+edx*4+38]	; ECX = gold value
	B8 56555555	mov eax,55555556	; EDX = ECX / 3
	F7 E9		imul ecx		; ""
	0FAF 56 1C 	imul edx,[esi+1C]	; EDX * number of units to be sacrificed
	EB 0B		jmp 5630E1		; -> [continue] (1630D6~E0 is free space)

	---------	-------------------------------------------------------------------------
	164ED4~E2	; ""
	---------	-------------------------------------------------------------------------
	8B 54 82 38	mov edx,[edx+eax*4+38]	; ECX = gold value

	B8 56555555	mov eax,55555556	; EDX = ECX / 3
	F7 EA		imul edx		; ""
	8B FA		mov edi,edx		; EDX * number of units to be sacrificed
	EB 09		jmp 564EEC		; -> [continue] (164EE3~B is free space)

Altars of Sacrifice are one of the few points in the game where hero alignment (good, neutral, or evil)
comes into play: good heroes may only sacrifice artifacts and evil ones may only sacrifice units, while
neutral heroes can sacrifice either. While flavorful, this is a quite senseless restriction in practice.
To allow sacrificing either regardless of class, set 160561 to 6A 01 59 EB 22 (free space: 160566~87).

-----------------------------------------------------------------------------------------

Finally, we have Sirens. The percentage of your army that remains (not that which you lose) is a QWORD
pointer at 1283DA (88 E6 63 00 = 70%). Changing the DC at 1283D8 to D8 switches it to DWORD, which makes
it easier for us swap in other values: B0 B8 63 00 (40%), CC B8 63 00 (50%), 98 05 64 00 (75%), or AC B8
63 00 (80%). There's also E0 B7 63 00 (90%), which is the only alternate QWORD value I know of, but at
that point you really need to start looking into increasing the experience gain per unit.

We have several options on how to go about this, one of which is to use the AI value of units like the
Altars of Sacrifice do instead of their HP (like experience from combat does). To do this, change 1283FE
from 4C to 3C. Whether we do this or not, we'll need to free up some space at the end of the routine for
some final adjustments since using just the unmodified AI values would be grossly overpowered.

Thankfully, there's some free space after the Siren routine, so we can just move the code like so:

	128419~3F > XX XX XX XX XX XX XX XX XX XX XX XX XX YY YY YY YY YY DB 45
		    FC D9 5D F0 D8 4D F0 E8 5B FB 0E 00 5F 5E 5B 8B E5 5D C3

	YY YY YY YY YY = E865C2FBFF (if you swapped the Learning and Eagle Eye bonus code earlier)
	YY YY YY YY YY = E885C6FBFF (if you have not moved Learning to the Eagle Eye bonus code)

This gives us 13 bytes (XX XX XX...) for the solution of our choice. Which route we take will depend on
if we want to lower the final result (if we switched to using AI values) or raise it (we stuck with HP).
To this end, here are two basic templates to work from:

### MULTIPLY/DIVIDE

| Assembly  | Mnemonic | Description                 |
|-----------|----------|-----------------------------|
| 8B 45 FC  | mov eax, [ebp-04] | Load value from [ebp-04] into eax |
| 6B C0 XX  | imul eax, (XX)    | Multiply eax by (XX)                |
| C1 F8 XX  | sar eax, (XX)     | Arithmetic right shift eax by (XX) bits |
| 89 45 FC  | mov [ebp-04], eax | Store the result back into [ebp-04]  |
| 90        | nop               | No operation                         |

### MULTIPLY/ADD

| Assembly  | Mnemonic | Description                 |
|-----------|----------|-----------------------------|
| 8B 45 FC  | mov eax, [ebp-04] | Load value from [ebp-04] into eax |
| 01 C0     | add eax, eax      | Add eax to itself (multiply by 2) |
| 05 XX XX XX XX | add eax, (XXXX) | Add (XXXX) to eax                  |
| 89 45 FC  | mov [ebp-04], eax | Store the result back into [ebp-04]  |

Starting on the left, we multiply a given integer and then divide by two "X" times. The multiply command
isn't necessary and can be NOP'ed (with 90's) if the desired result can be reached just though division
by two (i.e. 50%, 25%, 12.5%). But to get, say, 75%, we multiply by three and then divide twice by two.
This template will also work if you want to raise the final result; either NOP out the division or, for
example, multiply by five and then divide by two once to get 250% of the original value.

On the right, we double the final product and then add a baseline value to supplement it. The double is
optional (NOP out "add eax,eax" to remove it) and the only reason we're not using a more robust command
is the same reason that we don't have any addition on the left: we've only got 13 bytes to work with for
an inline edit. That said, you probably don't want to go too crazy with the multiplication if you've
added a baseline, so this should be sufficient for most anyone's needs.

Alternatively, we can scrap the idea of unit loss altogether and just invoke a battle with Harpies:

	----------	-------------------------------------------------------------------------
	1283A9~411	; SIRENS TO CALL BATTLE WITH HARPIES
	----------	-------------------------------------------------------------------------
	6A 00		push 00			; (text box setup)
	6A FF		push -01		; ""
	6A 00		push 00			; ""
	6A FF		push -01		; ""
	6A 00		push 00			; ""
	6A FF		push -01		; ""
	6A 00		push 00			; ""
	6A FF		push -01		; ""
	6A FF		push -01		; ""
	6A FF		push -01		; ""
	A1 686A6900	mov eax,[696A68]	; EAX = AdvEvent index
	8B 48 20	mov ecx,[eax+20]	; ECX = ???
	8B 89 18020000	mov ecx,[ecx+218]	; AdvEvent, line 135 (now a confirmation box)
	6A 02		push 02			; EDX = 02 (yes/no selection)
	5A		pop edx			; ""
	E8 2DE8FCFF	call 4F6C00		; message box
	8B 15 D0926900	mov edx,[6992D0]	; was "okay" clicked?
	817A3806780000	cmp [edx+38],7806	; ""
	74 57		je 528439		; if no -> [exit]
	6A 00		push 00			; (battle setup)
	6A 00		push 00			; ""
	6A FF		push -01		; ""
	6A 06		push 06			; 6 stacks
	6A 5A		push 5A			; 90 units
	6A 48		push 48			; 48 = Harpies
	8B 55 10	mov edx,[ebp+10]	; ???
	52		push edx		; ???
	8D 45 08	lea eax,[ebp+08]	; ???
	50		push eax		; ???
	50		push eax		; ???
	6A 49		push 49			; 49 = Harpy Hags
	C745081E000000	mov [ebp+08],1E		; 30 Units
	57		push edi		; push hero data
	8B CE		mov ecx,esi		; ECX = adventure manager
	E8 683EF8FF	call 4AC270		; call battle
	8B CF		mov ecx,edi		; ECX = hero data
	85 C0		test eax,eax		; did hero win battle?
	74 10		je 52841E		; if no -> exit
	31 C0		xor eax,eax		; EAX = 0
	EB 27		jmp 528439		; -> [continue] (128412~D is free space)

	12841E > B8 C4090000 ; 2,500 experience reward (C4 09)

	----------	-------------------------------------------------------------------------
	0A56A7~BD	; SIRENS (CONT.)
	----------	-------------------------------------------------------------------------
	8B 87 05010000	mov eax,[edi+105]	; frees space: 0A56BE~EF
	0D 00001000	or eax,100000		; ""
	89 87 05010000	mov [edi+105],eax	; ""
	5E		pop esi			; ""
	5F		pop edi			; ""
	5D		pop ebp			; ""
	C2 0C00		ret 000C		; ""

	0A560A > AB	; change jump pointer
	0A5655 > 62	; ""

>AdvEvent line 135, formerly "no units lost", is repurposed here as a confirmation dialogue

---------------------------------------------------------------------------------------------------------

## SKILL & SPELL TEACHING OBJECTS

One of the most noteworthy irritants in the base game (which is also commonly fixed in most mods) is the
inability to decline skills taught by Witch Huts, forcing you to reload a previous save if it's garbage
like Eagle Eye. Let's look at fixing it using more of the space we freed up from the magic spring:

-----------------------------------------------------------------------------------------

	0A7E64 > 02	; adds a "cancel" button to Witch Hut dialogue window

	------		-------------------------------------------------------------------------
	0A7E85		; WITCH HUT SKILL REFUSAL
	------		-------------------------------------------------------------------------
	E9 71B4FFFF     jmp 4A32FB		; -> free space (magic spring)

	---------	-------------------------------------------------------------------------
	0A32FB~1E	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	---------	-------------------------------------------------------------------------
	8A 45 10	mov al,[ebp+10]		; AL = player
	84 C0		test al,al		; is player AI?
	74 13		je 4A3315		; if yes -> (displaced code)
	8B 0D D0926900	mov ecx,[6992D0]	; (prepares ECX to check player response)
	81793805780000	cmp [ecx+38],7805	; did player click "OK" (yes)?
	0F85 7A4B0000	jne 4A7E8F		; if no -> [return - do not add skill]
	6A 01		push 01			; (displaced code)
	56		push esi		; ""
	8B CB		mov ecx,ebx		; ""
	E9 6B4B0000	jmp 4A7E8A		; return - add skill

	-----------------------------------------------------------------------------------------

	    Further, let's get Witch Huts to respect the inability of classes to learn skills.

	------		-------------------------------------------------------------------------
	0A7D93		; WITCH HUTS TO RESPECT CLASS INABILITY TO LEARN SKILLS
	------		-------------------------------------------------------------------------
	E9 87B5FFFF	jmp 4A331F		; -> free space (magic spring)
	90 90		nop			; -

	---------	-------------------------------------------------------------------------
	0A331F~4C	; (EXPANDED SPACE - OVERWRITES MAGIC SPRING)
	---------	-------------------------------------------------------------------------
	8B 0D ECDC6700	mov ecx,[67DCEC]	; ECX = class traits index
	0FBE 43 30	movsx eax,[ebx+30]	; EAX = hero class
	C1 E0 06	shl eax,06		; EAX = data range
	01 C1		add ecx,eax		; ECX = class data

	80 7C 31 18 00	cmp byte[ecx+esi+18],00	; is this class unable to learn this skill?
	75 0C		jne 4A3341		; if no -> (pass)

	8A 45 10	mov al,[ebp+10]		; AL = AI flag
	84 C0		test al,al		; AI player?
	74 05		je 4A3350		; if yes -> (pass)
	E9 9D4A0000	jmp 4A7DDE		; -> [rejection message]

	8A8433C9000000	mov al,[ebx+esi+C9]	; (pass - displaced code)
	E9 4D4A0000	jmp 4A7D9A		; -> [continue] (0A334D~9F is free space)

>we leave in an allowance for the AI to avoid "bouncing"

-----------------------------------------------------------------------------------------

	Contrary to Witch Huts and Scholars, I really don't have much to say about Universities that I haven't
	already covered earlier. I don't yet know how they load skills, so I can't say how to prevent them from
	doing so for skills you've removed from the game (such as Eagle Eye), but they aren't problematic since
	Universities respect inability to learn spells; removed skills will simply be blank entries (for now).

	What we can do, however, is edit the tuition costs from 2000 gold to, say, something more representative
	of how schools gouge the shit out of you in real life by editing all of the addresses below:

	1F0CF1: D0070000 (2000)     1F0FD6: D0070000 (2000)	1F1374: D0070000 (2000)
	1F02FC: D0070000 (2000)     1F10EE: D0070000 (2000)	1F147D: 30F8FFFF (-2000)

	    (Note that these changes will also affect Conflux's Magic University since it uses the same code)

	-----------------------------------------------------------------------------------------

	While Witch Huts won't teach either Necromancy or Leadership by default - and Universities will at least
	refuse to teach them to ineligible classes - spell shrines lack a similar override to prevent them from
	teaching Necromancer spells to Non-Necromancers. Let's go ahead and add one:

	----------	-------------------------------------------------------------------------
	0C19FC~200	; SPELL SHRINES BAN NECRO SPELLS (Lv.2)
	----------	-------------------------------------------------------------------------
	E8 6EF6FDFF	call 4A106F		; -> free space (Idol of Fortune, even day)

	--------	-------------------------------------------------------------------------
	0C1A67~B	; SPELL SHRINES BAN NECRO SPELLS (Lv.3)
	--------	-------------------------------------------------------------------------
	E8 03F6FDFF	call 4A106F		; -> free space (Idol of Fortune, even day)

-----------------------------------------------------------------------------------------

Even with this change, however, an inherent problem with spell shrines is that the spells they provide
(if random instead of specifically set in the map editor) are unlikely to be useful since the odds of
your hero possessing the requisite magic skill are relatively low and, if you do, there's a good chance
that it will be redundant with your mage guild. To this end, let's look at changing shrines to instead
sell scrolls, which we changed earlier to always cast spells at a minimum of basic expertise.

	---------	-------------------------------------------------------------------------
	0A5364~72	; SPELL SHRINES SELL SCROLLS
	---------	-------------------------------------------------------------------------
	E8 37010000	call 4A54A0		; -> free space (Wisdom check)
	0F8D A2000000	jge 4A5411		; -> not enough money (AdvEvent, Line 175)
	90 90 90 90	nop			; -

	--------	-------------------------------------------------------------------------
	0A5577~E	; ""
	--------	-------------------------------------------------------------------------
	E8 F5FEFFFF	call 4A5471		; -> free space (Wisdom check)
	90 90 90	nop			; -

	---------	-------------------------------------------------------------------------
	0A5459~BC	; INLINE EDIT (OVERWRITES WISDOM CHECK)
	---------	-------------------------------------------------------------------------
	8A 45 18	mov al,[ebp+18]		; ~~~needs finished commentary
	84 C0		test al,al		; AI player?
	0F85 EA000000	jne 4A554E		; if no -> sell scroll
	56		push esi		;
	8B CF		mov ecx,edi		;
	E8 34410300	call 4D95A0		; AI learns spell
	E9 0E010000	jmp 4A557F		;

	A1 D0926900	mov eax,[6992D0]	; was "okay" clicked?
	81783805780000	cmp [eax+38],7805	;
	74 01		je 4A5480		;
	C3		ret			;
	56		push esi		; ESI is spell ID
	6A 01		push 01			; 01 = scroll
	8D 0C 24	lea ecx,[esp]		;
	6A 01		push 01			;
	6A 01		push 01			;
	51		push ecx		;
	8B CF		mov ecx,edi		; ECX = hero data
	E8 4EDE0300	call 4E32E0		; add scroll
	59		pop ecx			;
	59		pop ecx			;
	E8 07000000	call 4A54A0		;
	29 81 B4000000	sub [ecx+B4],eax	; subtract money
	C3		ret			;

	8A 43 1E	mov eax,[ebx+1E]	;
	2C 58		sub al,58		;
	6B C0 64	imul eax,64		;
	6B C0 0A	imul eax,0A		;
	05 F4010000	add eax,1F4		;
	8B 0D FCCC6900	mov ecx,[69CCFC]	; EAX = active player data
	39 81 B4000000	cmp [ecx+B4],eax	; money check
	C3		ret			;

	0A556E > 02 ; add cancel button
	277752 > 00 00 00 00 ; text edit
	00D982 > E9 C9000000 ; remove "already learned" right click (00D987~EE is free space)

---------------------------------------------------------------------------------------------------------

## HILL FORTS & GARRISONS

The cost of upgrading units at a Hill Fort is dependent on the unit's level. The cost will be multiplied
according to the below table, which can be used to provide either a discount (as seen with the original
settings) or a markup. Note that, in order for first-level units to be set to anything other than free,
you will also need to change 0E8095 to EB (this will free space: E8097~DF).

	(Lv.1) 23EB4C = 00000000 (*Free)	(Lv.5) 23EB5C = 0000803F (1.00)
	(Lv.2) 23EB50 = 0000803E (0.25)		(Lv.6) 23EB60 = 0000803F (1.00)
	(Lv.3) 23EB54 = 0000003F (0.50)		(Lv.7) 23EB64 = 0000803F (1.00)
	(Lv.4) 23EB58 = 0000403F (0.75)

-----------------------------------------------------------------------------------------

Garrisons are a bit more curious since they offer nothing in the way of actual defense and, aside from
the anti-magic variety, are objectively worse than leaving units in a town where they'd have the benefit
of a hero with magic and stat boosts. Their best use, in theory, is to allow heroes to enforce a zone of
control by forcing any passing hero to fight them. One would expect them to act like forts, providing at
least siege walls and possibly a moat to its defenders. So let's look into setting that up:

	------		-------------------------------------------------------------------------
	0A8D55		; GARRISONS TO ACT AS SIEGE BATTLES (NO HERO)
	------		-------------------------------------------------------------------------
	E9 DBD6FFFF	jmp 4A6435		; -> free space (wise tree, gems)

	---------	-------------------------------------------------------------------------
	0A6435~4B	; (EXPANDED SPACE - OVERWTIES WISE TREE, GEMS)
	---------	-------------------------------------------------------------------------
	FF 05 023B6700	inc [673B02]		; set temp flag (no hero, just units)
	E8 206D0000	call 4AD160		; (displaced code)
	C605023B670000	mov byte [673B02],00	; needed for AI battles
	E9 0E290000 	jmp 4A8D5A		; return

	------		-------------------------------------------------------------------------
	0A8DCA		; GARRISONS TO ACT AS SIEGE BATTLES (WITH HERO)
	------		-------------------------------------------------------------------------
	E9 7DD6FFFF	jmp 4A644C		; -> free space (wise tree, gems)

	---------	-------------------------------------------------------------------------
	4A644C~5C	; (EXPANDED SPACE - OVERWTIES WISE TREE, GEMS)
	---------	-------------------------------------------------------------------------
	E8 1FC0FFFF	call 4A2470		; displaced code
	C605023B670000	mov byte [673B02],00	; needed for AI battles
	E9 72290000	jmp 4A8DCF		; reutrn

	------		-------------------------------------------------------------------------
	0A249F		; ""
	------		-------------------------------------------------------------------------
	E8 B93F0000	call 4A645D		; -> free space (wise tree, gems)
	90 90		nop			;

	---------	-------------------------------------------------------------------------
	0A645D~70	; (EXPANDED SPACE - OVERWTIES WISE TREE, GEMS)
	---------	-------------------------------------------------------------------------
	8DB44A20160200	lea esi,[edx+ecx*2+21620] ; ESI = hero data
	80 7E 0C 21	cmp byte ptr [esi+0C],21  ; is hero standing on a garrison?
	75 06		jne 4A6470		  ; if no -> return
	FF 05 023B6700	inc [673B02]		  ; set "temp" flag for garrison battle
	C3		ret			  ; return

	------		-------------------------------------------------------------------------
	063707		; GARRISONS TO ACT AS SIEGE BATTLES (MAIN ROUTINE)
	------		-------------------------------------------------------------------------
	E9 652D0400	jmp 4A6471		; -> free space (wise tree, gems)

	---------	-------------------------------------------------------------------------
	0A6471~D4	; (EXPANDED SPACE - OVERWTIES WISE TREE, GEMS)
	---------	-------------------------------------------------------------------------
	8A 15 023B6700	mov dl,[673B02]		; DL = temp flag
	84 D2		test dl,dl		; are we in a garrison?
	74 50		je 4A64CB		; if no -> displaced code

	FF 0D 023B6700	dec [673B02]		; unset "temp" flag
	8B 15 B8926900	mov edx,[6992B8]	; EDX = ???
	8B 42 58	mov eax,[edx+58]	; EAX = terrain

	83 F8 01	cmp eax,01		; Sand > Conflux (+7)
	74 1B		je 4A64AA
	83 F8 04	cmp eax,04		; Swamp > Fortress (+3)
	74 18		je 4A64AC
	83 F8 05	cmp eax,05		; Wasteland > Stronghold (+1)
	74 15		je 4A64AE
	83 F8 00	cmp eax,00		; Dirt > Rampart (+1)
	74 10		je 4A64AE
	83 F8 07	cmp eax,07		; Lava > Inferno (-4)
	74 0E		je 4A64B1
	83 F8 02	cmp eax,02		; Grassland > Castle (-2)
	74 0B		je 4A64B3
	EB 0A		jmp 4A64B4		; Snow/Sub-T > Tower/Dungeon (-1)

	04 04		add al,04		; +7
	40		inc eax			; +3
	40		inc eax			; -
	40		inc eax			; +1
	EB 04		jmp 4A64B4		; -> ECX = 1
	48		dec eax			; -4
	48		dec eax			; -
	48		dec eax			; -2
	48		dec eax			; -1

	41		inc ecx			; ECX = 1 (fort)
	89 8E F4320100	mov [esi+132F4],ecx	; set fort
	B9 203B6700	mov ecx,673B20		; ECX = 673B20 (this is our "town")
	89 41 04	mov [ecx+04],eax	; Town +4 = terrain
	8B D1		mov edx,ecx		; EDX = town
	E9 B1D2FBFF	jmp 46377C		; return to after Fort level has been checked

	8B 55 18	mov edx,[ebp+18]	; (displaced code)
	39 CA		cmp edx,ecx		; ""
	E9 37D2FBFF	jmp 46370C		; return

	--------	-------------------------------------------------------------------------
	063920~6	; GARRISONS WILL NOT PROVIDE TOWN BUILDING BONUSES
	--------	-------------------------------------------------------------------------
	E9 B02B0400	jmp 4A64D5		; -> free space (wise tree, gems)
	90 90		nop			; -

	---------	-------------------------------------------------------------------------
	0A64D5~E5	; (EXPANDED SPACE - OVERWTIES WISE TREE, GEMS)
	---------	-------------------------------------------------------------------------
	3D 203B6700	cmp eax,673B20		; garrison?
	75 03		jne 4A64DF		; if no -> jump table
	31 C9		xor ecx,ecx		; ECX = default exit (no buildings)
	41		inc ecx			; ""
	FF248D643C4600	jmp [ecx*4+463C64]	; -> [building bonuses]

	--------	-------------------------------------------------------------------------
	077F15~A	; ALLOW ESCAPE FROM GARRISON FIGHTS
	--------	-------------------------------------------------------------------------
	E9 CCE50200 	jmp 4A64E6		; -> free space (wise tree, gems)
	90		nop			; -

	---------	-------------------------------------------------------------------------
	0A64E6~FE	; (EXPANDED SPACE - OVERWTIES WISE TREE, GEMS)
	---------	-------------------------------------------------------------------------
	80 79 05 00	cmp byte [ecx+05],00	; garrisons check X coordinate to allow retreat
	0F84 491AFDFF	je 477F39		; if yes -> allow retreat
	80 79 04 06	cmp byte [ecx+04],06	; stronghold?
	0F85 561AFDFF	jne 477F50		; if no -> continue
	E9 1C1AFDFF	jmp 477F1B		; 0A64FF~50B is free space

Because we provide garrisons with walls by literally turnning them into towns, there are a few things to
consider. First is that we try to match up each terrain with its most appropriate town style - depending
on what else you change, you might want go with Necropolis for dirt instead of Rampart and/or Stronghold
for sand instead of Conflux. Second is that since it's looking at town code, we need a hard override to
stop it from trying to provide the stat bonuses from that town's buildings. Third, we also need a hard
override to allow retreat since you normally can't do that from siege battles. The way we do this is a
bit cheeky: we check the town's X coordinate and allow retreat if it's 0; this should only return true
for garrisons since towns will otherwise never be placed that close to the edge of the map.

---------------------------------------------------------------------------------------------------------

## WHIRLPOOLS & TELEPORTERS

To remove the effect of units being sent overboard, set 0A921A~F to 90 90 90 90 90 90. This will free up
a substantial amount of space (0AC783~89F), which we can use to change how the whirlpool system works.
Rather than them existing as one giant network, they will instead be linked as pairs according to the
order in which they were placed on the map. As an added bonus, since teleporters run through the same
code, we also have two-way portal networks exit sequentially instead of randomly.

There are a few caveats to this setup, the biggest being that AI players will still treat whirlpools as
one unified network because the AI expects it and they will otherwise get "stuck" on them. Also, the top
layer of the map will always be generated before the bottom layer, so regardless of the order whirlpools
were placed there can only be one possible connecting pair between the surface and the underground. I'd
like to fix both of these issues at some point in the future, but can't say when that might be.

	---------	-------------------------------------------------------------------------
	0CD94E~52	; ZELDA-STYLE WHIRLPOOLS (SETUP)
	---------	-------------------------------------------------------------------------
	E8 30EEFDFF	call 4AC783		; -> free space (whirlpool unit loss)

	---------	-------------------------------------------------------------------------
	0AC783~9F	; (EXPANDED SPACE - WHIRLPOOL UNIT LOSS)
	---------	-------------------------------------------------------------------------
	80 7D 10 2C	cmp byte [ebp+10],2C	; one-way portal?
	75 0E		jne 4AC797		; if no -> EAX = 0
	E8 32000600	call 50C7C0		; random exit
	C3		ret 			; return
	90		nop			; -
	90909090909090	nop			; (unusuable space)
	31 C0		xor eax,eax		; EAX = 0
	89 45 F8	mov [ebp-08],eax	; EPB-08 = closest destination (higher)
	89 45 20	mov [ebp+20],eax	; EBP+20 = counter
	C3		ret 			; return

	----------	-------------------------------------------------------------------------
	0CD9B4~A42	; ZELDA-STYLE WHIRLPOOLS (CONT.)
	----------	-------------------------------------------------------------------------
	81 F9 FFFF0F00	cmp ecx,FFFFF		; sanity check to prevent crashes
	0F87 83000000	ja 4CDA43		; ""
	8B 44 4A 1E	mov eax,[edx+ecx*2+1E]	; EAX = destination object type
	8D 14 4A	lea edx,[edx+ecx*2]	; EDX = destination object data
	83 F8 22	cmp eax,22		; 22 = ???
	75 3F		jne 4CDA0B		; if no -> compare destination object to source
	F6 42 0D 10	test byte [edx+0D],10	; (optimized code)
	74 39		je 4CDA0B		; ""
	8B 02		mov eax,[edx]		; ""
	8B 0D 38956900	mov ecx,[699538]	; ""
	69 C0 92040000	imul eax,eax,492	; ""
	8D840820160200	lea eax,[eax+ecx+21620]	; ""
	0FBE 40 0C	movsx eax,[eax+0C]	; ""
	EB 1E		jmp 4CDA0B		; ""

	3B 45 10	cmp eax,[ebp+10]	; compare destination object to source
	75 19		jne 4CDA29		; if not the same -> next object
	8B 45 14	mov eax,[ebp+14]	; EAX = source ID
	8B 0A		mov ecx,[edx]		; ECX = destination ID
	3B C8		cmp ecx,eax		; is destination the source?
	74 10		je 4CDA29		; if yes ->
	E8 82EDFDFF	call 4AC7A0		; -> free space (whirlpool unit loss)
	80 7D 10 2C	cmp byte [ebp+10],2C	; one-way portal?
	75 05		jne 4CDA29		; if no -> next object
	FF 4D FC	dec [ebp-04]		; are we done checking one-way portals?
	74 38		je 4CDA61		; if yes -> [exit]
	8B 45 F0	mov eax,[ebp-10]	; next object
	FF 45 F0	inc [ebp-10]		; ""
	83 45 08 04	add [ebp+08],04		; ""
	3B 45 F4	cmp eax,[ebp-0C]	; are we done checking?
	0F8C 39FFFFFF	jl 4CD975		; if no -> check next object
	E8 DBEDFDFF	call 4AC81C		; -> free space (whirlpool unit loss)
	75 1E		jne 4CDA61		; if there is a valid destination -> [continue]

	----------	-------------------------------------------------------------------------
	0AC7A0~854	; (EXPANDED SPACE - WHIRLPOOL UNIT LOSS)
	----------	-------------------------------------------------------------------------
	80 7D 10 2C	cmp byte [ebp+10],2C	; one-way portal?
	75 0A		jne 4AC7B0		; if no -> CX = destination object ID
	F6 42 0D 10	test byte [edx+0D],10	; is destination occupied?
	75 03		jne 4AC7AF		; if yes -> return
	FF 45 FC	inc [ebp-04]		; increment counter
	C3		ret			; return

	66 8B 4A 24	mov cx,[edx+24]		; CX = destination object ID
	52		push edx		; store EDX
	8B 55 D8	mov edx,[ebp-28]	; EDX = source object data
	66 8B 42 24	mov ax,[edx+24]		; AX = source object ID
	5A		pop edx			; retrieve EDX
	39 C8		cmp eax,ecx		; compare source ID to destination
	72 3F		jb 4AC800		; if destination is higher -> higher destination

	FF 45 20	inc [ebp+20]		; update number of higher destinations
	F6 42 0D 10 	test byte [edx+0D],10	; is (lower) destination occupied?
	74 35		je 4AC7FF		; if yes -> return
	83 7D FC 00	cmp [ebp-04],00		; do we have a stored ID lower than source?
	74 28		je 4AC7F8		; if no -> store (lower) destination
	A1 FCCC6900	mov eax,[69CCFC]	; EAX = active player data
	8A 80 E1000000	mov al,[eax+E1]		; AL = AI flag
	84 C0		test al,al		; AI player?
	74 06		je 4AC7E5		; if yes -> AX = stored destination ID (two-way)
	80 7D 10 2D	cmp byte [ebp+10],2D	; two-way portal?
	75 0A		jne 4AC7EF		; if no -> AX = stored destination ID (whirlpool)
	66 8B 45 24	mov ax,[ebp+24]		; AX = stored destination ID (two-way)
	66 39 C8	cmp ax,cx		; is new destination ID lower than the stored ID?
	77 0A		ja 4AC7F8		; if yes -> store new destination
	C3		ret			; return
	66 8B 45 24	mov ax,[ebp+24]		; AX = stored destination ID (whirlpool)
	66 39 C8	cmp ax,cx		; is new destination ID closer to the source ID?
	77 07		ja 4AC7FF		; if no -> return
	89 75 FC	mov [ebp-04],esi	; store new (lower) destination coordinates
	66 89 4D 24	mov [ebp+24],cx		; store new (lower) destination ID
	C3		ret			; return

	F6 42 0D 10 	test byte [edx+0D],10	; is (higher) destination occupied?
	74 15		je 4AC81B		; if yes -> return
	83 7D F8 00	cmp [ebp-08],00		; do we have a stored ID higher than source?
	74 08		je 4AC814		; if no -> store (higher) destination
	66 8B 45 26	mov ax,[ebp+26]		; AX = stored destination ID
	39 C8		cmp eax,ecx		; is new destination ID closer to the source ID?
	72 07		jb 4AC81B		; if no -> return
	89 75 F8	mov [ebp-08],esi	; store new (higher) destination coordinates
	66 89 4D 26	mov [ebp+26],cx		; store new (higher) destination ID
	C3		ret			; return

	80 7D 10 2C	cmp byte [ebp+10],2C	; one-way portal?
	74 27		je 4AC849		; if yes ->
	80 7D 10 2D	cmp byte [ebp+10],2D	; two-way portal?
	74 24		je 4AC84C		; if yes -> ESI = higher destination
	A1 FCCC6900	mov eax,[69CCFC]	; EAX = active player data
	8A 80 E1000000	mov al,[eax+E1]		; AL = AI flag
	84 C0		test al,al		; AI player?
	74 15		je 4AC84C		; if yes -> ESI = higher destination
	8B 45 20	mov eax,[ebp+20]	; EAX = # of destinations higher than source
	D1 F8		sar eax,1		; EAX / 2 (each whirlpool is 6 destinations)
	8B C8		mov ecx,eax		; ECX = EAX
	D1 F9		sar ecx,1		; EAX / 2 (drops remainder)
	01 C9		add ecx,ecx		; ECX + ECX
	39 C8		cmp eax,ecx		; ECX will = EAX if source ID is an odd number
	74 06		je 4AC84C		; if odd -> ESI = higher destination
	8B 75 FC	mov esi,[ebp-04]	; ESI = lower destination
	85 F6		test esi,esi		; is ESI empty?
	C3		ret			; return
	8B 75 F8	mov esi,[ebp-08]	; ESI = higher destination
	85 F6		test esi,esi		; is ESI empty?
	75 F8		jne 4AC84B		; if no -> return (0AC856~89F is free space)
	EB F1		jmp 4AC846		; -> ESI = lower destination

---------------------------------------------------------------------------------------------------------

## CARTOGRAPHERS

There are three types of cartographers: one that reveals all land tiles except for subterranean tiles,
one that reveals just all subterranean tiles, and one that reveals all water tiles. This is restrictive
in that it assumes that the underground layer will consist only of subterranean terrain, which it more
often than not doesn't. The below code will edit the two terrestrial cartographers to simply reveal all
of the non-water tiles in a map layer (surface or underground) regardless of terrain.

	---------	-------------------------------------------------------------------------
	0C9F7D~B2	; TERRESTRIAL CARTOGRAPHERS REVEAL ALL NON-WATER TILES IN MAP LAYER
	---------	-------------------------------------------------------------------------
	8B 8A 44FC0100	mov ecx,[edx+1FC44]	; (shifted code)
	8B C1		mov eax,ecx		; ""
	0FAF C3		imul eax,ebx		; ""
	01 F0		add eax,esi		; ""
	0FAF C1		imul eax,ecx		; ""
	01 F8		add eax,edi		; ""
	6B C0 13	imul eax,eax,13		; ""
	8B 8A 40FC0100	mov ecx,[edx+1FC40]	; ""
	8B 4C 41 04	mov ecx,[ecx+eax*2+04]	; CL = terrain type
	8B 45 08	mov eax,[ebp+08]	; EAX = cartographer type (00/40/BF)
	01 D8		add eax,ebx		; EAX +1 for underground tiles
	3C 01		cmp al,01		; water cartographer? (EAX = 00 or 01)
	77 07		ja 4C9FAC		; if no -> water tile? (terrestrial cartographer)
	80 F9 08	cmp cl,08		; water tile?
	74 09		je 4C9FB3		; if yes -> [reveal tile]
	EB 1B		jmp 4C9FC7		; -> [do not reveal tile]
	80 F9 08	cmp cl,08		; water tile? (terrestrial cartographer)
	74 16		je 4C9FC7		; if yes -> [do not reveal tile]
	EB 43		jmp 4C9FF6		; -> free space

	---------	-------------------------------------------------------------------------
	0C9FF6~FF	; (EXPANDED SPACE - UNUSED IN ORIGINAL GAME)
	---------	-------------------------------------------------------------------------
	3C 41		cmp al,41		; surface cartographer and tile?
	74 B9		je 4C9FB3		; if yes -> [reveal tile]
	3C BF		cmp al,-41		; sub-t cartographer and tile?
	74 B5		je 4C9FB3		; if yes -> [reveal tile]
	EB C7		jmp 4C9FC7		; -> [do not reveal tile]

---------------------------------------------------------------------------------------------------------

## TREASURE CHESTS & SEA CHESTS

You can change the amount of gold and/or experience you get from chests more or less to
your liking with a few caveats. First, to change the base amount of gold...

	---------	---------------------------------------------------------
	0A6262~70	; MODIFIABLE TREASURE CHEST VALUES
	---------	---------------------------------------------------------
	BA F4 01 00 00	mov edx,01F4	; EDX = "base" gold amount (01F4 = 500)
	90		nop		; (optional - see below)
	F7 EA		imul edx	; EAX = (EAX * EDX)
	90909090909090	nop		; -

By default, EAX is a random number here from 2~4, which corresponds with treasure chests
containing 1000, 1500, or 2000 gold, respectively. If desired, we can either increment
this value by changing the first 90 to a 40 (so 3~5 times the base value) or decrement
it with	a 48 (1~3 times the base value). Or, for more complex math, feel free to utilize
the 7 bytes of free space we have left over from optimizing this routine.

The static difference between experience and gold is specified as a DWORD value at 0A60C5
(0C FE FF FF). This is just like the gold value above, except you're counting backwards
to 500 (since it's a negative value) instead of forward. Alternatively, we can also make
the experience value half of the gold value by changing 0A60C3 to 8B C7 D1 F8 90 90.

We can also adjust the odds of each "tier" of treasure appearing:

				Tier 1 - 0C1AC3
				Tier 2 - 0C1AD9
				Tier 3 - 0C1AEB

Like with tavern advice, these addresses represent a range for each tier. We find a "20"
at 0C1AC3, which is 32 in decimal, which translates into a 32% chance of rolling tier 1.
At 0C1AD9, we find a 40, or 64(%) in decimal. Since a roll of 32 (out of 100) will go to
tier 1, this designates 33~64 as the tier 2 range, meaning that it also has a 32% chance
of being landed on. 0C1AEB, finally, is 5F, or 95, giving tier 3 a 31% chance (65~95) of
appearing. The remaining 5%, then, gives us an artifact. You can lower 5F as much as you
want to increase the chances of getting an artifact, bearing in mind that you may wish to
adjust the values at 0C1AC3 and 0C1AD9 to compensate. You can also raise 0C1AEB to 64 so
that artifacts can no longer be found in chests at all.

Sea chests use an identical structure, except the only two "tiers" are nothing and 1,500
gold, with the remainder again resulting in an artifact + 1,000 gold. These parameters
can be adjusted at the following addresses:

		0C1862: 14 (20% odds of nothing)
		0C1872: 5A (70% odds of 1,500 gold, 10% for 1,000 + artifact)

		0A4DA5: DC 05 00 00 = 1500 gold
		0A4DBD: ""

		0A4D40: E8 03 00 00 = 1000 gold
		0A4D65: ""

That said, getting nothing from a sea chest is kind of shitty, and it's also strange how
they don't provide the choice of experience like regular chests do. Let's look at adding
that choice, converting the chance of nothing into an actual reward in the process. This
will still leave us with just three tiers (two gold/experience and one gold + artifact),
but we will be able to adjust them to our liking just as with regular chests earlier.

	---------	-------------------------------------------------------------------------
	0A4CB7~EE	; SEA CHESTS TO OFFER CHOICE OF GOLD OR EXPERIENCE
	---------	-------------------------------------------------------------------------
	89 45 FC	mov [ebp-04],eax	; ~~~needs finished commentary
	89 45 F8	mov [ebp-08],eax	;
	8B F1		mov esi,ecx		;
	83 C7 03	add edi,03		; EDI = 3~5 (5 = artifact)
	83 FF 05	cmp edi,05		; artifact?
	7C 0F		jl 4A4CD6		; if no -> EDI is multiplier for gold
	8B 4D 08	mov ecx,[ebp+08]	;
	6A 01		push 01			;
	E8 5F460300	call 4D9330		;
	83 F8 40	cmp eax,40		;
	7C 19		jl 4A4CEF		;
	83 FF 05	cmp edi,05		;
	7E 03		jle 4A4CDE		;
	6A 05		push 05			;
	5F		pop edi			;
	68 F4010000	push 1F4		; 1F4 = 500 gold (base amount)
	58		pop eax			;
	F7 EF		imul edi		;
	8B 4D 14	mov ecx,[ebp+14]	;
	51		push ecx		;
	E9 9B000000	jmp 4A4D8A		;

	---------	-------------------------------------------------------------------------
	0A4D88~97	; ""
	---------	-------------------------------------------------------------------------
	74 73		je 4A4DFD		; ~~~ needs commentary
	8B 5D 08	mov ebx,[ebp+08]	; ""
	50		push eax		; ""
	53		push ebx		; ""
	8B CE		mov ecx,esi		; ""
	E8 1A130000	call 4A60B0		; ""
	EB 65		jmp 4A4DFD		; -> [continue] (0A4D98~FC is free space)

The key instruction to note above is when we add 3 to EDI, which starts out as 0 for the
"nothing" roll, 1 for 1,500 gold, and 2 for an artifact. We add to it here so we can use
it as the multiplier for our gold bonus later on, giving us 1,500 gold for the "nothing"
roll and 2,000 for the old 1,500 gold roll. Simply adjust this addition as desired for
the multiplier you want and then the following "cmp" instruction to match, since this is
checking for the artifact roll (2 + whatever) and sending it off to its own routine.

Finally, you're also able to adjust the "tier" of artifact received from treasure chests.
By default, only "treasure"-level artifacts (the weakest kind) can appear. The levels of
artifacts which can be found in chests is specified as a bitmask value at 0C1B02 for
regular treasure chests and 0C1887 for sea chests:

				BIT 4 (10) Relic
				BIT 5 (08) Major
				BIT 6 (04) Minor
				BIT 7 (02) Treasure

-----------------------------------------------------------------------------------------

## SHIPWRECK SURVIVORS & WARRIOR TOMBS

The odds of receiving each level of artifact from these locations is structured just like
the chest tiers above, with the first address specifying the odds of a "treasure"-class
artifact, the next two specifying the cumulative total for minor and major artifacts, and
the remainder being your odds of a relic. The addresses for each are as follows:

		SHIPWRECK SURVIVOR		WARRIOR'S TOMB
		------------------		--------------
		0C18C0 (Treasure)		0C1BEA (Treasure)
		0C18D5 (Minor)			0C1BF6 (Minor)
		0C18EA (Major)			0C1C04 (Major)

Assuming you remove the morale penalty for searching a warrior tomb (as discussed earlier
in this section), there's really no reason to have a confirmation prompt to do so. We can
remove this prompt by setting 0A78B6 to EB 7B, which frees up 0A78B8~F6.

-----------------------------------------------------------------------------------------

## MR. BONES (AKA "CORPSE")

The 20% odds of finding an artifact are set at 0C0DFF and the possible treasure levels
(see above for the bitmask settings) are set at 0C0E03 (06 = treasure or minor artifact).
If your hero's backpack is full, you'll instead get 1000 gold (set at 0A51E7 and 0A51F7).

-----------------------------------------------------------------------------------------

## FLOTSAM

four possible results, DWORD exits are as follows:

	4A20E0	BD 1E 4A 00 (nothing)
	4A20E4	F9 1E 4A 00 (5 wood)
	4A20E8	38 1F 4A 00 (5 Wood, 200 gold)
	4A20EC	83 1F 4A 00 (10 wood, 500 gold)

	5 Wood: 0A1F1B, 0A1F30
	---
	5 Wood: 0A1F5D, 0A1F72
	200 gold: 0A1F4F, 0A1F7C
	---
	10 wood: 0A1FA8, 0A1FBD
	500 gold: 0A1F9B, 0A1FC8

-----------------------------------------------------------------------------------------

## LOOSE RESOURCES

	0C17DE - maximum (wood/ore/gold)
	0C17E3 - minimum (wood/ore/gold)
	0C17B1 - maximum (mr/sf/cr/gm)
	0C17B6 - minimum (mr/sf/cr/gm)

-----------------------------------------------------------------------------------------

## CAMPFIRES

	0C0BA6 - quantity maximum
	0C0BAB - quantity minimum

	0C0BB8 - type maximum
	0C0BBC - type minimum (XOR = 0)

-----------------------------------------------------------------------------------------

## WAGONS

	0C1B96 0A = 10% odds of nothing
	0C1BA7 32 = 50% odds of artifact (else resource)
	0C1BB5 06 = artifact bitmask
	0C1B6F 05 - resource maximum
	0C1B74 02 - resource minimum

-----------------------------------------------------------------------------------------

## LEAN-TO'S

	0C123B - type maximum
	0C123F - type minimum (XOR = 0)

	0C1247 - quantity maximum
	0C124C - quantity minimum

-----------------------------------------------------------------------------------------

## REDWOOD OBERSVATORY/PILLAR OF FIRE

`0A9709 = 14 (view radius)`

-----------------------------------------------------------------------------------------

## CURSED GROUND

To remove the effects of Cursed Ground on spellcasting...

	19EE28 > EB	; in battle (this will make free space: 19EE2A~69)
	01C555 > 00 	; Cursed ground adventure map
	01C571 > EB	; "" (01C573~DC is free)

(Above overridden by wisdom mage guild change)

	092007 > EB	; unit spellcasters 092009~1C
	1A83ED > EB	; "" (free space: 1A83EF~405)

	-----------------------------------------------------------------------------------------


	277978 - table: value for all mines (except gold - the value here is unused)
	278288 - table: text string for all mines (including gold mines)

	0A0927 > EB 3A	; Skip Pandora's Box confirmation (0A0929~62 is free)
	0A0A0D > EB 32	; Skip Pandora's Box "empty" message (0A0A0F~40 is free)
	0A0995 > EB	; Skip Pandora's Box "trap" message 0A0997~C0 is free)

---------------------------------------------------------------------------------------------------------

## OBELISKS

Obelisk percentages required for AI to search for grail are at:

	282318: Easy	(9A 99 99 99 99 99 F1 3F = AI does not look for grail)
	282320: Normal	(00 00 00 00 00 00 E0 3F = over 75%)
	282328: Hard	(00 00 00 00 00 00 D0 3F = over 50%)
	282330: Expert	(00 00 00 00 00 00 00 00 = just one obelisk)
	282338: Ream Me	(00 00 00 00 00 00 00 00 = "")

Other breakpoints are C0 3F (at least 25%) and F0 3F (all obleisks are required)

-----------------------------------------------------------------------------------------

Let's look at requiring all of the obelisks for both the player and AI before you can dig
for the grail. For the AI, this is quite easy: we simply load a static QWORD value where
it would normally look for the table above. For the player, we hijack the requirement of
not being able to dig unless the hero has not yet moved (which is no longer necessary for
balance purposes if all obelisks are required) and jump to some free space.

Oddly, the code checks in two places to see if your hero has moved: once before and again
after asking you if you really want to dig. The first check occurs in HD_SOD.dll instead
of the main .exe file, which carries with it the same warning as when we edited Inferno's
Castle Gate: since HD Mod is still being updated, the address below is subject to change.
Again, you can double-check by looking at the preceding instruction (3B 51 49).

		01B503 (HD_SOD.dll): 0F 85 D4 00 00 00 > 90 90 90 90 90 90

	---------	--------------------------------------------------------------------------
	12CEDA~E0	; AI MUST FIND ALL OBELISKS BEFORE DIGGING FOR GRAIL
	---------	--------------------------------------------------------------------------
	DD 05 50AC6300	fld qword ptr [63AC50]	; frees space: 282318~3F
	90		nop			; -
	
	---------	--------------------------------------------------------------------------
	00EC3B~4E	; PLAYER MUST FIND ALL OBELISKS BEFORE DIGGING FOR GRAIL
	---------	--------------------------------------------------------------------------
	EB 05		jmp 40EC42		; (optimized code)
	31 FF		xor edi,edi		; ""
	89 7D F0	mov [ebp-10],edi	; ""
	31 DB		xor ebx,ebx		; EBX = 0
	E8 CF362700	call 682318		; -> free space (AI obelisk requirements)
	38 98 E8E30400	cmp [eax+4E3E8],bl	; has player seen every obelisk?
	
	---------	--------------------------------------------------------------------------
	282318~3F	; (EXPANDED SPACE - OVERWRITES AI OBELISK REQUIREMENTS)
	---------	--------------------------------------------------------------------------
	51		push ecx		; store ECX
	A1 38956900	mov eax,[699538]	; EAX = main index
	8A 0D F4CC6900	mov cl,[69CCF4]		; CL = player number
	31 D2		xor edx,edx		; DL = player bit
	42		inc edx			; ""
	D2 E2		shl dl,cl		; ""
	31 C9		xor ecx,ecx		; ECX = 0
	8AB408E9E30400	mov dh,[eax+ecx+4E3E9]	; DH = obelisk data
	84 D6		test dh,dl		; has player seen this obelisk?
	74 01		je 682337		; if no -> ECX +1
	43		inc ebx			; EBX +1 (# of obelisks that player has seen)
	41		inc ecx			; ECX +1 (next obelisk)
	83 F9 30	cmp ecx,30		; have we checked every obelisk?
	7C EE		jl 68232B		; if no -> DH = obelisk data
	59		pop ecx			; retrieve ECX
	C3		ret			; return
	
	0096B4 > F5 EB	; bypass initial movement check for "D" keyboard shortcut