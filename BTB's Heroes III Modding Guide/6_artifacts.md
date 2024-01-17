# 7. Artifacts

The ArTraits.txt file in the H3bitmap.lod archive allows you to edit the value, class (treasure, minor,
major, relic, etc.) equipment slot, and descriptions of artifacts. Most of their effects are hard-coded
throughout the .exe. The primary attribute bonuses are found in a table starting at 23E758, with 4 bytes
per artifact - 1 each for Attack, Defense, Spell Power, and Knowledge, respectively.

		ATTACK (WEAPONS)			    DEFENSE (SHIELDS)
	--------------------------------	--------------------------------
	23E774	Centaur's Axe			    23E78C	Shield of the Dwarven Lords
	23E778	Blackshard of the Dead Knight	23E790	Shield of the Yawning Dead
	23E77C	Greater Gnoll's Flail		23E794	Buckler of the Gnoll King
	23E780	Ogre's Club of Havoc		23E798	Targe of the Rampaging Ogre
	23E784	Sword of Hellfire		    23E79C	Shield of the Damned
	23E788	Titan's Gladius			    23E7A0	Sentinel's Shield

		KNOWLEDGE (HELMETS)			    SPELL POWER (ARMOR)
	--------------------------------	--------------------------------
	23E7A4	Helm of the Alabaster Unicorn	23E7BC	Breastplate of Petrified Wood
	23E7A8	Skull Helmet			    23E7C0	Rib Cage
	23E7AC	Helm of Chaos			    23E7C4	Scales of the Greater Basilisk
	23E7B0	Crown of the Supreme Magi	23E7C8	Tunic of the Cyclops King
	23E7B4	Hellstorm Helmet		    23E7CC	Breastplate of Brimstone
	23E7B8	Thunder Helmet			    23E7D0	Titan's Cuirass

		ANGELIC ALLIANCE			    DRAGON FATHER
	--------------------------------	--------------------------------
	23E7D4	Armor of Wonder			    23E7EC	Quiet Eye of the Dragon
	23E7D8	Sandals of the Saint		23E7F0	Red Dragon Flame Tongue
	23E7DC	Celestial Necklace of Bliss	23E7F4	Dragon Scale Shield
	23E7E0	Lion's Shield of Courage	23E7F8	Dragon Scale Armor
	23E7E4	Sword of Judgement		    23E7FC	Dragonbone Greaves
	23E7E8	Helm of Heavenly Enlightenment	23E800	Dragon Wing Tabard
	------	------------------------------	23E804	Necklace of Dragonteeth
	------	------------------------------	23E808	Crown of Dragontooth
	------	------------------------------	23E80C	Still Eye of the Dragon

		LUCK MODIFIERS				    MORALE MODIFIERS
	--------------------------------	--------------------------------
	23E810	Clover of Fortune		    23E81C	Badge of Courage
	23E814	Cards of Prophecy		    23E820	Crest of Valor
	23E818	Ladybird of Luck		    23E824	Glyph of Gallantry
	23E8AC	Hourglass of the Evil Hour	23E8A8	Spirit of Oppression

			    --- 23E908 Pendant of Courage ---

		MOVEMENT (LAND)				    MOVEMENT (SEA)
	--------------------------------	--------------------------------
	23E870	Equestrian's Gloves		    23E874	Necklace of Ocean Guidance
	23E8E0	Boots of Speed			    23E944	Sea Captain's Hat
	23E878	Angel Wings			        23E8C0	Boots of Levitation

		UNIT SPEED BONUS			    ELIXIR OF LIFE
	--------------------------------	--------------------------------
	23E8DC	Necklace of Swiftness		23E8D0	Ring of Vitality
	23E86C	Ring of the Wayfarer		23E8D4	Ring of Life
	23E8E4	Cape of Velocity		    23E8D8	Vial of Lifeblood

		WIZARD'S WELL				    RING OF THE MAGI
	--------------------------------	--------------------------------
	23E87C	Charm of Mana			    23E888	Collar of Conjuring
	23E880	Talisman of Mana		    23E88C	Ring of Conjuring
	23E884	Mystic Orb of Mana		    23E890	Cape of Conjuring

		SPELL BOOSTERS				    SPELL KNOWLEDGE
	--------------------------------	--------------------------------
	23E894	Orb of the Firmament		23E8B0	Tome of Fire Magic
	23E898	Orb of Silt			        23E8B4	Tome of Air Magic
	23E89C	Orb of Tempestuous Fire		23E8B8	Tome of Water Magic
	23E8A0	Orb of Driving Rain		    23E8BC	Tome of Earth Magic
	------	-------------------		    23E948	Spellbinder's Hat

		SPELL IMMUNITY				    RESOURCE PRODUCTION
	--------------------------------	--------------------------------
	23E8C8	Sphere of Permanence		23E90C	Everflowing Crystal Cloak
	23E8E8	Pendant of Dispassion		23E910	Ring of Infinite Gems
	23E8EC	Pendant of Second Sight		23E914	Everpouring Vial of Mercury
	23E8F0	Pendant of Holiness		    23E918	Inexhaustible Cart of Ore
	23E8F4	Pendant of Life			    23E91C	Eversmoking Ring of Sulfur
	23E8F8	Pendant of Death		    23E920	Inexhaustible Cart of Lumber
	23E8FC	Pendant of Free Will		23E924	Endless Sack of Gold
	23E900	Pendant of Negativity		23E928	Endless Bag of Gold
	23E904	Pendant of Total Recall		23E92C	Endless Purse of Gold

		MAGIC SUPPRESSION			    STATUE OF LEGION
	--------------------------------	--------------------------------
	23E8A4	Recanter's Cloak		    23E930	Legs of Legion
	23E950	Orb of Inhibition		    23E934	Loins of Legion
	------	-----------------		    23E938	Torso of Legion
	------	-----------------		    23E93C	Arms of Legion
	------	-----------------		    23E940	Head of Legion

		NECROMANCY				        ARCHERY
	--------------------------------	--------------------------------
	23E830	Amulet of the Undertaker	23E848	Bow of Elven Cherrywood
	23E834	Vampire's Cowl			    23E84C	Unicorn's Mane Bowstring
	23E838	Dead Man's Boots		    23E850	Angel Feather Arrows
	------	----------------		    23E8C4	Golden Bow

		SCOUTING				        EAGLE EYE
	--------------------------------	--------------------------------
	23E828	Speculum			        23E854	Bird of Perception
	23E82C	Spyglass			        23E858	Stoic Watchman
	------	--------			        23E85C	Emblem of Cognizance

		RESISTANCE				        DIPLOMACY
	--------------------------------	--------------------------------
	23E83C	Garniture of Interference	23E860	Statesman's Medal
	23E840	Surcoat of Counterpoise		23E864	Diplomat's Ring
	23E844	Boots of Polarity		    23E868	Ambassador's Sash

		MISCELLAENOUS				    CAMPAIGN-EXCLUSIVE
	--------------------------------	--------------------------------
	23E8CC	Orb of Vulnerability		23E954	Vial of Dragon Blood
	23E94C	Shackles of War			    23E958	Armageddon's Blade

				COMBINATION ARTIFACTS
	------------------------------------------------------------------------
	23E95C	Angelic Alliance		    23E974	Titan's Thunder
	23E960	Cloak of the Undead King	23E978	Admiral's Hat
	23E964	Elixir of Life			    23E97C	Sharpshooter's Bow
	23E968	Armor of the Damned		    23E980	Wizard's Well
	23E96C	Statue of Legion		    23E984	Ring of the Magi
	23E970	Power of the Dragon Father	23E988	Cornucopia

				WAR MACHINES & STUFF
	------------------------------------------------------------------------
	23E758	Spell Book			    23E768	Ballista
	23E75C	Spell Scroll			23E76C	Ammo Cart
	23E760	The Grail			    23E770	First Aid Tent
	23E764	Catapult			    ------	--------------

Values specified here can either be positive (most are) or negative (as seen on the Titan's equipment).
Remember that combination artifacts possess all the properties of their individual components, and that
includes their stats. Thus, any stats set for those artifacts will be an additional bonus.

If you wish to remove an artifact from the game, simply set it as class "S" (spellbook) in ArTraits.txt.
This will prevent it from appearing as a random artifact, but it can still appear if it's specifically
placed on a map or given via a campaign. One thing to be wary of is that the map editor will crash when
attempting to edit a quest requirement/reward or starting bonus that includes a spellbook-class artifact
since it considers them invalid, so you'll need to temporarily revert them to a valid class if you wish
to change them to something else (which I'm assuming you do if you want to get rid of them).

If desired, you can also null the graphic of any removed artifact in Objects.txt by replacing its call
(AVA0XXX.def) with DEFAULT.Def (a giant "no" symbol) to make it easier to notice them in the map editor.
One would assume that you can also use Objects.txt to swap the graphics of any artifacts with hard-coded
effects that you don't know how to edit (along with editing Artifact.def), but such artifacts will still
appear on the map with their original graphics if the map object is a random artifact and not a specific
one. Thus, it's best to instead swap the effects of the artifacts in the code (most of the artifact IDs
called for special effects will be shown below) or, failing that, rename the .def files in h3sprite.lod.

---------------------------------------------------------------------------------------------------------

## COMBINATION ARTIFACTS

The artifacts required to assemble a "combo" artifact are specified at the addresses in the table below.
The address of each component is shown, followed by an address specifying the total number of components
in the combo and finally the ID of the assembled artifact. This will allow you some freedom to make new
combo artifacts (such as allowing out-of-campaign assembly of Armageddon's Blade) provided you sacrifice
something else. Adding or removing a component from a combo is doable, but gets complicated (see below).

| ADMIRAL'S HAT        | CLOAK OF THE UNDEAD KING| SHARPSHOOTER'S BOW       |
|----------------------|-------------------------|--------------------------|
| 04C7BC (47)          | 04C676 (36)             | 04C7F1 (3C)             |
| 04C7C0 (7B)          | 04C674 (37)             | 04C7E2 (3D)             |
| 04C7C5 (#)           | 04C670 (38)             | 04C7E0 (3E)             |
| 04C7D9 (Combo ID)    | 04C67B (#)              | 04C7F6 (#)              |
| ------ (-)           | 04C68F (Combo ID)       | 04C80C (Combo ID)       |

| ELIXIR OF LIFE        | WIZARD'S WELL           | RING OF THE MAGI         |
|----------------------|-------------------------|--------------------------|
| 04C696 (5E)          | 04C826 (49)             | 04C85C (4C)             |
| 04C6A7 (5F)          | 04C824 (4A)             | 04C858 (4D)             |
| 04C698 (60)          | 04C820 (4B)             | 04C85A (4E)             |
| 04C6AC (#)           | 04C82B (#)              | 04C861 (#)              |
| 04C6C5 (Combo ID)    | 04C83F (Combo ID)       | 04C875 (Combo ID)       |

| CORNUCOPIA            | ARMOR OF THE DAMNED      | TITAN'S THUNDER          |
|----------------------|-------------------------|--------------------------|
| 04C880 (6D)          | 04C6D0 (08)             | 04C77E (0C)             |
| 04C87C (6E)          | 04C6CA (0E)             | 04C778 (12)             |
| 04C88F (6F)          | 04C6CE (1A)             | 04C78D (18)             |
| 04C87A (71)          | 04C6DF (14)             | 04C77C (1E)             |
| 04C894 (#)           | 04C6E4 (#)              | 04C792 (#)              |
| 04C8AA (Combo ID)    | 04C6FA (Combo ID)       | 04C7A8 (Combo ID)       |

| STATUE OF LEGION      | ANGELIC ALLIANCE         | POWER OF DRAGON FATHER   |
|----------------------|-------------------------|--------------------------|
| 04C718 (76)          | 04C63D (1F)             | 04C732 (25)             |
| 04C716 (77)          | 04C63B (20)             | 04C740 (26)             |
| 04C712 (78)          | 04C641 (21)             | 04C73E (27)             |
| 04C710 (79)          | 04C639 (22)             | 04C72C (28)             |
| 04C70E (7A)          | 04C63F (23)             | 04C72E (29)             |
| 04C71D (#)           | 04C643 (24)             | 04C742 (2A)             |
| 04C727 (Combo ID)    | 04C648 (#)              | 04C746 (2B)             |
| ------ (-)           | 04C65C (Combo ID)       | 04C755 (2C)             |
| ------ (-)           | ------ (-)              | 04C730 (2D)             |
| ------ (-)           | ------ (-)              | 04C75A (#)              |
| ------ (-)           | ------ (-)              | 04C773 (Combo ID)       |


Before getting into adding or removing artifacts from combos, we need to understand exactly what's going
on in the code. Each component artifact named above is being pushed onto the stack (6A XX) and it's thus
necessary to specify how many components are in each combo so we know how much to pop back off. Further,
the way this is handled requires the stack to be manually reset at two points: 04C763 (83 C4 60, or add
esp,60) and 04C8BD (83 C4 2C, or add esp,2C). Each push is 4 bytes, so we need to subtract 04 from one
of these two commands for every artifact we remove and add 4 for each one we add. 04C8BF (2C) should be
our first choice since it comes later in the code; only use 04C765 if editing 04C8BF causes the game to
crash when loading (for example, removing more than two components from Power of the Dragon Father).

Bearing the above in mind, removing an artifact is actually pretty simple: NOP out the push (6A XX -> 90
90), adjust the number of components in the artifact, and subtract 4 from 04C8BF. Adding a component is
equally simple, at least in theory. In practice, the combo artifact code is pretty unoptimized and kind
of a huge mess. This is both good and bad: bad because it's harder to read and understand, but good in
that it creates the possibility of making additions without jumping to free space.

Let's look at an example where we replace the Ring of the Magi with Armageddon's Blade:

	04C858 > 11 (Shield of the Damned)	04C861 > 04 (# of components)
	04C85A > 17 (Hellstorm Helmet)		04C875 > 80 (Armageddon's Blade)
	04C85C > 1D (Brimstone Breastplate)	04C8BF > 30 (+4 bytes to the stack)

		04C848 > 6A 06 59 6A 0B (04C84C = Sword of Hellfire)

So what's happening here? Most of this should be obvious, but how did we manage to clear up 2 bytes for
an extra push at 04C848? These 5 bytes are replacing a single opcode (B9 06 00 00 00) which sets ECX to
06. The new code accomplishes the same thing with only 3 bytes by pushing 06 onto the stack (6A 06) and
then popping it right back out and into ECX (59), leaving us with 2 bytes for another push.

The only thing to watch out for when dealing with the stack are two registers: EBP and ESP. ESP keeps
track of where the stack is at at all times and thus you only tend to see it being used to update EBP.
EBP is something we've seen quite a lot in the various coding examples thus far since it's how we pull
data out of the stack. Unlike ESP, it doesn't update every time the stack is changed so that we can use
the same reference points within a given block of memory.

Case in point, the instruction after the Sword of Hellfire push in the above example is lea esi,[ebp-2C]
(8D 75 D4), which directly references a point in the stack relative to the position of EBP. The addition
of another push onto the stack prior to this doesn't break anything since EBP will not change until ESP
is specifically copied into it, which generally happens when we call a subroutine.

Generally speaking, however, you want to leave the stack the way you found it: pop off anything that you
push onto it unless you have a very specific reason for leaving it there, such as what we've done here.

---------------------------------------------------------------------------------------------------------

## MORALE & LUCK ARTIFACTS

The artifacts which affect morale and/or luck are specified at the following addresses:

| Morale Artifact                          | Code 1                  | Code 2                  |
|-----------------------------------------|-------------------------|-------------------------|
| Pendant of Courage                      | 0E3CAB                  | 0DC612                  |
| Still Eye of the Dragon                 | 0E3CEC                  | 0DC66D                  |
| Badge of Courage                        | 0E3D2A                  | 0DC6C6                  |
| Crest of Valor                          | 0E3D68                  | 0DC71F                  |
| Glyph of Gallantry                      | 0E3DA7                  | 0DC779                  |

| Luck Artifact                            | Code 1                  | Code 2                  |
|------------------------------------------|-------------------------|-------------------------|
| Pendant of Courage                       | 0E3A52                  | 0DCDB2                  |
| Still Eye of the Dragon                  | 0E3A90                  | 0DCE0D                  |
| Clover of Fortune                        | 0E3ACD                  | 0DCE66                  |
| Cards of Prophecy                        | 0E3B0B                  | 0DCEBF                  |
| Ladybird of Luck                         | 0E3B43                  | 0DCF19                  |

The two addresses specified for each artifact above are for the actual effect and for the
right-click text, respectively. The +3 morale and luck bonuses for the Pendant of Courage
are specified at 0E3CE2/0DC666 and 0E3A89/0DCE06, respectively. The other bonuses - both
for the effect and right-click text - are all INC (+1) commands and are thus much harder
to change. This is normally where you'd expect to be told to find some free space to use,
but in this case the code which checks to see if a given artifact is equipped is horribly
unoptimized and doing so will not only make them much easier to edit, but will clear up
more free space than you'll know what to do with. Let's have a look:

    ---------	-------------------------------------------------------------------------
    0E3C9E~F7	; MORALE ARTIFACTS
    ---------	-------------------------------------------------------------------------
    6A 31		push 31			; 31 = Badge of Courage
    8B CF		mov ecx,edi		; ECX = hero data
    E8 B957FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 4E3CAE		; if no -> next check
    83 C3 01	add ebx,01		; +1 Morale

    6A 32		push 32			; 32 = Crest of Valor
    8B CF		mov ecx,edi		; ECX = hero data
    E8 A957FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 4E3CBE		; if no -> next check
    83 C3 01	add ebx,01		; +1 Morale

    6A 33		push 33			; 33 = Glyph of Gallantry
    8B CF		mov ecx,edi		; ECX = hero data
    E8 9957FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 4E3CCE		; if no -> next check
    83 C3 01	add ebx,01		; +1 Morale

    6A 2D		push 2D			; 2D = Still Eye of the Dragon
    8B CF		mov ecx,edi		; ECX = hero data
    E8 8957FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 4E3CDE		; if no -> next check
    83 C3 01	add ebx,01		; +1 Morale

    6A 53		push 6C			; 6C = Pendant of Courage
    8B CF		mov ecx,edi		; ECX = hero data
    E8 7957FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 4E3CEE		; if no -> next check
    83 C3 03	add ebx,03		; +3 Morale

    89 5D 0C	mov [ebp+0C],ebx	; store morale
    56		push esi		; (cleanup)
    E9 E8000000	jmp 4E3DDF		; -> [continue] (0E3CF8~DDE is free space)

    ----------	-------------------------------------------------------------------------
    0DC606~71D	; MORALE ARTIFACTS (RIGHT-CLICK INFO)
    ----------	-------------------------------------------------------------------------
    6A 31		push 31			; 31 = Badge of Courage
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 51CEFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DC633		; if no -> next check
    8B 15 38586A00	mov edx,[6A5838]	; ArrayTxt, line 91
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 71ECF3FF	call 41B2A0		; ""
    83 45 F0 01	add [ebp-10],01		; +1 Morale

    6A 32		push 32			; 32 = Crest of Valor
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 24CEFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DC660		; if no -> next check
    8B 15 3C586A00	mov edx,[6A583C]	; ArrayTxt, line 92
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 44ECF3FF	call 41B2A0		; ""
    83 45 F0 01	add [ebp-10],01		; +1 Morale

    6A 33		push 33			; 33 = Glyph of Gallantry
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 F7CDFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DC68D		; if no -> next check
    8B 15 40586A00	mov edx,[6A5840]	; ArrayTxt, line 93
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 17ECF3FF	call 41B2A0		; ""
    83 45 F0 02	add [ebp-10],01		; +1 Morale

    68 86000000	push 86			; 86 = Power of the Dragon Father
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 C7CDFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 22		je 4DC6BF		; if no -> next check
    8B 15 1C5F6A00	mov edx,[6A5F1C]	; ArrayTxt, line 17
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 E7EBF3FF	call 41B2A0		; ""
    83 45 F0 02	add [ebp-10],01		; +1 Morale
    EB 5A		jmp 4DC719		;

    6A 20		push 2D			; 2D = Still Eye of the Dragon
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 98CDFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DC6EC		; if no -> next check
    8B 15 34586A00	mov edx,[6A5834]	; ArrayTxt, line 90
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 B8EBF3FF	call 41B2A0		; ""
    83 45 F0 01	add [ebp-10],01		; +1 Morale

    6A 6A		push 6A			; 53 = Pendant of Courage
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 3ECDFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DC746		; if no -> [continue]
    8B 15 8C586A00	mov edx,[6A588C]	; ArrayTxt, line 112
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 5EEBF3FF	call 41B2A0		; ""
    83 45 F0 03	add [ebp-10],03		; +3 Morale
    E9 AE000000	jmp 004DC7CC		; -> [continue] (0DC71E~CB is free space)

    ---------	-------------------------------------------------------------------------
    0E3A46~9F	; LUCK ARTIFACTS
    ---------	-------------------------------------------------------------------------
    6A 2E		push 2E			; 2E = Clover of Fortune
    8B CE		mov ecx,esi		; ECX = hero data
    E8 115AFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 04		je 4E3A57		; if no -> next check
    83 45 0C 01	add [ebp+0C],01		; +1 Luck

    6A 2F		push 2F			; 2F = Cards of Prophecy
    8B CE		mov ecx,esi		; ECX = hero data
    E8 005AFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 04		je 4E3A68		; if no -> next check
    83 45 0C 01	add [ebp+0C],01		; +1 Luck

    6A 30		push 30			; 30 = Ladybird of Luck
    8B CE		mov ecx,esi		; ECX = hero data
    E8 EF59FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 04		je 4E3A79		; if no -> next check
    83 45 0C 01	add [ebp+0C],01		; +1 Luck

    6A 25		push 25			; 25 = Quiet Eye of the Dragon
    8B CE		mov ecx,esi		; ECX = hero data
    E8 DE59FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 04		je 4E3A8A		; if no -> next check
    83 45 0C 01	add [ebp+0C],01		; +1 Luck

    6A 53		push 6C			; 6C = Pendant of Courage
    8B CE		mov ecx,esi		; ECX = hero data
    E8 BC59FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 04		je 4E3AAC		; if no -> [continue]
    83 45 0C 03	add [ebp+0C],03		; +3 Luck
    E9 B2000000	jmp 4E3B52		; -> [continue] (0E3AA0~B51 is free space)

    ----------	-------------------------------------------------------------------------
    0DCDA6~EBD	; LUCK ARTIFACTS (RIGHT-CLICK INFO)
    ----------	-------------------------------------------------------------------------
    6A 2E		push 2E			; 2E = Clover of Fortune
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 B1C6FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DCDD3		; if no -> next check
    8B 15 A8536A00	mov edx,[6A53A8]	; ArrayTxt, line 65
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 D1E4F3FF	call 41B2A0		; ""
    83 45 F0 01	add [ebp-10],01		; +1 Luck

    6A 2F		push 2F			; 2F = Cards of Prophecy
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 84C6FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DCE00		; if no -> next check
    8B 15 AC536A00	mov edx,[6A53AC]	; ArrayTxt, line 66
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 A4E4F3FF	call 41B2A0		; ""
    83 45 F0 01	add [ebp-10],01		; +1 Luck

    6A 30		push 30			; 30 = Ladybird of Luck
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 57C6FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DCE2D		; if no -> next check
    8B 15 B0536A00	mov edx,[6A53B0]	; ArrayTxt, line 67
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 77E4F3FF	call 41B2A0		; ""
    83 45 F0 02	add [ebp-10],02		; +2 Luck

    68 86000000	push 86			; 86 = Power of the Dragon Father
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 27C6FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 22		je 4DCE5F		; if no -> next check
    8B 15 F8556A00	mov edx,[6A55F8]	; ArrayTxt, line 9
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 47E4F3FF	call 41B2A0		; ""
    83 45 F0 02	add [ebp-10],01		; +1 Luck
    EB 5A		jmp 4DCEB9		;

    6A 25		push 25			; 25 = Quiet Eye of the Dragon
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 F8C5FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DCE8C		; if no -> next check
    8B 15 A4536A00	mov edx,[6A53A4]	; ArrayTxt, line 64
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 18E4F3FF	call 41B2A0		; ""
    83 45 F0 01	add [ebp-10],01		; +1 Luck

    6A 53		push 6C			; 6C = Pendant of Courage
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 CBC5FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 20		je 4DCEB9		; if no -> next check
    8B 15 E8536A00	mov edx,[6A53E8]	;
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 EBE3F3FF	call 41B2A0		; ""
    83 45 F0 03	add [ebp-10],03		; +3 Luck
    E9 AE000000	jmp 4DCF6C		; -> [continue]

ArrayTxt.txt from the h3bitmap.lod archive is where all of the right-click messages for
morale and luck bonuses are stored, which leads us to our snag. Yes, in this particular
example we can re-use the same line for both the Still/Quiet Eye and Dragon Father since
it's technically the same bonuses from the same artifacts, but let's assume that we want
a separate line for the assembled combo. As you can see in the above example, it's not
necessary to call the combo separately when adding the actual morale/luck bonuses unless
you with to give it a further bonus beyond that of its components. For the right click
information, then, we simply skip over the component checks if the combo check passes.

As we learned earlier, HD Mod does not use the luck and morale text descriptors in lines
8~14 and 16~22, meaning that said descriptors are now unused lines in ArrayTxt.txt. The
relevant commands in the code above are when we load the text strings -	actually DWORD
poiners - into EDX. We use 1C 5F 6A 00 and F8 55 6A 00 here (lines 9 and 17, the next
free lines after adding Leadership and Luck specialists) for the right-click text on the
assembled combo. The pointers for the other lines are as follows:

	FC 55 6A 00: 10 ("Bad")			20 5F 6A 00: 18 ("Poor")
	00 56 6A 00: 11 ("Normal")		24 5F 6A 00: 19 ("Normal")
	04 56 6A 00: 12 ("Good")		28 5F 6A 00: 20 ("Good")
	08 56 6A 00: 13 ("Great")		2C 5F 6A 00: 21 ("Great")
	0C 56 6A 00: 14 ("Irish")		30 5F 6A 00: 22 ("Blood!")

Using these, you are free to create additional luck and/or morale-boosting artifacts.

-----------------------------------------------------------------------------------------

## SPEED & MOVEMENT ARTIFACTS

The speed-boosting artifacts and their bonuses are specified at the following addresses:

		0E65FF (Necklace of Swiftness)	0E6634 = 01 (+1 speed)
		0E6639 (Ring of the Wayfarer)	0E6645 = 47 (INC)
		0E6647 (Cape of Velocity)	0E6655 = 02 (+2 speed)

Again, we can optimize this substantially like so:

    ----------	-------------------------------------------------------------------------
    0E65F3~626	; SPEED ARTIFACTS OPTIMIZED
    ----------	-------------------------------------------------------------------------
    33 FF		xor edi,edi		; EDI = 0
    6A 61		push 61			; 61 = Necklace of Swiftness
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 622EFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 4E6605		; if no -> next check
    83 C7 01	add edi,01		; +1 Speed

    6A 45		push 45			; 45 = Seven League Boots
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 522EFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 4E6615		; if no -> next check
    83 C7 01	add edi,01		; +1 Speed

    6A 63		push 63			; 63 = Cape of Velocity
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 422EFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 4E6625		; if no -> next check
    83 C7 02	add edi,02		; +2 Speed
    EB 2F		jmp 4E6656		; -> [continue] (0E6627~55 is free space)

-----------------------------------------------------------------------------------------

The four artifacts which grant movement bonuses can be edited in Movement.txt, but there
will be some confusion as this document is mislabeled as follows:

	• The Boots of Speed are mislabeled as Ring of the Wayfarer

	• The Sea Captain's Hat uses the Lighthouse bonus (this setting affects both)

	• Angel Wings do not actually give a bonus (this setting does nothing)

The movement-based artifacts are named at the following addresses:

	0E4F56 (62 = Boots of Speed)		0E4D82 (47 = Necklace of Ocean Guidance)
	0E4F99 (46 = Equestrian's Gloves)	0E4CAF (7B = Sea Captain's Hat)
	16B77E (48 = Angel Wings)		    16B793 (5A = Boots of Levitation)

-----------------------------------------------------------------------------------------

## SKILL-BOOSTING ARTIFACTS

The artifacts which provide bonuses to skills are specified at the following addresses:

   NECROMANCY		   RESISTANCE		     ARCHERY		    EAGLE EYE
-----------------	-----------------	-----------------	-----------------
0E3FAE (Amulet)		0E49B9 (Garniture)	0E443D (Bow)		0E46FD (Bird)
0E3FF4 (Cowl)		0E49FF (Surcoat)	0E4483 (Bowstring)	0E4743 (Watchman)
0E403A (Boots)		0E4A46 (Boots)		0E44CA (Arrows)		0E478A (Emblem)
-----------------	-----------------	-----------------	-----------------
0E3FE7 (05% Bonus)	0E49F2 (05% Bonus)	0E4476 (05% Bonus)	0E4736 (05% Bonus)
0E402D (10% Bonus)	0E4A38 (10% Bonus)	0E44BC (10% Bonus)	0E477C (10% Bonus)
0E4074 (15% Bonus)	0E4A80 (15% Bonus)	0E4504 (15% Bonus)	0E47C4 (15% Bonus)

The percentages above are DWORD pointers, which we may be familiar with from having dealt
with them in the skill specialty code. Other options we have for these values include:

05% - E4 AE 63 00	10% - D0 B8 63 00	15% - 28 EB 63 00	20% - B4 B8 63 00
25% - 9C 05 64 00	30% - 24 EB 63 00	40% - B0 B8 63 00	50% - CC B8 63 00

(Or we can just make our own floating value as we learned in the "Skills" section above)

-----------------------------------------------------------------------------------------

The Cloak of the Undead King is named for its primary effect (see the Necromancy entry in
the "Skills" section) at 0E3EDD. It provides 30% necromancy to any hero with no skill at
0E4177; this can be removed by setting 0E3F60 to 18 02, which will free up 0E4130~7D.

>see skills section earlier for more on editing the cloak's effects

Aside from that, only the resistance-boosting artifacts don't require the hero to possess
the skill in question in order to be effective. The culprit is a short jump at 0E496E to
0E49AC which should be a long jump to 0E4A87. We'll look at fixing this (if so desired)
when we optimize the code to free up a metric fuckton of space. But first, let's look at
making the other three artifact sets boost the skills without needing to have them:

            NECROMANCY                  ARCHERY		                EAGLE EYE
    -------------------------	-------------------------	-------------------------
    0E3F60: 7E 40 90 90 90 90	0E43EE: 7E 40 90 90 90 90	0E46AE: 7E 40 90 90 90 90

A "slight" caveat with the Necromancy artifacts is that, since Necromancy Amplifiers and
the Soul Prison are part of the same routine, not requiring the Necromancy skill for the
artifacts also means that they won't require it, either. ~~~I can probably fix this

-----------------------------------------------------------------------------------------

Since we all know that Eagle Eye is a garbage skill that belongs in the garbage, let's
look at making those garbage-boosting artifacts boost Learning, instead:

				0E4ACC > 47(*)
				0E4AE0 > 33
				0E4AE6 > 2D
			0E4B12~E > EB 94 57 8B F9 E8 D4FBFFFF 5F EB EA

		(*omit this change for the artifacts to require the skill)

We will also need to make one last change for this to work, which will be covered in the
optimization process. As for Eagle Eye, we move it away from those artifacts (as well as
keep it functioning correctly) with the following edits:

				0E46C7 > C3
				0E46CD > BD
				0E468B > E9 3B010000

Of course, the above changes are not necessary if you've thrown Eagle Eye in the trash.
In fact, scrapping it will free up quite a bit of space: 0E47CB~EF & 0E4689~EF

-----------------------------------------------------------------------------------------

With that out of the way, let's get to optimizing!

    ---------	-------------------------------------------------------------------------
    0E4430~82	; ARCHERY ARTIFACTS
    ---------	-------------------------------------------------------------------------
    6A 3C		push 3C			; 3C = Elven Cherrywood Bow
    8B CF		mov ecx,edi		; ECX = hero data
    E8 2750FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E4449		; if no -> next check
    D9 45 FC	fld [ebp-04]		; load Archery skill
    D8 05 E4EA6300	fadd [63EAE4]		; Archery + 05%
    D9 5D FC	fstp [ebp-04]		; store Archery skill

    6A 3D		push 3D			; 3D = Unicorn Mane Bowstring
    8B CF		mov ecx,edi		; ECX = hero data
    E8 0E50FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E4462		; if no -> next check
    D9 45 FC	fld [ebp-04]		; load Archery skill
    D8 05 D0B86300	fadd [63B8D0]		; Archery + 10%
    D9 5D FC	fstp [ebp-04]		; store Archery skill

    6A 3E		push 3E			; 3E = Angel Feather Arrows
    8B CF		mov ecx,edi		; ECX = hero data
    E8 F54FFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E447B		; if no -> (cleanup)
    D9 45 FC	fld [ebp-04]		; load Archery skill
    D8 05 28EB6300	fadd [63EB28]		; Archery + 15%
    D9 5D FC	fstp [ebp-04]		; store Archery skill

    D9 45 FC	fld [ebp-04]		; (cleanup)
    5F		pop edi			; ""
    8B E5		mov esp,ebp		; ""
    5D		pop ebp			; ""
    C3		ret			; return (0E4484~51F is free space)

    0E43F0 > 87 00	; update jump to cleanup (artifacts will require skill)

    ---------	-------------------------------------------------------------------------
    0E49AC~FF	; RESISTANCE ARTIFACTS
    ---------	-------------------------------------------------------------------------
    EB 05		jmp 4E49B3		; -> first artifact check
    E9 D4000000	jmp 4E4A87		; (no skill) -> (cleanup)

    6A 39		push 39			; 39 = Garniture of Interference
    8B CF		mov ecx,edi		; ECX = hero data
    E8 A44AFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E49CC		; if no -> next check
    D9 45 FC	fld [ebp-04]		; load Resistance skill
    D8 05 E4EA6300	fadd [63EAE4]		; Resistance +05%
    D9 5D FC	fstp [ebp-04]		; store Resistance skill

    6A 3A		push 3A			; 3A = Surcoat of Counterpoise
    8B CF		mov ecx,edi		; ECX = hero data
    E8 8B4AFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E49E5		; if no -> next check
    D9 45 FC	fld [ebp-04]		; load Resistance skill
    D8 05 D0B86300	fadd [63B8D0]		; Resistance +10%
    D9 5D FC	fstp [ebp-04]		; store Resistance skill

    6A 3B		push 3B			; 3B = Boots of Polarity
    8B CF		mov ecx,edi		; ECX = hero data
    E8 724AFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E49FE		; if no -> [continue]
    D9 45 FC	fld [ebp-04]		; load Resistance skill
    D8 05 28EB6300	fadd [63EB28]		; Resistance +15%
    D9 5D FC	fstp [ebp-04]		; store Resistance skill
    EB AE		jmp 4E49AE		; -> [continue] (0E4A00~86 is free space)

    0E496F > 3E	; Resistance artifacts require skill to work

    ----------	-------------------------------------------------------------------------
    0E46F0~73F	; LEARNING/EAGLE EYE ARTIFACTS
    ----------	-------------------------------------------------------------------------
    6A 3F		push 3F			; 3F = Bird of Perception
    8B CF		mov ecx,edi		; ECX = hero data
    E8 674DFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E4709		; if no -> next check
    D9 45 FC	fld [ebp-04]		; load Learning skill
    D8 05 E4EA6300	fadd [63EAE4]		; Learning +05%
    D9 5D FC	fstp [ebp-04]		; store Learning skill

    6A 40		push 40			; 40 = Stoic Watchman
    8B CF		mov ecx,edi		; ECX = hero data
    E8 4E4DFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E4722		; if no -> next check
    D9 45 FC	fld [ebp-04]		; load Learning skill
    D8 05 D0B86300	fadd [63B8D0]		; Learning +10%
    D9 5D FC	fstp [ebp-04]		; store Learning skill

    6A 41		push 41			; 41 = Emblem of Cognizance
    8B CF		mov ecx,edi		; ECX = hero data
    E8 354DFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E473B		; if no -> [continue]
    D9 45 FC	fld [ebp-04]		; load Learning skill
    D8 05 28EB6300	fadd [63EB28]		; Learning +15%
    D9 5D FC	fstp [ebp-04]		; store Learning skill
    E9 8B000000(*)	jmp 4E47CB		; -> [continue] (0E4740~CA is free space)

    	    (*For Learning artifacts, replace this instruction with C3)

    ---------	-------------------------------------------------------------------------
    0E3FA2~F1	; NECROMANCY ARTIFACTS
    ---------	-------------------------------------------------------------------------
    6A 38		push 38			; 38 = Dead Man's Boots
    8B CF		mov ecx,edi		; ECX = hero data
    E8 B554FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E3FBB		; if no -> next check
    D9 45 FC	fld [ebp-04]		; load Necromancy skill
    D8 05 E4EA6300	fadd [63EAE4]		; Necromancy +05%
    D9 5D FC	fstp [ebp-04]		; store Necromancy skill

    6A 37		push 37			; 37 = Vampire's Cowl
    8B CF		mov ecx,edi		; ECX = hero data
    E8 9C54FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E3FD4		; if no -> next check
    D9 45 FC	fld [ebp-04]		; load Necromancy skill
    D8 05 D0B86300	fadd [63B8D0]		; Necromancy +10%
    D9 5D FC	fstp [ebp-04]		; store Necromancy skill

    6A 36		push 36			; 36 = Death's Head Pendant
    8B CF		mov ecx,edi		; ECX = hero data
    E8 8354FFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 4E3FED		; if no -> [continue]
    D9 45 FC	fld [ebp-04]		; load Necromancy skill
    D8 05 28EB6300	fadd [63EB28]		; Necromancy +15%
    D9 5D FC	fstp [ebp-04]		; store Necromancy skill
    E9 89000000	jmp 4E407B		; -> [continue] (0E3FF2~407A is free space)

-----------------------------------------------------------------------------------------

## SPYGLASS & SPECULUM

These are named at 0E4355 and 0E4392, respectively. Their +1 visibility bonuses are coded
as increments to EBX (43) at 0E438A and 0E43C6, respectively.

-----------------------------------------------------------------------------------------

## RESOURCE ARTIFACTS

The IDs of artifacts which generate resources are specified at the following addresses:

	0B8A5B = 72 (Wood)	0B8A46 = 6E (Gems)	0B8A1D = 71 (Sulfur)
	0B8A6C = 70 (Ore)	0B8A7D = 6D (Crystal)	0B8A31 = 6F (Mercury)

The Cornucopia is named for its effect at 0B8A0E. To change how many of each resource it
generates, go to 0B8A19 and replace "8D 14 80" with "6B C0 XX", where "XX" is the desired
quantity (in addition to the +1 from the component artifacts), and then set 0B8A21 to 45.

-----------------------------------------------------------------------------------------

## SPELL IMMUNITY & SUPPRESSION ARTIFACTS

The IDs of artifacts which block spells are specified at the following addresses:

		04A2BF = 64 (blocks Berserk)
		04A273 = 65 (blocks Blind)
		04A32F = 66 (blocks Curse)
		04A381 = 67 (blocks Death Ripple)
		04A394 = 68 (blocks Destroy Undead)
		04A2DD = 69 (blocks Hypnotize)
		04A2CF = 6A (blocks Lightning Bolt & Chain Lightning)
		04A2E8 = 6B (blocks Forgetfulness)
		04A1EF = 86 (blocks lv.1-4 spells)
		04A469 = 31 (blocks mind spells)
		----------------------------------
		04A215 = 5C (blocks Dispel)
		1A845B = ""
		1A84E6 = ""
		04A425 = 5D (Orb of Vulnerability)
		04A43B = 5D ("")
		19EE7E = 53 (Recanter's Cloak)
		1A841A = 53 ("")
		1A842F = 53 ("")
		19ECDA = 7E (Orb of Inhibition)
		19ECD9 = 7E ("")

The Badge of Courage gives you immunity to mind magic, which one would assume is a bug
caused by it receiving a bonus intended for a different artifact that got cut from the
final game but actually was an intentional (albeit stupid) decision caused by a series
of poor design choices. In any case, you can remove this effect by setting 74 to EB at
04A473 or you can specify a different artifact at 04A469.

All of the above artifacts except for the Power of the Dragon father are specified with
signed pushes (6A XX); remember than in order to name an artifact with an ID higher than
7F, you'll need to jump to free space to use a longer/unsigned push (68 XX 00 00 00) or
get a little cheeky with it like with the below example where we move the mind immunity
effect of the Badge of Courage to Titan's Thunder:

    --------	-------------------------------------------------------------------------
    04A462~79	; O-Mind to Titan's Thunder
    --------	-------------------------------------------------------------------------
    75 31		jne 44A495		; -> [immunity] (moved jump)
    85 DB		test ebx,ebx		; (unchanged)
    74 1F		je 44A487		; ""
    68 87000000	push 87			; 87 = Titan's Thunder
    8B CB		mov ecx,ebx		; ECX = hero data
    E8 ECEF0800	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0C		je 44A484		; if no -> [continue]
    EB 1B		jmp 44A495		; -> [immunity] (04A47A~83 is free)

Essentially, this edit takes advantage of the fact that the artifact spell immunity block
contains a lot of the same code copy/pasted for each check, and so we can free up space
by simply jumping to the same code in the next artifact check.

-----------------------------------------------------------------------------------------

## DIPLOMACY ARTIFACTS

These are specified at 0E4859 (Medal), 0E489F (Ring), and 0E48E6 (Sash).

Their surrender cost discounts are DWORD pointers located at 0E4892, 0E48D8, and 0E4920,
respectively (all three are D0 B8 63 00, or 10%, by default); see the above entry on
skill-boosting artifacts for other values that can be used here.

-----------------------------------------------------------------------------------------

## ELEMENTAL ORBS

These are specified at 0E5A02 (Air), 0E5A4F (Earth), 0E5A9A (Fire), and 0E5ADE (Water).

The 50% damage bonus is a single DWORD pointer located at 0E5B17 (30 EB 63 00, or 50%);
other values you can set are 25% (14 83 67 00), 20% (28 83 67 00), or 10% (F0 82 67 00).

(Note: these values differ from the ones above since they're actually 1.XX, not 0.XX)

-----------------------------------------------------------------------------------------

## Other Artifacts
### RING OF THE MAGI

The components are specified at 0E5033 (Collar), 0E5072 (Ring), and 0E50AF (Cape); the
assembled Ring of the Magi is named at 0E50ED with a longer command (since 8B > 7F).

The duration bonuses are located at 0E5068, 0E50A8, 0E50E6, and 0E5126, respectively.

A substantial amount of space (0E5012~12F) can be freed by gutting this entire routine:

	03C535 > EB 0F    (03C537~45 is free space)	025C53 > 90 90 90 90 90
	1A03C2 > EB 10    (1A03C4~D3 is free space)	1272AF > 90 90 90 90 90
	1A7194 > 31C0EB0E (1A7198~A5 is free space)	-----------------------

-----------------------------------------------------------------------------------------

### WIZARD'S WELL

The components are specified at 0E4226 (Charm), 0E4262 (Talisman), and 0E42A0 (Orb).

The amount of SP restored daily by the Talisman and Mystic Orb of Mana are specified at
0E4298 and 0E42D6, respectively. The Charm of Mana will require a longer patch to edit:

				0E4228 > 30
				0E4241 > EB
				0E4259 > 83 C3 XX

			   ("XX" is the desired value)

As for the Wizard's Well, a long patch will replace the routine of "if max SP > current
SP, current SP = max SP" with one that only restores a percentage of your maximum spell
points (in addition to whatever the components have been set to give):

	0C7F5F > 0E DB 45 F8 D8 0D XX XX XX XX 50 DB 1C E4 58 0F BF 1E 01 C3 90

"XX XX XX XX" is a DWORD pointer to the desired percentage; see the earlier entry on
skill-boosting artifacts examples of other values that can be set here.

-----------------------------------------------------------------------------------------

### ELIXIR OF LIFE

The components are specified at 0E667C (Vitality), 0E66BB (Life), and 0E66C9 (Lifeblood);
0E66FA is the Elixir of Life call. These artifacts are all named again at 0E5E0C, 0E5E4D,
0E5E8B, and 0E5EE8, respectively, in a routine that's unused so far as I can tell.

Similar to the above: the Ring of Vitality and Vial of Lifeblood bonuses are specified at
0E66B3 and 0E66D7, respectively, but the Ring of Life is an INC located at 0E66C7 which,
as we know by now, can't be changed without freeing up some space. As for the 25% bonus
from the assembled Elixir, that's something we can't easily change even with free space
since it's accomplished via a bitshift at 0E6718. Long story short, this is yet another
situation where my ultimate solution was a complete rewrite.

Static health bonuses are disproportionately beneficial for lower-level units and totally
inconsequential for higher-level ones, which is why the First Aid overhaul we saw earlier
multiplied its effect by the unit's level. And that's pretty much the exact same thing
that we'll be doing with the three Elixir of Life components in the code below:

    ---------	-----------------------------------------------------------------------
    0E666D~D8	; HEALTH BONUS ARTIFACTS
    ---------	-----------------------------------------------------------------------
    31 DB		xor ebx,ebx		; EBX = 0
    8B 0D B0476700	mov ecx,[6747B0]	; ECX = unit index
    8B 7D 08	mov edi,[ebp+08]	; EDI = unit ID
    6B FF 74	imul edi,74		; EDI = data range
    F6 44 39 10 10	test byte[ecx+edi+10],10; is unit living?
    74 59		je 4E66DB		; if no -> [exit]

    6A 5E		push 5E			; 5E = Ring of Vitality
    8B 4D FC	mov ecx,[ebp-04]	; ECX = hero data
    E8 D42DFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 0B		je 4E669B		; if no -> next check
    8B 15 B0476700	mov edx,[6747B0]	; EDX = unit index
    03 5C 3A 04	add ebx,[edx+edi+04]	; Health bonus (EBX) + unit's level (0~6)
    43		inc ebx			; EBX +1

    6A 5F		push 5F			; 5F = Ring of Life
    8B 4D FC	mov ecx,[ebp-04]	; ECX = hero data
    E8 BB2DFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 10		je 4E66B9		; if no -> next check
    8B 15 B0476700	mov edx,[6747B0]	; EDX = unit index
    8B 54 3A 04	mov edx,[edx+edi+04]	; EDX = unit's level (0~6)
    42		inc edx			; EDX +1
    6B D2 02	imul edx,edx,02		; EDX *2
    01 D3		add ebx,edx		; add EDX to health bonus (EBX)

    6A 60		push 60			; 60 = Vial of Troll's Blood
    8B 4D FC	mov ecx,[ebp-04]	; ECX = hero data
    E8 9D2DFFFF	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 10		je 4E66D7		; if no -> [exit]
    8B 15 B0476700	mov edx,[6747B0]	; EDX = unit index
    8B 54 3A 04	mov edx,[edx+edi+04]	; EDX = unit's level (0~6)
    42		inc edx			; EDX +1
    6B D2 03	imul edx,03		; EDX *3
    01 D3		add ebx,edx		; add EDX to health bonus (EBX)
    EB 44		jmp 4E671D		; -> [exit] (0E66D9~71D is free space)

I opted not to have an additional health boost for the Elixir (though this is certainly
easy enough to change by tweaking the above code) since it already adds in regeneration.
The Elixir of Life is called for the regeneration routine at 046C1A; you can specify a
different artifact here if you wish. You can also skip the "living" unit requirement by
going to 046BFE and NOPing out the jump (0F 84 ED 01 00 00 -> 90 90 90 90 90 90).

-----------------------------------------------------------------------------------------

### ANGELIC ALLIANCE

There's a known bug with the primary effect of the Angelic Alliance wherein it doesn't
treat either Conflux or unaffiliated units as neutrally-aligned for the purposes of
allowing them to be freely mixed without morale penalty. This can be fixed thusly:

  04AC56~62 > 83 FE 03 7C 05 83 FE 06 7C 01 43 EB 0E (Conflux units; 04AC63~70 is free)
   04B942~E > 83 FE 03 7C 05 83 FE 06 7C 01 43 EB 0E (""; 04B94F~5C is free)
     04AB98 > BA (unaffiliated units; requires Conflux unit edit)
     04B877 > C7 ("")

If you instead think that the bug is that Stronghold and Fortress units are allowed and
simply want the Angelic Alliance to allow mixing "good" units, the code gets simpler:

	  04AC56~5D > 83 FE 03 7D 16 43 EB 13 (04AC5E~70 is free)
	   04B942~9 > 83 FE 03 7D 16 43 EB 13 (04B94A~5C is free)

 (Unaffiliated units may also be allowed with the above code via the edit just above it)

Another issue with the Angelic Alliance is that it affects all allied heroes instead of
just the user. We can change it to a local effect with the following edits:

	    0C6ADF~E5 > 68 81 00 00 00 EB 1F (0C6AE6~B04 is free)
	    0636AB~B4 > 8B 4D 0C E8 AD 5D 07 00 EB 0D (0636B5~C1 is free)

The artifact ID for the spell cast at the beginning of combat is named at 064FBB.

The spell itself can be modified at the following addresses:

		064FD8 = Spell ID (Prayer)	064FE5 = Power
		064FEF = Spell ID (*)		064FE7 = Level

		(*If editing spell IDs, both addresses must be changed)

Beware that setting this to a spell which cannot properly multi-target will crash the
game; if you want to remove the spell, the easiest way is to set it to one that isn't
flagged as a battlefield spell, i.e. Summon Boat (00).

-----------------------------------------------------------------------------------------

### ARMOR OF THE DAMNED

Same deal as the above, except four spells are cast (artifact ID is at 064FF8):

|         |      SLOW         |      CURSE        |     WEAKNESS      |    MISFORTUNE     |
|---------|-------------------|-------------------|-------------------|-------------------|
| Spell ID1 |      065019       |      065046       |      065073       |      0650A0       |
| Spell ID2 |      065030       |      06505D       |      06508A       |      0650B7       |
| Power   |      065026       |      065053       |      065080       |      0650AD       |
| Level   |      065028       |      065055       |      065082       |      0650AF       |


Note that if you're looking for some free space, axing this effect wholesale will free up
a pretty massive chunk of it. Replace the push at 064FF7 (68 84 00 00 00) with a jump to
0650BF (E9 C3 00 C0 FF) and you've got yourself nearly 200 bytes. And since this routine
directly follows the Angelic Alliance routine, you can trash them both by instead editing
the push at 064FBA (68 81 00 00 00 -> E9 00 01 C0 FF) to earn over 250 bytes!

Alternatively, there's perhaps an even more interesting use for this effect...

-----------------------------------------------------------------------------------------

### ARMAGEDDON'S BLADE

Setting 0E52FA to EB 4F makes the Armageddon spell respect the hero's Fire Magic level
rather than always being cast at expert level and frees 0E52FC~34A while immunity to the
Armageddon spell can be removed by setting 1A86E6 to 90 E9 (instead of 0F 84), but we can
do better than just that. Armageddon immunity is cheaper than a two-dollar whore, but the
game's titular artifact is kind of garbage if we take that away, so let's say we have the
sword itself cast Armageddon at the start of combat on your enemies only (your troops are
immune), but casting it yourself still hits both parties. This not only makes more sense
from a thematic standpoint, but it's a hell of a lot more balanced.

Rather than skipping over the Angelic Alliance spellcast code (per the above suggestion),
the below code hijacks it for Armageddon's Blade. Since we'll need to add some more code
to temporarily flag our own units with Armageddon immunity, this will end up running into
the Armor of the Damned spellcast code - this example thus assumes you're trashing both.

    064FC9 > 39	; extends existing jump to exit
    064FE3 > 1F	; ""

    ------		-------------------------------------------------------------------------
    064FF2		; ARMAGEDDON'S BLADE CASTS ARMAGEDDON ON FOES AT THE START OF COMBAT
    ------		-------------------------------------------------------------------------
    FF 05 013B6700	inc [673B01]		; set "temp" flag (for Armageddon immunity)
    E8 41B11300	call 5A013E		; -> Armageddon immunity routine
    FF 0D 013B6700	dec [673B01]		; clear "temp" flag
    E9 B7000000	jmp 4650BF		; -> [exit]

    ------		-------------------------------------------------------------------------
    1A8700		; (ARMAGEDDON IMMUNITY ROUTINE NOW USED ONLY FOR THIS PURPOSE)
    ------		-------------------------------------------------------------------------
    E9 03C9EBFF	jmp 465008		; -> free space (angelic alliance/damned armor)
    90		nop			; -

    ---------	-------------------------------------------------------------------------
    065008~1F	; (EXPANDED SPACE - OVERWRITES ANGELIC ALLIANCE/DAMNED ARMOR SPELLS)
    ---------	-------------------------------------------------------------------------
    A0 013B6700	mov al,[673B01]		; AL = "temp" flag
    84 C0		test al,al		; are we immune?
    0F84 8D381400	je 5A88A2		; if no -> [exit]
    D9 05 64AC6300	fld dword ptr [63AC64]	; immunity (load "0" value)
    E9 E6361400	jmp 5A8706		; -> [exit] (065020~BE is free space)

So far as the blade teaching Armageddon, removing it (so far as I know, anyway) will be a
package deal along with removing the spell from Titan's Thunder (see below).

-----------------------------------------------------------------------------------------

### TITAN'S THUNDER

To remove the spells taught by both Titan's Thunder and Armageddon's Blade, go to 0D9920
and change 88 01 to 90 90 (note: this does NOT interfere with spell scrolls).

You may also wish to set 0E2CD2 to EB 2B; this skips the code where Titan's Thunder will
give the hero a spellbook if they don't already have one (and frees space: 0E2CD4~FE).

-----------------------------------------------------------------------------------------

### SHARPSHOOTER'S BOW

As we went over earlier, the Sharpshooter's Bow is called for the "no obstacle penalty"
bonus at 0671AC and "no range penalty" at 06722D. Its final effect is located at 042680
and 045874 (change both), which makes all ranged attacks unblockable. This differs from
the traditional "no melee penalty" in that units with ranged attacks will always be able
to use them regardless of if an enemy unit is adjacent to them.

-----------------------------------------------------------------------------------------

### STATUE OF LEGION

Changing the effects of the legion statue artifacts requires a bit of work, but the end
result is complete control over how they operate. First off, we'll need some patches to
allow us to change the growth bonuses (XX) for each component:

    	 Legs of Legion					 Loins of Legion
    -----------------------------------------	--------------------------------------
    1BFE37 > 84 C0 74 06 83 C7 XX 90 90 90		1BFE74 > 84 C0 74 06 83 C7 XX 90 90 90
    1BFE53 > 84 C0 74 07 83 C7 XX 90 90 90 90	1BFE90 > 84 C0 74 04 83 C7 XX 90

    	 Torso of Legion				 Arms of Legion
    -----------------------------------------	--------------------------------------
    1BFEAE > 84 C0 74 06 83 C7 XX 90 90 90		1BFEE7 > 84 C0 74 05 83 C7 XX 90 90
    1BFEC6 > 84 C0 74 07 83 C7 XX 90 90 90 90	1BFEFE > 84 C0 74 04 83 C7 XX 90

    	 Head of Legion			 (Artifact IDs are named at these addresses)
    -----------------------------		----------------------------------------------
    1BFF1C > 84 C0 74 03 83 C7 XX		1BFE31 (Legs)	1BFEE1 (Arms)	1BFF16 (Head)
    1BFF31 > 84 C0 74 03 83 C7 XX		1BFE6E (Ass)	1BFEA8 (Torso)	-------------

----------------------------------------------------------------------------------------

Changing the unit level is more involved. First, we'll need to modify the switch:

				1BFE1B > FF
				1BFE1E > 06

Next, we look at the address of each level and specify the artifact which grants a bonus
to it; this means that two pieces of the statue can't boost the same level, but multiple
levels can receive a bonus from the same piece. If you've been reading the whole guide up
until this point, you may recognize the below as a DWORD pointer list - for each address
on the left, enter the corresponding 4-bytes on the right which will point to the routine
for the desired artifact (i.e. the "Legs" code starts at 1BFE2C, thus 2C FE 5B 00).

		  Tier 1: 1BFF44	Legs.... 2C FE 5B 00
		  Tier 2: 1BFF48	Loins... 69 FE 5B 00
		  Tier 3: 1BFF4C	Torso... A3 FE 5B 00
		  Tier 4: 1BFF50	Arms.... DC FE 5B 00
		  Tier 5: 1BFF54	Head.... 11 FF 5B 00
		  Tier 6: 1BFF58	None.... 38 FF 5B 00
		  Tier 7: 1BFF5C	Statue.. (20 50 46 00; see below)

This covers the actual functionality (we'll get to the part about using the assembled
statue as an additional component shortly), but we still need to update the right-click
descriptions to reflect those changes. We'll start by writing the following code:

	1C6297~C3 > 42 83 FA 06 77 27 FF 24 95 A4 67 5C 00 6A 76 EB 15 6A 77 EB 11 6A 78
		    EB 0D 6A 79 EB 09 6A 7A EB 05 68 85 00 00 00 58 90 90 90 90 90 90

An astute reader may notice that the bulk of above code is pushing the artifact ID of
each component, all of which are then followed by a jump to the end of the code block.
These pushes will be the destinations specified in a secondary DWORD pointer table:

		Tier 1: 1C67A4		Legs.... A4 62 5C 00
		Tier 2: 1C67A8		Loins... A8 62 5C 00
		Tier 3: 1C67AC		Torso... AC 62 5C 00
		Tier 4: 1C67B0		Arms.... B0 62 5C 00
		Tier 5: 1C67B4		Head.... B4 62 5C 00
		Tier 6: 1C67B8		Statue.. B8 62 5C 00
		Tier 7: 1C67BC		None.... C4 62 5C 00

Finally, let's address the effect of the assembled statue. +50% growth in all towns is
ridiculously overpowered, even moreso than the Grail. So let's get rid of that...

			    1C0082 > E9 83 00 00 00 90
			    1BFC46 > E9 9F 00 00 00 90

...and instead have the statue itself act as the final component that provides a growth
bonus only to the town that it's in. This requires some free space, which we thankfully
just created a lot of a few entries back. The below example uses space from the Angelic
Alliance/Armor of the Damned code block, but can be placed anywhere you want to - again,
all that you'll need to update are the long jumps/calls and the DWORD pointer above.

    ---------	-------------------------------------------------------------------------
    065020~5B	; STATUE OF LEGION TO ACT LIKE COMPONENTS (OVERWRITES AA/DAMNED ARMOR)
    ---------	-------------------------------------------------------------------------
    85 C9		test ecx,ecx		; ???
    74 11		je 465035		; ???
    68 85000000	push 85			; 85 = Head of Legion
    E8 32440700	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 465035 		; if no -> ???
    83 C7 XX	add edi,XX		; XX = growth bonus
    8B 4D 08	mov ecx,[ebp+08]	; ???
    85 C9		test ecx,ecx		; ???
    0F84 F8AE1500	je 5BFF38		; ???
    68 85000000	push 85			; 85 = Head of Legion
    E8 16440700	call 4D9460 		; check for artifact
    84 C0		test al,al		; do we have it?
    74 03		je 465051		; if no -> (cleanup)
    83 C7 XX	add edi,XX		; XX = growth bonus
    8B C7		mov eax,edi		; (cleanup)
    5F		pop edi			; ""
    5E		pop esi			; ""
    5B		pop ebx			; ""
    8B E5		mov esp,ebp		; ""
    5D		pop ebp			; ""
    C2 04 00	ret 0004		; return (06505C~BE is free space)

---------------------------------------------------------------------------------------------------------

Finally, let's take a quick look at the "artifact" starting bonus, wherein you begin the scenario with a
randomly-selected treasure-level artifact. Easily the most powerful of the three starting bonuses (we'll
look at improving the other two later on), its only drawback is the potential of providing you with an
artifact which is inappropriate/useless for your starting faction. Specifically, we'll be checking for
the Amulet of the Undertaker on any faction other than Necropolis and the Ring of Vitality or any morale
artifact for either Necropolis or Conflux and replacing them with something more appropriate.

    ------		-------------------------------------------------------------------------
    0C0058		; PREVENT STARTING ARTIFACTS THAT ARE INAPPROPRIATE FOR YOUR FACTION
    ------		-------------------------------------------------------------------------
    E9 9F520200 	jmp 4E52FC		; -> free space (Armageddon's Blade master cast)

    ----------	-------------------------------------------------------------------------
    0E52FC~342	; (EXPANDED SPACE - OVERWRITES ARMAGEDDON'S BLADE MASTER CAST)
    ----------	-------------------------------------------------------------------------
    8A 4E 30	mov cl,[esi+30]		; CL = starting hero class
    D0 E9		shr cl,1		; CL = starting faction

    80 F9 04	cmp cl,04		; Necropolis?
    75 14		jne 4E531A		; if no -> Conflux?
    83 F8 31	cmp eax,31		; Badge of Courage? (if yes -> replace)
    74 0A		je 4E5315		; ""
    83 F8 32	cmp eax,32		; Crest of Valor? (if yes -> replace)
    74 05		je 4E5315		; ""
    83 F8 5e	cmp eax,5E		; Ring of Vitality?
    75 24		jne 4E5339		; if no -> (displaced code)
    6A 36		push 36			; replace with Undertaker's Amulet
    58		pop eax			; ""
    EB 1F		jmp 4E5339		; -> (displaced code)

    80 F9 08	cmp cl,08		; Conflux?
    75 12		jne 4E5331		; if no -> Dead Man's Boots?
    83 F8 31	cmp eax,31		; Badge of Courage? (if yes -> replace)
    74 0A		je 4E532E		; ""
    83 F8 32	cmp eax,32		; Crest of Valor? (if yes -> replace)
    74 05		je 4E532E		; ""
    83 F8 5E	cmp eax,5E		; Ring of Vitality?
    75 03		jne 4E5331		; if no -> Dead Man's Boots?
    6A 2E		push 2E			; replace with Clover of Fortune
    58		pop eax			; ""

    83 F8 36	cmp eax,36		; Undertaker's Amulet?
    75 03		jne 4E5339		; if no -> (displaced code)
    6A 2E		push 2E			; replace with Clover of Fortune
    58		pop eax			; ""

    6A 01		push 01			; (displaced code)
    8D 4D E8	lea ecx,[ebp-18]	; ""
    E9 1AADFDFF	jmp 4C005D		; return

One warning regarding the code above is that it's a hard override and thus won't care if it's providing
an artifact that has been banned on the selected map for whatever reason. If you choose to modify which
artifacts it provides, you should thus choose them with that consideration in mind. Another note is that
this will make both Conflux and Necropolis considerably more likely to start out with the artifact that
is specified to replace the morale artifacts and Ring of Vitality, which could prove beneficial.