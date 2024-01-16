## 2. HEROES

Everything about editing hero classes (i.e. Knight, Cleric, Ranger, etc.) is done via the HcTraits.txt
file inside the H3bitmap.lod archive. This includes their base attributes, attribute growth, secondary
skill growth, and appearance probabilities per town - as well as the "aggression" factor which seems to
determine how likely the AI is to attack when controlling that hero type. HoTraits.txt defines the names
of heroes and the values (but not type) of their starting unit stacks. Individual heroes are otherwise
handled mostly through two arrays in the .exe: one for most of their data and one for their specialties
(labeled below as "Bonus"). The offsets for each hero are as follows:


	KNIGHTS		DATA	BONUS		CLERICS		DATA	BONUS
	------------------------------		------------------------------
	Orrin		279DD0	278420		Rion		27A0B0	278560
	Valeska		279E2C	278448		Adela		27A10C	278588
	Edric		279E88	278470		Cuthbert	27A168	278588
	Sylvia		279EE4	278498		Adelaide	27A1C4	2785D8
	Lord Haart	279F40	2784C0		Ingham		27A220	278600
	Sorsha		279F9C	2784E8		Sanya		27A27C	278628
	Christian	279FF8	278510		Loynis		27A2D8	278650
	Tyris		27A054	278538		Caitlin		27A334	278678

	RANGERS		DATA	BONUS		DRUIDS		DATA	BONUS
	------------------------------		------------------------------
	Mephala		27A390	2786A0		Coronius	27A670	2787E0
	Ufretin		27A3EC	2786C8		Uland		27A6CC	278808
	Jenova		27A448	2786F0		Elleshar	27A728	278830
	Ryland		27A4A4	278718		Gem		    27A784	278858
	Thorgrim	27A500	278740		Malcom		27A7E0	278880
	Ivor		27A55C	278768		Melodia		27A83C	2788A8
	Clancy		27A5B8	278790		Alagar		27A898	2788D0
	Kyrre		27A614	2787B8		Aeris		27A8F4	2788F8

	ALCHEMISTS	DATA	BONUS		WIZARDS		DATA	BONUS
	------------------------------		------------------------------
	Piquedram	27A950	278920		Astral		27AC30	278A60
	Thane		27A9AC	278948		Halon		27AC8C	278A88
	Josephine	27AA08	278970		Serena		27ACE8	278AB0
	Neela		27AA64	278998		Daremyth	27AD44	278AD8
	Torosar		27AAC0	2789C0		Theodorus	27ADA0	278B00
	Fafner		27AB1C	2789E8		Solmyr		27ADFC	278B28
	Rissa		27AB78	278A10		Cyra		27AE58	278B50
	Iona		27ABD4	278A38		Aine		27AEB4	278B78

	DEMONIACS	DATA	BONUS		HERETICS	DATA	BONUS
	------------------------------		------------------------------
	Fiona		27AF10	278BA0		Ayden		27B1F0	278CE0
	Rashka		27AF6C	278BC8		Xyron		27B24C	278D08
	Marius		27AFC8	278BF0		Axsis		27B2A8	278D30
	Ignatius	27B024	278C18		Olema		27B304	278D58
	Octavia		27B080	278C40		Calid		27B360	278D80
	Calh		27B0DC	278C68		Ash		    27B3BC	278DA8
	Pyre		27B138	278C90		Zydar		27B418	278DD0
	Nymus		27B194	278CB8		Xarfax		27B474	278DF8

	DEATH KNIGHTS	DATA	BONUS		NECROMANCERS	DATA	BONUS
	------------------------------		------------------------------
	Straker		27B4D0	278E20		Septienna	27B7B0	278F60
	Vokial		27B52C	278E48		Aislinn		27B80C	278F88
	Moandor		27B588	278E70		Sandro		27B868	278FB0
	Charna		27B5E4	278E98		Nimbus		27B8C4	278FD8
	Tamika		27B640	278EC0		Thant		27B920	279000
	Isra		27B69C	278EE8		Xsi		    27B97C	279028
	Clavius		27B6F8	278F10		Vidomina	27B9D8	279050
	Galthran	27B754	278F38		Nagash		27BA34	279078

	OVERLORDS	DATA	BONUS		SORCERERS	DATA	BONUS
	------------------------------		------------------------------
	Lorelei		27BA90	2790A0		Alamar		27BD70	2791E0
	Arlach		27BAEC	2790C8		Jaegar		27BDCC	279208
	Dace		27BB48	2790F0		Malekith	27BE28	279230
	Ajit		27BBA4	279118		Jeddite		27BE84	279258
	Damacon		27BC00	279140		Geon		27BEE0	279280
	Gunnar		27BC5C	279168		Deemer		27BF3C	2792A8
	Synca		27BCB8	279190		Sephinroth	27BF98	2792D0
	Shakti		27BD14	2791B8		Darkstorn	27BFF4	2792F8

	BARBARIANS	DATA	BONUS		BATTLEMAGES	DATA	BONUS
	------------------------------		------------------------------
	Yog		    27C050	279320		Gird		27C330	279460
	Gurnisson	27C0AC	279348		Vey		    27C38C	279488
	Jabarkas	27C108	279370		Dessa		27C3E8	2794B0
	Shiva		27C164	279398		Terek		27C444	2794D8
	Gretchin	27C1C0	2793C0		Zubin		27C4A0	279500
	Krellion	27C21C	2793E8		Gundula		27C4FC	279528
	Crag Hack	27C278	279410		Oris		27C558	279550
	Tyraxor		27C2D4	279438		Saurug		27C5B4	279578

	BEASTMASTERS	DATA	BONUS		WITCHES		DATA	BONUS
	------------------------------		------------------------------
	Bron		27C610	2795A0		Mirlanda	27C8F0	2796E0
	Drakon		27C66C	2795C8		Rosic		27C94C	279708
	Wystan		27C6C8	2795F0		Voy		    27C9A8	279730
	Tazar		27C724	279618		Verdish		27CA04	279758
	Alkin		27C780	279640		Merist		27CA60	279780
	Korbac		27C7DC	279668		Styg		27CABC	2797A8
	Gerwulf		27C838	279690		Andra		27CB18	2797D0
	Broghild	27C894	2796B8		Tiva		27CB74	2797F8

	PLANESWALKERS	DATA	BONUS		ELEMENTALISTS	DATA	BONUS
	------------------------------		------------------------------
	Pasis		27CBD0	279820		Luna		27CEB0	279960
	Thunar		27CC2C	279848		Brissa		27CF0C	279988
	Ignissa		27CC88	279870		Ciele		27CF68	2799B0
	Lacus		27CCE4	279898		Labetha		27CFC4	2799D8
	Monere		27CD40	2798C0		Inteus		27D020	279A00
	Erdamon		27CD9C	2798E8		Aenain		27D07C	279A28
	Fiur		27CDF8	279910		Gelare		27D0D8	279A50
	Kalt		27CE54	279938		Grindan		27D134	279A78

	(CAMPAIGN)	DATA	BONUS		(CAMPAIGN)	DATA	BONUS
	------------------------------		------------------------------
	Sir Mullich	27D190	279AA0		Lord Haart	27D3B8	279B90
	Adrienne	27D1EC	279AC8		Mutare		27D414	279BB8
	Catherine	27D248	279AF0		Roland		27D470	279BE0
	Dracon		27D2A4	279B18		Mutare Drake	27D4CC	279C08
	Gelu		27D300	279B40		Boragus		27D528	279C30
	Kilgor		27D35C	279B68		Xeron		27D584	279C58

>(NOTE: Morgan Kendal and Ordwald are copies of other heroes and do not have their own data)

---------------------------------------------------------------------------------------------

				HERO DATA (92 bytes)
				--------------------

	BYTE 01: Gender				BYTE 37: 1st unit ID
	BYTE 05: Race				BYTE 41: 2nd unit ID *OR* war machine
	BYTE 09: Class				BYTE 45: 3rd unit ID
	BYTE 13: 1st skill (ID)			BYTE 49: Small portrait
	BYTE 17: 1st skill (level)		BYTE 53: Large portrait
	BYTE 21: 2nd skill (ID)			BYTE 57: Allowed in RoE (Y/N)
	BYTE 25: 2nd skill (level)		BYTE 58: Allowed in AB/SoD (Y/N)
	BYTE 29: Spellbook (Y/N)		BYTE 59: Campaign-only hero (Y/N)
	BYTE 33: Spell ID			BYTE 60: (Unused beyond this point)

While first stack of units for any hero is guaranteed, the second two are not. Set 0C94A0 to 00 for the
second stack to be guaranteed and 0C9522 to 00 for the third. By default, any hero beyond the first two
in your tavern each week will come with only one unit; to remove this rule, set 0C841C to 00.

The hero portraits are DWORD pointers to a table starting at 27DCF4 which specifies the actual filenames
to load. If you wish to change these for whatever reason, such as to allow your custom portraits to have
more organized names, it's generally best to edit the table directly (note the "text" column in your hex
editor) rather than editing the pointers in the hero data. Note that if you do change these, you'll also
want to edit the same table in the Map Editor, which starts at 189720.

The only hero with byte 58 set to 0 is Lord Haart, who is banned by default in any AB/SoD map unless Sir
Mullich is banned. This itself is problematic - you'll need to allow and then re-ban Mullich every time
you save the map to allow Haart to appear. The easiest solution I've found for this problem is to enable
Haart's "allowed in AB/SoD" flag in the map editor (1859A9: 00 -> 01) to enable manual control over his
availability. If both are enabled, Sir Mullich will be available to recruit in-game but unavailable as a
starting hero since the selection of starting heroes cuts off after 16.

To disable Sir Mullich from random maps, flag him as a campaign-only hero in Heroes3 HD.exe. To disable
him by default in new maps, do the same thing in the map editor (188BFA: -> 01).

-----------------------------------------------------------------------------------------------

			      HERO SPECIALTIES (28 bytes)
			      ---------------------------

		BYTE 01: Specialty type

			00 = Skill
			01 = Unit (scaling)
			02 = Resource
			03 = Spell
			04 = Unit (static)
			05 = Speed (Sir Mullich)
			06 = Conversion (Gelu & Dracon)
			07 = Dragon (Mutare)

		BYTE 05: Skill, Unit, Resource, or Spell ID (type 0-4),
			 1st unit ID allowed for conversion (type 6),
			 (*See below for type 5 bonus)

		BYTE 09: Attack bonus (type 4/7)

		BYTE 13: Defense bonus (type 4/7)

		BYTE 17: Damage bonus (type 4/7)

		BYTE 21: 2nd unit ID allowed for conversion (type 6)

		BYTE 25: Resulting unit ID after conversion (type 6)

>(*The type 5 speed bonus is actually a global setting located at 0E6669)


Skill bonuses are a flat 5% per level, but this is multiplicative rather than additive to
the base bonus (i.e. 5% of a 20% bonus is 1%, so the net result is a 21% bonus, not 25%).
This can be changed, either to a different percentage or to an additive bonus - how to do
so (and more) will be discussed in "Skills" section below.

Scaling unit specialties use a formula for their attack and defense bonuses that becomes
exponentially weaker at higher levels; the consensus is that this bonus is garbage beyond
2nd-level units aside from the +1 speed bonus that this specialty also provides, whereas
the bonus for 1st-level units has the potential to become extremely overpowered. Although
the scaling factor itself (a DWORD pointer located at 0E6548) is modifiable, the general
behavior - and thus the inherent underlying balance issue presented - is irreconcilable.
I would recommend switching to static unit specialties (type 4) in all cases.

The exception to the above recommendation is an Artillery skill bonus, which is actually
a scaling bonus with the ballista (ID 92) set as the specialized unit. You can increase
the strength of the bonus by lowering the ballista's level at 2745E4 (default 04: lv 5).
You can give it a bonus of +1 Attack (and/or Defense) per level (roughly) by setting the
level to 00, the base stat to 10, and the scaling factor to 10% (0E6548 > 40 23 64 00).
Better yet, keep reading for a much more customizable solution.

The value of resource specialties is hardcoded; the only one I know how to edit is gold
specialties (0E4681 = 5E 01 00 00, or 350 gold). These specialties are dumb, anyways.

Spell bonuses vary per the spell in question; this will be discussed later.

-------------------------------------------------------------------------------

The only drawback to moving from scaling to static unit specialties is that the latter does not have the
+1 speed bonus except for Xyron, who the code specifically checks for. However, we can rewrite the code
to not only include a customizable speed bonus, but also one for health using bytes 21 and 25 above.

    ---------	-------------------------------------------------------------------------
    **0E65AD~CF	; STATIC UNIT SPECIALTIES TO INCLUDE SPEED AND HEALTH BONUSES**
    ---------	-------------------------------------------------------------------------
    8B 47 08	mov eax,[edi+08]	; Byte 9 = Attack bonus
    01 46 54	add [esi+54],eax	; ""
    8B 47 0C	mov eax,[edi+0C]	; Byte 13 = Defense bonus
    01 46 58	add [esi+58],eax	; ""
    8B 47 10	mov eax,[edi+10]	; Byte 17 = Speed Bonus
    01 46 50	add [esi+50],eax	; ""
    8B 47 14	mov eax,[edi+14]	; Byte 21 = Damage bonus
    01 46 5C	add [esi+5C],eax	; ""
    01 46 60	add [esi+60],eax	; ""
    8B 47 18	mov eax,[edi+18]	; Byte 25 = Health bonus
    01 46 4C	add [esi+4C],eax	; ""
    EB 1A		jmp 4E65EA		; -> [continue]

>(Note that this will overwrite the check for Xeron, so his bonus will need to be updated)

Assuming the removal of the scaling bonus in a traditional sense (still leaving it intact for Artillery
specialists) and a completely useless check for basic elemental units on RoE maps, we can simplify the
code drastically while allowing for complete customization of the remaining specialty types:

    ---------	------------------------------------------------------------------
    **0E6457~D5	; NEW UNIT BONUS CODE (TYPES 1/4/5/7 - OVERWRITES ROE MAP CHECK)**
    ---------	------------------------------------------------------------------
    8B 55 08	mov edx,[ebp+08]	; EDX = unit ID
    83 F8 01	cmp eax,01		; type 1 (scaling unit) specialty?
    74 21		je 4E6480		; if yes -> ECX = hero's specialty unit
    83 F8 04	cmp eax,04		; type 4 (static unit) specialty?
    74 1C		je 4E6480		; if yes -> ECX = hero's specialty unit
    83 F8 05	cmp eax,05		; type 5 (global unit) specialty?
    74 2A		je 4E6493		; if yes -> apply bonus
    83 F8 07	cmp eax,07		; type 7 (dragon) specialty?
    75 63		jne 4E64D1		; if no -> [continue]
    6B D2 1D	imul edx,1D		; EDX = data range
    A1 B0476700	mov eax,[6747B0]	; EAX = unit index
    8A 44 90 13	mov al,[eax+edx*4+13]	; AL = unit data
    A8 80		test al,-80		; is unit a dragon?
    74 50		je 4E64CE		; if no -> [continue]
    EB 1E		jmp 4E649E		; -> apply bonus

    8B 4F 04	mov ecx,[edi+04]	; ECX = hero's specialty unit
    39 CA		cmp edx,ecx		; match? (if yes -> apply bonus)
    74 0C		je 4E6493		; ""
    E8 4446F9FF	call 47AAD0		; check for unit upgrade (EAX)
    8B 4D 08	mov ecx,[ebp+08]	; ECX = unit ID
    39 C1		cmp ecx,eax		; match? (if no -> [continue])
    75 3E		jne 4E64D1		; ""

    83 3F 01	cmp [edi],01		; type 1 (scaling unit) specialty?
    75 06		jne 4E649E		; if no -> ECX = 1
    0FBE 4B 55	movsx ecx, [ebx+55]	; ECX = hero's level
    EB 03		jmp 4E64A1		; -> apply bonus
    6A 01		push 01			; ECX = 1
    59		pop ecx			; ""

    8B 47 08	mov eax,[edi+08]	; Byte 9 = Attack bonus (* ECX)
    0FAF C1		imul eax,ecx		; ""
    01 46 54	add [esi+54],eax	; ""
    8B 47 0C	mov eax,[edi+0C]	; Byte 13 = Defense bonus (* ECX)
    0FAF C1		imul eax,ecx		; ""
    01 46 58	add [esi+58],eax	; ""
    8B 47 10	mov eax,[edi+10]	; Byte 17 = Speed bonus (* ECX)
    0FAF C1		imul eax,ecx		; ""
    01 46 50	add [esi+50],eax	; ""
    8B 47 14 	mov eax,[edi+14]	; Byte 21 = Damage bonus (* ECX)
    0FAF C1		imul eax,ecx		; ""
    01 46 5C	add [esi+5C],eax	; ""
    01 46 60	add [esi+60],eax	; ""
    8B 47 18 	mov eax,[edi+18]	; Byte 25 = Health bonus (* ECX)
    0FAF C1		imul eax,ecx		; ""
    01 46 4C	add [esi+4C],eax	; ""
    E9 14010000	jmp 4E65EA		; -> [continue] (0E64D3~5E9 is free space)

    0E6656 > EB 12	; remove old global speed bonus (0E6658~6A is free space)

Basically, type 1, 4, 5, and 7 specialties are all run through the same block of code that applies any
available attack, defense, speed, damage, and health bonuses. Type 5 - the old speed bonus - will apply
whatever bonuses are specified to all units while type 1 will multiply all bonuses by the hero's level.
This is effectively the old scaling bonus with the unit's level hard-coded to 1.

-----------------------------------------------------------------------------------------

When changing hero specialties, you will also need to edit HeroSpec.txt from the H3bitmap.lod archive as
well as the icons stored in UN32.def and UN44.def, both located in H3sprite.lod. The .def archives are
collections of images along with an index which lists the order in which they are called. In this case,
the order of the images in UN(XX).def is the hero index - the same order as they appear in HeroSpec.txt.

If a new specialty is added, such as 7th-level unit bonuses, then you'll need to create some new images.
To do this, extract the .def archive for the unit in question from H3sprite.lod, then select the desired
animation frame (usually the first one) as a base, resize it to 44x44, remove the transparency layer by
deleting all of the cyan pixels, then paste it onto the "blank" template image found in SecSkill.def.
For the UN32 icon, either resize the 44x44 icon or use the small unit portrait from CrSmall.def.

When doing this, be sure that the resulting image is still 256 colors - I prefer to promote images to 16
million colors before resizing them for better quality and then reduce the depth back to 256 afterward.
However, the first color in the palette index - generally the darkest color in the image - is set as the
transparent color in-game. So set this color to something bright/noticeable like hot pink and paint over
any instances of it in your image (usually just a pixel or two) with the closest color you have to it.

Note that the above information is applicable to any kind of graphics editing, such as creating your own
hero portraits. Feel free to edit any images you find, simply bearing in mind that they must be reduced
to 256-color bitmaps and the first color will always be treated as a transparency layer.


### EXPERIENCE & LEVELS

Experience requirements are set values up until level 12 (see table below), beyond which the requirement
for each successive level increases by 20% from the one prior:

Level 1: 279C88		Level 4: 279C8E		Level 7: 279C94		Level 10: 279C9A
Level 2: 279C8A		Level 5: 279C90		Level 8: 279C96		Level 11: 279C9C
Level 3: 279C8C		Level 6: 279C92		Level 9: 279C98		Level 12: 279C9E

This formula can be rewritten to something a lot more customizable - including a hard level cap of your
choosing - that also takes up much less space. The level code consists of three very similar blocks, all
of which need to be edited, as well as a fourth block for right-click info, a fifth to show you how much
experience is needed to reach the next level (used by Altars of Sacrifice), and a sixth for enforcing a
level cap on maps which feature them. The new code below specifies static experience increases for each
level between set thresholds: 1,000 experience per lv. until the 6th (5,000 total), 2,500 per lv. up to
10 (15,000 total), 5,000 per lv. up to 17 (50,000 total), 10,000 per lv, up to 22 (100,000 total), and
finally 25,000 per level up tp 30 (300,000 total), which is set as the maximum.

    ---------	-------------------------------------------------------------------------
    0DA69E~DB	; AUTO-LEVEL CODE
    ---------	-------------------------------------------------------------------------
    83 FE 06	cmp esi,06		; level 06?
    7E 11		jle 4DA6B4		; if less or equal -> "EAX = 1,000"

    83 FE 0A	cmp esi,0A		; level 10?
    7E 13		jle 4DA6BB		; if less or equal -> "EAX = 2,500"

    83 FE 11	cmp esi,11		; level 17?
    7E 15		jle 4DA6C2		; if less or equal -> "EAX = 5,000"

    83 FE 16	cmp esi,16		; level 22?
    7E 17		jle 4DA6C9		; if less or equal -> "EAX = 10,000"

    EB 1C		jmp 4DA6D0		; (lv. 23+) -> "EAX = 25,000"

    B8 E8030000	mov eax,03E8		; experience between levels (EAX) = 1,000
    EB 1A		jmp 4DA6D5		; -> (cleanup)
    B8 C4090000	mov eax,09C4		; experience between levels (EAX) = 2,500
    EB 13		jmp 4DA6D5		; -> (cleanup)
    B8 88130000	mov eax,1388		; experience between levels (EAX) = 5,000
    EB 0C		jmp 4DA6D5		; -> (cleanup)
    B8 10270000	mov eax,2710		; experience between levels (EAX) = 10,000
    EB 05		jmp 4DA6D5		; -> (cleanup)
    B8 A8610000	mov eax,61A8		; experience between levels (EAX) = 25,000
    5F		pop edi			; (cleanup)
    5E		pop esi			; ""
    5B		pop ebx			; ""
    8B E5		mov esp,ebp		; ""
    5D		pop ebp			; ""
    C3		ret			; return (0DA6DC~77F is free space)

    ----------	-------------------------------------------------------------------------
    0E37C4~811	; LEVEL-UP CODE A
    ----------	-------------------------------------------------------------------------
    31 D2		xor edx,edx		; EDX = 0
    3B DA		cmp ebx,edx		; compare hero's experience (EBX) to EDX
    0F 8C 97000000	jl 4E3865		; if less -> [raise hero's level to ECX-1]

    41		inc ecx			; ECX +1 (level counter; starts at 0)
    83 F9 06	cmp ecx,06		; level 06?
    7E 16		jle 4E37EA		; if less or equal -> "EDX +1,000"

    83 F9 0A	cmp ecx,0A		; level 10?
    7E 19		jle 4E37F2		; if less or equal -> "EDX +2,500"

    83 F9 11	cmp ecx,11		; level 17?
    7E 1C		jle 4E37FA		; if less or equal -> "EDX +5,000"

    83 F9 16	cmp ecx,16		; level 22?
    7E 1F		jle 4E3802		; if less or equal -> "EDX +10,000"

    83 F9 1E	cmp ecx,1E		; level 30?
    7E 22		jle 4E380A		; if less or equal -> "EDX +25,000"

    EB 7B		jmp 4E3865		; -> [level cap] (0E3812~3C is free space)

    81 C2 E8030000	add edx,03E8		; EDX +1,000
    EB D4		jmp 4E37C6		; -> compare EBX,EDX
    81 C2 C4090000	add edx,09C4		; EDX +2,500
    EB CC		jmp 4E37C6		; -> compare EBX,EDX
    81 C2 88130000	add edx,1388		; EDX +5,000
    EB C4		jmp 4E37C6		; -> compare EBX,EDX
    81 C2 10270000	add edx,2710		; EDX +10,000
    EB BC		jmp 4E37C6		; -> compare EBX,EDX
    81 C2 A8610000	add edx,61A8		; EDX +25,000
    EB B4		jmp 4E37C6		; -> compare EBX,EDX

    ----------	-------------------------------------------------------------------------
    0DA9BB~A0B	; LEVEL-UP CODE B
    ----------	-------------------------------------------------------------------------
    31 D2		xor edx,edx		; EDX = 0
    39 D7		cmp edi,edx		; compare hero's experience (EDI) to EDX
    0F 8C 10010000	jl 4DAAD5		; if less -> [raise hero's level to ECX-1]
    41		inc ecx			; ECX +1 (level counter; starts at 0)

    83 F9 06	cmp ecx,06		; level 06?
    7E 19		jle 4DA9E4		; if less or equal -> "EDX +1,000"

    83 F9 0A	cmp ecx,0A		; level 11?
    7E 1C		jle 4DA9EC		; if less or equal -> "EDX +2,500"

    83 F9 11	cmp ecx,11		; level 17?
    7E 1F		jle 4DA9F4		; if less or equal -> "EDX +5,000"

    83 F9 16	cmp ecx,16		; level 22?
    7E 22		jle 4DA9FC		; if less or equal -> "EDX +10,000"

    83 F9 1E	cmp ecx,1E		; level 30?
    7E 25		jle 4DAA04		; if less or equal -> "EDX +25,000"

    E9 F1000000	jmp 4DAAD5		; -> [level cap] (0DAA0C~39 is free space)

    81 C2 E8030000	add edx,03E8		; EDX +1,000
    EB D1		jmp 4DA9BD		; -> compare EDI,EDX
    81 C2 C4090000	add edx,09C4		; EDX +2,500
    EB C9		jmp 4DA9BD		; -> compare EDI,EDX
    81 C2 88130000	add edx,1388		; EDX +5,000
    EB C1		jmp 4DA9BD		; -> compare EDI,EDX
    81 C2 10270000	add edx,2710		; EDX +10,000
    EB B9		jmp 4DA9BD		; -> compare EDI,EDX
    81 C2 A8610000	add edx,61A8		; EDX +25,000
    EB B1		jmp 4DA9BD		; -> compare EDI,EDX

    ---------	-------------------------------------------------------------------------
    0DDB3F~A7	; TOTAL EXPERIENCE NEEDED FOR NEXT LEVEL (RIGHT-CLICK INFO)
    ---------	-------------------------------------------------------------------------
    31 C9		xor ecx,ecx		; ECX = 0

    83 F8 1E	cmp eax,1E		; level 30? (EAX = current level)
    74 62 		je 4DDBA8		; -> [max level has been reached]

    83 F8 16	cmp eax,16		; level 22?
    7C 10		jl 4DDB5B		; if less -> level 17?
    8D 78 EB	lea edi,[eax-15]	; EDI = (current level - 21)
    69 FF A8610000	imul edi,61A8		; EDI * 25,000
    01 F9		add ecx,edi		; Add EDI to total experience required (ECX)
    6A 05		push 05			; EDI = # of levels (5) separated by 10,000 exp.
    5F		pop edi			; ""
    EB 08		jmp 4DDB63		; -> EDI * 10,000

    83 F8 11	cmp eax,11		; level 17?
    7C 10		jl 4DDB70		; if less -> level 10?
    8D 78 F0	lea edi,[eax-10]	; EDI = (current level - 16)
    69 FF 10270000	imul edi,2710		; EDI * 10,000
    01 F9		add ecx,edi		; Add EDI to total experience required (ECX)
    6A 07		push 07			; EDI = # of levels (7) separated by 5,000 exp.
    5F		pop edi			; ""
    EB 08		jmp 4DDB78		; -> EDI * 5,000

    83 F8 0A	cmp eax,0A		; level 10?
    7C 10		jl 4DDB85		; if less -> level 6?
    8D 78 F7	lea edi,[eax-09]	; EDI = current level -9
    69 FF 88130000	imul edi,1388		; EDI * 5,000
    01 F9		add ecx,edi		; Add EDI to total experience required (ECX)
    6A 04		push 04			; EDI = # of levels (4) separated by 2,500 exp.
    5F		pop edi			; ""
    EB 08		jmp 4DDB8D		; -> EDI * 2,500

    83 F8 06	cmp eax,06		; level 6?
    7C 10		jl 4DDB95		; if less -> EDI = current level
    8D 78 FB	lea edi,[eax-05]	; EDI = current level -5
    69 FF C4090000	imul edi,09C4		; EDI * 2,500
    01 F9		add ecx,edi		; Add EDI to total experience required (ECX)
    6A 05		push 05			; EDI = # of levels (5) separated by 1,000 exp.
    5F		pop edi			; ""
    EB 02		jmp 4DDB9C		; -> EDI * 1,000

    8B F8		mov edi,eax		; EDI = current level
    69 FF E8030000	imul edi,03E8		; EDI * 1,000
    01 F9		add ecx,edi		; Add EDI to total experience required (ECX)

    8D 78 01	lea edi,[eax+01]	; EDI = next level
    90		nop			; old experience table (279C88~9F) is free space

    ---------	-------------------------------------------------------------------------
    0DA617~80	; EXPERIENCE NEEDED FOR NEXT LEVEL (ALTAR OF SACRIFICE)
    ---------	-------------------------------------------------------------------------
    31 C0		xor eax,eax		; EAX = 0

    83 F9 1E	cmp eax,1E		; level 30? (ECX = current level)
    74 63 		je 4DA681		; -> [max level has been reached]

    83 F9 16	cmp eax,16		; level 22?
    7C 10		jl 4DA633		; if less -> level 17?
    8D 79 EB	lea edi,[ecx-15]	; EDI = (current level - 21)
    69 FF A8610000	imul edi,61A8		; EDI * 25,000
    01 F8		add eax,edi		; Add EDI to total experience required (EAX)
    6A 05		push 05			; EDI = # of levels (5) separated by 10,000 exp.
    5F		pop edi			; ""
    EB 08		jmp 4DA63B		; -> EDI * 10,000

    83 F9 11	cmp ecx,11		; level 17?
    7C 10		jl 4DA648		; if less -> level 10?
    8D 79 F0	lea edi,[ecx-10]	; EDI = (current level - 16)
    69 FF 10270000	imul edi,2710		; EDI * 10,000
    01 F8		add eax,edi		; Add EDI to total experience required (EAX)
    6A 07		push 07			; EDI = # of levels (7) separated by 5,000 exp.
    5F		pop edi			; ""
    EB 08		jmp 4DA650		; -> EDI * 5,000

    83 F9 0A	cmp ecx,0A		; level 10?
    7C 10		jl 4DA65D		; if less -> level 6?
    8D 79 F7	lea edi,[ecx-09]	; EDI = current level -9
    69 FF 88130000	imul edi,1388		; EDI * 5,000
    01 F8		add eax,edi		; Add EDI to total experience required (EAX)
    6A 04		push 04			; EDI = # of levels (4) separated by 2,500 exp.
    5F		pop edi			; ""
    EB 08		jmp 4DA665		; -> EDI * 2,500

    83 F9 06	cmp ecx,06		; level 6?
    7C 10		jl 4DA672		; if less -> EDI = current level
    8D 79 FB	lea edi,[ecx-05]	; EDI = current level -5
    69 FF C4090000	imul edi,09C4		; EDI * 2,500
    01 F8		add eax,edi		; Add EDI to total experience required (EAX)
    6A 05		push 05			; EDI = # of levels (5) separated by 1,000 exp.
    5F		pop edi			; ""
    EB 02		jmp 4DA674		; -> EDI * 1,000

    8B F9		mov edi,ecx		; EDI = current level
    69 FF E8030000	imul edi,03E8		; EDI * 1,000
    01 F8		add eax,edi		; Add EDI to total experience required (EAX)
    90 90 90 90 90	nop			; -

    1627CC > 90	; EAX = current level instead of next level in above code

    ---------	-------------------------------------------------------------------------
    0E365B~6A	; MAP MAXIMUM LEVEL
    ---------	-------------------------------------------------------------------------
    8A 5F 32	mov bl,[edi+32]		; BL = Hero's Level
    38 C3		cmp bl,al		; Compare to map maximum
    0F85 47010000	jne 4E37AD		; if not equal -> [exit]
    E9 86000000	jmp 4E36F1		; -> [max level] (0E366B~F0 is free space)

-----------------------------------------------------------------------------------------

The basic experience formula is quite simple: 1 point of experience per point of health of units killed
plus a bonus of 500 experience each for siege battles and/or battling another hero. This is flawed in
several ways and can be modified to provide experience more appropriate to the difficulty of the battle.
The below code uses AI value instead of health (modify the divisor of 12 as needed) and changes the flat
experience bonuses for siege and hero battles to multipliers (+12.5% and +25%, respectively).

    ---------	-------------------------------------------------------------------------
    069F8A~E6	; NEW EXPERIENCE FORMULA
    ---------	-------------------------------------------------------------------------
    50		push eax		; store EAX
    52		push edx		; store EDX
    8B 3D B0476700	mov edi,[6747B0]	; EDI = unit index
    6B F6 1D	imul esi,esi,1D		; ESI = data range
    8B 44 B7 40	mov eax,[edi+esi*4+40]	; EAX = AI value
    0FAF C1		imul eax,ecx		; EAX * # of units in stack
    6A 0C		push 0C			; EAX / 12
    59		pop ecx			; ""
    31 D2		xor edx,edx		; ""
    F7 F9		idiv ecx		; ""
    01 C3		add ebx,eax		; add EAX to experience total (EBX)
    5A		pop edx			; retrieve EDX
    58		pop eax			; retrieve EAX
    8B 4D FC	mov ecx,[ebp-04]	; (shifted/optimized code)
    05 48050000	add eax,548		; ""
    49		dec ecx			; ""
    89 4D FC	mov [ebp-04],ecx	; ""
    75 AF		jne 469F64		; ""

    8B 45 F8	mov eax,[ebp-08]	; EAX = combat manager
    8B 88 C8530000	mov ecx,[eax+53C8]	; ECX = town data (if siege battle)
    85 C9		test ecx,ecx		; was this a siege battle?
    74 0E		je 469FD0		; if no -> ECX = enemy hero data
    8B 4D 08	mov ecx,[ebp+08]	; ???
    85 C9		test ecx,ecx		; ???
    75 07		jne 469FD0		; ???
    8B CB		mov ecx,ebx		; (siege battle) ECX = experience total
    C1 E9 03	shr ecx,03		; ECX / 8 (12.5%)
    01 CB		add ebx,ecx		; add ECX to experience total

    8B8C90CC530000	mov ecx,[eax+edx*4+53CC]; ECX = enemy hero data
    85 C9		test ecx,ecx		; is there an enemy hero?
    74 07		je 469FE2		; if no -> store experience total
    8B CB		mov ecx,ebx		; (hero battle) ECX = experience total
    C1 E9 02	shr ecx,02		; ECX / 4 (25%)
    01 CB		add ebx,ecx		; add ECX to experience total
    89 5D FC	mov [ebp-04],ebx	; store experience total
    EB 18		jmp 469FFF		; -> [continue] (069FE7~FE is free space)

    069F6B > 3B	; expanded jump
    069F77 > 2F	; ""
    069F81 > 25	; ""

-----------------------------------------------------------------------------------------

Another thing that we can look into doing is allowing both starting enemy hero experience and army size
to scale with difficulty if specified in the editor. This is mainly important for quest-style maps with
designated AI opponents where the goal is for human player(s) to achieve their objective with little to
no outside interference, since the difficulty setting will otherwise have little impact. The below code
sets any hero with 300,000 starting experience to level 1, 5, 10, 15, or 30 (assuming use of the values
in the example above) depending on the difficulty. It will then take any starting unit stack set to over
9,000 and use that value minus 9,000 as the "base" amount, so 9,100 would equal a stack size of 100 on
hard. For other difficulties, it will add/subtract 25% (Normal/Expert) or 50% (Easy/Impossiburu).

    --------	-------------------------------------------------------------------------
    0C2A15~9	; STARTING EXPERIENCE SCALES WITH DIFFICULTY LEVEL IF SET TO CAP
    --------	-------------------------------------------------------------------------
    E8 C27C0100	call 4DA6DC		; -> free space (auto-level code)

    ----------	-------------------------------------------------------------------------
    0DA6DC~718	; (EXPANDED SPACE - AUTO-LEVEL CODE)
    ----------	-------------------------------------------------------------------------
    8B 4D D4	mov ecx,[ebp-2C]	; ECX = hero experience
    81 F9 E0930400	cmp ecx,493E0		; is exp 300,000?
    75 2F		jne 4DA716		; if no -> update hero experience
    A1 38956900	mov eax,[699538]	; EAX = main index
    8A 80 D8F60100	mov al,[eax+1F6D8]	; AL = player difficulty (0~4)

    3C 04		cmp al,04		; Impossiburu?
    74 20		je 4DA716		; if yes -> update hero experience (Lv. 30)
    81 E9 605B0300	sub ecx,35B60		; ECX -220,000 (80,000)

    3C 03		cmp al,03		; Expert?
    74 16		je 4DA716		; if yes -> update hero experience (Lv. 15)
    81 E9 E8FD0000	sub ecx,FDE8		; ECX -65,000 (15,000)

    3C 02		cmp al,02		; Hard?
    74 0C		je 4DA716		; if yes -> update hero experience (Lv. 10)
    81 E9 F82A0000	sub ecx,2AF8		; ECX -11,000 (4,000)

    3C 01		cmp al,01		; Normal?
    74 02		je 4DA716		; if yes -> update hero experience (Lv. 5)

    31 C9		xor ecx,ecx		; Easy = no experience (Lv. 1)

    89 0F		mov [edi],ecx		; update hero experience
    C3		ret			; return

-----------------------------------------------------------------------------------------

    ---------	-------------------------------------------------------------------------
    102B44~50	; ALLOW STARTING UNITS TO SCALE WITH DIFFICULTY LEVEL
    ---------	-------------------------------------------------------------------------
    66 8B 4D EA	mov cx,[ebp-16]		; CX = number of units in stack
    E8 CC7BFDFF	call 4DA719		; -> free space (auto-level code)
    83 C7 04	add edi,04		; (shifted code)
    90		nop			; -

    ---------	-------------------------------------------------------------------------
    0DA719~7F	; (EXPANDED SPACE - AUTO-LEVEL CODE)
    ---------	-------------------------------------------------------------------------
    66 81 F9 2823	cmp cx,2328		; is stack size OVER NINE THOUSAND
    7E 59		jle 4DA779		; if no -> EAX = hero data
    8B 15 38956900	mov edx,[699538]	; EDX =  main index
    8A 92 D8F60100	mov dl,[edx+1F6D8]	; DL = difficulty level
    66 81 E9 2823	sub cx,2328		; CX -9000
    66 89 4D EA	mov [ebp-16],cx		; store baseline ("normal") stack size

    6A 05		push 05			; EAX = 5
    58		pop eax			; ""
    66 83 E9 28	sub cx,28		; CX -40
    66 83 F9 00	cmp cx,00		; is CX less than 0? (stack size 1~39)
    7C 12		jl 4DA754		; if yes -> ECX = baseline ("normal") stack size

    04 05		add al,05		; EAX +5
    66 83 E9 14	sub cx,14		; CX -20
    66 83 F9 00	cmp cx,00		; is CX less than 0?
    7C 06		jl 4DA754		; if yes -> ECX = baseline ("normal") stack size
    3C FF		cmp al,-01		; has EAX reached 255 (maximum factor)?
    74 02		je 4DA754		; if yes -> ECX = baseline ("normal") stack size
    EB EE		jmp 4DA742		; -> EAX +5 (loop)

    8B 4D EA	mov ecx,[ebp-16]	; ECX = baseline ("normal") stack size
    84 D2		test dl,dl		; Easy?
    74 12		je 4DA76D		; if yes -> subtract EAX*2 from stack size
    FE CA		dec dl			; Normal?
    74 10		je 4DA76F		; if yes -> subtract EAX from stack size
    FE CA		dec dl			; Hard?
    74 16		je 4DA779		; if yes -> EAX = hero data
    FE CA		dec dl			; Expert?
    74 02		je 4DA769		; if yes -> add EAX to stack size
    01 C1		add ecx,eax		; (Impossiburu) add EAX*2 to stack size
    01 C1		add ecx,eax		; (Expert) add EAX to stack size
    EB 0C		jmp 4DA779		; -> EAX = hero data
    29 C1		sub ecx,eax		; (Easy) subtract EAX*2 from stack size
    29 C1		sub ecx,eax		; (Normal) subtract EAX from stack size
    66 83 F9 00	cmp cx,00		; is CX less than 0?
    7D 02		jnl 4DA779		; if no -> EAX = hero data
    31 C9		xor ecx,ecx		; CX = 0
    8B 45 E4	mov eax,[ebp-1C]	; EAX = hero data
    66 89 08	mov [eax],cx		; move stack size to hero data
    C3		ret			; return
