# 5. UNITS

The CrTraits.txt file in the H3bitmap.lod archive allows you to edit the basic unit settings, which are
their costs (in both gold and resources), base growth, AI value, stats, and the minimum/maximum numbers
in which they will randomly appear in the wild. The "horde growth" value here is for reference only and
is non-functional; refer to the "Buildings" section further below for how to edit them. War machine data
is included in this file, but only gold and wood costs will be considered by War Machine Factories while
Blacksmiths will only use gold. It's possible to have War Machine Factories charge a different amount of
gold than Blacksmiths do: change 1D17CB from 38 to 34, 1D2264 from 07 to 05, and 1D226C from 20 to 24.
This will make Blacksmiths instead look in the (otherwise unused) "gems" column for gold costs.

The Arrow Tower stats specified in CrTraits.txt are also not used at all; their damage is hard-coded to
increase with the number of buildings, the attack stat does nothing, and HP is handled within Walls.txt.
See the "Buildings" section of the guide for more information regarding arrow towers and castle walls.

Regarding "fight" versus AI value, the former is used exclusively to determine which unit stacks the AI
will target in combat while the latter is used at many points, most notably to determine army strength.
One issue in the original game is that several upgraded units have a fight value either identical to or
insignificantly higher than that of their base unit. Archers and Marksmen, for example, have the same
fight values, leading the AI to treat a stack of 37 Archers as a bigger threat than 36 Marksmen.

All of the other unit settings, namely their unique abilities, are scattered all over the place in the
executable file. The main location is a table starting at 2703B8, storing 116 bytes per unit (although
most of these are unused). At least seven other tables exist: two for resistances & weaknesses, two for
special attack properties, two for units who cast spells, and one for their shot animations; each table
containing one byte for each unit within its range. The offsets for each unit are as follows:

|   CASTLE UNIT	|		|	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Pikeman	|		|	2703B8	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBA2|
|   Halberdier	|		|	27042C	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBA3|
|   Archer	|		|	2704A0	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBA4|
|   Marksman	|		|	270514	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBA5|
|   Griffin	|		|	270588	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBA6|
|   Royal Griffin	| |	2705FC	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBA7|
|   Swordsman	|		|	270670	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBA8|
|   Crusader	|		|	2706E4	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBA9|
|   Monk	|		|			270758	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBAA|
|   Zealot	|		|	2707CC	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBAB|
|   Cavalier	|		|	270840	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBAC|
|   Champion	|		|	2708B4	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBAD|
|   Angel	|		|	270928	|	------	|	------	|	------	|	------	|	------	|	------	|	03DBAE|
|   Archangel	|		|	27099C	|	------	|	------	|	------	|	------	|	048488	|	092ED4	|	03DBAF|

|   RAMPART UNIT	|		|	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Centaur	|		|	270A10	|	------	|	------	|	------	|	------	|	048489	|	092ED5	|	03DBB0|
|   Centaur Captain	| |	270A84	|	------	|	------	|	------	|	------	|	04848A	|	092ED6	|	03DBB1|
|   Dwarf	|		|	270AF8	|	04A658	|	------	|	------	|	------	|	04848B	|	092ED7	|	03DBB2|
|   Battle Dwarf	|		|	270B6C	|	04A659	|	------	|	------	|	------	|	04848C	|	092ED8	|	03DBB3|
|   Wood Elf	|		|	270BE0	|	04A65A	|	------	|	------	|	------	|	04848D	|	092ED9	|	03DBB4|
|   Grand Elf	|		|	270C54	|	04A65B	|	------	|	------	|	------	|	04848E	|	092EDA	|	03DBB5|
|   Pegasus	|		|	270CC8	|	04A65C	|	------	|	------	|	------	|	04848F	|	092EDB	|	03DBB6|
|   Silver Pegasus	||	270D3C	|	04A65D	|	------	|	------	|	------	|	048490	|	092EDC	|	03DBB7|
|   Dendroid Guard	||	270DB0	|	04A65E	|	------	|	------	|	04065C	|	048491	|	092EDD	|	03DBB8|
|   Dendroid Soldier	||	270E24	|	04A65F	|	------	|	------	|	04065D	|	048492	|	092EDE	|	03DBB9|
|   Unicorn	|		|	270E98	|	04A660	|	------	|	------	|	04065E	|	048493	|	092EDF	|	03DBBA|
|   War Unicorn	|		|	270F0C	|	04A661	|	------	|	------	|	04065F	|	048494	|	092EE0	|	03DBBB|
|   Green Dragon	|		|	270F80	|	04A662	|	------	|	------	|	040660	|	048495	|	092EE1	|	03DBBC|
|   Gold Dragon	|		|	270FF4	|	04A663	|	------	|	------	|	040661	|	048496	|	092EE2	|	03DBBD|


|   TOWER UNIT	|		|	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Gremlin	|		|	271068	|	04A664	|	------	|	------	|	040662	|	048497	|	092EE3	|	03DBBE|
|   Master Gremlin	||	2710DC	|	04A665	|	------	|	------	|	040663	|	048498	|	092EE4	|	03DBBF|
|   Stone Gargoyle	||	271150	|	04A666	|	------	|	------	|	040664	|	048499	|	092EE5	|	03DBC0|
|   Obsidian Gargoyle	||	2711C4	|	04A667	|	------	|	------	|	040665	|	04849A	|	092EE6	|	03DBC1|
|   Stone Golem	|		|	271238	|	04A668 | 04B280	|	------	|	040666	|	04849B	|	092EE7	|	03DBC2|
|   Iron Golem	|		|	2712AC	|	04A669	|	04B281	|	------	|	040667	|	04849C	|	092EE8	|	03DBC3|
|   Mage			|		|	271320	|	04A66A	|	04B282	|	------	|	040668	|	04849D	|	092EE9	|	03DBC4|
|   Arch Mage	|		|	271394	|	04A66B	|	04B283	|	------	|	040669	|	04849E	|	092EEA	|	03DBC5|
|   Genie	|		|	271408	|	04A66C	|	04B284	|	------	|	04066A	|	04849F	|	092EEB	|	03DBC6|
|   Master Genie	|		|	27147C	|	04A66D	|	04B285	|	------	|	04066B	|	0484A0	|	092EEC	|	03DBC7|
|   Naga			|		|	2714F0	|	04A66E	|	04B286	|	------	|	04066C	|	0484A1	|	092EED	|	03DBC8|
|   Naga Queen	|		|	271564	|	04A66F	|	04B287	|	------	|	04066D	|	0484A2	|	092EEE	|	03DBC9|
|   Giant	|		|	2715D8	|	04A670	|	04B288	|	------	|	04066E	|	0484A3	|	092EEF	|	03DBCA|
|   Titan	|		|	27164C	|	04A671	|	04B289	|	------	|	04066F	|	0484A4	|	092EF0	|	03DBCB|

|   INFERNO UNIT	|		|	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Imp	|				|	2716C0	|	04A672	|	04B28A	|	------	|	040670	|	0484A5	|	092EF1	|	03DBCC|
|   Familiar	|		|	271734	|	04A673	|	04B28B	|	------	|	040671	|	0484A6	|	092EF2	|	03DBCD|
|   Gog	|				|	2717A8	|	04A674	|	04B28C	|	------	|	040672	|	0484A7	|	092EF3	|	03DBCE|
|   Magog	|		|	27181C	|	04A675	|	04B28D	|	------	|	040673	|	0484A8	|	092EF4	|	03DBCF|
|   Hell Hound	|		|	271890	|	04A676	|	04B28E	|	------	|	040674	|	0484A9	|	092EF5	|	03DBD0|
|   Cerberus	|		|	271904	|	04A677	|	04B28F	|	------	|	040675	|	0484AA	|	092EF6	|	03DBD1|
|   Demon	|		|	271978	|	04A678	|	04B290	|	------	|	040676	|	0484AB	|	092EF7	|	03DBD2|
|   Horned Demon	|		|	2719EC	|	04A679	|	04B291	|	------	|	040677	|	0484AC	|	092EF8	|	03DBD3|
|   Pit Fiend	|		|	271A60	|	04A67A	|	04B292	|	------	|	040678	|	0484AD	|	092EF9	|	03DBD4|
|   Pit Lord	|		|	271AD4	|	04A67B	|	04B293	|	------	|	040679	|	0484AE	|	092EFA	|	03DBD5|
|   Efreeti	|		|	271B48	|	04A67C	|	04B294	|	------	|	04067A	|	0484AF	|	092EFB	|	03DBD6|
|   Efreet Sultan	||	271BBC	|	04A67D	|	04B295	|	------	|	04067B	|	0484B0	|	092EFC	|	03DBD7|
|   Devil	|		|	271C30	|	04A67E	|	04B296	|	------	|	04067C	|	0484B1	|	092EFD	|	03DBD8|
|   Archdevil	|		|	271CA4	|	04A67F	|	04B297	|	------	|	04067D	|	0484B2	|	092EFE	|	03DBD9|

|   NECROPOLIS UNIT	|	|DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Skeleton	|		|	271D18	|	04A680	|	04B298	|	------	|	04067E	|	0484B3	|	092EFF	|	03DBDA|
|   Skeleton Warrior	||	271D8C	|	04A681	|	04B299	|	------	|	04067F	|	0484B4	|	092F00	|	03DBDB|
|   Walking Dead	|		|	271E00	|	04A682	|	04B29A	|	------	|	040680	|	0484B5	|	092F01	|	03DBDC|
|   Zombie	|		|	271E74	|	04A683	|	04B29B	|	------	|	040681	|	0484B6	|	092F02	|	03DBDD|
|   Wight	|		|	271EE8	|	04A684	|	04B29C	|	------	|	040682	|	0484B7	|	092F03	|	03DBDE|
|   Wraith	|		|	271F5C	|	04A685	|	04B29D	|	------	|	040683	|	0484B8	|	092F04	|	03DBDF|
|   Vampire	|		|	271FD0	|	04A686	|	04B29E	|	------	|	040684	|	0484B9	|	092F05	|	03DBE0|
|   Vampire Lord	|		|	272044	|	04A687	|	04B29F	|	0412D8	|	040685	|	0484BA	|	092F06	|	03DBE1|
|   Lich			|		|	2720B8	|	04A688	|	04B2A0	|	0412D9	|	040686	|	0484BB	|	092F07	|	03DBE2|
|   Power Lich	|		|	27212C	|	04A689	|	04B2A1	|	0412DA	|	040687	|	0484BC	|	092F08	|	03DBE3|
|   Black Knight	|		|	2721A0	|	04A68A	|	04B2A2	|	0412DB	|	040688	|	0484BD	|	092F09	|	03DBE4|
|   Dread Knight	|		|	272214	|	04A68B	|	04B2A3	|	0412DC	|	040689	|	0484BE	|	092F0A	|	03DBE5|
|   Bone Dragon	|		|	272288	|	04A68C	|	04B2A4	|	0412DD	|	04068A	|	0484BF	|	092F0B	|	03DBE6|
|   Ghost Dragon	|		|	2722FC	|	04A68D	|	04B2A5	|	0412DE	|	04068B	|	0484C0	|	092F0C	|	03DBE7|

|   DUNGEON UNIT	|		|	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Troglodyte	|		|	272370	|	04A68E	|	04B2A6	|	0412DF	|	04068C	|	0484C1	|	092F0D	|	03DBE8|
|   Infernal Troglodyte	||	2723E4	|	04A68F	|	04B2A7	|	0412E0	|	04068D	|	0484C2	|	092F0E	|	03DBE9|
|   Harpy	|		|	272458	|	04A690	|	04B2A8	|	0412E1	|	04068E	|	0484C3	|	092F0F	|	03DBEA|
|   Harpy Hag	|		|	2724CC	|	04A691	|	04B2A9	|	0412E2	|	04068F	|	0484C4	|	092F10	|	03DBEB|
|   Beholder	|		|	272540	|	04A692	|	04B2AA	|	0412E3	|	040690	|	0484C5	|	092F11	|	03DBEC|
|   Evil Eye	|		|	2725B4	|	04A693	|	04B2AB	|	0412E4	|	040691	|	0484C6	|	092F12	|	03DBED|
|   Medusa	|		|	272628	|	04A694	|	04B2AC	|	0412E5	|	040692	|	0484C7	|	092F13	|	03DBEE|
|   Medusa Queen	|		|	27269C	|	04A695	|	04B2AD	|	0412E6	|	040693	|	0484C8	|	092F14	|	03DBEF|
|   Minotaur	|		|	272710	|	04A696	|	04B2AE	|	0412E7	|	040694	|	0484C9	|	092F15	|	03DBF0|
|   Minotaur King	||	272784	|	04A697	|	04B2AF	|	0412E8	|	040695	|	0484CA	|	092F16	|	03DBF1|
|   Manticore	|		|	2727F8	|	04A698	|	04B2B0	|	0412E9	|	040696	|	0484CB	|	092F17	|	03DBF2|
|   Scorpicore	|		|	27286C	|	04A699	|	04B2B1	|	0412EA	|	040697	|	0484CC	|	092F18	|	03DBF3|
|   Red Dragon	|		|	2728E0	|	04A69A	|	04B2B2	|	0412EB	|	040698	|	0484CD	|	092F19	|	03DBF4|
|   Black Dragon	|		|	272954	|	04A69B	|	04B2B3	|	0412EC	|	040699	|	0484CE	|	092F1A	|	03DBF5|

|   STRONGHOLD UNIT	||	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Goblin	|		|	2729C8	|	04A69C	|	04B2B4	|	0412ED	|	04069A	|	0484CF	|	092F1B	|	03DBF6|
|   Hobgoblin	|		|	272A3C	|	04A69D	|	04B2B5	|	0412EE	|	04069B	|	0484D0	|	092F1C	|	03DBF7|
|   Wolf Rider	|		|	272AB0	|	04A69E	|	04B2B6	|	0412EF	|	04069C	|	0484D1	|	092F1D	|	03DBF8|
|   Wolf Raider	|		|	272B24	|	04A69F	|	04B2B7	|	0412F0	|	04069D	|	0484D2	|	092F1E	|	03DBF9|
|   Orc	|		|			272B98	|	04A6A0	|	04B2B8	|	0412F1	|	04069E	|	0484D3	|	092F1F	|	03DBFA|
|   Orc Chieftain	||	272C0C	|	04A6A1	|	04B2B9	|	0412F2	|	04069F	|	0484D4	|	092F20	|	03DBFB|
|   Ogre	|		|			272C80	|	04A6A2	|	04B2BA	|	0412F3	|	0406A0	|	0484D5	|	092F21	|	03DBFC|
|   Ogre Mage	|		|	272CF4	|	04A6A3	|	04B2BB	|	0412F4	|	0406A1	|	0484D6	|	092F22	|	03DBFD|
|   Roc	|		|			272D68	|	04A6A4	|	04B2BC	|	0412F5	|	0406A2	|	0484D7	|	092F23	|	03DBFE|
|   Thunderbird	|		|	272DDC	|	04A6A5	|	04B2BD	|	0412F6	|	0406A3	|	0484D8	|	092F24	|	03DBFF|
|   Cyclops	|		|	272E50	|	04A6A6	|	04B2BE	|	0412F7	|	0406A4	|	0484D9	|	092F25	|	03DC00|
|   Cyclops King	|		|	272EC4	|	04A6A7	|	04B2BF	|	0412F8	|	0406A5	|	0484DA	|	092F26	|	03DC01|
|   Behemoth	|		|	272F38	|	04A6A8	|	04B2C0	|	0412F9	|	0406A6	|	0484DB	|	092F27	|	03DC02|
|   Ancient Behemoth	||	272FAC	|	04A6A9	|	04B2C1	|	0412FA	|	0406A7	|	0484DC	|	092F28	|	03DC03|

|   FORTRESS UNIT	||	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Gnoll	|		|	273020	|	04A6AA	|	04B2C2	|	0412FB	|	0406A8	|	0484DD	|	092F29	|	03DC04|
|   Gnoll Marauder	||	273094	|	04A6AB	|	04B2C3	|	0412FC	|	0406A9	|	0484DE	|	092F2A	|	03DC05|
|   Lizardman	|		|	273108	|	04A6AC	|	04B2C4	|	0412FD	|	0406AA	|	0484DF	|	092F2B	|	03DC06|
|   Lizard Warrior	||	27317C	|	04A6AD	|	04B2C5	|	0412FE	|	0406AB	|	0484E0	|	092F2C	|	03DC07|
|   Serpent Fly	|		|	2732D8	|	04A6B0	|	04B2C8	|	041301	|	0406AE	|	0484E1	|	092F2D	|	03DC0A|
|   Dragon Fly	|		|	27334C	|	04A6B1	|	04B2C9	|	041302	|	0406AF	|	0484E2	|	092F2E	|	03DC0B|
|   Basilisk	|		|	2733C0	|	04A6B2	|	04B2CA	|	041303	|	0406B0	|	0484E3	|	092F2F	|	03DC0C|
|   Greater Basilisk|	|	273434	|	04A6B3	|	04B2CB	|	041304	|	0406B1	|	0484E4	|	092F30	|	03DC0D|
|   Gorgon	|		|	2731F0	|	04A6AE	|	04B2C6	|	0412FF	|	0406AC	|	0484E5	|	092F31	|	03DC08|
|   Mighty Gorgon	||	273264	|	04A6AF	|	04B2C7	|	041300	|	0406AD	|	0484E6	|	092F32	|	03DC09|
|   Wyvern	|		|	2734A8	|	04A6B4	|	04B2CC	|	041305	|	0406B2	|	0484E7	|	092F33	|	03DC0E|
|   Wyvern Monarch	||	27351C	|	04A6B5	|	04B2CD	|	041306	|	0406B3	|	0484E8	|	092F34	|	03DC0F|
|   Hydra	|		|	273590	|	04A6B6	|	04B2CE	|	041307	|	0406B4	|	0484E9	|	092F35	|	03DC10|
|   Chaos Hydra	|		|	273604	|	04A6B7	|	04B2CF	|	041308	|	0406B5	|	0484EA	|	092F36	|	03DC11|

|   CONFLUX UNIT	|		|	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Pixie	|		|	273930	|	04A6BE	|	04B2D6	|	04130F	|	0406BC	|	0484F1	|	092F3D	|	03DC18|
|   Sprite	|		|	2739A4	|	04A6BF	|	04B2D7	|	041310	|	0406BD	|	0484F2	|	092F3E	|	03DC19|
|   Air Elemental	||	273678	|	04A6B8	|	04B2D0	|	041309	|	0406B6	|	0484EB	|	092F37	|	03DC12|
|   Storm Elemental	||	273D44	|	04A6C7	|	04B2DF	|	041318	|	0406C5	|	0484FA	|	092F46	|	03DC21|
|   Water Elemental	||	2737D4	|	04A6BB	|	04B2D3	|	04130C	|	0406B9	|	0484EE	|	092F3A	|	03DC15|
|   Ice Elemental	||	273B74	|	04A6C3	|	04B2DB	|	041314	|	0406C1	|	0484F6	|	092F42	|	03DC1D|
|   Fire Elemental	||	273760	|	04A6BA	|	04B2D2	|	04130B	|	0406B8	|	0484ED	|	092F39	|	03DC14|
|   Energy Elemental	||	273E2C	|	04A6C9	|	04B2E1	|	04131A	|	0406C7	|	0484FC	|	092F48	|	03DC23|
|   Earth Elemental	||	2736EC	|	04A6B9	|	04B2D1	|	04130A	|	0406B7	|	0484EC	|	092F38	|	03DC13|
|   Magma Elemental	||	273C5C	|	04A6C5	|	04B2DD	|	041316	|	0406C3	|	0484F8	|	092F44	|	03DC1F|
|   Psychic Elemental	||	273A18	|	04A6C0	|	04B2D8	|	041311	|	0406BE	|	0484F3	|	092F3F	|	03DC1A|
|   Magic Elemental	||	273A8C	|	04A6C1	|	04B2D9	|	041312	|	0406BF	|	0484F4	|	092F40	|	03DC1B|
|   Firebird	|		|	273EA0	|	04A6CA	|	------	|	04131B	|	0406C8	|	0484FD	|	092F49	|	03DC24|
|   Phoenix	|		|	273F14	|	04A6CB	|	------	|	04131C	|	0406C9	|	0484FE	|	092F4A	|	03DC25|

|   NEUTRAL UNIT	|		|	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Gold Golem	|		|	273848	|	04A6BC	|	04B2D4	|	04130D	|	0406BA	|	0484EF	|	092F3B	|	03DC16|
|   Diamond Golem	||	2738BC	|	04A6BD	|	04B2D5	|	04130E	|	0406BB	|	0484F0	|	092F3C	|	03DC17|
|   Azure Dragon	|		|	273F88	|	04A6CC	|	------	|	04131D	|	0406CA	|	0484FF	|	092F4B	|	03DC26|
|   Crystal Dragon	||	273FFC	|	04A6CD	|	------	|	04131E	|	0406CB	|	048500	|	092F4C	|	03DC27|
|   Faerie Dragon	||	274070	|	------	|	------	|	04131F	|	0406CC	|	048501	|	092F4D	|	03DC28|
|   Rust Dragon	|		|	2740E4	|	------	|	------	|	041320	|	0406CD	|	------	|	------	|	03DC29|
|   Enchanter	|		|	274158	|	------	|	------	|	------	|	0406CE	|	------	|	------	|	03DC2A|
|   Sharpshooter	|		|	2741CC	|	------	|	------	|	------	|	0406CF	|	------	|	------	|	03DC2B|
|   Halfling	|		|	274240	|	------	|	------	|	------	|	0406D0	|	------	|	------	|	03DC2C|
|   Peasant	|		|	2742B4	|	------	|	------	|	------	|	0406D1	|	------	|	------	|	03DC2D|
|   Boar	|				|	274328	|	------	|	------	|	------	|	0406D2	|	------	|	------	|	03DC2E|
|   Mummy	|		|	27439C	|	------	|	------	|	------	|	0406D3	|	------	|	------	|	03DC2F|
|   Nomad	|		|	274410	|	------	|	------	|	------	|	------	|	------	|	------	|	03DC30|
|   Rogue	|		|	274484	|	------	|	------	|	------	|	------	|	------	|	------	|	03DC31|
|   Troll	|		|	2744F8	|	------	|	------	|	------	|	------	|	------	|	------	|	03DC32|

|   WAR MACHINES/OTHER	||	DATA	|	RES.A	|	RES.B	|	ATK.A	|	ATK.B	|	SPL.A	|	(*)	|	SHOT|
|   ------------|------|-------|--------|---------|--------|--------|--------|--------|-----------|
|   Catapult	|		|	27456C	|	------	|	------	|	------	|	------	|	------	|	------	|	03DC33|
|   Ballista	|		|	2745E0	|	------	|	------	|	------	|	------	|	------	|	------	|	03DC34|
|   First Aid Tent	||	274654	|	------	|	------	|	------	|	------	|	------	|	------	|	------|
|   Ammo Cart	|		|	2746C8	|	------	|	------	|	------	|	------	|	------	|	------	|	------|
|   Arrow Tower	|		|	27473C	|	------	|	------	|	------	|	------	|	------	|	------	|	------|

>(*This table is redundant; setting 092A63 to 88 84 44 will always use SPL.A and free up 092ED4~F4F)

---------------------------------------------------------------------------------------------------------

					UNIT DATA (116 bytes)
					---------------------

		BYTE 01: Alignment			BYTE 05: Level (0-6)

		 00 = Castle      05 = Dungeon		BYTE 09: Small portrait
		 01 = Rampart     06 = Stronghold
		 02 = Tower       07 = Fortress		BYTE 13: Large portrait
		 03 = Inferno     08 = Conflux
		 04 = Necropolis  FF = Neutral		-----------------------

		BYTE 17: Ability flags			BYTE 18: Ability flags

		 BIT 1 (01) Unit occupies 2 hexes	 BIT 1 (01) Slayer lv. 2
		 BIT 2 (02) Flying			 BIT 2 (02) Slayer lv. 3
		 BIT 3 (04) Ranged attack		 BIT 3 (04) Mind immunity
		 BIT 4 (08) Attack hits 2 hexes		 BIT 4 (08) Shoots beam (GFX)
		 BIT 5 (10) Living unit			 BIT 5 (10) No melee penalty
		 BIT 6 (20) Can attack walls		 BIT 6 (20) (-)
		 BIT 7 (40) War Machine			 BIT 7 (40) Fire immunity
		 BIT 8 (80) Slayer lv. 1		 BIT 8 (80) Attacks twice

		BYTE 19: Ability flags			BYTE 20: Ability flags

		 BIT 1 (01) No enemy retaliation	 BIT 1 (01) (-)
		 BIT 2 (02) Morale has no effect	 BIT 2 (02) (-)
		 BIT 3 (04) Undead unit			 BIT 3 (04) (-)
		 BIT 4 (08) AoE melee attack		 BIT 4 (08) (-)
		 BIT 5 (10) *AoE ranged attack		 BIT 5 (10) (-)
		 BIT 6 (20) (-)				 BIT 6 (20) (-)
		 BIT 7 (40) (-)				 BIT 7 (40) (-)
		 BIT 8 (80) (-)				 BIT 8 (80) Unit is a dragon

		(*AI flag only; the actual ability is specified elsewhere)

			BYTE 21: (Unused beyond this point)

-----------------------------------------------------------------------------------------

Unless you're either changing the level of a neutral unit or fixing the bug where Ice, Energy, and Magma
Elementals have the incorrect level, you'll also need to edit the dwellings of any unit whose level you
intend to change (refer to the "Buildings" section below). For all practical purposes, the setting here
only concerns how certain spell specialties will affect them, the cost of Hill Fort upgrades, and their
appearance as random units on the adventure map. In effect, this setting is also used by towns to make
sure that everything behaves properly and things will break if you set multiple units from the same town
to the same level (i.e. Conflux's four elemental units), so you'll have to take a different approach if
that's what you're trying to do. In the below example, we'll use the free space from the redundant spell
table (see above) to set the four basic elemental units to level three and their upgrades to level four;
Psychic and Magic Elementals are set to five and six, respectively.

	------		-------------------------------------------------------------------------
	0C910E		; ELEMENTAL UNIT LEVELS (RANDOM UNITS)
	------		-------------------------------------------------------------------------
	EB 72		jmp 4C9182		; hop to long jump
	90 90		nop			; -

	------		-------------------------------------------------------------------------
	0C9182		; ""
	------		-------------------------------------------------------------------------
	E8 4D9DFCFF	call 492ED4		; -> free space (redundant spell table)
	EB 89		jmp 4C9112		; return

	------		-------------------------------------------------------------------------
	0E62BD		; ELEMENTAL UNIT LEVELS (SPELL SPECIALTIES)
	------		-------------------------------------------------------------------------
	57		push edi		; store EDI
	E8 17CCFAFF	call 492EDA		; -> free space (redundant spell table)
	5F		pop edi			; retrieve EDI

	------		-------------------------------------------------------------------------
	0E8021		; ELEMENTAL UNIT LEVELS (HILL FORTS)
	------		-------------------------------------------------------------------------
	E8 C6AEFAFF	call 492EEC		; -> free space (redundant spell table)
	90		nop			; -

	----------	-------------------------------------------------------------------------
	092ED4~F1E	; (EXPANDED SPACE - OVERWRITES REDUNDANT SPELL TABLE)
	----------	-------------------------------------------------------------------------
	8B 44 31 04	mov eax,[ecx+esi+04]	; (RANDOM UNITS:) EAX = unit's level
	EB 1B		jmp 492EF5		;

	8B 7E 34	mov edi,[esi+34]	; (SPELL SPECIALTIES:) EDI = unit ID
	8B C1		mov eax,ecx		; EAX = unit's level
	E8 11000000	call 492EF5		;
	8B0485C4EA6300	mov eax,[eax*4+63EAC4]	; (displaced code)
	C3		ret			; return

	8B 44 82 04	mov eax,[edx+eax*4+04]	; (HILL FORTS:) EAX = unit's level
	8B 13		mov edx,[ebx]		; (displaced code)
	8B 79 40	mov edi,[ecx+40]	; ""

	83 FF 70	cmp edi,70		; Air Elementals?
	74 20		je 492F1A		; if yes -> EAX +1

	83 FF 72	cmp edi,72		; Fire Elementals?
	74 1E		je 492F1D		; if yes -> EAX -1

	83 FF 71	cmp edi,71		; Earth Elementals?
	74 18		je 492F1C		; if yes -> EAX -2

	83 FF 7F	cmp edi,7F		; Storm Elementals?
	74 10		je 492F19		; if yes -> EAX +2

	83 FF 7B	cmp edi,7B		; Ice Elementals?
	74 0C		je 492F1A		; if yes -> EAX +1

	83 FF 7D	cmp edi,7D		; Magma Elementals?
	74 0A		je 492F1D		; if yes -> EAX -1

	83 FF 78	cmp edi,78		; Mind Elementals?
	74 05		je 492F1D		; if yes -> EAX -1
	C3		ret			; return

	40		inc eax			; EAX +2
	40		inc eax			; EAX +1
	C3		ret			; return

	48		dec eax			; EAX +2
	48		dec eax			; EAX -1
	C3		ret			; return (092F1F~4F is free space)

Regarding ranged attacks, removing them is as simple as unsetting the "ranged" flag and	setting the shot
count to 0 in CrTraits.txt. Adding a ranged attack is far more complicated outside of Centaurs, who were
originally intended to be ranged units as they were in previous games. This is evidenced by the presence
of ranged attack data for them in CrAnims.txt as well as the the fact that they're the only non-ranged
unit that can be given a ranged attack without crashing the game. In addition to flagging them as ranged
and giving them shots in CrTraits.txt, you will need to do two other things:

	• Edit their entries in the shot animations table:

		00 = Archer			09 = Orc
		01 = Monk			0A = Cyclops
		02 = Elf/Sharpshooter		0B = Lizardman
		03 = Master Gremlin		0C = Ice Elemental
		04 = Mage/Evil Eye		0D = Halfling
		05 = Titan/Storm Elemental	0E = Catapult
		06 = Gog			0F = Ballista
		07 = Lich			10 = (N/A)
		08 = Medusa			----------

	• Add a SFX for Centaur Captain shots to Heroes3.snd

The second point up there is especially peculiar, since it tells us that standard Centaurs actually have
shot SFX in the game data, but not their upgraded forms (likely owing to the fact that Centaurs weren't
upgradeable in HoMM2). The easiest solution here is to export the "CNTRSHOT.82M" sound effect file from
Heroes3.snd and rename it to "ECNTSHOT.82M", which can then be placed inside the "data" folder where it
will be automatically "soft"-patched into the game just as a .txt file would.

As for units with AoE ranged attacks, these are specified at the following addresses:

			03F72E: Fireball (Magog)
			------
			03FA21: Death Cloud (Liches)
			03FA2A: Death Cloud (Power Liches)

	(We'll look at some tweaks for both of these abilities further below)

The "can attack walls" ability will only work on a unit that has a ranged attack. Cyclopses and Cyclops
Kings are specifically named and given basic and advanced Ballistics skills, respectively, at 045AD4 and
045ACD; any other unit given this flag will attack with no skill. More specifically, the routine checks
for Cyclopses at 045AB1 by subtracting 5E (Cyclops ID) from EDI (ID of the active stack) and subtracting
01 if that check fails to check for Cyclops Kings. Finally, we subtract 32 from EDI at 045AB9 to check
for the catapult - thus, this value will also need to be changed if you edit the unit ID at 045AB1.

The "no enemy retaliation" flag is standard on all units with AoE melee attacks, but it's safe to remove
if so desired; they will only be countered by their "focused" target.

Proper unliving units combine three flags: "living" (unset), mind immunity, and "morale has no effect".
Gargoyles, notably, only have the "living" flag unset and thus lack several properties of unliving units
as defined by the original game (arguably a bug). Things that check the unliving flag for immunity are:

			Regeneration (Elixir Of Life)
			Life Drain   (Vampire Lords)
			Death Cloud  (Liches)
			Death Stare  (Mighty Gorgons)
			Aging        (Ghost Dragons)
			Disease      (Zombies)
			Poison       (Wyvern Monarchs)
			Sacrifice    (this includes the Pit Lord ability)
			Resurrection (this includes the Archangel ability)

Death Ripple SHOULD check for the "living" flag, but doesn't; a fix can be found in the "Spells" section
above. The petrify and paralyze unit abilities really should check for it, as well, but fixing those is
slightly trickier and will be discussed later. The "Artifacts" section further below will also show how
the Elixir of Life can be made to ignore this flag, if so desired.

The "mind immunity" flag is a bit more transparent: the list of mind spells is commonly known and can be
double-checked in the code as discussed earlier. Less well-known is that Psychic Elementals will do half
damage to any unit with mind immunity (they are named for this ability at 4392E).

Undead units combine all three of the "unliving" flags with the "undead" flag (naturally).


| Resistance A                        | Resistance B                            |
| ----------------------------------- | --------------------------------------- |
| 00 = 20% magic resist               | 00 = 50% spell damage resist            |
| 01 = 40% magic resist               | 01 = 75% spell damage resist            |
| 02 = Immune to lv. 1-3 spells       | 02 = Vulnerable to Lightning            |
| 03 = Immune to lv. 1-4 spells       | 03 = Vulnerable to Meteor Shower        |
| 04 = Immune to ALL spells            | 04 = Vulnerable to Ice                 |
| 05 = Immune to Meteor Shower        | 05 = Vulnerable to Fire                |
| 06 = Immune to Lightning             | 06 = 85% spell damage resist           |
| 07 = Immune to Ice                   | 07 = 95% spell damage resist           |
| 08 = None                            | 08 = None                              |


The values of 20% and 40% for the two magic resistance abilities are specified at 04A4C1
(CD CC 4C 3F = 0.80) and 04A4E8 (9A 99 19 3F = 0.60), respectively.

Elemental immunities and vulnerabilities (except for fire immunity, which is specified in
the unit data and blocks ALL fire spells - even beneficial ones) each check for specific
spell IDs, which can be changed at the following addresses:

| LIGHTNING WEAKNESS        | ICE WEAKNESS            | FIRE WEAKNESS            |
| ------------------------ | ------------------------| ------------------------ |
| 04B1A4 (Armageddon)       | 04B1C5 (Ice Bolt)       | 04B1EA (Fireball)        |
| 04B1A9 (Lightning Bolt)   | 04B1CA (Frost Ring)     | 04B1EF (Inferno)         |
| 04B1AE (Chain Lightning)  | ------ (-)              | 04B1F4 (Armageddon)      |
| 04B1B3 (Titan's Bolt)     | ------ (-)              |                          |

| METEOR SHOWER WEAKNESS    |                          |                          |
| ------------------------- | ------------------------ | ------------------------ |
| 04B1DC (Meteor Shower)    |                          |                          |

| LIGHTNING IMMUNITY        | ICE IMMUNITY             | METEOR SHOWER IMMUNITY   |
| ------------------------ | ------------------------ | ------------------------ |
| 04A50F (Armageddon)       | 04A535 (Ice Bolt)        | 04A4F3 (Meteor Shower)   |
| 04A514 (Lightning Bolt)   | 04A53A (Frost Ring)      |                          |
| 04A519 (Chain Lightning)  | ------ (-)              |                          |
| 04A51E (Titan's Bolt)     | ------ (-)              |                          |


>(Elemental units dealing extra damage to each other is not due to these settings, but is
 rather a function of a hard-coded ability called "hate", which will be covered later.)


Regarding fire immunity and its failure to distinguish between beneficial and harmful spells, there is
thankfully exactly enough space in the immunity code to rewrite it into something that makes more sense.
Note that this will replace immunity to Meteor Shower (which is dumb) with fire immunity (much better).

 	---------	---------------------------------------------------------------
	04A4EE~0E	; FIRE IMMUNITY (REPLACES METEOR SHOWER IMMUNITY)
	---------	---------------------------------------------------------------
	8B 45 F0	mov eax,[ebp-10]	; EAX = spell ID
	83 F8 0D	cmp eax,0D		; Fire Wall?
	74 0A		je 44A4FB		; if yes -> immunity

	83 F8 15	cmp eax,15		; Fireball?
	74 05		je 44A4FB		; if yes -> immunity

	83 F8 16	cmp eax,16		; Inferno? (the spell)
	75 C5		jne 44A4C5		; if no -> [exit]

	D9 05 64AC6300	fld [63AC64]		; immunity (load "0" value)
	5F 5E 5B	pop edi			; cleanup
	5E		pop esi			; ""
	5B		pop ebx			; ""
	8B E5		mov esp,ebp		; ""
	5D		pop ebp			; ""
	C2 08 00	ret 0008		; return

	---------	---------------------------------------------------------------
	04A50F~2F	; LIGHTNING IMMUNITY
	---------	---------------------------------------------------------------
	8B 45 F0	mov eax,[ebp-10]	; EAX = spell ID
	83 F8 11	cmp eax,11		; Lightning Bolt?
	74 0A		je 44A521		; if yes -> immunity

	83 F8 13	cmp eax,13		; Chain Lightning?
	74 05		je 44A521		; if yes -> immunity

	83 F8 4D	cmp eax,4D		; Thunder? (unit ability)
	75 A4		jne 44A4C5		; if no -> [exit]

	D9 05 64AC6300	fld [63AC64]		; immunity (load "0" value)
	5F 5E 5B	pop edi			; cleanup
	5E		pop esi			; ""
	5B		pop ebx			; ""
	8B E5		mov esp,ebp		; ""
	5D		pop ebp			; ""
	C2 08 00	ret 0008		; return

	04A64C > 0F	; moves Lightning Immunity exit pointer to new address

	------		---------------------------------------------------------------
	04A530		; ICE IMMUNITY
	------		---------------------------------------------------------------
	8B 45 F0	mov eax,[ebp-10]	; EAX = spell ID
	83 F8 10	cmp eax,10		; Ice Bolt?
	74 05		je 44A53D		; if yes -> immunity

	83 F8 14	cmp eax,14		; Frost Ring?
	75 88		jne 44A4C5		; if no -> [exit]

	D9 05 64AC6300	fld [63AC64]		; immunity (load "0" value)
	5F 5E 5B	pop edi			; cleanup
	5E		pop esi			; ""
	5B		pop ebx			; ""
	8B E5		mov esp,ebp		; ""
	5D		pop ebp			; ""
	C2 08 00	ret 0008		; return


This code does take a few creative liberties, most notably by adding the Thunderbird proc to lightning
immunity and removing Armageddon immunity for balance reasons (Armageddon spam strats are bullshit, yo).
This code can be modified to re-add Armageddon to fire immunity in place of Thunder immunity (in which
case it will no longer be necessary to move the lightning immunity exit pointer since the code will be
shifted back to its original location), but adding any more spells will mean finding some free space.

As we saw above, the "Resistance A" table runs up to Crystal Dragons, notably excluding Faerie and Rust
Dragons. Since the latter seems like a good candidate for fire immunity and there are two unused bytes
(04A6CD~F) at the end of the table, we can push it out to include them by changing 04A4AC to 77.

-----------------------------------------------------------------------------------------

Like fire immunity, immunity to lv. 1-X spells does not distinguish between friendly and harmful magic.
One balance issue in the original game is that Green and Red Dragons can be resurrected while Gold and
Black ones can't. One solution is to unflag all dragons as "living" units, thus rendering them immune to
Resurrection, or perhaps set Resurrection as a mind (or fire) spell and then give dragons the necessary
resistance. But these solutions are hacky at best and all go the route of making Green and Red Dragons
immune to resurrection rather than allowing it for Gold and Black. I would thus suggest the more elegant
approach of replacing spell immunity wholesale with spell damage resistance (used by Golems) combined if
so desired by immunity to mind spells to effectively block most harmful magic.

If you don't like the vanilla selection of spell damage resistance values, here are some others:

	66% Resistance: B8 56 55 55 55 F7 E9 8B CA 8B C1 5E 5D C2 04 00
	33% Resistance: B8 56 55 55 55 6B C9 02 F7 E9 8B CA 8B C1 5E 5D C2 04 00

Space-wise, this assumes that the two routines you'll be interested in changing are the ones for 85% and
95% spell damage resistance, both of which are substantially longer than the ones for 50% and 75% damage
resistance. Please note if overwriting the 95% resistance routine that the default (no resistance) exit
points to 04B253 and thus shares the "cleanup" portion of its code (8B C1 5E 5D C2 04 00).

One problem with the above recommendation is that the four "neutral" dragons are not within range of the
"Resistance B" table and are therefore ineligible for the spell damage reduction bonus unless we expand
it. We know how to do this now, and there are 14 free bytes at the end of the table for us to work with,
but that is unfortunately just shy of accomodating everything I want to do with it. Let's say we want to
pull the table back to include Dendroids so that they can be given a fire weakness, which we do by going
to 04B189 (the ID of the first unit on the table) and changing E0 (-20 for Stone Golems) to EA (-16 for
Dendroids). If we do this, however, we only have enough room at 04B18C to push the table out to include
Azure and Crystal Dragons before we run out of space. Thankfully, there's a way to fudge it that doesn't
even require any free space if we replace the 85% and 95% resistance routines with 33% and 66%.

	------		-------------------------------------------------------------------------
	04B187		; ADD DENDROIDS & FAERIE/RUST DRAGONS TO "RESISTANCE B" TABLE
	------		-------------------------------------------------------------------------
	E9 A7000000	jmp 44B233		; -> free space (85%/95% spell damage resistance)
	90		nop			; -

	---------	-------------------------------------------------------------------------
	04B233~44	; (EXPANDED SPACE - OVERWRITES 85%/95% SPELL DAMAGE RESISTANCE)
	---------	-------------------------------------------------------------------------
	8D 70 EA	lea esi,[eax-16]	; ESI = Unit ID -16
	83 FE 01	cmp esi,01		; is ESI <= 01? (Dendroid or Great Dendroid)
	77 02		ja 44B23D		; if no -> continue
	EB AB		jmp 44B1E8		; -> [X-Fire]
	4E		dec esi			; ESI = Unit ID -18 (table start = Unicorns)
	4E		dec esi			; ""
	83 FE 6F	cmp esi,6F		; is ESI > 6F? (table end = Rust Dragons)
	E9 46FFFFFF	jmp 44B18D		; return
	90 90 90	nop			; -

	---------	-------------------------------------------------------------------------
	04B220~32	; 33% SPELL DAMAGE RESISTANCE
	---------	-------------------------------------------------------------------------
	B8 56555555	mov eax,55555556	; EAX = divisor
	6B C9 02	imul ecx,02		; ECX*2
	F7 E9		imul ecx		; EDX = 2/3 damage
	8B CA		mov ecx,edx		; cleanup
	8B C1		mov eax,ecx		; ""
	5E		pop esi			; ""
	5D		pop ebp			; ""
	C2 04 00	ret 0004		; return

	---------	-------------------------------------------------------------------------
	04B24A~59	; 66% SPELL DAMAGE RESISTANCE
	---------	-------------------------------------------------------------------------
	B8 56555555	mov eax,55555556	; EAX = divisor
	F7 E9		imul ecx		; EDX = 1/3 damage
	8B CA		mov ecx,edx		; cleanup
	8B C1		mov eax,ecx		; "" (note: default exit points here)
	5E		pop esi			; ""
	5D		pop ebp			; ""
	C2 04 00	ret 0004		; return

	04B278 > 4A	; update exit pointer for 95% (now 66%) routine

In short, what we're doing here is setting the table to run from Unicorns to Rust Dragons, which is all
that the space will allow. We check specifically for Dendroids/Great Dendroids before we head into the
table and just send them directly to the fire weakness routine on a match. Remember that this code will
shift the "Resistance B" table (04B280~EF) forward by 8 bytes - i.e. Stone Golems will move from 04B280
to 04B288 - and so everything on it will need to be edited to compensate.

Finally, just as Psychic Elementals do half damage to targets with mind magic immunity, so too do Magic
Elementals deal half damage to those with immunity to all spells. However, while Psychic Elementals will
properly check their targets for the mind immunity flag, Magic Elementals instead just check to see if
their target is one of the only two fully magic-immune units in the game: Black Dragons (at 04395C) or
other Magic Elementals (043957). And this brings us back to the topic of "hate" from earlier.

As mentioned above, the ability of elementals to do extra damage to each other is a actually function of
the "hate" mechanic, more commonly recognized as the tendency of certain units to deal extra damage to
their perennial rivals. The units who hate each other are named at the following addresses:

	0431B5	Devil		0431C5	Angel		04314A	Air		043157	Earth
	0431BA	Archdevil	0431CA	Archangel	04314F	Storm		04315C	Magma
	-----------------	-----------------	-------------		-------------
	0431D5	Genie		0431E5	Efreet		043166	Fire		043182	Water
	0431DA	Master G	0431EA	Sultan		04316A	Energy(*)	043187	Ice
	----------------	--------------
	0431F5	Titan		0431FA	Black D		*this is a long/unsigned CMP function

>(Note that only Titans and Black Dragons hate each other; Giants and Red Dragons do not)

Where this all comes together is that I think we can do much better than this. Hate is kind of a stupid
idea to begin with, but elemental units respecting the elemental resistances and immunities of other
units with their attacks is a much better one that just needs a little fleshing out.

	---------	------------------------------------------------------------------------
	04312B~A3	; PHYSICAL ATTACKS CONSIDER ELEMENTAL WEAKNESSES (OVERWRITES HATE)
	---------	------------------------------------------------------------------------
	8B 4B 34	mov ecx,[ebx+34]	; ECX = Attacker
	8B 47 34	mov eax,[edi+34]	; EAX = Defender

	8D 40 EA	lea eax,[eax-16]	; EAX -16
	83 F8 01	cmp eax,01		; is EAX <= 01? (Dendroid or Great Dendroid)
	77 02		ja 44313B		; if no -> EAX = Unit ID -18
	EB 12		jmp 44314D		; -> Gogs?

	48		dec eax			; EAX = Unit ID -18 (table start = Unicorns)
	48		dec eax			; ""
	83 F8 6F	cmp eax,6F		; is EAX > 6F? (table end = Rust Dragons)
	77 5D		ja 44319F		; if yes -> exit

	8A 80 80B24400	mov al,[eax+44B280]	; AL = Resistance B (Weakness)

	83 F8 05	cmp eax,05		; X-Fire? (if no -> X-Ice?)
	75 14		jne 443161		; ""
	83 F9 2C	cmp ecx,2C		; Gogs? (if yes -> +50% damage)
	74 40		je 443192		; ""
	83 F9 2D	cmp ecx,2D		; Magogs? (if yes -> "")
	74 3B		je 443192		; ""
	83 F9 72	cmp ecx,72		; Fire Elementals? (if yes -> "")
	74 36		je 443192		; ""
	83 F9 7D	cmp ecx,7D		; Magma Elementals? (if yes -> "")
	74 31		je 443192		; ""

	83 F8 04	cmp eax,04		; X-Ice? (if no -> X-Ice?)
	75 0A		jne 443170		; ""
	83 F9 73	cmp ecx,73		; Water Elementals? (if yes -> +50% damage)
	74 27		je 443192		; ""
	83 F9 7B	cmp ecx,7B		; Ice Elementals? (if yes -> "")
	74 22		je 443192		; ""

	83 F8 02	cmp eax,02		; X-Lightning? (if no -> Troglodyte Soldiers?)
	75 0D		jne 443182		; ""
	83 F9 7F	cmp ecx,7F		; Storm Elementals? (if yes -> +50% damage)
	74 18		je 443192		; ""
	81 F9 81000000	cmp ecx,81		; Energy Elementals? (if yes -> "")
	74 10		je 443192		; ""

	83 F9 47	cmp ecx,47		; Troglodyte Soldiers? (if no -> exit)
	75 18		jne 44319F		; ""
	8A 8F 90020000	mov cl,[edi+290]	; CL = target's "Blind" duration
	80 F9 00	cmp cl,00		; Blind? (if no -> exit)
	74 0D		je 44319F		; ""
	8B 55 08	mov edx,[ebp+08]	; +50% damage
	8B 45 F0	mov eax,[ebp-10]	; ""
	01 D0		add eax,edx		; ""
	89 45 F0	mov [ebp-10],eax	; ""
	EB 67		jmp 443206		; continue
	E9 6C020000	jmp 443410		; exit (0431A2~220 is free space - see below)

	------		------------------------------------------------------------------------
	04394D		; PHYSICAL ATTACKS CONSIDER ELEMENTAL IMMUNITIES
	------		------------------------------------------------------------------------
	8B 4B 34	mov ecx,[ebx+34]	; ECX = Defender
	E9 4FF8FFFF	jmp 4431A4		; -> free space (hate)

	---------	------------------------------------------------------------------------
	0431A4~FD	; (EXPANDED SPACE - OVERWRITES HATE)
	---------	------------------------------------------------------------------------
	8D 49 F0	lea ecx,[ecx-10]	; ECX = Defender -10
	83 F9 77	cmp ecx,77		; is ECX > 77? (table end = Rust Dragons)
	77 4D		ja 4431F9		; if yes -> exit

	8A 89 58A64400	mov cl,[ecx+44A658]	; CL = Resistance A

	83 F9 05	cmp ecx,05		; O-Fire? (if no -> O-Ice?)
	75 14		jne 4431CB		; ""
	83 F8 2C	cmp eax,2C		; Gogs? (if yes -> [half damage])
	74 37		je 4431F3		; ""
	83 F8 2D	cmp eax,2D		; Magogs? (if yes -> "")
	74 32		je 4431F3		; ""
	83 F8 72	cmp eax,72		; Fire Elementals? (if yes -> "")
	74 2D		je 4431F1		; ""
	83 F8 7D	cmp eax,7D		; Magma Elementals? (if yes -> "")
	74 28		je 4431F1		; ""

	83 F9 06	cmp ecx,06		; O-Ice? (if no -> O-Lightning?)
	75 0A		jne 4431DA		; ""
	83 F8 73	cmp eax,73		; Water Elementals? (if yes -> [half damage])
	74 1E		je 4431F3		; ""
	83 F8 7B	cmp eax,7B		; Ice Elementals? (if yes -> "")
	74 19		je 4431F3		; ""

	83 F9 05	cmp ecx,05		; O-Lightning? (if no -> O-Magic?)
	75 0C		jne 4431EB		; ""
	83 F8 7F	cmp eax,7F		; Storm Elementals? (if yes -> [half damage])
	74 0F		je 4431F3		; ""
	3D 81000000	cmp eax,81		; Energy Elementals? (if yes -> "")
	74 08		je 4431F3		; ""

	83 F9 04	cmp ecx,04		; O-Magic? (if no -> exit)
	75 09		jne 4431F9		; ""
	83 F8 79	cmp eax,79		; Magic Elementals? (if yes -> [half damage])
	0F84 66070000	je 44395F		; ""

	E9 6D070000	jmp 44396B		; -> [continue]
	90 90 90 90	nop			; -
	90 90 90 90	nop			; -

	------		-------------------------------------------------------------------------
	03F8E7		; FIRE IMMUNITY NEGATES DAMAGE FROM EXPLOSIVE FIREBALLS (MAGOGS)
	------		-------------------------------------------------------------------------
	E9 DC3B0000	jmp 4434C8		; -> free space (hate)
	90		nop			; -

	---------	-------------------------------------------------------------------------
	0434C8~F1	; (EXPANDED SPACE - OVERWRITES HATE)
	---------	-------------------------------------------------------------------------
	83 FF 06	cmp edi,06		; is defender the main target of the attack?
	74 1A		je 4434E7		; if yes -> (displaced code)

	8B 48 34	mov ecx,[eax+34]	; ECX = Defender
	8D 49 F0	lea ecx,[ecx-10]	; ECX -10
	83 F9 77	cmp ecx,77		; is ECX > 77? (table end = Rust Dragons)
	77 0F		ja 4434E7		; if yes -> (displaced code)

	8A 89 58A64400	mov cl,[ecx+44A658]	; CL = Resistance A
	83 F9 05	cmp ecx,05		; O-Fire?
	0F84 9BC4FFFF	je 43F982		; if yes -> [no damage]
	8B 0D 20946900	mov ecx,[699420]	; (displaced code)
	E9 FBC3FFFF	jmp 43F8ED		; -> [continue]

	--------	-------------------------------------------------------------------------
	04396B~F	; RESISTANCE SPELLS REDUCE DAMAGE FROM ELEMENTALS
	--------	-------------------------------------------------------------------------
	E9 82FBFFFF	jmp 4434F2		; -> free space (hate)

	----------	-------------------------------------------------------------------------
	0434F2~543	; (EXPANDED SPACE - OVERWRITES HATE)
	----------	-------------------------------------------------------------------------
	83 7E 34 70	cmp [esi+34],70		; Air Elementals? (if no -> Earth Elementals?)
	75 09		jne 443501		; ""
	80BB1002000000	cmp byte [ebx+210],0	; Air Resistance? (if yes -> half damage)
	7F 2D		jg 44352E		; ""
	83 7E 34 71	cmp [esi+34],71		; Earth Elementals? (if no -> Fire Elementals?)
	75 09		jne 443510		; ""
	80BB1C02000000	cmp byte [ebx+21C],0	; Earth Resistance? (if yes -> half damage)
	7F 1E		jg 44352E		; ""
	83 7E 34 72	cmp [esi+34],72		; Fire Elementals? (if no -> Water Elementals?)
	75 09		jne 44351F		; ""
	80BB1402000000	cmp byte [ebx+214],0	; Fire Resistance? (if yes -> half damage)
	7F 0F		jg 44352E		; ""
	83 7E 34 73	cmp [esi+34],73		; Water Elementals? (if no -> displaced code)
	75 15		jne 44353A		; ""
	80BB1802000000	cmp byte [ebx+218],0	; Water Resistance? (if no -> displaced code)
	74 0C		je 44353A		; ""
	DD 45 F8	fld qword [ebp-08]	; load damage
	DC 0D 70AC6300	fmul qword [63AC70]	; damage * 0.50
	DD 5D F8	fstp qword [ebp-08]	; store damage
	8A 45 0C	mov al,[ebp+0C]		; (displaced code)
	84 C0		test al,al		; ""
	E9 2C040000	jmp 443970		; return (043544~5F is free space)

So, what's going on here? Simply put, elemental damage from physical attacks is multiplied by 1.5 on a
weakness and halved on resistance, either unit-inherent or from a spell. This code assumes that you've
expanded the resistance tables per the above suggestions and will need to be adjusted if you haven't.
Also of note is halved damage from Magic Elementals on magic-immune units, which now specifically looks
for a value of 4 in Resistance A. If you've changed this ability to spell damage resistance as per the
earlier suggestion, then we can use the Resistance A setting here purely to denote that a unit should
take half damage from Magic Elementals; simply change its exit pointer to the default exit (04A644~5 to
C5 A4) to remove the original effect of being immune to all spells.

While the resistance tables are used to determine if the defender resists or is weak against the attack,
we do have to specifically name units to determine the type of damage being dealt. For this, I erred on
the side of both symmetry and common sense: Fire and Magma Elementals deal "fire" damage, Water and Ice
Elementals deal "ice" damage, and Storm and Energy Elementals deal "lightning" damage - thus leaving Air
and Earth Elementals dealing neutral damage. The only other units which deal elemental damage are Gogs,
which are a little tricky to handle. The explosive effect of Magog fireballs is the source of much ire
due to their tendency to damage nearby friendlies, so we set fire-immune units to completely negate the
splash damage while the target unit at the center (if immune) will still take half damage as normal.

Resistance spells are coded to work a bit differently than natural resistances for several reasons, both
balance-wise (since the spells can be cast on any unit) and just to work how you'd expect them to. Thus,
resistance spells offer a straight 50% damage reduction regardless of magnitude and reduce damage only
from the four basic elemental units excluding their upgrades. Natural resistances will stack with spell
resistance for a total reduction of 75%, but this is easy to undo if so desired. Simply point the exit
for no natural resistance to the resist spell check (0431FA > F4 02) and omit the jump at 04396B.

Beyond that, anyone who actually reads the commentary on this stuff will probably notice the rider that
was slipped into the weakness code for Infernal Troglodytes hitting a weakness on targets with the blind
status (it makes more sense within the context of my own hack where blind has been re-branded as "fear"
to be more indicative of how it actually functions).

In any case, if you use the new code above (or even if you don't), you'll probably want to go into the
GenrlTxt.txt file and rewrite the "burning with anger" to something closer to "strikes a weakness".


		ATTACK A					ATTACK B
		--------					--------
	00 = Life Drain	    (Vampire Lord)		00 = Entangle	    (Dendroid)
	01 = Thunderbolt    (Thunderbird)		01 = Blind	    (Unicorn)
	02 = Death Stare    (Mighty Gorgon)		02 = Disease	    (Zombie)
	03 = Dispel	    (Serpent Fly)		03 = Curse	    (Black Knight & Mummy)
	04 = *Acid Breath   (Rust Dragon)		04 = Aging	    (Ghost Dragon)
	05 = None					05 = Petrify	    (Medusa & Basilisk)
	     ---					06 = Paralyze	    (Scorpicore)
	     ---					07 = Poison	    (Wyvern Monarch)
	     ---					08 = *Acid Breath   (Rust Dragon)
	     ---					09 = None

	     (*Attack A is the chance for extra damage, Attack B is the defense reduction)


Many of the abilities specified above - as well as several that aren't - have a random
chance of activating after every attack made by the unit. The odds for such abilities to
"proc" are 20% for the most part, although they're specified individually for each:

	040264 = Aging		04033E = Blind		040C07 = Death Stare
	040433 = Curse		0404A7 = Petrify	040EC4 = Thunderbolt
	0436E0 = Deathblow	0405D1 = Paralyze	0411DE = Acid Breath
	0402D9 = Disease	040560 = Poison		0649D8 = Fear*

		*This isn't a % chance, but rather the inverse (see below)

Fear, for whatever reason, is coded completely differently than the other random effects.
The value of 0A here, or "10" in decimal format, doesn't mean 10% like the others all do.
Rather, it means, "select a random number between 1 and this value and apply the effect
if the chosen number is that value". 0A thus actually does give us a 10% chance, but 05
would give us 20% and 14 (20 in decimal) would give us 5%.

Death Stare also behaves a bit differently than you might expect - though the 0A here at
least does actually mean 10%. Each Mighty Gorgon in the stack has its own 10% chance of
insta-killing its target unit, with the stipulation that the total number of insta-kills
can't exceed 1/10 of the number of Mighty Gorgons attacking. Thus, a stack of 10 Mighty
Gorgons has an effective 65% chance (1 - 0.9^10) of insta-killing a unit whereas a stack
of 20 has an 88% chance (1 - 0.9^20) of insta-killing at LEAST one unit. The math gets
confusing beyond this point, and I'm also not sure if the value at 040C07 concerns the
hard limit on the total number of insta-kills or just the chance of rolling them.

Blind, petrify, and paralyze are named at 043E1C, 043E25, and 043E2E, respectively, for
removal if the afflicted unit is attacked. We will go over shortly how to set variable
durations for different statuses (the standard 3-turn duration is specified at 068CD9).

The blind status, when set by a unit, will be set with no skill level (i.e. the target
will retaliate at the strength specified in SpTraits.txt if attacked). Paralyzed targets,
when attacked, will retaliate at half strength. If desired, we can make them inable to
retaliate at all - which is notably separate from paralyze not being removed when hit.

	---------	-------------------------------------------------------------------------
	041ACD~E9	; PARALYZED UNITS WILL NOT BE ABLE TO RETALIATE
	---------	-------------------------------------------------------------------------
	8B 4D 08	mov ecx,[ebp+08]	; (shifted code)
	51		push ecx		; ""
	56		push esi		; ""
	8B CF		mov ecx,edi		; ""
	E8 57F8FFFF	call 441330		; ""
	8B 8E C0020000	mov ecx,[esi+2C0]	; ECX = defender's paralyze duration
	85 C9		test ecx,ecx		; is defender paralyzed?
	0F85 9E000000	jne 441B85		; if yes -> [no retaliation]
	90 90 90	nop			; -

The half damage to petrified units is specified by a QWORD pointer at 043D49. Changing
the DC at 043D47 to D8 switches this to a DWORD pointer and gives us some more options:

    05% - E4 AE 63 00	10% - D0 B8 63 00	15% - 28 EB 63 00	20% - B4 B8 63 00
    25% - 9C 05 64 00	30% - 24 EB 63 00	40% - B0 B8 63 00	75% - 98 05 64 00

>(Or we can just make our own floating value as we learned in the "Skills" section above)

The value of both the attack and defense reductions from disease is specified at 0446EF.
We can also set it to lower speed by an adjustable amount with the following rewrite:

    ---------	-------------------------------------------------------------------------
    044BED~38	; DISEASE ALSO LOWERS SPEED
    ---------	-------------------------------------------------------------------------
    8B BE CC000000	mov edi,[esi+CC]	; EDI = target's DEF
    8B 86 C8000000	mov eax,[esi+C8]	; EAX = target's ATK
    8B CA 		mov ecx,edx		; ECX = magnitude

    39 C8		cmp eax,ecx		; is target's ATK less than the magnitude?
    7D 02		jnl 444C01		; if no -> check defense
    8B C8		mov ecx,eax		; do not subtract more ATK than target has

    39 D7		cmp edi,edx		; is target's DEF less than the magnitude?
    7D 02		jnl 444C07		; if no -> subtract defense
    8B D7		mov edx,edi		; do not subtract more ATK than target has

    29 96 CC000000	sub [esi+CC],edx	; subtract DEF
    29 8E C8000000	sub [esi+C8],ecx	; subtract ATK
    88 D5		mov ch,dl		; ECX = attack & defense subtracted
    89 8E D0040000	mov [esi+4D0],ecx	; store above for when status is removed

    6A XX		push XX			; EDX = SPD magnitude (XX)
    5A		        pop edx			; ""
    8B BE C4000000	mov edi,[esi+C4]	; EDI = target's SPD
    39 D7		cmp edi,edx		; is target's ATK less than the magnitude?
    7D 02		jnl 444C2A		; if no -> subtract defense
    8B D7		mov edx,edi		; do not subtract more SPD than target has

    29 96 C4000000	sub [esi+C4],edx	; subtract SPD
    89 96 D4040000	mov [esi+4D4],edx	; store above for when status is removed
    90 90 90	nop			        ; -

    ---------	-------------------------------------------------------------------------
    0444B9~E0	; "" (WHEN REMOVING STATUS)
    ---------	-------------------------------------------------------------------------
    668B8ED0040000	mov cx,[esi+4D0]	; CL/CH = ATK/DEF to restore
    8B 96 D4040000	mov edx,[esi+4D4]	; EDX = SPD to restore
    00 8E C8000000 	add [esi+C8],cl		; restore ATK
    00 AE CC000000	add [esi+CC],ch		; restore DEF
    01 96 C4000000	add [esi+C4],edx	; restore SPD
    90 90 90 90 90	nop			; -
    90 90 90 90	        nop			        ; -

    ---------	-------------------------------------------------------------------------
    0443B3~C5	; "" (UPDATE STONESKIN REMOVAL TO NO LONGER SHARE ABOVE CODE)
    ---------	-------------------------------------------------------------------------
    8B 86 70040000	mov eax,[esi+470]	; EAX = DEF to remove
    29 86 CC000000	sub [esi+CC],eax	; remove DEF
    E9 1D010000	        jmp 4444E1		; -> [continue]
    90 90		nop			; -

The value of the defense reduction of Acid Breath B is specified at 1A2188 (FD, or -3).
Unlike nearly every other bit of text in the game, the in-battle text for Acid Breath's
defense reduction is for some reason hard-coded in the .exe file (starting at 2884A0).

-----------------------------------------------------------------------------------------

As mentioned earlier, neither paralyze nor petrify check for immunity, which they probably should. These
checks can be easily added with some free space, which in the below examples will come from the removal
of the lengthy "Acid Breath A" routine. Regardless of what space you use, you'll need to go to the exit
pointers for Petrify (040648) and/or Paralyze (04064C) and edit them to point to the new address. These
are DWORD pointers, as we should know by now, so remember that they're written backwards: "96 04 44 00"
will thus point to 440496. This address doesn't actually exist in the .exe file because runtime offsets
all memory by 400000. Thus, in a hex editor, this points to 040496.

	---------	-------------------------------------------------------------------------
	0411BF~D7	; PETRIFY IMMUNITY CHECK (OVERWRITES "ACID BREATH A")
	---------	-------------------------------------------------------------------------
	8B 7D 08	mov edi,[ebp+08]	; EDI = defender
	8B 87 84000000	mov eax,[edi+84]	; EAX = defending unit data
	C1 E8 04	shr eax,04		; shift to "living" flag
	A8 01		test al,01		; is unit alive?
	0F 84 DBF0FFFF	je 4402AE		; if no -> [exit]
	E9 BEF2FFFF	jmp 440496		; -> [petrify]

	---------	-------------------------------------------------------------------------
	0411D8~F0	; PARALYZE IMMUNITY CHECK (OVERWRITES "ACID BREATH A")
	---------	-------------------------------------------------------------------------
	8B 7D 08	mov edi,[ebp+08]	; EDI = defender
	8B 87 84000000	mov eax,[edi+84]	; EAX = defending unit data
	C1 E8 04	shr eax,04		; shift to "living" flag
	A8 01		test al,01		; is unit alive?
	0F 84 C2F0FFFF	je 4402AE		; if no -> [exit]
	E9 CFF3FFFF	jmp 4405C0		; -> [paralyze] (0411F1~2AA is free space)

Now, suppose we want to take these immunities one step farther and tie them to a different flag so that
certain "living" units (Angels or Genies, for example) can be given them. Bit 6 on byte 18 is unused, so
we'll use that for this example. The relevant command in the above examples is the bit shift (C1 E8 04),
which we simply change to C1 E8 0D to check for the different bit. Then, because we're checking for the
presence of this flag rather than its absence, we change the jumps from "jump if equal" (74 XX or 0F 84
XX XX XX XX) to "jump if not equal" (75 XX or 0F 85 XX XX XX XX).

The abilities which already check the "living" flag can be edited at the following addresses:

	    DISEASE		    POISON		     AGING		  DEATH STARE
	---------------		---------------		---------------		----------------
	0402C3: 04 > 0D		040545: 04 > 0D		04024D: 04 > 0D		040BE3: 04 > 0D
	0402C6: 74 > 75		04054A: 84 > 85		040251: 74 > 75		040BE8: 84 > 85


Continuing with the space we freed from "Acid Breath A", let's allow variable odds of "Attack B" effects
depending on the relative sizes of the attacking and defending stacks, as well as allowing certain units
to have a higher success rate. The below code will specify a 30% chance of success for stacks that are
relatively even in size with a variance of up to +/-20% if either side is outnumbered by more than 3:1.
After that, certain units will have their success rate doubled - potentially allowing for 100% odds.

	----------	-------------------------------------------------------------------------
	0411F1~286	; VARIABLE "ATTACK B" ODDS (OVERWRITES "ACID BREATH A")
	----------	-------------------------------------------------------------------------
	E8 CAB50C00	call 50C7C0		; EAX = 0~64 (displaced code)

	8B 4E 4C	mov ecx,[esi+4C]	; ECX = # of attackers
	8B 57 4C	mov edx,[edi+4C]	; EDX = # of defenders
	39 D1		cmp ecx,edx		; more attackers than defenders?
	7F 35		jg 441235		; if yes ->

	01 C9		add ecx,ecx		; do defenders outnumber more than 2:1?
	39 D1		cmp ecx,edx		; ""
	7F 12		jg 441218		; if yes -> next check

	03 4E 4C	add ecx,[esi+4C]	; do defenders outnumber more than 1.5:1?
	C1 F9 02	sar ecx,02		; ""
	39 D1		cmp ecx,edx		; ""
	7F 04		jg 441214		; if yes -> 25% odds
	6A 1E		push 1E			; 30% odds
	EB 50		jmp 441264		; ""
	6A 19		push 19			; 25% odds
	EB 4C		jmp 441264		; ""

	01 C9		add ecx,ecx		; do defenders outnumber more than 3:1?
	39 D1		cmp ecx,edx		; ""
	7F 11		jg 44122F		; if yes -> 10% odds

	03 4E 4C	add ecx,[esi+4C]	; do defenders outnumber more than 2.5:1?
	D1 F9		sar ecx,1		; ""
	39 D1		cmp ecx,edx		; ""
	7F 04		jg 44122B		; if yes -> 15% odds
	6A 14		push 14			; 20% odds
	EB 39		jmp 441264		; ""
	6A 0F		push 0F			; 15% odds
	EB 35		jmp 441264		; ""
	6A 0A		push 0A			; 10% odds
	EB 31		jmp 441264		; ""

	01 D2		add edx,edx		; do attackers outnumber more than 2:1?
	39 D1		cmp ecx,edx		; ""
	7F 12		jg 44124B		; if yes -> next check

	03 57 4C	add edx,[edi+4C]	; do attackers outnumber more than 1.5:1?
	C1 FA 02	sar edx,02		; ""
	39 D1		cmp ecx,edx		; ""
	7F 04		jg 441247		; if yes -> 35% odds
	6A 1E		push 1E			; 30% odds
	EB 1D		jmp 441264		; ""
	6A 23		push 23			; 35% odds
	EB 19		jmp 441264		; ""

	01 D2		add edx,edx		; do attackers outnumber more than 3:1?
	39 D1		cmp ecx,edx		; ""
	7F 11		jg 441262		; if yes -> 50% odds

	03 57 4C	add edx,[edi+4C]	; do attackers outnumber more than 2.5:1?
	D1 F9		sar ecx,1		; ""
	39 D2		cmp edx,edx		; ""
	7F 04		jg 44125E		; if yes -> 45% odds
	6A 28		push 28			; 40% odds
	EB 06		jmp 441264		; ""
	6A 2D		push 2D			; 45% odds
	EB 02		jmp 441264		; ""
	6A 32		push 32			; 50% odds
	59		pop ecx			; ECX = odds

	8B 56 34	mov edx,[esi+34]	; EDX = unit ID

	83 FA 3B   	cmp edx,3B		; Zombies?
	74 17		je 441284		; if yes -> double odds

	83 FA 4D	cmp edx,4D		; Medusa Queens?
	74 12		je 441284		; if yes -> 2/3 odds

	83 FA 69	cmp edx,69		; Dragonflies?
	74 0D		je 441284		; if yes -> 2/3 odds

	83 FA 6B	cmp edx,6B		; Greater Basilisks?
	74 08		je 441284		; if yes -> 2/3 odds

	81 FA 8D000000	cmp edx,8D		; Mummies?
	75 02		jne 441286		; if no -> return

	01 C9		add ecx,ecx		; double odds
	C3		ret 			; return

	...and then we just call this code as desired from the following routines like so:

			Curse      04042C > E8 C00D0000 39 C8 90
			Blind      040337 > E8 B50E0000 39 C8 90
			Disease    0402D2 > E8 1A0F0000 39 C8 90
			Petrify    0404A0 > E8 4C0D0000 39 C8 90
			Paralyze   0405CA > E8 220C0000 39 C8 90
			Poison     040559 > E8 930C0000 39 C8 90
			Aging      04025D > E8 8F0F0000 39 C8 90


Next, let's look at setting variable durations for unit-set statuses depending on the status being set.
The below code takes the somewhat-obvious route of reducing the ones that completely disable units to 2
turns while substantially raising the others to the point that either a First Aid Tent or the Cure spell
will be needed to get rid of them in a timely manner.

	------		-------------------------------------------------------------------------
	068CD8		; VARIABLE "ATTACK B" DURATION
	------		-------------------------------------------------------------------------
	E9 AA85FDFF	jmp 441287		; -> free space (Acid Breath A)
	90		nop			; -

	---------	-------------------------------------------------------------------------
	041287~AA	; (EXPANDED SPACE - OVERWRITES "ACID BREATH A")
	---------	-------------------------------------------------------------------------
	83 F8 46	cmp eax,46		; Petrify?
	74 0A		je 441296		; if yes -> 2 turns

	83 F8 4A	cmp eax,4A		; Paralyze?
	74 05		je 441296		; if yes -> 2 turns

	83 F8 3E	cmp eax,3E		; Blind?(*)
	75 06		jne 44129C		; if no -> 5 turns

	6A 02		push 02			; 2 turns
	6A 02		push 02			; advanced level (for Blind)
	EB 04		jmp 4412A0		; -> (displaced code)

	6A 05		push 05			; 5 turns (Disease, Poison, Aging)
	6A 00		push 00			; unskilled (for Acid Breath B - see below)
	6A FF		push -01		; (displaced code)
	E9 377A0200	jmp 468CDE		; return
	90 90 90 90	nop			; -

>(*This is important if you changed Blind's duration earlier to depend on skill level)

Of particular note is the fact that the original code does not check to see if the target unit has yet
taken its turn, meaning that the standard 3-turn duration was effectively 2~3 turns in practice since
statuses are cleared at the beginning of each combat round. This was discussed earlier with the Frenzy
spell edit, where we saw how to route every spell with a duration through a check to see if the target
stack has moved. That edit also affects physical statuses, as they are treated as spells in the code.

-----------------------------------------------------------------------------------------

While we have axed the "Acid Breath A" routine, the one that reduces defense (Acid Breath B) is still
perfectly usable independent of its counterpart. If it seems familiar, that's because it literally just
casts the Disrupting Ray spell with a different animation. The below code will change this effect to use
the standard spell animation while repurposing the modified one for a new counterpart effect which will
instead increase the attacker's attack power for every non-lethal(*) attack. Both effects will share an
exit pointer in the "Attack B" table; we'll just check for a specific unit once we get there.

>(*The "non-lethal" bit is necessary since it would otherwise prevent the victim's death animation)

Also note: since we're flat-out casting Disrupting Ray with this effect, the magnitude will be limited
to whatever the spell itself is set to. The desired skill level can be adjusted in the "Variable Attack
B Duration" code above - see the "unskilled" push, which will only affect this ability.

	---------	-------------------------------------------------------------------------
	04050A~39	; DISRUPTING RAY & ENRAGE (FORMERLY "ACID BREATH B")
	---------	-------------------------------------------------------------------------
	8B 45 08	mov eax,[ebp+08]	; EAX = defender
	8B 48 4C	mov ecx,[eax+4C]	; ECX = # of units in defending stack
	85 C9		test ecx,ecx		; is defender is dead?
	7E 1C		jle 440530		; if yes -> exit

	8B 4E 34	mov ecx,[esi+34]	; ECX = attacking unit ID
	83 F9 4F	cmp ecx,4F		; Minotaur Kings?
	75 0B		jne 440527		; if no -> Disrupting Ray
	6A 50		push 50			; 50 = Enrage
	59		pop ecx			; ""
	89 8E EC000000	mov [esi+EC],ecx	; move to attacker's stack data
	EB 09		jmp 440530		; -> [exit]

	6A 2F		push 2F			; 2F = Disrupting Ray
	59		pop ecx			; ""
	89 88 EC000000	mov [eax+EC],ecx	; move to defender's stack data
	E9 79FDFFFF	jmp 4402AE		; -> [exit]
	9090909090	nop			; -

	--------	-------------------------------------------------------------------------
	1A2180~8	; ENRAGE (ATTACK UP INSTEAD OF DEFENSE DOWN)
	--------	-------------------------------------------------------------------------
	8387C8000000XX	add [edi+C8],XX		; Attack +X
	EB 14		jmp 5A219D		; -> [continue] 1A2189~9C is free

	---------	-------------------------------------------------------------------------
	2884A0~CF	; ENRAGE TEXT (CHANGED FROM ACID BREATH)
	---------	-------------------------------------------------------------------------
	54 68 65 20 61 74 74 61 63 6B 20 6F 66 20 74 68	; "The attack of the %s increases by %i"
	65 20 25 73 20 69 6E 63 72 65 61 73 65 73 20 62	; ""
	79 20 25 69 00 00 00 00 00 00 00 00 00 00 00 00	; ""

	---------	-------------------------------------------------------------------------
	1A222A~35	; ENRAGE TEXT (VALUE OF %I)
	---------	-------------------------------------------------------------------------
	8D 55 88	lea edx,[ebp-78]	; (displaced code)
	6A XX		push XX			; Attack +X
	90909090909090	nop			; -

---------------------------------------------------------------------------------------------------------

## UNIT SPELLCASTERS

The "spell" array above points specific units to their appropriate routines. Unfortunately, whether or
not a unit can cast spells in the first place is hard-coded elsewhere and is also limited to units with
casting animations, so this information can't be used as a way to add more casters. And since removing a
unit's ability to cast spells is a simple matter of setting the appropriate value in CrTraits.txt to 0,
the only thing you can do with this information is point an existing caster to another spell routine.

		00 = Archangels		    05 = Magma Elementals
		01 = Master Genies	    06 = Storm Elementals
		02 = Pit Lords		    07 = Energy Elementals
		03 = Ogre Magi		    08 = Faerie Dragons
		04 = Ice Elementals	    09 = N/A

As you can see, both Archangels and Pit Lords are considered to be spellcasters here, meaning that the
"once per battle" limitations for both are specified in the "spells" field of CrTraits.txt. Further, the
target unit summoned by Pit Lords is specified at 1A776B (again, this is a signed value, so anything
higher than 7F will crash the game). The other routines can be edited at the following locations:

| Elemental / Creature      | Power             | Level             | Spell ID          |
| --------------------------| ------------------| ------------------| ------------------|
| Storm Elementals          | 048388            | 04838A            | 048391            |
| Ice Elementals            | 048398            | 04839A            | 0483A1            |
| Energy Elementals         | 0483A8            | 0483AA            | 0483B1            |
| Magma Elementals          | 0483B8            | 0483BA            | 0483C1            |

| Creature                  | Power             | Level             | Spell ID          |
| --------------------------| ------------------| ------------------| ------------------|
| Ogre Mages                | 0483C8            | 0483CA            |                  |
| Master Genies             | 047CE1            | 047CE3            |                  |
| Enchanters                | 047F66            | 047F68            |                  |
| Faerie Dragons(*)         | 048370            | 048375            | 1A01DE            |

>(*See below for details)

Before you go too crazy editing the above addresses, however, there are several caveats that need to be
discussed about unit spellcasters as a whole. With the exceptions of Enchanters and Faerie Dragons, they
are only able to target friendly units, so any kind of offensive spell is out. They are also unable to
handle spells with any additional required input - assigning Teleport to a unit spellcaster will cause
them to disappear into the ether whenever they cast it. On the plus side, they can be made to allow for
self-targeting  by setting 07601C to EB (for human players) and 020F84 to 90 90 (for the AI).

For units which cast a specific spell (Ogre Magi and the upgraded Elementals), you'll need to update the
battle log hover text in the following locations if you change the spell:

	    092BFA = 00 10 (Resist Air)	    092C39 = 10 11 (Resist Water)
	    092C88 = 88 10 (Resist Fire)    092CC7 = 98 11 (Resist Earth)
	    092D50 = E8 16 (Bloodlust)	    -----------------------------

The above values are the spell ID multiplied by 88 (hex) plus 10 (also hex). For example, if we want to
change Bloodlust to Frenzy, we open up Windows calculator because fuck trying to do this by hand, set it
to "programmer" mode, change it from decimal to hex, and then multiply 38 (Frenzy's spell ID) by 88, and
then add 10 to get a value of 1DD4. We then break it up into two bytes (1D and D4) and then, because it
needs to be inverted in the actual code, write D4 1D to 092D50.

We'll also need to update the AI settings to prevent it from unnecessarily spamming the new spell over
and over again. We find a value of 44 02 at 03BF8F, which is equal to 198 plus Bloodlust's spell ID (2B)
multiplied by 4. - for Frenzy, we need to change this value to 78 02. The AI is specifically looking for
the presence of a status on the unit to determine if the spellcast is necessary, and so this will pose a
problem for any non-status spell. Cure can work, however, with a value of 50 00 (check for missing HP).

(|I have no idea where similar checks exist for the upgraded elemental units)

The power for Faerie Dragon spells is five times the number of dragons in the stack. This multiplier can
be changed to any value you wish by changing 048370 to 6B C0 XX (where "XX" is the desired number). The
skill level of their spells is specified at 048375 (0 = Basic, 1 = Advanced, 2 = Expert) except when on
Magic Plains, in which case it instead uses 1A01DE (0 = Unskilled, 1 = Basic, 2 = Advanced, 3 = Expert).

Faerie Dragons and Enchanters both behave differently than other unit spellcasters in a number of ways.
Most obviously, they cast their spells differently: Enchanters will do so before they attack instead of
instead of attacking and Faerie Dragons will always attack with spells unless they have no alternative.
They're also the only units that can cast spells offensively and do so from set pools (see below) rather
than being limited to just one. Finally, there is no limit to how many spells they can cast per battle.

As for which spells they can cast, their tables start at 23B850 and 2608B8, respectively:

	--------------------				      ----------------
	FAERIE DRAGON SPELLS				      ENCHANTER SPELLS
	--------------------				      ----------------

   23B850 = 10 00 00 00    23B854 = 16 00 00 00	2608B8 = 35 00 00 00	2608BC = 0F 00 00 00
   23B858 = 11 00 00 00    23B85C = 16 00 00 00	2608C0 = 1C 00 00 00	2608C4 = 0A 00 00 00
   23B860 = 15 00 00 00    23B864 = 15 00 00 00	2608C8 = 36 00 00 00	2608CC = 0A 00 00 00
   23B868 = 0F 00 00 00    23B86C = 0A 00 00 00	2608D0 = 2E 00 00 00	2608D4 = 0F 00 00 00
   23B870 = 14 00 00 00    23B874 = 0A 00 00 00	2608D8 = 2B 00 00 00	2608DC = 05 00 00 00
   23B878 = 13 00 00 00    23B87C = 05 00 00 00	2608E0 = 29 00 00 00	2608E4 = 0F 00 00 00
   23B880 = 17 00 00 00    23B884 = 05 00 00 00	2608E8 = 25 00 00 00	2608EC = 0A 00 00 00
   23B888 = 16 00 00 00    23B88C = 05 00 00 00	2608F0 = 2D 00 00 00	2608F4 = 04 00 00 00

The first byte of each entry in the columns on the left are spell IDs, while the following byte in the
right column is the "weight" of that spell (i.e. how likely it is to be chosen). The sum of these values
is different for each table, so it doesn't appear to be a situation where everything has to add up to a
specific number like with hero skill probabilities, so feel free to edit them to your liking. Your only
major limitation is that there's no room in either table to add more spells without rewriting some code.

Finally, Master Genies are the only other unit to cast more than one spell. Rather, they will cast ANY
friendly battle spell in the game at random. This is probably more annoying than useful, especially if
you want to remove any spells that they may cast. Simply moving their exit pointer to either the Faerie
Dragon or Enchanter routines isn't an option due to how differently they work from normal spellcasters,
but it's a fairly simple matter to rewrite the Master Genie routine to suit your tastes. There are two
examples below: one to give them a single spell and one to give them a custom pool. Both will free up a
substantial amount of space since the routine to pick any available spell was quite suboptimal.

	048464 > F1 7B	; update exit pointer (needed for both of the below, frees 048351~D)

	----------	-------------------------------------------------------------------------
	047BF1~C0E	; MASTER GENIE SPELLCAST TO A SPECIFIC SPELL
	----------	-------------------------------------------------------------------------
	8B 45 08	mov eax,[ebp+08]	; EAX = target
	8B 0D 20946900	mov ecx,[699420]	; ECX = combat manager
	6A XX		push XX			; XX = magic power
	6A XX		push XX			; XX = skill level (0~3)
	6A FF		push -01		; ???
	6A 01		push 01			; ???
	50		push eax		; push target
	6A XX		push XX			; XX = spell ID
	E8 36851500	call 5A0140		; cast spell
	E9 CE070000	jmp 4483DD		; -> [continue]

	----------	-------------------------------------------------------------------------
	047BF1~C1D	; MASTER GENIE SPELLCAST TO A SPELL POOL
	----------	-------------------------------------------------------------------------
	31 C9		xor ecx,ecx		; ECX = 0
	6A XX		push XX			; XX = number of spells in pool -1
	5A		pop edx			; EDX = XX
	E8 C54B0C00 	call 50C7C0		; EAX = 0~XX
	8A 80 1E7C4400	mov al,[eax+00447C1E]	; EAX = spell ID
	8B 55 08 	mov edx,[ebp+08]	; EDX = target
	8B 0D 20946900	mov ecx,[699420]	; ECX = combat manager
	6A XX		push XX			; XX = magic power
	6A XX		push XX			; XX = skill level (0~3)
	6A FF		push -01		; ???
	6A 01		push 01			; ???
	52		push edx		; push target
	50		push eax		; push spell ID
	E8 27851500	call 5A0140		; cast spell
	E9 BF070000	jmp 4483DD		; -> [continue]

	447C1E > XX XX XX... ; spell ID 1, 2, 3... (space is free up to 047BFF)

Again, the only limitations here are that they must be friendly spells (unless you like killing your own
units) and must require no further input (Teleport won't work). While there's no "weighting" like in the
other pools, you can accomplish the same thing with less space by having multiple entries for any spell
that you'd like to show up more frequently. There's upwards of 200 bytes that will be free after the new
routine, so you can get as precise as you'd like with it. As for the hover text, Master Genies use line
303 in GenrlTxt.txt ("cast a spell on...") which is unique to them, so feel free to modify it as needed.

Master Genies do, however, run a similar status check to Ogre Magi to determine whether or not to cast a
spell. For a specific spell, we'll need to update that check. We do so by running Master Genies and Ogre
Magi through the same routine and simply adjusting one variable as needed, which frees up a significant
amount of space from the old Master Genie routine (03C0EE~24B).

	---------	-------------------------------------------------------------------------
	43BF76~92	; COMBINE MASTER GENIE & OGRE MAGI STATUS CHECK ROUTINES (INLINE EDIT)
	---------	-------------------------------------------------------------------------
	55		push ebp		; (shifted code)
	8B EC		mov ebp,esp		; ""
	83 EC 3C	sub esp,3C		; ""
	53		push ebx		; ""
	56		push esi		; ""
	8B 5D 08	mov ebx,[ebp+08]	; ""
	8B F1		mov esi,ecx		; ""
	BA 58020000	mov edx,258		; EDX = 258 (Prayer)
	83 F8 25	cmp eax,25		; Master Genies?
	74 03		je 43BF90		; if no -> EAX = unit's status duration
	83 C2 20	add edx,20		; EDX +20 (278 = Frenzy)
	8B 04 1A	mov eax,[edx+ebx]	; EAX = unit's status duration

	020FC0 > 05	; Master Genies to same routine as Ogre Magi (020FD7~E5 is free space)
	020FCE > A4	; adjust call to status check routine to use prior free space

As you can see in the above example, we have selected Prayer as our Master Genie spell and Frenzy as our
Ogre Magi spell. We initially set EDX to 258 for Prayer and then add 20 to get 278 for Ogre Magi. Adjust
these two values as needed for whatever other spell you set them to. I believe that a similar edit would
be necessary for the spell pool approach above, but I have not looked into it as of yet.

---------------------------------------------------------------------------------------------------------

## NO RANGE & NO OBSTACLE (I.E. SIEGE WALL) PENALTIES

Units and artifacts with these abilities are named at the following addresses:

    NO OBSTACLE PENALTY			NO RANGE PENALTY
    -------------------			----------------
    06719A = 5B (Golden Bow)		067217 = 5B (Golden Bow)
    0671AC = 89 (Sharpshooter's Bow)	06722D = 89 (Sharpshooter's Bow)

    06711F = 22 (Mages)			067242 = 95 (Arrow Tower)
    067128 = 23 (Archmagi)			06724D = 89 (Sharpshooters)
    067130 = 88 (Enchanters)		---------------------------
    06713B = 89 (Sharpshooters)		---------------------------
    067146 = 95 (Arrow Tower)		---------------------------

>(The range penalty threshold of 10 hexes is specified at 06732F)

As we saw earlier with the elemental summon spells, the CMP opcodes used for Mages and
Archmages (83 F8 XX) use one signed byte and are thus limited to values of 7F or lower.
All of the other unit checks here are using the longer CMP opcode (3D XX 00 00 00) which
allows for higher values. The artfiact checks are similar, except they're using "push"
commands (6A 5B for the Golden Bow and 68 89 00 00 00 for the Sharpshooter's Bow).

(Since most unit IDs are <= 7F, most of the checks we'll see will be signed ones.)

Something else to keep in mind as we move forward is that you can remove a unit from this
list by specifying a redundant ID or one of the unused creature IDs: 7A, 7C, 7E, or 80.
I'd advise not using that last one for reasons that are hopefully obvious by now.

With the addition of the Sharpshooter's Bow in the SoD expansion, the Golden Bow ends up
feeling weirdly redundant. Should you choose to remove it from the game (we'll go over
how to do so later on), here's some code to transfer its bonus to two more units:

	---------	-------------------------------------------------------------------------
	067214~40	; NO RANGE PENALTY: MARKSMEN & TITANS (OVERWRITES GOLDEN BOW)
	---------	-------------------------------------------------------------------------
	74 12		je 467228		; (shortened jump)
	68 89000000	push 89			; Sharpshooter's Bow?
	E8 40220700	call 4D9460		; ""
	84 C0		test al,al		; ""
	0F85 E7010000	jne 46740F		; if yes -> [pass]

	8B 47 34	mov eax,[edi+34]	; EAX = attacker unit ID

	83 F8 03	cmp eax,03		; Marksmen?
	0F84 DB010000	je 46740F		; if yes -> [pass]

	83 F8 29	cmp eax,29		; Titans?
	0F84 D2010000	je 46740F		; if yes -> [pass]
	90 90 90 90	nop			; -

-----------------------------------------------------------------------------------------

## UNITS' special abilities

### REGENERATION (WIGHTS/WRAITHS & TROLLS)

The magnitude of this effect is set at 046C2F and 046C35 (both addresses must be edited).
The default is 32 (50 HP), which is more than a full heal for all three units with this
ability (Wights/Wraiths and Trolls) - the primary reason to edit this value is that it's
also used by the Elixir of Life (see the "Artifacts" section for details on editing it).

Which units possess this ability are specified at 046BD8 (Wight), 046BDD (Wraith), and
046BE1 (Troll). To reiterate the above, Trolls are using a longer CMP opcode than Wights
and Wraiths since their ID is greater than 7F.

-----------------------------------------------------------------------------------------

### MAGIC MIRROR, CRYSTAL GENERATION, & FEAR (FAERIE/CRYSTAL/AZURE DRAGONS)

The unit IDs for these abilities are at 04852B, 0B8933, and 0649AB, respectively.

Fear, curiously, checks the "morale has no effect" flag for immunity instead of the mind
immunity flag. To have Fear check mind immunity, go to 064934 and set 11 to 0A.

Alternatively, getting rid of fear entirely can be accomplished by going to 64920 and
writing C2 04 00, which will free up a substantial amount of space (064923~B2F) that we
will be looking into using for several new abilities below.

-----------------------------------------------------------------------------------------

### JOUSTING (CAVALIERS) & JOUSTING IMMUNITY (PIKEMEN)

The unit IDs for the jousting ability are set at 043068 and 043074.

(NOTE: unlike in the arcade days, jousting will not work on flying units)

Pikemen and Halberdiers (both immune to jousting) are specifically checked as defenders
at 04307A and 043080, respectively. However, while most checks are CMP (3 byte) commands,
the check for Pikemen (ID 0) is a 2-byte command which can only check for a zero value.
This is a pretty lame bonus, however, so I opted to overwrite it with code that doubles
the jousting bonus from 5% per hex to 10% for Champions.

	---------	-------------------------------------------------------------------------
	043077~94	; 2X JOUSTING BONUS FOR CHAMPIONS
	---------	-------------------------------------------------------------------------
	DB 45 08	fild [ebp+08]		; (original code shifted upward)
	DD 5D E4	fstp [ebp-1C]		; ""
	DB 45 18	fild [ebp+18]		; ""
	DD 5D EC	fstp [ebp-14]		; ""
	DD 45 E4	fld [ebp-1C]		; ""
	DC 4D EC	fmul [ebp-14]		; ""

	83 F8 0A	cmp eax,0A		; Champions?
	74 07		je 443095		; if no -> [exit]

	DC 0D 40AC6300	fmul [63AC40]		; doubles Jousting bonus
	90		nop			; -


As for Pikemen, let's dive into the "Fear" space we cleared out above and use it for two
new abililities: double bonus to defense when defending (for Pikemen and Halberdiers) and
first-strike retaliation when defending (Halberdiers only).

	------		-------------------------------------------------------------------------
	0790C3		; 2x DEFENSE BONUS WHEN DEFENDING (PIKEMEN & HALBERDIERS)
	------		-------------------------------------------------------------------------
	E8 5BB8FEFF	call 464923		; -> free space (Fear)

	---------	-------------------------------------------------------------------------
	064923~31	;  (EXPANDED SPACE - OVERWRITES FEAR)
	---------	-------------------------------------------------------------------------
	83 7B 34 01	cmp [ebx+34],01		; is unit ID <= 01? (Pikeman or Halberdier)
	7F 03		jg 46492C		; if higher -> (displaced code)
	6B C9 02	imul ecx,02		; double defense bonus
	8B 43 4C	mov eax,[ebx+4C]	; (displaced code)
	39 F8		cmp eax,edi		; ""
	C3		ret			; return

	------		-------------------------------------------------------------------------
	041A22		; FIRST-STRIKE RETALIATION WHEN DEFENDING (HALBERDIERS)
	------		-------------------------------------------------------------------------
	E9 0B2F0200	jmp 464932		; -> free space (Fear)
	90 90 90	nop			; -

	---------	-------------------------------------------------------------------------
	064932~78	; (EXPANDED SPACE - OVERWRITES FEAR)
	---------	-------------------------------------------------------------------------
	85 F6		test esi,esi		; is there a valid defender? (displaced code)
	0F84 4CD3FDFF	je 441C86		; if no -> [exit] ""

	83 7E 34 01	cmp [esi+34],01		; Halberdier?
	75 34		jne 464974		; if no -> return

	8B 96 84000000	mov edx,[esi+84]	; EDX = defender unit data
	C1 EA 1B	shr edx,1B		; shift to "defending" flag
	F6 C2 01	test dl,01		; is unit defending?
	74 26		je 464974		; if no -> return

	8B 8E 54040000	mov ecx,[esi+454]	; ECX = defender's retaliations
	85 C9		test ecx,ecx		; any left?
	74 1C		je 464974		; if no -> return

	FF 8E 54040000	dec [esi+454]		; defender's retaliations -1
	FF 87 54040000	inc [edi+454]		; attacker's retaliations +1
	FF 86 57040000	inc [esi+457]		; set attacker's "retaliation" flag (see below)
	FF 87 57040000	inc [edi+457]		; set defender's "retaliation" flag ("")
	57		push edi		; swap attacker and defender
	56		push esi		; ""
	5F		pop edi			; ""
	5E		pop esi			; ""
	E9 B1D0FDFF	jmp 441A2A		; return

The flags we set to indicate a retaliation in the above code aren't strictly necessary
for the effect to function, but rather are for compatibility with the Counterstrike edit
from earlier. It will also allow for compatibility with a brand new effect, which allows
Battle Dwarves (or any other unit) to inherently deal more damage with retaliations:

	---------	-------------------------------------------------------------------------
	04172E~32	; 25% DAMAGE BONUS WHEN RETALIATING (BATTLE DWARVES)
	---------	-------------------------------------------------------------------------
	E9 46320200	jmp 464979		; -> free space (Fear)

	---------	-------------------------------------------------------------------------
	064979~8E	; (EXPANDED SPACE - OVERWRITES FEAR)
	---------	-------------------------------------------------------------------------
	E8 E2F2FDFF	call 443C60		; (displaced code)
	83 7E 34 11	cmp [esi+34],11		; Battle Dwarves?
	75 06		jne 46498A		; if no -> ECX = Counterstrike level
	6B C0 05	imul eax,05		; damage * 5
	C1 F8 02	sar eax,02		; damage / 4 (result: 125%)
	E9 A4CDFDFF	jmp 441733		; return

	---------	-------------------------------------------------------------------------
	041B5D~61	; SET RETALIATION FLAG FOR BATTLE DWARVES(*)
	---------	-------------------------------------------------------------------------
	E8 2D2E0200	call 46498F		; -> free space (Fear)

	041B4D > 90 90	; NOP out pushes to be moved to free space

	---------	-------------------------------------------------------------------------
	06498F~9D	; (EXPANDED SPACE - OVERWRITES FEAR)
	---------	-------------------------------------------------------------------------
	53		push ebx		; (displaced code)
	57		push edi		; ""
	80B65704000001	xor byte [esi+457],01	; toggle "temp" flag before calling damage routine
	E8 93C9FDFF	call 441330		; damage routine (retaliation)
	C3 		ret			; return
	---------	-------------------------------------------------------------------------
	041B78~92	; UNSET RETALIATION FLAG(*)
	---------	-------------------------------------------------------------------------
	FF 8E 54040000	dec [esi+454]		; (optimized code)
	31 C0		xor eax,eax		; ""
	8986C0040000	mov [esi+4C0],eax	; ""
	C6865704000000	mov byte [esi+457],00	; unflag retaliation
	909090909090	nop			; -

	041B20 > 5D	; update jump pointer(*)
	041B24 > 59	; ""
	041B16 > 67	; ""
	041B0C > 71	; ""
	041AFB > 7F	; ""
	041AE3 > 97	; ""

>*These edits are redundant with the Counterstrike overhaul; only one set is needed

-----------------------------------------------------------------------------------------

### EXTRA RETALIATIONS (GRIFFINS)

The unit ID for two retaliations is set at 03D6A2 & 046E67 (change both), while the value
of 2 is specified at 03D6B8 & 046E89.

The unit ID for infinite retaliations is set at 03D6BE & 046E8F (again change both),
while a value of "88 13" (5,000 retaliations) is specified at 03D6C7 & 046E98.

It's possible to optimize the code so that we can add this ability to more units; the
below example will add a second retaliation to Naga Queens and Boars:

	---------	-------------------------------------------------------------------------
	03D6A0~CA	; ADD EXTRA RETALIATIONS TO NAGA QUEENS AND HOBGOBLINS
	---------	-------------------------------------------------------------------------
	89 4E 5C	mov [esi+5C],ecx	; (shifted code)

	83 F8 04	cmp eax,04		; Griffins?
	74 15		je 43D6BD		; if yes -> 2 retaliations

	83 F8 05	cmp eax,05		; Royal Griffins?
	74 14		je 43D6C1		; if yes -> infinite retaliations

	83 F8 27	cmp eax,27		; Naga Queens?
	74 0B		je 43D6BD		; if yes -> 2 retaliations

	3D 8C000000	cmp eax,8C		; Boars?
	74 04		je 43D6BD		; if yes -> 2 retaliations

	6A 01		push 01			; 1 retaliation
	EB 06		jmp 43D6C3		; -> EAX = retaliations
	6A 02		push 02			; 2 retaliations
	EB 02		jmp 43D6C3		; -> EAX = retaliations
	6A 69		push 69			; infinite retaiations (nice)
	58		pop eax			; EAX = retaliations
	89 86 54040000	mov [esi+454],eax	; store retaliations
	90		nop			; -

	---------	-------------------------------------------------------------------------
	046E65~9B	; ""
	---------	-------------------------------------------------------------------------
	89 9E 84000000	mov [esi+84],ebx	; (shifted code)
	8B CB		mov ecx,ebx		; ""
	C686F004000000	mov byte [esi+4F0],00	; ""

	83 F8 04	cmp eax,04		; Griffins?
	74 15		je 446E8E		; if yes -> 2 retaliations

	83 F8 05	cmp eax,05		; Royal Griffins?
	74 14		je 446E92		; if yes -> infinite retaliations

	83 F8 27	cmp eax,27		; Naga Queens?
	74 0B		je 446E8E		; if yes -> 2 retaliations

	3D 8C000000	cmp eax,8C		; Boars?
	74 04		je 446E8E		; if yes -> 2 retaliations

	6A 01		push 01			; 1 retaliation
	EB 06		jmp 446E94		; -> EAX = retaliations
	6A 02		push 02			; 2 retaliations
	EB 02		jmp 446E94		; -> EAX = retaliations
	6A 69		push 69			; infinite retaiations (nice)
	58		pop eax			; EAX = retaliations
	89 86 54040000	mov [esi+454],eax	; store retaliations
	90		nop			; -

-----------------------------------------------------------------------------------------

### RESISTANCE AURA (UNICORNS & WAR UNICORNS)

The unit IDs for this ability are set at 03E802 and 03E807.

-----------------------------------------------------------------------------------------

### SPELL DAMPER (PEGASI & SILVER PEGASI) & DISCOUNT (MAGES & ARCHMAGES)

The unit IDs for the damper ability are set at 0E554D and 0E555A, while the amount of SP
added to enemy spell costs is set at 0E5568.

The unit IDs for the discount ability are set at 0E5570 and 0E557D, while the amount of
SP subtracted from spell costs is set at 0E558B.

A problem with both of these abilities is that they will continue to work for the rest of
a battle even after the stacks are dead. I elected to address each issue separately: the
"damper" ability felt extremely awkward as a unit ability and so I set it to an artifact
power instead, while the spell discount is fixed by making it only work during the turn
of the unit that provides it. The magnitude for both has been increased, substantially so
in the case of the "damper" effect (note that I attached it to a combo artifact), and in
both cases the amount is dependent on the spell's level. Making this an inline edit that
requires no free space does limit you to just one unit for the discount, however; I went
with Familiars since this actually seemed like a more fitting ability for them.

	---------	-------------------------------------------------------------------------
	0E5530~9F	; SPELL DAMPER TO ARTIFACT & DISCOUNT TO ONLY WORK ON UNIT'S TURN
	---------	-------------------------------------------------------------------------
	57		push edi		; store EDI (repositioned code)
	8B 15 A87F6800	mov edx,[687FA8]	; EDX = spell index
	69 F6 88000000	imul esi,88		; ESI = data range
	8B 7C 32 18	mov edi,[edx+esi+18]	; EDI = spell level
	8D 34 86	lea esi,[esi+eax*4]	; ESI + skill level
	8B 74 32 20	mov esi,[edx+esi+20]	; ESI = spell cost
	8B 45 0C	mov eax,[ebp+0C]	; EAX = defending army (if in combat)
	85 C0		test eax,eax		; are we in combat?
	74 48		je 4E5597		; if no -> (cleanup)

	A1 20946900	mov eax,[699420]	; EAX = combat manager
	8B 90 C8320100	mov edx,[eax+132C8]	; EDX = active stack data
	85 D2		test edx,edx		; is there an active unit?
	74 39		je 4E5597		; if no -> (cleanup)
	83 7A 34 2B	cmp [edx+34],2B		; Familiars?
	75 02		jne 4E5566		; if no -> ECX = active stack's owner
	29 FE		sub esi,edi		; subtract spell level from cost

	8B 8A F4000000	mov ecx,[edx+F4]	; ECX = active stack's owner (0/1)
	83BA8802000000	cmp [edx+288],00	; is stack Hypnotized?
	74 03		je 4E5578		; if yes -> ECX = enemy hero data
	83 F1 01	xor ecx,01		; invert ECX
	8B8C88CC530000	mov ecx,[eax+ecx*4+53CC]; ECX = enemy hero data
	85 C9		test ecx,ecx		; is there any enemy hero?
	74 14		je 4E5597		; if no -> (cleanup)

	68 8A000000	push 8A			; 8A = Wizard's Well
	E8 D33EFFFF	call 4D9460		; check for artifact
	84 C0		test al,al		; do we have it?
	74 06		je 4E5597		; if no -> is spell cost <=0?
	47		inc edi			; EDI (spell level) + 1
	6B FF 05	imul edi,05		; EDI * 5
	01 FE		add esi,edi		; add EDI to spell cost

	8B C6		mov eax,esi		; (cleanup)
	5F		pop edi			; ""
	5E		pop esi			; ""
	5B		pop ebx			; ""
	5D		pop ebp			; ""
	EB 44		jmp 4E55E3		; -> free space
	90		nop			; -

	--------	-------------------------------------------------------------------------
	0E55E3~C	; (EXPANDED SPACE - UNUSED IN ORIGINAL GAME)
	--------	-------------------------------------------------------------------------
	3C 00		cmp al,00		; has spell cost been reduced below 1?
	7F 03		jg 4E55EA		; if no -> return
	31 C0		xor eax,eax		; spell cost = 1
	40		inc eax			; ""
	C2 0C00		ret 0C			; return

-----------------------------------------------------------------------------------------

### MAGIC CHANNEL (FAMILIARS)

The unit ID for this ability is set at 1A24F6.

The percentage of enemy spell costs absorbed is calculated by some bullshit division that
starts at 1A249F. The default amount is 20%; two easy alternative options are:

			50%	1A24B4 > 8B 55 98 D1 EA
			100%	1A24B4 > 8B 55 98 90 90

The "05" at 1A2498 specifies the minimum spell cost to channel and will	also need to be
edited (i.e. to 02 if you go with 50% or 01 for 100%) to match your new percentage.

Like the above, this ability has the issue of continuing to work for the remainder of the
battle even after the units are dead. And like the damper effect specifically, it's one
that I felt was better suited to an artifact rather than a unit.

	---------	-------------------------------------------------------------------------
	1A2493~E7	; MAGIC CHANNEL TO ARTIFACT ABILITY
	---------	-------------------------------------------------------------------------
	68 8B000000	push 8B			; 8B = Ring of the Magi
	8B C8		mov ecx,eax		; ECX = hero data
	E8 C16FF3FF	call 4D9460		; check for artifact
	84 C0		test al,al		; do we have it?
	0F84 F3050000 	je 5A2A9A		; if no -> [exit]
	31 F6		xor esi,esi		; ESI = 0
	8B 45 98	mov eax,[ebp-68]	; (shifted code, swaps use of EAX and ECX)
	89 45 14	mov [ebp+14],eax	; ""
	66 01 41 18	add [ecx+18],ax		; ""
	8B CB		mov ecx,ebx		; ""
	E8 C67BECFF	call 46A080		; ""
	84 C0		test al,al		; ""
	0F85 D8050000	jne 5A2A9A		; ""
	8A 55 13	mov dl,[ebp+13]		; ""
	88 55 D8	mov [ebp-28],dl		; ""
	89 45 DC	mov [ebp-24],eax	; ""
	89 45 E0	mov [ebp-20],eax	; ""
	89 45 E4	mov [ebp-1C],eax	; ""
	8B 15 680B6600	mov edx,[660B68]	; ""
	8B 82 60110000	mov eax,[edx+1160]	; "" (see below)
	8B 0D C45D6A00	mov ecx,[6A5DC4]	; ""
	E9 75020000	jmp 5A275D		; -> [continue] (1A24E8~75C is free space)
To change the artifact in the above code, simply replace 8B in the first instruction with
the ID of the desired artifact and edit the (mov eax,[edx+1160]) instruction for the text
string. Similar to changing the text for a unit's spellcast, we get the value of 1160 by
multiplying the artifact ID times 20h (a calculator will be handy here), and then reverse
the bytes in the code, so "11 60" becomes "60 11".

-----------------------------------------------------------------------------------------

### MANA DRAIN (WRAITHS)

The unit ID for this ability is specified at 0650D2. Like with Cyclopses and Ballistics,
there are several checks lumped together here. If the Wraith check fails, it subtracts 49
and checks again (3D + 49 = 86, or Faerie Dragons), and then again after subtracting 2
(88 = Enchanters). You'll need to edit them accordingly if you want to move the MP drain
ability to a different unit. To just remove the MP drain ability from Wraiths, NOP out
the jump (0650D3 > 90 90). This will free up a substantial amount of space (065128~3E1).

The amount of MP drained is specified at 065176 (FE, or -2).

-----------------------------------------------------------------------------------------

### FIRE SHIELD (EFREETI SULTANS)

The unit ID for this ability is set at 0225D9 and 042E64 (edit both).

The magnitude of its effect (which will only occur if the unit does not have an ACTUAL
Fire Shield up) is a DWORD pointer located at 042E69 (0063B8B4 = 0.20). We can rearrange
the code here so that the effect is instead stackable with the Fire Shield spell, as
well as specifying whatever magnitude we wish (the below example uses 33%).

	---------	-------------------------------------------------------------------------
	042E50~78	; EFREETI SULTAN FIRE SHIELD IS STACKABLE WITH THE SPELL
	---------	-------------------------------------------------------------------------
	83 79 34 35	cmp [ecx+34],35		; Efreeti Sultan?
	75 08		jne 442E5E		; if no -> load 0%
	D9 05 752E4400	fld dword [442E75]	; load custom floating value
	EB 06		jmp 442E64		; -> EAX = Fire Shield magnitude
	D9 05 64AC6300	fld dword [63AC64]	; load 0%
	8B 81 0C020000	mov eax,[ecx+20C]	; EAX = Fire Shield magnitude
	85 C0		test eax,eax		; Fire Shield?
	74 06		je 442E74		; if no -> return
	D8 81 A0040000	fadd dword [ecx+4A0]	; add Fire Shield magnitude
	C3		ret			; return
	AB AA AA 3E	33% (floating value)	; -
-----------------------------------------------------------------------------------------

### BAD LUCK (DEVILS & ARCHDEVILS)

The unit IDs for this ability are set at 04B001/04C032 (edit both) and 04B011/04C04B.

Seeing as bad luck mechanics were never properly implemented in the game, a luck penalty
for your enemies is questionably useful at best. However, with just a few byte changes,
we can change it into a luck bonus for our own team:

			04AFF6 > 38	; enemy team > yours
			04B01F > 40	; sub (-1) > inc (+1)
			04C01F > 55 38	; enemy team > yours (r-click info)

|the r-click info will attribute the bonus to "spells"; this is a low-priority fix

Alternatively, we can just get rid of the luck/morale effects on units...

    04AFF4 > EB 2A		; remove devil luck			04AFF6~B01F is free
    04C01E > E9 A0000000	; ""					04C023~C2 is free

    04ACD8 > EB 54		; remove angel/bone dragon morale	04ACDA~D2D is free
    04BA3F > E9 32010000	; ""  					04BA44~B75 is free

-----------------------------------------------------------------------------------------

### DEATHBLOW (DREAD KNIGHTS)

The unit ID for this ability is set at 0435A8.

Similar to the case with Cyclopses and Ballistics, the code then subtracts 4F at 0435B1
to check for the Ballista (43 + 4F = 92) for its chance of dealing double damage. Thus,
you will also need to change this value if a different unit is specified for Deathblow.

-----------------------------------------------------------------------------------------

### IMMUNE TO BLIND & PETRIFY (TROGLODYTES)

The unit IDs for blind immunity are set at 04A28C and 04A295.

The unit IDs for petrify immunity are set at 04A3CC and 04A3D1.

-----------------------------------------------------------------------------------------

### ALWAYS POSITIVE MORALE (MINOTAURS & MINOTAUR KINGS) & LUCK (HALFLINGS)

The unit IDs for morale are at 03DDD0/04AEF9/04BC50 (Minotaurs) and 03DDD5/04AEFE/04BC55
(Minotaur Kings). The unit ID for luck is at 03DCE2/04C134/04C134 (Halflings).

Since negative morale is mostly the result of unit mixing (which means that all of your
other units are suffering) and negative luck does nothing, these are of questionable use
at best. Let's look at converting them into +(X) bonuses, instead:

	03DDD8 > 83 C6 XX 90 90 90 90 90 90 90	; morale
	04BC5B > 83 C6 XX 90 90			; morale (right-click info)
	04BCB6 > 90 90 90 90 90			; ""
	04AF01 > 83 C6 XX 90 90 90 90 90 90 90	; ""

	03DCE8 > 83 C6 XX 90 90 90 90 90 90 90	; luck
	03DCF3 > B7				; ""
	04C13D > 8B F0 83 C6 XX 90 90 90 90	; luck (right-click info)
	04B124 > 83 C0 XX 90 90 90 90 90 90	; ""

For the morale right-click text, you will need to edit GenrlTxt.txt. The text for luck,
possibly because the developers were drunk that day, is hardcoded at 260B50. You'll need
to add a line break (0A) to prevent it from occupying the same line as the previous text
and be sure to end with 00 or else it will just keep reading on until it finds one.

			I suggest the following text string:

		   260B50 > 0A 25 73 20 28 2B 32 29 00 ([unit] +2)

The [unit] bit up there is a variable string specified at 04C14E (A0 3E = Halflings), so
it'll keep naming them specifically unless we change it. Horny demons, for example, will
require changing that value to 4C 16. Similar to some other examples above, we get this
value by multiplying the unit's ID by 74h and adding 18h to get 164C, and then inverting
the two bytes as we enter them into the code.

-----------------------------------------------------------------------------------------

### IGNORES DEFENSE (BEHEMOTHS & ANCIENT BEHEMOTHS)

The unit IDs for this ability are set at 0422E5 (Behemoths) and 0422FB (Ancient).

The magnitudes of 40% and 80% are DWORD pointers located at 0422F3 (B0 B8 63 00 = 0.40)
and 042309 (AC B8 63 00 = 0.80), respectively. Other values we can easily specify here
are 50% (CC B8 63 00) and 75% (98 05 64 00), else we can simply create our own floating
values as we learned earlier in the "Skills" section.

-----------------------------------------------------------------------------------------

### WEAKNESS (DRAGONFLIES)

The spell ID for Weakness is located at 0411A6 and 041185 (change both), the expertise
level is at 04119F, the duration at 04119D, and the unit ID is at 04119A. Note that this
proc is a rider of the "dispel" attack bonus (see "Attack A" table above) and will not be
called otherwise. If you wish to repurpose the "Acid Breath A" pointer, you can change
0412D0 from BF 11 44 00 to 44 11 44 00 to make a unit directly call this effect.

Your choice of spells here is mostly limited to status spells since many others seem to
crash the game. Setting the expertise level high enough will cause them to mass target,
interestingly enough. Even more interestingly, summon spells work here with one catch:
they'll crash the game if the unit casting it has no hero since the text output for
summon spells assumes that a hero must be casting it. This can be fixed, however.

Since we'll be putting this new effect on Wraiths, who are just outside the "Attack A"
table, we'll need to change 040908 from C1 (-3F) to C3 (-3D) and edit the other entries
on the table to account for the 2-byte shift like we did earlier with Resistance B.

	---------	-------------------------------------------------------------------------
	041141~83	; WRAITHS SUMMON WIGHTS FROM SLAIN FOES (OVERWRITES WEAKNESS PROC)
	---------	-------------------------------------------------------------------------
	E9 65010000	jmp 4412AB		; frees space: 041146~BE
	8B 0D 20946900	mov ecx,[699420]	; ECX = combat manager
	8B 97 84000000	mov edx,[edi+84]	; EDX = defender unit data
	C1 EA 04	shr edx,04		; shift to "living" flag"
	F6 C2 01	test dl,01		; is unit alive?
	74 17		je 441171		; if no -> (cleanup)

	8B 55 3C	mov edx,[ebp+3C]	; EDX = units killed
	85 D2		test edx,edx		; were any units killed?
	74 10		je 441171		; if no -> (cleanup)

	52		push edx		; power = # of units killed
	6A 00		push 00			; unskilled
	6A FF		push -01		; ???
	6A 01		push 01			; ???
	6A 00		push 00			; "temp" flag
	6A 42		push 42			; spell ID
	E8 CFEF1500	call 5A0140		; -> [cast spell]

	5F 		pop edi			; (cleanup)
	5E		pop esi			; ""
	5B		pop ebx			; ""
	8B 4D F4	mov ecx,[ebp-0C]	; ""
	64890D00000000	mov fs:[0],ecx		; ""
	8B E5		mov esp,ebp		; ""
	5D		pop ebp			; ""
	C2 1000		ret 0010		; return

	------		-------------------------------------------------------------------------
	1A2040		; WRAITHS SUMMON WIGHTS FROM SLAIN FOES (CONT.)
	------		-------------------------------------------------------------------------
	E9 3FF1E9FF	jmp 441184		; -> free space

	---------	-------------------------------------------------------------------------
	041184~98	; WRAITHS SUMMON WIGHTS FROM SLAIN FOES (CONT.)
	---------	-------------------------------------------------------------------------
	52		push edx		; (displaced code)
	8A 55 0C	mov dl,[ebp+0C]		; EDX = "temp" flag (00 = ability, else spell)
	84 D2		test dl,dl		; ability?
	74 04		je 441190		; if yes -> Wights
	6A 72		push 72			; Fire Elementals
	EB 02		jmp 441192		; -> (displaced code)
	6A 3C		push 3C			; Wights
	6A 42		push 42			; (displaced code)
	E9 AC0E1600	jmp 5A2045		; return (041199~BE is free space)

	------		-------------------------------------------------------------------------
	1A7579		; WRAITHS SUMMON WIGHTS FROM SLAIN FOES (CONT.)
	------		-------------------------------------------------------------------------
	68 95866800	push 688695		; pushes null text instead of hero name
	8B 80 900A0000	mov eax,[eax+A90]	; (original code shifted upward)
	90 90 90909090	nop			; -

This will remove the hero name from the summon text, which the Wraith ability will then
share; I rewrote it to say "The void sends forth%s %d %s" (note that we still need to
include the variable string for the hero name even though it's now blank).

-----------------------------------------------------------------------------------------

...but wait, there's more! One major drawback of the abilities on the "Attack A/B" tables
is that they all trigger only on melee strikes. And at least one of those abilities makes
a lot more sense as a ranged ability, so without further ado...

	----------	-------------------------------------------------------------------------
	03FAFF~B04	; ARCHMAGE SHOTS DISPEL POSITIVE STATUSES
	----------	-------------------------------------------------------------------------
	E9 95160000	jmp 441199		; -> free space
	90		nop			; -

	---------	-------------------------------------------------------------------------
	041199~BE	; (EXPANDED SPACE - OVERWRITES WEAKNESS PROC)
	---------	-------------------------------------------------------------------------
	83 7E 34 23	cmp [esi+34],23		; Archmage?
	75 15		jne 4411B4		; if no -> displaced code
	56		push esi		; push attacker onto the stack
	56		push esi		; (garbage push needed for subroutine call)
	56		push esi		; ""
	56		push esi		; ""
	56		push esi		; ""
	E8 02000000	call 4411AB		; -> prepare to enter subroutine
	EB 08		jmp 4411B3		; -> cleanup
	55		push ebp		; prepare to enter subroutine
	8B EC		mov ebp,esp		; ""
	E9 34FFFFFF	jmp 4410E7		; -> [dispel subroutine]
	5E		pop esi			; cleanup
	8B B6 7C010000	mov esi,[esi+17C]	; (displaced code)
	E9 46E9FFFF	jmp 43FB05		; return

The above is quite janky, to say the least. On the surface, it's actually a very simple
matter of jumping away at the end of the ranged attack routine and checking to see if we
apply the dispel effect. The only information we need to feed the subroutine that isn't
already present is the single push of the attacker onto the stack, which we also need to
pop back off of it once we return since the subroutine will change it and we still need
it for one last check in the ranged attack routine.

The problem here is that, in calling the Dispel effect without going through the normal
channels, we're jumping into the middle of a subroutine and missing that critial setup
phase that we see at the beginning of them, and so we need to fudge it. This code will
actually work with just two ESI pushes and a call directly to 4410E7, except we'll never
come back here - we'll go to where we'd normally go when the ranged attack routine ends.
This doesn't crash the game because everything gets reset at that point and the last bit
of code in the ranged attack routine doesn't appear to be anything important. Still, in
the interest of doing things right, we push garbage onto the stack so that we come back
here when we're done, which in turn necessitates the proper setup heading in.

-----------------------------------------------------------------------------------------

### REBIRTH (PHOENIXES)

The unit ID for this ability is specified at 06905A.

The number of times that the routine is checked on the death of the unit stack is the
number of spells in CrTraits.txt, so this ability conflicts with unit spellcasters.

-----------------------------------------------------------------------------------------

### SANDWALKER (NOMADS) & SPYING (ROGUES)

The units with these abilities are specified at 0B177C and 0E605D, respectively.

The terrain (01 = Sand) for the former ability is specififed at 0B14C7.

---------------------------------------------------------------------------------------------------------

## FACTION ALIGNMENT & NATIVE TERRAIN

Each faction has a "home" terrain upon which all its units will receive +1 to their Attack, Defense, and
Speed. This speed bonus will not affect the hero's movement points (as calculated according to the speed
of the slowest unit in their army), but an army consisting entirely of units native to the same terrain
will negate that terrain's movement penalty. Native terrain is specified at the following addresses:

	Castle     2436A8	Inferno	    2436B4	Stronghold  2436C0
	Rampart    2436AC	Necropolis  2436B8	Fortress    2436C4
	Tower      2436B0	Dungeon	    2436BC	Conflux	    2436C8

			    Neutral/Unaffiliated  2436A4

Note that siege battles will always occur on the defender's native terrain as specified here, regardless
of what the battle background graphics would imply. Changing Rampart's native terrain from grassland to
dirt, for example, will cause any Rampart siege to take place on dirt even though the background will
still look like grassland. Each faction has a special siege background image (located in H3Bitmap.lod)
named Sg(XX)Back, where "XX" is an abbreviation of the faction name. Thus, we can take the SgRmBack file
and layer it on top of CmBkDrTr (the "dirt" battlefield with trees in the distance) in Photoshop, then
do some selective erasing to reveal the new terrain underneath while retaining the necessary features.

Neutral units don't have native terrain, which is somewhat counter-intuitive in some cases, particularly
Nomads since sand is sort of their thing. Special terrain is another issue since one would expect, say,
undead units to receive a bonus on cursed ground or elemental units to recieve one on elemental terrain.
We can address both of these with an inline edit thanks to a largely unneccessary bit of code that sets
the four basic elementals to factionless (for native terrain purposes) on ROE maps:

	----------	-------------------------------------------------------------------------
	03D492~543	; NOMADS RECEIVE NATIVE TERRAIN BONUS ON SAND + SPECIAL TERRAIN BONUSES
	----------	-------------------------------------------------------------------------
	8B 0D B0476700	mov ecx,[6747B0]	; (shifted code)
	8B 14 0A	mov edx,[edx+ecx]	; ""
	8B 4D 10	mov ecx,[ebp+10]	; ""
	8D 73 74	lea esi,[ebx+74]	; ""
	89 16		mov [esi],edx		; ""
	33 FF		xor edi,edi		; ""
	39 F9		cmp ecx,edi		; ""
	74 07		je 43D4B0		; ""
	56		push esi		; ""
	50		push eax		; ""
	E8 E08E0A00	call 4E6390		; ""

	A1 20946900	mov eax,[699420]	; EAX = combat manager
	8B B0 94530000	mov esi,[eax+5394]	; ESI = terrain
	8B 80 C0530000	mov eax,[eax+53C0]	; EAX = special terrain
	31 C9		xor ecx,ecx		; ECX = 0

	83 F8 02	cmp eax,02		; Cursed Ground?
	75 10		jne 43D4D8		; if no -> EDX = unit ID
	8B 93 84000000	mov edx,[ebx+84]	; EDX = unit data
	C1 EA 12	shr edx,12		; Shift to "undead" bit
	F6 C2 01	test dl,01		; is unit undead?
	74 51		je 43D527		; if yes -> native terrain (+2)
	EB 46		jmp 43D51E		; -> not native terrain

	8B 53 34	mov edx,[ebx+34]	; EDX = unit ID
	83 FA 73	cmp edx,73		; Water Elemental?
	75 05		jne 43D4E5		; if no -> next check
	83 F8 06	cmp eax,06		; Lucid Pools?
	74 41		je 43D526		; if yes -> native terrain (+3)

	83 FA 72	cmp edx,72		; Fire Elemental?
	75 05		jne 43D4EF		; if no -> next check
	83 F8 07	cmp eax,07		; Fire Fields?
	74 37		je 43D526		; if yes -> native terrain (+3)

	83 FA 71	cmp edx,71		; Earth Elemental?
	75 05		jne 43D4F9		; if no -> next check
	83 F8 08	cmp eax,08		; Rocky Flats?
	74 2D		je 43D526		; if yes -> native terrain (+3)

	83 FA 70	cmp edx,70		; Air Elemental?
	75 05		jne 43D503		; if no -> next check
	83 F8 09	cmp eax,09		; Heavy Clouds?
	74 23		je 43D526		; if yes -> native terrain (+3)

	81 FA 8E000000	cmp edx,8E		; Nomads?
	75 05		jne 43D510		; if no -> EDX = unit faction
	83 FE 01	cmp esi,01		; Sand?
	74 16		je 43D526		; if yes -> native terrain (+3)

	8B 53 74	mov edx,[ebx+74]	; EDX = unit faction
	8B1495A8366400	mov edx,[edx*4+6436A8]	; EDX = faction's native terrain
	39 F2		cmp edx,esi		; Natrive terrain?
	74 0A		je 43D528		; if yes -> native terrain (+1)
	88 8B D8040000	mov [ebx+4D8],cl	; not native terrain (set bit to 0)
	EB 1C		jmp 43D542		; -> cleanup

	41		inc ecx			; native terrain (+3)
	41		inc ecx			; native terrain (+2)
	41		inc ecx			; native terrain (+1)
	C683D804000001	mov byte [ebx+4D8],01	; set "native terrain" bit to 1
	01 8B C4000000	add [ebx+C4],ecx	; +Speed
	01 8B C8000000	add [ebx+C8],ecx	; +Attack
	01 8B CC000000	add [ebx+CC],ecx	; +Defense
	B1 02		mov cl,02		; (cleanup)

While nice, the above code only addresses specific units and does not function to make units properly
native to the terrain in question. Thankfully, doing so is a relatively simple matter. Aside from native
terrain, the only thing that faction alignment affects is the morale penalty for non-homogenous armies.
Thus, we can simply set a neutral unit's faction to one that shares its desired native terrain, i.e.
Trolls to Fortress, and then manually adjust them when checking the army composition for morale:

	---------	-------------------------------------------------------------------------
	04A8CF~E3	; PEASANTS CAN MIX INTO ANY ARMY + NEUTRAL UNITS CAN HAVE NATIVE TERRAIN
	---------	-------------------------------------------------------------------------
	3D 8B000000	cmp eax,8B		; Peasants?
	74 21		je 44A8F7		; if yes -> [do not add to faction pool]
	3D 84000000	cmp eax,84		; unit ID 84 (Azure Dragons)?
	72 14		jb 44A8F1		; if below -> [get faction]
	31 C0		xor eax,eax		; EAX = -1 (no faction)
	48		dec eax			; ""
	EB 11		jmp 44A8F3		; -> [add to pool] (04A8E2~F0 is free space)

This will manually set any neutral units except for Gold and Diamond Golems (which, quite frankly, have
no business NOT being classified as Tower units in this case) to factionless for the purposes of morale.
Note that this is an inline edit due to removing yet another unnecessary check that sets the four basic
elementals to factionless in RoE maps. Also note the rider ability that allows Peasants to mix into any
army without causing a mixed-faction morale penalty because they suck enough even with it.

With just the above change in place, however, the background displayed in the unit's right-click screen
will change from the neutral "wasteland" appearance to that of whichever faction they are set to. We can
correct this with a bit of free space, which we can get by removing the "spying" ability from Rogues.

	------		-------------------------------------------------------------------------
	03D49E		; NEUTRAL UNITS CAN HAVE NATIVE TERRAIN (CORRECTS BACKGROUND GFX)
	------		-------------------------------------------------------------------------
	E8 B88B0A00	call 4E605B		; -> free space (Spying)

	------		-------------------------------------------------------------------------
	15000F		; ""
	------		-------------------------------------------------------------------------
	E8 5760F9FF	call 4E606B		; -> free space (Spying)
	90 90		nop			; ""

	---------	-------------------------------------------------------------------------
	0E6053~7F	; (EXPANDED SPACE - OVERWRITES SPYING)
	---------	-------------------------------------------------------------------------
	8B 86 29010000	mov eax,[esi+129]	; frees space
	5E		pop esi			; ""
	C3		ret			; ""

	3D 84000000	cmp eax,84		; unit ID 84 (Azure Dragons)?
	7C 03 		jl 4E6065		; if below -> (displaced code)
	31 D2		xor edx,edx		; EDX = -1 (no faction)
	4A		dec edx			; ""
	8D 73 74	lea esi,[ebx+74]	; (displaced code)
	89 16		mov [esi],edx		; ""
	C3		ret			; return

	81 FF 84000000	cmp edi,84		; unit ID 84 (Azure Dragons)?
	7C 03		jl 4E6076		; if below -> (displaced code)
	31 C9		xor ecx,ecx		; EDX = -1 (no faction)
	49		dec ecx			; ""
	8B0C8D60296800	mov ecx,[ecx*4+682960]	; (displaced code)
	C3		ret			; return
	90 90		nop			; -


One minor problem with this approach is that it does make growth weeks possible for the units that you
assign factions to, but that will be addressed just below.

Finally, you can prevent the game from forcing the "sub-t" terrain (both graphically and mechanically)
for any non-siege battle that takes place in the underground layer by changing 064044 from 7E to EB.

---------------------------------------------------------------------------------------------------------

## GROWTH WEEKS & MONTHS

By default, the odds of a growth bonus week are 25%. This can be raised to 33% or 50% by setting 0C846C
to 3 or 2, respectively (1/3 or 1/2), or lowered by raising the value. The odds of a silent (non-growth)
month are set at 0C8C46, with a second check at 0C8C55 for a month of the plague. This is a sequential
check of a random value between 1 and 10: if it's greater than 05 (0C8C46), then we move on to check if
it's greater than 09 (0C8C55), going to a plague month if it is or a growth month if it isn't. Months of
the plague can thus be disabled by setting 0C8C55 to 0A.

While growth week bonuses can be for any unit, only certain units are eligible for growth month bonuses
as specified on a table starting at 23E678:

	    68 = Serpent Fly	    04 = Griffin	    0E = Centaur
	    1C = Gremilin	    55 = Hobgoblin	    2C = Gog
	    46 = Troglodyte	    48 = Harpy		    64 = Lizardman
	    14 = Pegasus	    56 = Orc		    3C = Wight

Note that there's a bug in HD Mod wherein growth weeks can override growth months since it runs through
both routines regardless. The effect of the "month" creature appearing at random spots on the map still
occurs, but the growth bonus will be a weekly one (and most likely for a completely different creature).
We can fix this by going to 4C8C53~C and writing C6 05 A0 77 69 00 00 6A 0B 5A. The "0B" in this string
is the number of candidates for month growth bonuses, so it can be lowered if so desired.

Aside from that, there are several things about this mechanic that we can look into improving. To begin
with, we can replace the flat +5 bonus (specified at 0C847F) for growth weeks with one that scales with
the unit's level since any static bonus is going to be too low for low-level units and/or too high for
high-level ones. By contrast, since you'll likely want to keep the month growth units in a more narrow
level range, a static bonus is more appropriate here than the original effect of doubling the existing
population. Finally, we'll look at applying growth bonuses without regard to whether or not the dwelling
is upgraded instead of the base and upgraded units being considered separate for bonus purposes.

In the below example, we've chosen Air, Earth, Fire, and Water Elementals as the only units eligible for
growth months. Aside from being in that third-level sweet spot of difficulty for when they randomly pop
up all over the map, it doesn't favor any one specific faction except the one that's already an outlier
and, equally importantly, won't provide Necropolis with a free lunch if we also change Necromancy to no
longer be effective on unliving units (as explained earlier). For weekly bonuses, every affiliated unit
is eligible except for Conflux units. This is partly to balance the fact that Conflux gets all of the
monthly bonuses and partly to keep the code simple; in either case, there's plenty of leftover space to
modify the below example to your liking should you want something different.

	---------	-------------------------------------------------------------------------
	0C84A1~C7	; GROWTH WEEK BONUS TO 2X BASE GROWTH + CONFLUX UNITS ARE INELIGIBLE
	---------	-------------------------------------------------------------------------
	BA 6F000000	mov edx,6F		; EDX = 6F (all units from the first 8 factions)
	31 C9		xor ecx,ecx		; ECX = 0
	E8 13430400	call 50C7C0		; EAX = 0~6F
	D1 F8		sar eax,1		; EAX / 2 (drops remainder)
	01 C0		add eax,eax		; EAX * 2 (base units only)
	8B D8		mov ebx,eax		; EBX = EAX
	6B DB 74	imul ebx,ebx,74		; EBX = data range
	8B 15 B0476700	mov edx,[6747B0]	; EDX = unit index
	8B 4C 1A 44	mov ecx,[edx+ebx+44]	; ECX = unit's base growth
	89 4D F4	mov [ebp-0C],ecx	; store ECX as bonus
	E9 C0000000	jmp 4C8588		; -> [continue]

	---------	-------------------------------------------------------------------------
	0C8D38~42	; GROWTH MONTH BONUS TO STATIC VALUE
	---------	-------------------------------------------------------------------------
	83 04 33 XX	add [ebx+esi],XX	; XX = bonus
	90 90 90 90	nop			; -
	90 90 90	nop			; -

	--------	-------------------------------------------------------------------------
	1C0203~9	; WEEKLY GROWTH BONUS APPLIES TO BOTH BASE AND UPGRADED DWELLINGS
	--------	-------------------------------------------------------------------------
	E8 C082F0FF	call 4C84C8		; -> free space (growth week unit selection)
	90 90		nop			; -

	---------	-------------------------------------------------------------------------
	0C84C8~D5	; (INLINE EDIT - OVERWRITES GROWTH WEEK UNIT SELECTION)
	---------	-------------------------------------------------------------------------
	8B0C8DB4476700	mov ecx,[ecx*4+6747B4]	; ECX = unit ID for current dwelling
	42		inc edx			; EDX = upgraded version of bonus week unit
	39 D1		cmp ecx,edx		; is this an upgraded dwelling for that unit?
	74 01		je 4C84D5		; if yes -> return (dwelling gets the bonus)
	4A		dec edx			; EDX = bonus week unit
	C3		ret			; return

	---------	-------------------------------------------------------------------------
	0C8D2D~33	; MONTHLY GROWTH BONUS APPLIES TO BOTH BASE AND UPGRADED DWELLINGS
	---------	-------------------------------------------------------------------------
	E8 A4F7FFFF	call 4C84D6		; -> free space (growth week unit selection)
	90 90		nop			; -

	----------	-------------------------------------------------------------------------
	0C84D6~513	; (INLINE EDIT - OVERWRITES GROWTH WEEK UNIT SELECTION)
	----------	-------------------------------------------------------------------------
	8B148DB4476700	mov edx,[ecx*4+6747B4]	; EDX = unit ID for current dwelling
	83 FA 7F	cmp edx,7F		; is this an upgraded Air Altar?
	75 08		jne 4C84EA		; if no -> next dwelling check
	83 F8 70	cmp eax,70		; month of the Air Elemental?
	75 02		jne 4C84E9		; if no -> return
	8B C2		mov eax,edx		; EAX = EDX (dwelling gets the bonus)
	C3		ret			; return

	83 FA 7D	cmp edx,7D		; is this an upgraded Earth Altar?
	75 08		jne 4C84F7		; if no -> next dwelling check
	83 F8 71	cmp eax,71		; month of the Earth Elemental?
	75 02		jne 4C84F6		; if no -> return
	8B C2		mov eax,edx		; EAX = EDX (dwelling gets the bonus)
	C3		ret			; return

	81 FA 81000000	cmp edx,81		; is this an upgraded Fire Altar?
	75 08		jne 4C8507		; if no -> next dwelling check
	83 F8 72	cmp eax,72		; month of the Fire Elemental?
	75 02		jne 4C8506		; if no -> return
	8B C2		mov eax,edx		; EAX = EDX (dwelling gets the bonus)
	C3		ret			; return

	83 FA 7B	cmp edx,7B		; is this an upgraded Water Altar?
	75 07		jne 4C8513		; if no -> return
	83 F8 73	cmp eax,73		; month of the Water Elemental?
	75 02		jne 4C8513		; if no -> return
	8B C2		mov eax,edx		; EAX = EDX (dwelling gets the bonus)
	C3		ret			; return (0C8514~87 is free space)

-----------------------------------------------------------------------------------------

By default, the growth rate of random unit stacks on the map is 10% (minus any remainder) per week. This
is mostly serviceable, but its exponential nature gives it potential to get out of hand on any map that
lasts too long. Let's look into implementing a more linear formula that incorporates player difficulty:

		WEEKLY RANDOM UNIT GROWTH = 2 + Difficulty (1~5) + Month - Unit Lv. (1~7)

	--------	-------------------------------------------------------------------------
	0C8872~B8	; WEEKLY RANDOM UNIT GROWTH FORMULA
	--------	-------------------------------------------------------------------------
	8A 4E 22	mov cl,[esi+22]		; ECX = unit ID
	6B C9 74	imul ecx,ecx,74		; ECX = data range
	8B 15 B0476700	mov edx,[6747B0]	; EDX = unit index
	8B 4C 11 04	mov ecx,[ecx+edx+04]	; ECX = unit lv. (0~6)

	8B 15 38956900	mov edx,[699538]	; EDX = main index
 	0FBE82D8F60100	movsx eax, [edx+1F6D8]	; EAX = player difficulty (0~4)
	83 C0 02	add eax,02		; EAX +2
	29 C8		sub eax,ecx		; EAX - ECX

	8A 8A 42F60100	mov cl,[edx+1F642]	; ECX = month
	80BA40F6010005	cmp byte [edx+1F640],05	; month rollover?
	75 01		jne 4C88A4		; if no -> EAX + ECX
	41		inc ecx			; ECX +1
	01 C8		add eax,ecx		; EAX + ECX

	83 F8 00	cmp eax,00		; growth should be at least +1
	7F 03		jg 4C88AE		; ""
	6A 01		push 01			; ""
	58		pop eax			; ""

	8B 16		mov edx,[esi]		; EDX = random unit data
	01 C2		add edx,eax		; add growth
	89 16		mov [esi],edx		; update random unit data
	E9 D1000000	jmp 4C898A		; -> [continue] (0C88B9~C6 is free)

This new formula sticks relatively close to the vanilla growth rates on Hard (the mid-range difficulty)
while making the easier difficulties easier and the harder difficulties, well... harder. Feel free to
adjust it as so desired, most easily by changing the baseline value of 2 (add eax,02).

-----------------------------------------------------------------------------------------

Finally, we have the random unit "upstack", as it's known to most players. This is the stack of upgraded
units that sometimes appears in a battle with a random stack of base units. While seemingly random, this
effect is actually deterministic based on the stack's map coordinates (in a presumed attempt to appear
random too the unobservant eye). We can make this effect more appropriately random as well as tie it to
the chosen difficulty level by tying it to the stack's aggression with the below code:

	---------	-------------------------------------------------------------------------
	0AC288~A7	; RANDOM UNIT UPSTACK TIED TO DIFFICULTY AND AGGRESSION
	---------	-------------------------------------------------------------------------
	31 C0		xor eax,eax		; EAX = 0
	8A 46 01	mov al,[esi+01]		; EAX = random stack sata
	C1 E8 04	shr eax,04		; shift to "aggression" value
	8B 15 38956900	mov edx,[699538]	; EDX = main index
	8A 92 D8F60100	mov dl,[edx+1F6D8]	; DL = player difficulty (0~4)
	00 D2 		add dl,dl		; DL * 2
	42		inc edx			; DL + 1
	31 C9		xor ecx,ecx		; ECX = 0 (upstack)
	38 D0		cmp al,dl		; is stack's aggression greater than DL?
	7F 31		jg 4AC2D6		; if yes -> [continue]
	41		inc ecx			; ECX = 1 (no upstack)
	EB 2E		jmp 4AC2D6		; -> [continue] (0AC2A8~D5 is free space)

What we are effectively doing with this code is specifying a minimum aggression threshold for an upstack
to occur based on the difficulty setting, else there will be no upstack. The thresholds are as follows:

				    Easy....... 10
				    Normal...... 8
				    Hard........ 6
				    Expert...... 4
				    Pound Me.... 2

-----------------------------------------------------------------------------------------

>couldn't think of anywhere better to put these:

4430E1 = 58AC6300 (Attack in damage formula, 0.050)
4438F6 = C0B86300 (Defense in damage formula, 0.025)