# 2. SKILLS

The effectiveness of most secondary skills can be edited in the .exe file in a table starting at 23E998.
Each skill occupies 16 bytes consisting of 4 DWORD (4-byte) values: one value each for unskilled, basic,
advanced, and expert levels. The offsets for each skill in this table are as follows:

    Luck		23E998		Offense		23E9F8		Learning	23EA58
    Leadership	23E9A8		Armorer		23EA08		Logistics	23EA68
    Necromancy	23E9B8		Estates		23EA18		Sorcery		23EA78
    Mysticism	23E9C8		Eagle Eye	23EA28		Intelligence	23EA88
    Scouting	23E9D8		Diplomacy	23EA38		First Aid	23EA98
    Archery		23E9E8		Resistance	23EA48		Artillery	23B810

Most of the above skills use percentages rather than static values. Some examples:

    05% - CD CC 4C 3D	10% - CD CC CC 3D	15% - 9A 99 19 3E	20% - CD CC 4C 3E
    25% - 00 00 80 3E	30% - 9A 99 99 3E	40% - CD CC CC 3E	50% - 00 00 00 3F

To calculate different percentages, go to - [https://gregstoll.com/~gregstoll/floattohex/](https://gregstoll.com/~gregstoll/floattohex/)
and enter the desired decimal-format percentage (i.e. 0.10) into the "float value" field.
To avoid needing to invert the resulting hex value, check the "swap endianness" box.

-----------------------------------------------------------------------------------------

The Estates skill, in order to actually be viable, deals with static values greater than 255 (one byte).
For this, the second DWORD byte is used as a "tens" column, so to speak, except each increment increases
the number by 256. Therefore, a DWORD value of 500 would be expressed as F4 (244) 01 (256) 00 00.

First Aid is also different in that the float value specified will be multiplied by 25 (the tent's base
value) - setting it to 50% will thus give you a whopping bonus of 12.5 more HP. Clearly, we're going to
need some bigger values here, as seen below:

	 25 HP = 00 00 00 00	 50 HP = 00 00 80 3F	 75 HP = 00 00 00 40
	100 HP = 00 00 40 40	150 HP = 00 00 A0 40	200 HP = 00 00 E0 40

Of course, the First Aid skill is going to be bad no matter how high we set this value unless we remove
the random factor and have it always heal the maximum amount. To do this, set 07852C~D to EB 0A (this
creates free space until 078537). If you want to keep some randomness, the minimum value is at 07852F.

(We'll go over a lot more you can do to make First Aid less shitty further below)

-----------------------------------------------------------------------------------------

To remove a skill from the game, it must be removed both from all classes in HcTraits.txt and from any
hero who starts with it. However, this leaves it randomly available from certain map locations: Scholars,
Witch Huts, and Universities (Leadership and Necromancy are banned by default from the latter two, but
not from Scholars). You can mitigate this to some degree by manually editing every map to ban the skill
in question, but the more elegant and thorough solution is to ban them in the game code.

    --------	-------------------------------------------------------------------------
    0C25B3~A	; REMOVE SKILLS FROM THE GAME
    --------	-------------------------------------------------------------------------
    E8 6FD00000	call 4CF627		; -> free space
    89 4D C0	mov [ebp-40],ecx	; store banned skill list

    --------	-------------------------------------------------------------------------
    0CF627~F	; (EXPANDED SPACE - UNUSED IN ORIGINAL GAME)
    --------	-------------------------------------------------------------------------
    81 C9 XXXXXXXX	or ecx,XXXXXXXX		; set banned skills (bitset; see below)
    31 F6		xor esi,esi		; (displaced code)
    C3		    ret			; return

The value of "XXXXXXXX" is a bitset, meaning that we add the below values for each of the skills that we
want to ban. For example, axing Ballistics, Eagle Eye, Scholar, and Intelligence will give us a value of
01040C00 (400 + 800 + 40000 + 1000000). We then break it up into bytes (01 04 0C 00) and reverse them in
the actual code, and so the instruction at 0CF627 will be 81 C9 00 0C 04 01.

    01 = Pathfinding	10 = Diplomacy		100 = Mysticism		1000 = Necromancy
    02 = Archery		20 = Navigation		200 = Luck		2000 = Estates
    04 = Logistics		40 = Leadership		400 = Ballistics	4000 = Fire Magic
    08 = Scouting		80 = Wisdom		800 = Eagle Eye		8000 = Air Magic

    10000 = Water Magic	100000 = Artillery	1000000 = Intelligence	----------------
    20000 = Earth Magic	200000 = Learning	2000000 = Sorcery	----------------
    40000 = Scholar		400000 = Offense	4000000 = Resistance	----------------
    80000 = Tactics		800000 = Armorer	8000000 = First Aid	----------------

(You'll also have to axe the shitcanned skill as a starting bonus from campaigns or from any maps where
it's specifically offered as a quest reward from Seer's Huts or from events, but you knew that already.)


## SKILL SPECIALTIES

As mentioned earlier, skill specialties can be edited to scale better than they do in the original game.
The code to apply a hero specialty bonus is copy/pasted for most skills (including several which don't
have specialists, so the framework to make one is there), so the process will be the same for them all.
There are three instructions we'll be looking at here: one which multiplies the hero's level by a given
percentage, one which adds 1.00 to the result, and one which multiplies the base effect of the skill by
the result of the previous command. To make the bonus additive rather than multiplicative, we need only
change the third command from a multiply (4D) to add (45). Then, we NOP out the second command (D8 05 E0
B6 63 00 -> 90 90 90 90 90 90) since we no longer need to add 1.0 to the bonus and then change the DWORD
pointer in the first command (all skills are set to E4 EA 63 00, or 5% by default) as we see fit.

Assuming we want to go with a 1% bonus per level, we'll need to create a 0.01 floating point value for
our DWORD pointer since one doesn't already exist anywhere in the code. Simply put, a DWORD pointer is
just an address to somewhere else in the code that's written backwards (E4 EA 63 00 = 63EAE4, or 23EAE4
in a hex editor), and in this case what it's expecting to find there is a floating point value (like the
percentages we use in the skill table above). The good news is that there's no real restrictions as to
where this needs to be - we can point to literally anywhere in the code where the desired value exists,
including the skill table itself if we really want to. By far the easiest solution, however, is to just
use the 6 bytes of space we free up by removing the second command above.

Rather than 90 90 90 90 90 90, let's instead replace the ADD with EB 04 0A D7 23 3C. The 0A D7 23 3C is
our floating point value, while the EB 04 means "don't process the next 4 bytes" since it's not actually
an instruction and the game would crash if it tried to interpret it as such. We can then reference this
value by taking the address and converting it to a DWORD pointer, as seen on the table below.

		Skill		Bonus%	  ADD -> NOP  (DWORD PTR)  4D -> 45
		-----------------------------------------------------------
		Archery		0E4420	    0E4424   (26 44 4E 00)  0E442B
		Armorer		0E45C9	    0E45CD   (CF 45 4E 00)  0E45D4
		Diplomacy	0E483C	    0E4840   (42 48 4E 00)  0E4847
		Eagle Eye	0E46E0	    0E46E4   (E6 46 4E 00)  0E46EB
		Estates		0E464F	    0E4653   (55 46 4E 00)  0E465A
		First Aid	0E4BD9	    0E4BDD   (DF 4B 4E 00)  0E4BE4
		Intelligence	0E4B69	    0E4B6D   (6F 4B 4E 00)  0E4B74
		Leadership	0E3C81	    0E3C85   (87 3C 4E 00)  0E3C8C
		Learning	0E4AF9	    0E4AFD   (FF 4A 4E 00)  0E4B04
		Logistics	0E4F1E	    0E4F22   (24 4F 4E 00)  0E4F29
		Luck		0E3A2B	    0E3A2F   (31 3A 4E 00)  0E3A36
		Mysticism	0E41FE	    0E4202   (04 42 4E 00)  0E4209
		Necromancy	0E3F92	    0E3F96   (98 3F 4E 00)  0E3F9D
		Offense		0E4569	    0E456D   (6F 45 4E 00)  0E4574
		Resistance	0E499C	    0E49A0   (A2 49 4E 00)  0E49A7
		Scouting	0E432E	    0E4332   (34 43 4E 00)  0E4339
		Sorcery		0E5B61	    0E5B65   (67 5B 4E 00)  0E5B6C


Moving on, there are a handful of skills on the above list where this new approach is still undesirable.
Some skills just shouldn't have specialists (i.e. Diplomacy, Scouting, or, quite frankly, First Aid) or
are just garbage to begin with (Eagle Eye), but others just don't work well with bonuses that scale with
level and/or are percentage-based. We'll go over some individual solutions below.

First let's look at Mysticism, which regenerates a static number of spell points per skill level and so
any level increase whose percentage bonus doesn't bring you up to the next full integer will do nothing.
The original code does try to combat this by providing a baseline of at least 1 extra spell point for
Mysticism specialists (0E4218 = 43,INC EBX), but more ideal would be a flat bonus of 1 extra spell point
per level. This one is a quick and easy change that replaces most of the previous routine:

	--------    ---------------------------------------------------------
	0E41F3~6    ; NEW MYSTICISM BONUS
	--------    ---------------------------------------------------------
	01 CB	    add ebx,ecx	      ; add level (ECX) to mana regen (EBX)
	EB 22	    jmp 4E4219	      ; continue (0E41F7~218 is free space)

We can use the leftover space to provide a small amount of mana regeneration based on the percentage of
unused movement points from the previous turn. The below code will restore 4 spell points if 75% or more
movement points are unused, 3 spell points for 50-74%, 2 for 25-49%, or else just 1. Note that this will
be in addition to what Mysticism provides, so the "unskilled" value at 23E9C8 should be set to 0.

    ----------	-------------------------------------------------------------------------
    0E41F5~218	; MANA REGENERATION FOR UNUSED MOVEMENT POINTS
    ----------	-------------------------------------------------------------------------
    8B 57 4D	mov edx,[edi+4D]	; EDX = unspent movement
    8B 4F 49	mov ecx,[edi+49]	; ECX = maximum movement
    D1 F9		sar ecx,1		; ECX / 2
    39 CA		cmp edx,ecx		; 50% or more left over?
    7D 08		jnl 4E4209		; if yes -> ECX / 2 (further down)
    D1 F9		sar ecx,1		; ECX / 2
    39 CA		cmp edx,ecx		; 25% or more left over?
    7D 0D		jnl 4E4214		; if yes -> +2 spell points
    EB 0C		jmp 4E4215		; +1 spell point

    D1 F9		sar ecx,1		; ECX / 2
    6B C9 03	imul ecx,03		; ECX * 3
    39 CA		cmp edx,ecx		; 75% or more left over?
    7C 01		jl 4E4213		; if no -> +3 spell points

    43		inc ebx			; +4 spell points
    43		inc ebx			; +3 spell points
    43		inc ebx			; +2 spell points
    43		inc ebx			; +1 spell point
    90 90 90	nop			; -

    0E41EB > 09	; shortened jump
    0E41E5 > 0F	; ""
    0E41D0 > 24	; ""

Next up is Estates, which is basically the same problem we had with Mysticism just to a lesser degree.
The fix is, again, pretty simple: we just multiply the hero's level by the desired amount after loading
it (the below example uses 32h, or 50 gold per level) and then just add it to the base amount.

	--------    ---------------------------------------------------------
	0E4641~7    ; NEW ESTATES BONUS
	--------    ---------------------------------------------------------
	6B D2 32    imul edx,edx,32   ; Estates skill (EDX) * 50
	01 D0	    add eax,edx	      ; add EDX to hero's income (EAX)
	EB 1F	    jmp 4E4667	      ; -> [continue] (0E4648~66 is free)

And then we have Logistics, which has sort of the same problem as Estates and Mysticism except that it
can get so overpowered at higher levels that Logistics specialists are often banned in competitive play.
I've got a much more in-depth solution for this one, so read on...

---------------------------------------------------------------------------------------------------------

### MOVEMENT & TERRAIN

Logistics is generally seen as one of the best skills in the game since a flat bonus to movement points
is universally useful on pretty much any hero while the other two movement-boosting skills (Pathfinding
and Navigation) are only situationally useful. My solution to this was to rework Logistics to specify a
minimum unit speed for the purposes of movement point calculation. So instead of acting as a flat bonus
to movement regardless of army composition, it allows armies with slower units to keep up with ones that
are comprised only of faster units. The below example sets a minimum unit speed of 6 at basic Logistics,
7 for advanced, and 8 for expert - or 8, 9, and 10, respectively, for specialists. Base movement costs
according to an army's slowest unit can be edited in Movement.txt from the h3bitmap.lod archive.

    ----------	---------------------------------------------------------------------
    0E4ECE~F0C	; LOGISTICS TO INCREASE MINIMUM SPEED INSTEAD OF A FLAT BONUS
    ----------	---------------------------------------------------------------------
    8A 83 CB000000	mov al,[ebx+CB]		; EAX = Logistics skill
    0F BE D0	movsx edx,al		; EDX = EAX (EDX will be our minimum speed)

    84 C0		test al,al		; do we have Logistics?
    7E 20		jle 4E4EFB		; if no -> "ECX = slowest unit"

    8B 43 1A	mov eax,[ebx+1A]	; EAX = hero ID
    8B 0D 809C6700	mov ecx,[679C80]	; ECX = specialty index
    8D 04 80	lea eax,[eax+eax*4]	; EAX = data range
    8D 04 C1	lea eax,[ecx+eax*8]	; ""
    83 38 00	cmp [eax],00		; skill specialist?
    75 09		jne 4E4EF7		; if no -> "EDX+5"
    83 78 04 02	cmp [eax+04],02		; Logistics specialist?
    75 03		jne 4E4EF7		; if no -> "EDX+5"
    83 C2 02	add edx,02		; EDX+2
    83 C2 05	add edx,05		; EDX+5

    8B 4D FC	mov ecx,[ebp-04]	; ECX = slowest unit
    39 D1		cmp ecx,edx		; is ECX greater than Logistics minimum (EDX)?
    7F 02		jg 4E4F03		; if no -> "EDI = base movement points"
    8B CA		mov ecx,edx		; Slowest unit = logistics minimum

    8B3C8DE88A6900	mov edi,[ecx*4+698AE8]	; EDI = base movement points
    EB 3A		jmp 4E4F47		; continue (0E4F0D~46 is free space)

>(NOTE: the values at 23EA68 will no longer be used)

A common optimization in high-level play is to garrison all but a hero's fastest unit whenever they end
their turn in a town in order to maximize movement points for the following turn. We can avoid the need
for this by simply basing a hero's movement points on the speed of their fastest unit whenever they end
their turn in a town. The free space we use for this comes from the code which allowed the +1 speed from
the type 1 unit specialties to factor into movement point calculation. This exception was inconsistent
with how the rules behaved, since movement point calculation otherwise ignores speed bonuses.

    ---------	-------------------------------------------------------------------------
    0E4E39~8A	; IN-TOWN MOVEMENT BASED ON FASTEST UNIT (OVERWRITES UNIT SPECIALTY)
    ---------	-------------------------------------------------------------------------
    83 7B 0C 62	cmp [ebx+0C],62		; is hero in a town?
    75 04		jne 4E4E43		; if no -> (shifted code A)
    83 6D FC 11	sub [ebp-04],11		; compare against minimum speed instead of max
    8B 45 08	mov eax,[ebp+08]	; (shifted code A)
    8B 30		mov esi,[eax]		; ""
    83 FE FF	cmp esi,-01		; ""
    74 2A		je 4E4E77		; ""
    A1 B0476700	mov eax,[6747B0]	; ""
    8D0CF500000000	lea ecx,[esi*8]		; ""
    29 F1		sub ecx,esi		; ""
    8D 14 8E	lea edx,[esi+ecx*4]	; ""
    8B 7C 90 50	mov edi,[eax+edx*4+50]	; ""

    83 7B 0C 62	cmp [ebx+0C],62		; is hero in a town?
    75 07		jne 4E4E6F		; if no -> check for slowest unit
    3B 7D FC	cmp edi,[ebp-04]	; is this this fastest unit thus far?
    7E 0A		jle 4E4E77		; if no -> (shifted code B)
    EB 05		jmp 4E4E74		; -> update army speed

    3B 7D FC	cmp edi,[ebp-04]	; is this this slowest unit thus far?
    7D 03		jge 4E4E77		; if no -> (shifted code B)
    89 7D FC	mov [ebp-04],edi	; update army speed
    8B 4D 08	mov ecx,[ebp+08]	; (shifted code B)
    8B 45 F8	mov eax,[ebp-08]	; ""
    83 C1 04	add ecx,04		; ""
    48		    dec eax			; ""
    89 4D 08	mov [ebp+08],ecx	; ""
    89 45 F8	mov [ebp-08],eax	; ""
    75 BA		jne 4E4E43		; -> (loop to check all units)
    EB 43		jmp 4E4ECE		; -> [continue] 0E4E8B~CD is free


Pathfinding is handled through a table similar to the one for skills which states the base movement cost
for each terrain type (again in a 4-byte DWORD value) followed by the movement costs at basic, advanced,
and expert Pathfinding. Included in this table are the movement costs for roads, which combined with the
base speed and Navigation settings in Movement.txt affords you full control over movement as a whole.

			      TERRAIN				        ROADS
      ----------------------------------------------------	   ---------------
      Dirt    23E510	Snow    23E540	    Sub-T   23E570	   Dirt     23E5B0
      Sand    23E520	Swamp   23E550	    Lava    23E580	   Gravel   23E5C0
      Grass   23E530	Rough   23E560	    Water   23E590	   Cobble   23E5D0

       (See also the Units section below for information on native terrain bonuses)


Finally, let's look at having Navigation reduce the movement penalty for boarding/unboarding a ship in
addition to its standard effect of increasing movement points over water. We'll be stealing the effect
from the Admiral's Hat to achieve this - we'll go over how to remove artifacts from the game later on
since this removes the only thing that the hat has going for it and puts it in a more reasonable place.
For the free space, we'll be using some of what we freed up with the Logistics change above.

    ---------	-------------------------------------------------------------------------
    0A0CD3~E8	; NAVIGATION REDUCES BOARDING PENALTY (OVERWRITES ADMIRAL'S HAT)
    ---------	-------------------------------------------------------------------------
    8A 86 CE000000	mov al,[esi+CE]		; AL = Navigation skill
    84 C0		test al,al		; do we have Navigation?
    74 2B		je 4A0D08		; if no -> [full penalty]
    8B 4E 49	mov ecx,[esi+49]	; ECX = maximum movement points
    8B 56 4D	mov edx,[esi+4D]	; EDX = current movement points
    E8 25420400	call 4E4F0D		; -> free space (Logistics)
    90		nop			; -

    ---------	-------------------------------------------------------------------------
    09E30F~24	; NAVIGATION REDUCES UNBOARDING PENALTY (OVERWRITES ADMIRAL'S HAT)
    ---------	-------------------------------------------------------------------------
    8A 86 CE000000	mov al,[esi+CE]		; AL = Navigation skill
    84 C0		test al,al		; do we have Navigation?
    74 27		je 49E340		; if no -> [full penalty]
    8B 7E 49	mov edi,[esi+49]	; EDI = maximum movement points
    8B 56 4D	mov edx,[esi+4D]	; EDX = current movement points
    E8 E96B0400	call 4E4F0D		; -> free space (Logistics)
    90		nop			; -

    09E32A > 55	; use EDX for current movement instead of ECX

    ---------	-------------------------------------------------------------------------
    0E4F0D~1C	; (EXPANDED SPACE - OVERWRITES OLD LOGISTICS SPECIALTY)
    ---------	-------------------------------------------------------------------------
    3C 03		cmp al,03		; Expert Navigation?
    74 0B		je 4E4F1C		; if yes, -> return (100% penalty reduction)
    D1 EA		shr edx,1		; EDX / 2
    3C 01		cmp al,01		; Basic Navigation?
    74 05 		je 4E4F1C		; if yes -> return (50% penalty reduction)
    D1 EA		shr edx,1		; EDX / 2
    6B D2 03	imul edx,edx,03		; EDX * 3 (75% penalty reduction)
    C3		ret			; return


### LUCK & MORALE

Off-hand, editing either Leadership or the Luck skill is inherently pointless since neither can exceed a
total value of 3 (positive or negative), so before we do anything else we should address that issue. The
maximum value for morale is specified at 064586 and 0645A0; the minimum value (FD, or -03) is located at
064754 and 06477C; both addresses must be edited in either case. Each point of positive morale confers a
1/24 chance getting of an extra turn while each negative point is a 1/12 chance of losing a turn. These
divisors are specified at 0645AA (positive) and 06479E (negative). Negative luck mechanics were never
properly implemented, so for that we only have to change the maximum value (03F658/03F65F for ranged
attacks, 04153A/041541 for melee) and the divisor (03F66C for ranged attacks, 04154E for melee).

With that out of the way, let's look at making Luck and Leadership hero specialists. The nature of these
skills makes them poor candidates for a scaling bonus, so we go with a flat one instead.

    --------	-------------------------------------------------------------------------
    0E3A19~E	; LUCK SPECIALTY
    --------	-------------------------------------------------------------------------
    83 45 0C XX	add [ebp+0C],XX		; +XX luck
    EB 27		jmp 4E3A46		; -> [continue] (0E3A1F~45 is free)

    ----------	-------------------------------------------------------------------------
    0DD195~222	; "" (R-CLICK)
    ----------	-------------------------------------------------------------------------
    8A 83 D2000000	mov al,[ebx+D2]		; AL = hero's Luck
    3C 01		cmp al,01		; basic Luck?
    75 08		jne 4DD1A7		; if no -> advanced?
    8B 15 D0536A00	mov edx,[6A53D0]	; ArrayTxt, line 75
    EB 16		jmp 4DD1BD		; -> text

    3C 02		cmp al,02		; advanced Luck?
    75 08		jne 4DD1B3		; if no -> expert?
    8B 15 D4536A00	mov edx,[6A53D4]	; ArrayTxt, line 76
    EB 0A		jmp 4DD1BD		; -> text

    3C 03		cmp al,03		; expert Luck?
    75 67		jne 4DD21E		; if no -> [continue]
    8B 15 D8536A00	mov edx,[6A53D8]	; ArrayTxt, line 77
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 CDE0F3FF	call 41B2A0		; ""
    0FBE83D2000000	movsx eax,[ebx+D2]	; EAX = hero's Luck
    8B048598E96300	mov eax,[eax*4+63E998]	; EAX = luck bonus
    01 45 F0	add [ebp-10],eax	; add luck bonus

    8B 0D 809C6700	mov ecx,[679C80]	; ECX = specialty index
    8B 43 1A	mov eax,[ebx+1A]	; EAX = hero ID
    8D 04 80	lea eax,[eax+eax*4]	; EAX = data range
    8D 04 C1	lea eax,[ecx+eax*8]	; ""
    83 38 00	cmp [eax],00		; skill specialist?
    75 26		jne 4DD21E		; if no -> [continue]
    83 78 04 09	cmp [eax+04],09		; Luck specialist?
    75 20		jne 4DD21E		; if no -> [continue]
    8B 15 F4556A00	mov edx,[6A55F4]	; ArrayTxt, line 8
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 86E0F3FF	call 41B2A0		; ""
    83 45 F0 XX	add [ebp-10],XX		; add XX to luck bonus
    E9 8C000000	jmp 4DD2AF		; -> [continue] (0DD223~AE is free space)

    ---------	-------------------------------------------------------------------------
    0E3C6F~73	; LEADERSHIP SPECIALTY
    ---------	-------------------------------------------------------------------------
    83 C3 XX	add ebx,XX		; +XX morale
    EB 2A		jmp 4E3C9E		; -> [continue] (0E3C74~9D is free space)

    ----------	-------------------------------------------------------------------------
    0DC9C4~A51	; "" (R-CLICK)
    ----------	-------------------------------------------------------------------------
    8A 83 CF000000	mov al,[ebx+CF]		; AL = hero's Leadership
    3C 01		cmp al,01		; basic Leadership?
    75 08		jne 4DC9D6		; if no -> advanced?
    8B 15 74586A00	mov edx,[6A5874]	; ArrayTxt, line 106
    EB 16		jmp 4DC9EC		; -> text

    3C 02		cmp al,02		; expert Leadership?
    75 08		jne 4DC9E2		; if no -> expert?
    8B 15 78586A00	mov edx,[6A5878]	; ArrayTxt, line 107
    EB 0A		jmp 4DC9EC		; -> text

    3C 03		cmp al,03		; master Leadership?
    75 67		jne 4DCA4D		; if no -> [continue]
    8B 15 7C586A00	mov edx,[6A587C]	; ArrayTxt, line 108
    83 C9 FF	or ecx,-01		; (text bullshit)
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 9EE8F3FF	call 41B2A0		; ""
    0FBE83CF000000	movsx eax,[ebx+CF]	; EAX = hero's Leadership
    8B0485A8E96300	mov eax,[eax*4+63E9A8]	; EAX = morale bonus
    01 45 F0	add [ebp-10],eax	; add morale bonus

    8B 0D 809C6700	mov ecx,[679C80]	; ECX = specialty index
    8B 43 1A	mov eax,[ebx+1A]	; EAX = hero ID
    8D 04 80	lea eax,[eax+eax*4]	; EAX = data range
    8D 04 C1	lea eax,[ecx+eax*8]	; ""
    83 38 00	cmp [eax],00		; skill specialist?
    75 26		jne 4DCA4D		; if no -> [continue]
    83 78 04 06	cmp [eax+04],06		; Leadership specialist?
    75 20		jne 4DCA4D		; if no -> [continue]
    8B 15 185F6A00	mov edx,[6A5F18]	; ArrayTxt, line 16
    83 C9 FF	or ecx,-01		; ""
    8B FA		mov edi,edx		; ""
    31 C0		xor eax,eax		; ""
    F2 AE		repne scasb		; ""
    F7 D1		not ecx			; ""
    49		dec ecx			; ""
    51		push ecx		; ""
    52		push edx		; ""
    8D 4D D8	lea ecx,[ebp-28]	; ""
    E8 57E8F3FF	call 41B2A0		; ""
    83 45 F0 XX	add [ebp-10],XX		; add XX to morale bonus
    E9 8C000000	jmp 4DCADE		; -> [continue] (0DCA52~DD is free space)

Of note are the calls above to lines 8 and 16 in ArrayTxt to denote Luck and Leadership specialties in
the list of modifiers. These are text descriptors for luck and morale that are unused in HD mod. Lines
9~14 and 17~22 are also unused, and we'll look into finding a use for them a little bit later on.

While the above code takes care of everything you may want to do with luck and morale from a mechanical
standpoint, we're left with a snag in the graphics department since there are only three graphics each
for positive bonuses. Even if you are keen on doing a bit of graphics editing (which we'll get to just
below), a good approach if you're raising the bonus caps is to set up each graphic to represent a range
of values rather than an exact one. The below code will establish an easily-modifiable framework which
can be adjusted to whatever specifications you wish; in this example, we will be doubling the bonus cap
from 3 to 6 and using each graphic to represent a range of 2 (1~2, 3~4, and 5~6, respectively).

    ---------	-------------------------------------------------------------------------
    051AED~F2	; MODIFIED MORALE DISPLAY (ADVENTURE MAP STATUS WINDOW)
    ---------	-------------------------------------------------------------------------
    E8 4296FFFF	call 44B134		; -> free space (unnecessary luck cap removal A)

    ---------	-------------------------------------------------------------------------
    1F424E~5D	; MODIFIED MORALE DISPLAY (UNIT R-CLICK, ADVENTURE MAP)
    ---------	-------------------------------------------------------------------------
    8B 43 68	mov eax,[ebx+68]	; EAX = morale bonus
    E8 DE6EE5FF	call 44B134		; -> free space (unnecessary luck cap removal A)
    6A 10		push 10			; (shifted code)
    6A 00		push 00			; ""
    6A 00		push 00			; ""
    EB 1E		jmp 5F427C		; -> [continue] (1F425E~7B is free space)

    ---------	-------------------------------------------------------------------------
    1F3A99~A8	; MODIFIED MORALE DISPLAY (UNIT R-CLICK, COMBAT)
    ---------	-------------------------------------------------------------------------
    8B 46 68	mov eax,[esi+68]	; EAX = morale bonus
    E8 9376E5FF	call 44B134		; -> free space (unnecessary luck cap removal A)
    6A 10		push 10			; (shifted code)
    6A 00		push 00			; ""
    6A 00		push 00			; ""
    EB 1E		jmp 5F3AC7		; -> [continue] (1F3AB9~C6 is free space)

    ---------	-------------------------------------------------------------------------
    0E1A31~53	; MODIFIED MORALE DISPLAY (HERO SCREEN)
    ---------	-------------------------------------------------------------------------
    E8 FE96F6FF	call 44B134		; -> free space (unnecessary luck cap removal A)
    5F		pop edi			; (shifted code)
    5E		pop esi			; ""
    5B		pop ebx			; ""
    8D 4D D4	lea ecx,[ebp-2C]	; ""
    51		push ecx		; ""
    8B 0D C88A6900	mov ecx,[698AC8]	; ""
    89 45 EC	mov [ebp-14],eax	; ""
    C745DC74000000	mov [ebp-24],74		; ""
    A3 303B6700	mov [673B30],eax	; ""
    EB 13		jmp 4E1A67		; -> [continue] (0E1A54~66 is free space)

    --------	-------------------------------------------------------------------------
    06C896~B	; MODIFIED MORALE DISPLAY (HERO, COMBAT)
    --------	-------------------------------------------------------------------------
    E8 54730700	call 4E3BEF		; -> free space (unnecessary luck cap removal B)
    90		nop			; -

    ---------	-------------------------------------------------------------------------
    0E3BEF~F7	; (INLINE EDIT - OVERWRITES UNNECESSARY LUCK CAP REMOVAL B)
    ---------	-------------------------------------------------------------------------
    E8 4075F6FF	call 44B134		; -> free space (unnecessary luck cap removal A)
    8B 4F 4C	mov ecx,[edi+4C]	; (displaced code)
    C3		ret			; -

    ---------	-------------------------------------------------------------------------
    0F6035~40	; MODIFIED MORALE DISPLAY (MESSAGE BOX GRAPHIC, POSITIVE)
    ---------	-------------------------------------------------------------------------
    A1 303B6700	mov eax,[673B30]	; EAX = hero's morale
    89 43 28	mov [ebx+28],eax	; (optimized code)
    EB AA		jmp 4F5FE9		; ""
    90 90		nop			; -

    ----------	-------------------------------------------------------------------------
    0F60DB~E6	; MODIFIED MORALE DISPLAY (MESSAGE BOX GRAPHIC, NEGATIVE)
    ----------	-------------------------------------------------------------------------
    A1 303B6700	mov eax,[673B30]	; EAX = hero's morale
    89 43 28	mov [ebx+28],eax	; (optimized code)
    EB AA		jmp 4F608F		; ""
    90 90		nop			; -

    04B050~5 > 5F5E5DC21800		; (A) remove unncessary cap (04B056~8F is free space)
    0E3E80~9 > 8BC35B5F8BE55DC20C00 ; (B) "" (0E3E8A~CF is free space)

    -----------------------------------------------------------------------------------------

    ---------	-------------------------------------------------------------------------
    051B52		; MODIFIED LUCK DISPLAY (ADVENTURE MAP STATUS WINDOW)
    ---------	-------------------------------------------------------------------------
    E8 DD95FFFF	call 44B134		; -> free space (unnecessary luck cap removal A)

    ---------	-------------------------------------------------------------------------
    1F432C~55	; MODIFIED LUCK DISPLAY (UNIT R-CLICK, ADVENTURE MAP)
    ---------	-------------------------------------------------------------------------
    50		push eax		; store EAX
    8B 43 7C	mov eax,[ebx+7C]	; EAX = luck bonus
    E8 FF6DE5FF	call 44B134		; -> free space (unnecessary luck cap removal A)
    59		pop ecx			; retrieve EAX into ECX
    6A 10		push 10			; (shifted code)
    6A 00		push 00			; ""
    6A 00		push 00			; ""
    6A 00		push 00			; ""
    50		push eax		; ""
    68 D0C66800	push 68C6D0		; ""
    68 DC000000	push DC			; ""
    6A 26		push 26			; ""
    6A 2A		push 2A			; ""
    68 BD000000	push BD			; ""
    6A 4D		push 4D			; ""
    EB 22		jmp 5F4378		; -> [continue] (1F4356~79 is free space)

    ---------	-------------------------------------------------------------------------
    1F3BDC~E8	; MODIFIED LUCK DISPLAY (UNIT R-CLICK, COMBAT)
    ---------	-------------------------------------------------------------------------
    E8 5375E5FF	call 44B134		; -> free space (unnecessary luck cap removal A)
    6A 10		push 10			; (shifted code)
    6A 00		push 00			; ""
    6A 00		push 00			; ""
    EB 1E		jmp 5F3C07		; -> [continue] (1F3BE9~C06 is free space)

    ---------	-------------------------------------------------------------------------
    0E19CF~E3	; MODIFIED LUCK DISPLAY (HERO SCREEN)
    ---------	-------------------------------------------------------------------------
    E8 5C1F0000	call 4E3930		; EAX = hero's luck
    E8 5B97F6FF	call 44B134		; -> free space (unnecessary luck cap removal A)
    8D 4D D4	lea ecx,[ebp-2C]	; (shifted code)
    51		push ecx		; ""
    A3 2C3B6700	mov [673B2C],eax	; store luck in memory (used by message boxes)
    EB 1F		jmp 4E1A03		; -> [continue] (0E19E4~A02 is free space)

    --------	-------------------------------------------------------------------------
    06C8B0~5	; MODIFIED LUCK DISPLAY (HERO, COMBAT)
    --------	-------------------------------------------------------------------------
    E8 43730700	call 4E3BF8		; -> free space (unnecessary luck cap removal B)
    90		nop			; -

    ----------	-------------------------------------------------------------------------
    0E3BF8~C00	; (INLINE EDIT - OVERWRITES UNNECESSARY LUCK CAP REMOVAL B)
    ----------	-------------------------------------------------------------------------
    E8 3775F6FF	call 44B134		; -> free space (unnecessary luck cap removal A)
    8B 4F 50	mov ecx,[edi+50]	; (displaced code)
    C3 		ret			; return (0E3C01~1F remains free)

    ---------	-------------------------------------------------------------------------
    11D99B~D9	; MODIFIED LUCK DISPLAY (KINGDOM OVERVIEW)
    ---------	-------------------------------------------------------------------------
    50		push eax		; store EAX
    8B C6		mov eax,esi		; EAX = luck bonus
    E8 91D7F2FF	call 44B134		; -> free space (unnecessary luck cap removal)
    59		pop ecx			; retrieve EAX into ECX
    6A 10		push 10			; (optimized code)
    6A 00		push 00			; ""
    6A 00		push 00			; ""
    6A 00		push 00			; ""
    50		push eax		; ""
    8B 55 0C	mov edx,[ebp+0C]	; ""
    81 C2 BB000000	add edx,BB		; ""
    68 F4176800	push 6817F4		; ""
    52		push edx		; ""
    8B D3		mov edx,ebx		; ""
    6B D2 74	imul edx,74		; ""
    83 C2 34	add edx,34		; ""
    6A 14		push 14			; ""
    6A 1E		push 1E			; ""
    52		push edx		; ""
    68 F6000000	push F6			; ""
    E8 2DCEFCFF	call 4EA800		; ""
    90909090909090	nop			; -

    ---------	-------------------------------------------------------------------------
    0F612E~39	; MODIFIED LUCK DISPLAY (MESSAGE BOX GRAPHIC)
    ---------	-------------------------------------------------------------------------
    A1 2C3B6700	mov eax,[673B2C]	; EAX = hero's luck
    89 43 28	mov [ebx+28],eax	; (optimized code)
    EB AB		jmp 4F60E3		; ""
    90 90		nop			; -

    04B12E~33 > 5F5E5DC21400 	; (A) remove unncessary cap (frees space, see below)
    0E3BE7~E  > 5F5E8BE55DC21400 	; (B) "" (frees space, see above)

    ---------	-------------------------------------------------------------------------
    0E4FDD~FF	; "" (SHARED CODE)
    ---------	-------------------------------------------------------------------------
    74 0B		je 4E4FEA		; (shortened jump)
    8B 15 E48A6900	mov edx,[698AE4]	; (optimized code)
    01 55 08	add [ebp+08],edx	; ""
    01 D0		add eax,edx		; ""
    C6052C3B670004	mov byte [673B2C],04	; +1 luck gfx (adventure map message boxes)
    C605303B670004	mov byte [673B30],04	; +1 morale gfx (adventure map message boxes)
    E9 CBFDFFFF 	jmp 4E4DC8		; -> [continue]
    90 90 90	nop			; -

    ---------	-------------------------------------------------------------------------
    04B134~5A	; SHARED CODE (INLINE EDIT - OVERWRITES UNNECESSARY LUCK CAP A)
    ---------	-------------------------------------------------------------------------
    83 C0 03	add eax,03		; EAX (Luck or Morale) +3
    83 F8 00	cmp eax,00		; is EAX <=00 (-3 Luck or Morale)?
    7D 02		jnl 4E19E9		; if no -> next check
    31 C0		xor eax,eax		; EAX = 00
    83 F8 09	cmp eax,09		; is EAX > 09 (+6 Luck or Morale)?
    7E 05		jle 4E19F3		; if no -> EAX = image index
    B8 09000000	mov eax,09		; EAX = 09
    8A 80 51B14400	mov al,[eax+44B151]	; EAX = image index
    8B CE		mov ecx,esi		; (displaced code)
    C3		ret			; return (04B15B~68 is free space)

    00 01 02 03	; -3~0 Luck/Morale	(iXXXYYb3/b2/b1/g0.bmp)
    04 04		; 1~2 Luck/Morale	(iXXXYYg1.bmp)
    05 05		; 3~4 Luck/Morale	(iXXXYYg2.bmp)
    06 06		; 5~6 Luck/Morale	(iXXXYYg3.bmp)

There's a lot of code up there, but we're mostly only interested in the last bit: the shared subroutine
that's being used by most of the code above it. For graphical purposes only, we establish a range of 9
possible values for luck and morale by first adding 3 to the hero's value (EAX) and then capping it at a
minimum value of 0 (-3) or a maximum of 9 (+6). We then convert this value to the appropriate graphic
using the table below, with each value there representing an index in the cooresponding .def archive.

There are twelve graphic archives involved in the above code: I(MRL/LCK)(22/30/42/82/b/s).def. The work
to actually make the new graphics aside, adding more is a simple matter of appending the archives and
then calling the new graphic(s) with a 07/08/09, or so on in the table above. To expand the range of the
table to include more bonuses, simply raise the cap (09) and then add an additional value to the lookup
table for each additional value that's added to the range.

One last thing to note is how we handle the large graphics used in message boxes (the "x82" archives).
Since these are also used by adventure map locations and any trace of what the hero's actual morale or
luck values are is long gone from memory by the time we get to the code for them, we fudge it by writing
the hero's luck and morale values to an unused part of memory whenever we're in the hero screen or right
clicking on a unit. We then simply force these values to 4 (+1 luck or morale) whenever a hero moves so
that those graphics will be used on all adventure map message boxes.

---------------------------------------------------------------------------------------------------------

### TACTICS

The effect of tactics is specified via a command at 075D36 which loads two times EAX (the hero's Tactics
skill) +1 into ECX. The 01 at 075D39 is the "+1" part of the formula, so you can adjust it as desired or
simply replace the entire command with something else (you can free up two additional bytes if needed by
replacing the "mov esi,11" instruction just before it with 6A 11 5E, or "push 11" and "pop esi").

We can also look into allowing Tactics hero specialists. Like with Luck and Leadership, a scaling bonus
doesn't really work too well with this type of skill and so the below example goes with a static bonus.
The free space we use for this comes from the removal of the pop-up message box explaining how Tactics
works at the beginning of every battle, which is something I imagine most people will want to do anyway.

    ---------	-------------------------------------------------------------------------
    062802~27	; TACTICS SPECIALTY
    ---------	-------------------------------------------------------------------------
    89 B3 EC320100	mov [ebx+132EC],esi	; (optimized code)
    31 FF		xor edi,edi		; ""
    85 C0		test eax,eax		; ""
    74 09		je 462817		; ""
    E8 87050000	call 462D9A		; -> free space (tactics instruction box)

    8B F9		mov edi,ecx		; (optimzied code)
    31 C9		xor ecx,ecx		; ""
    8B 83 D0530000	mov eax,[ebx+53D0]	; ""
    85 C0		test eax,eax		; ""
    74 07		je 462828		; ""
    E8 74050000	call 462D9A		; -> free space (tactics instruction box)
    90 90		nop			; -

    ---------	-------------------------------------------------------------------------
    062D98~BE	; (EXPANDED SPACE - OVERWRITES INSTRUCTIONAL MESSAGE BOX)
    ---------	-------------------------------------------------------------------------
    EB 30		jmp 462DCA		; skip tactics instruction box (frees 062D9A~C9)
    0FBE88DC000000	movsx ecx,[eax+DC]	; ECX = hero's Tactics skill
    8B 15 809C6700	mov edx,[679C80]	; EDX = specialty index
    8B 40 1A	mov eax,[eax+1A]	; EAX = hero ID
    8D 04 80	lea eax,[eax+eax*4]	; EAX = data range
    8D 04 C2	lea eax,[edx+eax*8]	; ""
    83 38 00	cmp [eax],00		; skill specialist?
    75 09		jne 462DBF		; if no -> return
    83 78 04 13	cmp [eax+04],13		; Tactics specialist?
    75 03		jne 462DBF		; if no -> return
    83 C1 XX	add ecx,XX		; +XX hexes
    C3		ret			; return

---------------------------------------------------------------------------------------------------------

### NECROMANCY

The ID of the base unit resurrected by Necromancy is named at 0E3F3A; the units to be resurrected with
the Cloak of the Undead King equipped are specified at 0E3F33 (Basic Necromancy), 0E3F2A (Advanced), and
0E3F1F (Expert). By default, the Cloak revives Walking Dead, Wights, and Liches, respectively.

Something to bear in mind when changing these settings is that the number of units resurrected is based
on the total HP of all slain units relative to the HP of the resurrected unit. Thus, you'll receive far
more Skeletons (6 HP) than Wights (18 HP) or Liches (30 HP). This fact alone, however, is misleading.

In a vacuum, you'll get the same economy in terms of total health regardless of the unit specified - 10
Skeletons (60 HP) are equal to 2 Liches. The critical detail, however, is that you can't resurrect more
units than you kill, meaning that the ratio is only optimal when the slain units are equal to or weaker
than the ones being resurrected (hence why Necropolis thrives on having lots of peasants to kill and not
just any random monsters). Thus, while you'll raise fewer Liches from a stack of slain Ogres, the total
health of those Liches will be greater than if you had raised Skeletons or Zombies.

On the other hand, the more HP of the resurrected unit, the more you'll ultimately lose due to rounding.
Going back to the above example, 10 Skeletons are equal to 2 Liches, but a fight that would give you 14
Skeletons (84 HP) will still only give you 2 Liches. So while killing stronger units is preferable for
resurrecting units with higher HP, killing weaker ones will actually give you better economy otherwise.
This is doubly true considering that each enemy stack is calculated individually, meaning there can be
more rounding losses from the exact same number of units if they're grouped into more stacks. We'll look
at eliminating these rounding errors with a complete formula rewrite below.

-----------------------------------------------------------------------------------------

Another technical issue with Necromancy is that it doesn't discriminate between enemy units which are
living versus those that aren't (i.e. Gargoyles, Golems) despite the fact that it's not supposed to work
on the latter. Assuming that this is the only change you wish to make to the formula (otherwise refer to
the complete rewrite further below), we can make it respect this property and not harvest anything from
unliving units using the space we freed up with the Estates specialty. Note that the "unliving" umbrella
includes undead units, so you can't raise Skeletons from other Skeletons; if you would prefer it to be possible, adding a second check for the unliving flag to the below code is quite trivial.

    --------	-------------------------------------------------------------------------
    076F63~8	; NECROMANCY TO NOT WORK ON UNLIVING UNITS
    --------	-------------------------------------------------------------------------
    E8 ????????	call 4E4648		; -> free space (old Estates specialty)
    90		nop			; -

    ---------	-------------------------------------------------------------------------
    0E4648~66	; (EXPANDED SPACE - OVERWRITES OLD ESTATES SPECIALTY)
    ---------	-------------------------------------------------------------------------
    8B 44 82 10	mov eax,[edx+eax*4+10]	; EAX = unit data
    C1 E8 04	shr eax,04		; shift to "living" flag
    A8 01		test al,01		; alive?
    75 04		jne ??????		; if yes -> EAX = unit HP
    31 C0		xor eax,eax		; EAX = 0
    EB 04		jmp ??????		; -> (displaced code)
    8B 44 82 4C	mov eax,[edx+eax*4+4C]	; EAX = unit HP
    39 C8		cmp eax,ecx		; (displaced code)
    C3		ret			; return

    076FC9 > 00	; removes minimum of 1


~~~total formula rewrite simplifies to a 1:1 ratio of slain units to revival
thus, killing 60 peasants with Basic Necromancy (10%) will give 6 skeletons
the only caveat is that there is no accomodation for the few units with less HP than Skeletons
which tend to appear in very large numbers (Peasants specifically),
which will need to be addressed separately
As a balancing factor, we no longer revive upgraded units
Also, the Lich Cloak only raises Liches from level 5 and higher units
To just disallow upgrades, set 069B2E to E9 81000000, which will free up 069B33~B3.

    ----------	-------------------------------------------------------------------------
    076EF4~FAE	; SIMPLIFIED NECROMANCY FORMULA
    ----------	-------------------------------------------------------------------------
    68 82000000	push 82			; 82 = Lich Cloak
    E8 62250600	call 4D9460		; check for artifact
    89 45 E4	mov [ebp-1C],eax	; store result
    C745E814000000	mov [ebp-18],14		; number of stacks to check
    8B 55 E0	mov edx,[ebp-20]	; EDX = losing team (0 or 1)
    8D 04 D2	lea eax,[edx+edx*8]	; EBX = stack
    8D 04 82	lea eax,[edx+eax*4]	; ""
    C1 E0 05	shl eax,05		; ""
    29 D0		sub eax,edx		; ""
    8D 14 40	lea edx,[eax+eax*2]	; ""
    8D9CD600550000	lea ebx,[esi+edx*8+5500]; ""
    8B 03		mov eax,[ebx]		; EAX = unit ID
    83 F8 FF	cmp eax,-01		; empty stack?
    74 47		je 476F6E		; if yes -> next stack
    8B 7B 2C	mov edi,[ebx+2C]	; EDI = units in stack
    8B 53 18	mov edx,[ebx+18]	; EDX = units left alive
    29 D7		sub edi,edx		; subtract units left from total
    85 FF		test edi,edi		; did we kill any?
    7E 3B		jle 476F6E		; if no -> next stack

    8D14C500000000	lea edx,[eax*8]		; EAX = data range
    29 C2		sub edx,eax		; ""
    8D 04 90	lea eax,[eax+edx*4]	; ""
    8B 15 B0476700	mov edx,[6747B0]	; EDX = unit index
    8B 4C 82 10	mov ecx,[edx+eax*4+10]	; ECX = unit data
    C1 E9 04	shr ecx,04		; switch to living flag
    F6 C1 01	test cl,01		; living?
    74 1D		je 476F6E		; if no -> next stack
    80 7D E4 01	cmp byte [ebp-1C],01	; Lich Cloak?
    75 11		jne 476F68		; if no -> add to Skeleton pile
    8B 44 82 04	mov eax,[edx+eax*4+04]	; EAX = unit's level
    83 F8 04	cmp eax,04		; is level less than 5?
    7C 08		jl 476F68		; if yes -> add to Skeleton pile
    01 BE 503D0100	add [esi+13D50],edi	; add to Lich pile
    EB 06		jmp 476F6E		; -> next stack
    01 BE 4C3D0100	add [esi+13D4C],edi	; add to Skeleton pile
    81 C3 48050000	add ebx,548		; next stack
    FF 4D E8	dec [ebp-18]		; decrease stacks to check
    75 A7		jne 476F20		; if not zero -> loop (EAX = unit ID)

    DB 86 4C3D0100	fild dword [esi+13D4C]	; load Skeleton pile
    D9 5D D8	fstp dword [ebp-28]	; store as floating value
    D9 45 D8	fld dword [ebp-28]	; load floating value
    D8 4D DC	fmul dword [ebp-24]	; multiply by Necromancy
    E8 07101A00	call 617F94		; convert to integer
    89 86 4C3D0100	mov [esi+13D4C],eax	; store Skeletons

    DB 86 503D0100	fild dword [esi+13D50]	; load Lich pile
    D9 5D D8	fstp dword [ebp-28]	; store as floating value
    D9 45 D8 	fld dword [ebp-28]	; load floating value
    D8 4D DC	fmul dword [ebp-24]	; multiply by Necromancy
    E8 ED0F1A00	call 617F94		; convert to integer
    89 86 503D0100	mov [esi+13D50],eax	; store Liches
    EB 1E		jmp 476FCD		; -> [continue] (076FAF~CD is free space)

    ----------	-------------------------------------------------------------------------
    026E29~94	; SIMPLIFIED NECROMANCY FORMULA (AI)
    ----------	-------------------------------------------------------------------------
    68 82000000	push 82			; 82 = Lich Cloak
    E8 2D260B00	call 4D9460		; check for artifact
    84 C0		test al,al		; do we have it?
    74 04		je 426E3B		; if no -> skeletons
    6A 40		push 40			; 40 = Liches
    EB 02		jmp 426E3D		; -> EBX = unit to revive
    6A 38		push 38			; 38 = Skeletons
    5B		pop ebx			; EBX = unit to revive
    C745FC00000000	mov [ebp-04],00		; ~~~needs finished commentary
    C745F007000000	mov [ebp-10],07		;
    8B 06		mov eax,[esi]		;
    83 F8 FF	cmp eax,-01		;
    74 24		je 426E77		;
    8D14C500000000	lea edx,[eax*8]		;
    29 C2		sub edx,eax		;
    8D 04 90	lea eax,[eax+edx*4]	;
    8B 15 B0476700	mov edx,[6747B0]	;
    8B 4C 82 10	mov ecx,[edx+eax*4+10]	;
    C1 E9 04	shr ecx,04		;
    F6 C1 01	test cl,01		;
    74 06		je 426E77		;
    8B 46 1C	mov eax,[esi+1C]	;
    01 45 FC	add [ebp-04],eax	;
    83 C6 04	add esi,04		;
    FF 4D F0	dec [ebp-10]		;
    75 CD		jne 426E4C		;
    DB 45 FC	fild dword [ebp-04]	; load pile
    D9 5D FC	fstp dword [ebp-04]	; store as floating value
    D9 45 FC	fld dword [ebp-04]	; load floating value
    D8 4D F8	fmul dword [ebp-08]	; multiply by Necromancy
    E8 04111F00	call 617F94		; convert to integer
    89 45 FC	mov [ebp-04],eax	; store pile
    EB 30		jmp 426EC5		; -> [continue] (026E95~C4 is free space)

    ----------	-------------------------------------------------------------------------
    069B07~B48	; DO NOT RAISE UPGRADED UNITS
    ----------	-------------------------------------------------------------------------
    8B 86 503D0100	mov eax,[esi+13D50]	; EAX = Lich pile
    85 C0		test eax,eax		; Liches?
    7E 14		jle 469B25		; if no -> Skeleton Pile
    6A FF		push -01		; (filler push?)
    50		push eax		; push Lich pile
    6A 40		push 40			; 40 = Liches
    8B 7D 08	mov edi,[ebp+08]	; EDI = hero's team
    8B8CBEC4540000	mov ecx,[esi+edi*4+54C4]; ECX = hero's army
    E8 8B0EFEFF	call 44A9B0		; add Liches to hero's army

    8B 86 4C3D0100	mov eax,[esi+13D4C]	; EAX = Skeleton pile
    85 C0		test eax,eax		; Skeletons?
    7E 14		jle 469B43		; if no -> (cleanup)
    6A FF		push -01		; (filler push?)
    50		push eax		; push Skeleton pile
    6A 38		push 38			; 38 = Skeletons
    8B 7D 08	mov edi,[ebp+08]	; EDI = hero's team
    8B8CBEC4540000	mov ecx,[esi+edi*4+54C4]; ECX = hero's army
    E8 6D0EFEFF	call 44A9B0		; add Skeletons to hero's army

    5F		pop edi			; (cleanup)
    5E		pop esi			; ""
    5D		pop ebp			; ""
    C2 0400		ret 04			; return (069B49~BF is free space)

    ----------	-------------------------------------------------------------------------
    0AE26A~328	; NECROMANCY MESSAGE BOX
    ----------	-------------------------------------------------------------------------
    8B 81 503D0100	mov eax,[ecx+13D50]	; EAX = Lich pile
    85 C0		test eax,eax		; Liches?
    74 04		je 4AE278		; if no -> EAX = Skeleton pile
    6A 40		push 40			; 40 = Liches
    EB 08		jmp 4AE280		; -> ECX = unit to raise
    8B 81 4C3D0100	mov eax,[ecx+13D4C]	; EAX = Skeleton pile
    6A 38		push 38			; 38 = Skeletons
    59		pop ecx			; ECX = unit to raise
    6B C9 1D	imul ecx,1D		; ECX = data range
    8B 15 B0476700	mov edx,[6747B0]	; EDX = unit index
    83 F8 01	cmp eax,01		; are we only raising one unit?
    75 24		jne 4AE2B3		; if no -> EDX = unit name (plural)
    8B 54 8A 14	mov edx,[edx+ecx*4+14]	; EDX = unit name (singular)
    8B 0D C45D6A00	mov ecx,[6A5DC4]	; (textbox shit)
    8B 49 20	mov ecx,[ecx+20]	; ""
    8B 89 4C020000	mov ecx,[ecx+24C]	; ""
    52		push edx		; ""
    51		push ecx		; ""
    68 28746900	push 697428		; ""
    E8 30971600	call 6179DE		; ""
    83 C4 0C	add esp,0C		; ""
    EB 23		jmp 4AE2D6		; -> EAX = Combat Manager

    8B 54 8A 18	mov edx,[edx+ecx*4+18]	; EDX = unit name (plural)
    8B 0D C45D6A00	mov ecx,[6A5DC4]	; (textbox shit)
    8B 49 20	mov ecx,[ecx+20]	; ""
    8B 89 48020000	mov ecx,[ecx+248]	; ""
    52		push edx		; ""
    50		push eax		; ""
    51		push ecx		; ""
    68 28746900	push 697428		; ""
    E8 0B971600 	call 6179DE		; ""
    83 C4 10	add esp,10		; ""

    A1 20946900	mov eax,[699420]	; EAX = Combat Manager
    8B 90 503D0100	mov edx,[eax+13D50]	; EDX = Lich pile
    85 D2		test edx,edx		; Liches?
    74 04		je 4AE2E9		; if no -> EDX = Skeleton pile
    6A 40		push 40			; 40 = Liches
    EB 08		jmp 4AE2F1		; -> ECX = unit to raise
    8B 90 4C3D0100	mov edx,[eax+13D4C]	; EDX = Skeleton pile
    6A 38		push 38			; 38 = Skeletons
    59		pop ecx			; ECX = unit to raise
    6A 00		push 00			; (displaced code)
    EB 33		jmp 4AE329		; -> [continue]

    83BA503D010000	cmp [edx+13D50],00	; (Skeleton pile empty) check Lich pile
    74 6D		je 4AE36C		; if empty -> [exit, no message box]
    E9 0EFFFFFF	jmp 4AE212		; -> [continue]

    8B 15 20946900	mov edx,[699420]	; EDX = Combat Manager
    83BA503D010000	cmp [edx+13D50],00	; check Lich pile
    74 0D		je 4AE320		; if empty -> (displaced code)
    31 C9		xor ecx,ecx		; ECX = 0
    89 8A 503D0100	mov [edx+13D50],ecx	; empty Lich pile
    E9 DEFEFFFF	jmp 4AE1FE		; -> [loop]

    8B 15 38956900	mov edx,[699538]	; (displaced code)
    EB 2F		jmp 4AE357		; -> [continue]
    90		nop			; -

    --------	-------------------------------------------------------------------------
    0AE351~6	; NECROMANCY MESSAGE BOX (CONT.)
    --------	-------------------------------------------------------------------------
    EB B1		jmp 4AE304		; -> free space (inline - see above)
    90 90 90 90 	-

    0AE20E > E4 00	; adjusted jump to free space above

-----------------------------------------------------------------------------------------

### SCOUTING

No amount of buffing the effect of Scouting changes the fact that it's a purely informational skill and
of therefore limited use. My solution to this problem was to create a secondary effect for Scouting that
increases the stat bonuses that units recieve on native terrain. The free space that we use for this is
more of the space we freed earlier for in-town movement point calculation.

    --------	-------------------------------------------------------------------------
    03D551~9	; SCOUTING INCREASES NATIVE TERRAIN BONUSES
    --------	-------------------------------------------------------------------------
    E8 29790A00	call 4E4E7F		; -> free space (unit specialist movement bonus)
    90 90 90 90	nop			; -

    ---------	-------------------------------------------------------------------------
    0E4E7F~BB	; (EXPANDED SPACE - OVERWRITES UNIT SPECIALIST MOVEMENT BONUS)
    ---------	-------------------------------------------------------------------------
    80BBD804000001	cmp byte [ebx+4D8],01	; are we on native terrain?
    75 2A		jne 4E4EB2		; if no -> (displaced code)

    8B 0D 20946900	mov ecx,[699420]	; ECX = combat manager
    8B8C81CC530000	mov ecx,[ecx+eax*4+53CC]; ECX = active hero data
    85 C9		test ecx,ecx		; is there an active hero?
    74 19		je 4E4EB2		; if no -> (displaced code)

    0FBE89CC000000	movsx ecx,[ecx+CC]	; ECX = hero's scouting skill
    01 8B CC000000	add [ebx+CC],ecx	; add Scouting skill to Defense
    01 8B C8000000	add [ebx+C8],ecx	; add Scouting skill to Attack
    01 8B C4000000	add [ebx+C4],ecx	; add Scouting skill to Speed

    83 C9 FF	or ecx,-01		; (displaced code)
    89 83 F4000000	mov [ebx+F4],eax	; ""
    C3		ret			; return (0E4EBC~CD is free space)

---------------------------------------------------------------------------------------------------------

### DIPLOMACY & EAGLE EYE

The percentage values for Diplomacy concern only the reduction to surrender costs and not the primary
effect of the skill; see below for more information on that. Similarly, the percentage bonuses for Eagle
Eye only concern your chances to learn a spell that you witness, not the maximum level. Eagle Eye can be
made to allow the learning of fifth-level spells by raising the skill's base effectiveness; go to 1A028A
and write the following string of code (the third byte is the "base" effect of the skill):

`83 C2 02 3B 50 18 7C 47 8B 4D C4 E8 F6 43 F4 FF D8 0D 68 AC 63 00 E8 EF 7C 07 00 6A 64 5A`

As for Diplomacy's surrender bonus, it's of questionable use since players often prefer to fight battles
rather than surrendering. Using the space from Diplomacy's (unused) specialty bonus along with that from
the artifacts which reduce surrender costs, we'll be going over a number of changes below to improve the
skill as a whole. As for the soon to be rendered useless Diplomacy artifacts, we'll discuss later on how
you can either get rid of them or repurpose them into something else entirely.

I'll preface the rest of this section with a point aimed toward anyone who's decided to simply trash the
Diplomacy skill (or at least its primary effect) entirely. Random units will offer to join for "greater
glory" but never for gold unless either Diplomacy is in play OR the difficulty level is set to Easy, in
which case players are given a +1 bonus to their Diplomacy skill even if that skill is 0. This bonus can
be removed by setting 0A74EE to EB 30, freeing up 0A74F0~51F. Alternatively, you can remove join offers
entirely by setting 017237 from 02 to 00 and 017246, 0A75A9, and 0A755D all from 7F to EB.

Whenever any hero encounters an enemy unit in the wild, the game first calculates the relative strength
of both armies as a ratio by dividing one by the other. This includes a multiplier for the hero's army
that accounts for their attack and defense stats - for reference, this multiplier is 1.5 for a hero with
5 in each stat and 2 for a hero with 10 in each stat. What happens next differs depending on the result;
if it's greater than or equal to 1 (i.e. the hero's army is stronger than or equal to the enemy units),
we subtract 1, multiply by 2, and then round down to the nearest whole number. If the hero's army is
weaker than the enemy units, we get -1, -2, or -3, depending on the severity of the divide.

Next, the game adds any bonuses for Diplomacy and "Sympathy". Sympathy is a +1 bonus if the hero's army
contains at least one unit from the enemy stack (the base or upgraded versions both qualify) or +2 if
that unit comprises the majority of the hero's army; Diplomacy is a value between 0 (unskilled) and 3
(expert). This final value is then compared to the "aggression" value of the enemy unit, a hidden number
between 1 and 10(*) that's randomly determined when the game begins. If the aggression value is higher
the enemy unit fights; if it's equal to or lower than our other value, we continue.

>(*This value is somewhat controllable in the map editor; I'll explain later)

The next thing we do is set the army strength comparison value to 1 (so, just: 1 + Diplomacy + Sympathy)
and check against aggression again. If our number is greater than or equal to aggression, the wandering
stack joins for free, else we run the check a third time with the diplomacy bonus doubled. If the third
check passes, the stack offers to join for gold, else it either flees or fights depending on the results
of the initial fight check above (equal = fight, lower = flee). This shows us: A) why most random units
will just run away if all you do is stack Archangels; B) why paid join offers don't happen beyond Easy
difficulty without Diplomacy, and C) how overpowered Diplomacy can be. At expert level, Diplomacy gives
you a base value of 7 to match or beat a random number from 1 to 10, and that's without even considering
the Sympathy bonus or the fact that, the Diplomacy bonus is also applied to the initial fight check.

I mentioned earlier that the aggression value for random enemy units was controllable in the map editor.
Each one has five generic aggression settings, each with its own range of possible integer values:

			    Compliant	-4 (always joins)
			    Friendly	1..7
			    Aggressive	1..10
			    Hostile	4..10
			    Savage	10 (never joins)

As you can see here, any stack set as "Compliant" will always join since the lowest possible value that
we can have to compare to it is -3. This also shows us exactly how unlikely it is for a typical stack to
join without either Diplomacy or Sympathy in play, since we'd need to roll a value of 1 on a friendly or
aggressive stack in addition to having an army that's at least equal in power. I said that aggression is
a random number between 1 and 10 because "Aggressive" is the default setting for wandering unitss and is
by far the most common setting you'll encounter on pretty much any map, at least in the base game.

If you wish to edit the above values, they can be changed at the following addresses:

	        FRIENDLY	       AGGRESSIVE	        HOSTILE
	    ----------------	    ----------------	    ----------------
	    101AFD (Min: 01)	    101B0E (Min: 01)	    101B1F (Min: 04)
	    101AF8 (Max: 07)	    101B09 (Max: 0A)	    101B1A (Max: 0A)

This can be further fine-tuned to allow Friendly and Hostile units to maintain a 10-point spread that's
weighted toward higher (Hostile) or lower (Friendly) results. We do this by getting a random number from
1 to 10 for all three variable aggression settings and then, in the case of Friendly and Hostile units,
check to see if the result is above or below a given threshold. If so, it's then manually adjusted.

    ----------	-------------------------------------------------------------------------
    101AEC~B1F	; WEIGHTED AGGRESSION SETTINGS
    ----------	-------------------------------------------------------------------------
    6A 01		push 01			; 01 = minimum aggression
    6A 0A		push 0A			; 0A = maximum aggression
    5A		pop edx			; ""
    59		pop ecx			; ""
    FF2485C81D5000	jmp [eax*4+501DC8]	; -> (aggression setting)

    B0 FC		mov al,-04		; (COMPLIANT): EAX = -4
    EB 34		jmp 501B31		; -> continue

    E8 BEAC0000	call 50C7C0		; (FRIENDLY): EAX = 1~10
    83 F8 08	cmp eax,08		; is aggression (EAX) >= 8?
    7E 2A		jle 501B31		; if no -> continue
    B0 01		mov al,01		; EAX = 1
    EB 26		jmp 501B31		; -> continue

    E8 B0AC0000	call 50C7C0		; (AGGRESSIVE): EAX = 1~10
    EB 1F		jmp 501B31		; -> continue

    E8 A9AC0000	call 50C7C0		; (HOSTILE): EAX = 1~10
    83 F8 03	cmp eax,03		; is aggression (EAX) <= 3?
    7D 15		jge 501B31		; if no -> continue
    B0 0A		mov al,0A		; EAX = 10
    EB 11		jmp 501B31		; -> continue (101B20~7 is free space)

    101DC8 > F9	; update jump pointer
    101DCC > FD	; ""
    101DD0 > 0B	; ""
    101DD4 > 12	; ""

Beyond that, what you can do about this depends either on how dirty you feel like getting your hands or
how much you like the example I'm about to give. A quick and fairly effective nerf is to change 017246
from 7F to EB and 0A75A5 from 4A to 11, which will make any potential "paid" joiners flee. But, really,
this formula is practically begging for a rewrite. Let's look at some key addresses to start off:

	0A752A - 03 C2	      ; adds Sympathy (EDX) to EAX for fight check
	0A752C - 03 C1	      ; adds Diplomacy (ECX) to EAX for fight check
	0A7553 - 8D 44 0A 01  ; sets EAX to EDX+ECX+1 for free join check
	0A75A3 - 8D 4C 4A 01  ; sets ECX to EDX+ECX*2+1 for paid join check

As you can see, the important registers - EDX and ECX - retain the same values throughout the routine,
which makes editing it much easier on us. If you wish only to change which values are used here, such as
removing the Sympathy bonus, then you need only edit these addresses to the appropriate opcodes (this is
where a disassembler like Cheat Engine will come in handy, since it will translate the assembly command
into raw hex for you). That said, I've opted to go for more of a total rewrite, as seen below:

    --------	---------------------------------------------------------------------
    0A7550~E	; NEW JOIN OFFER FORMULA
    --------	---------------------------------------------------------------------
    29 D0		sub eax,edx		; removes Sympathy (EDX) after fight check
    29 C8		sub eax,ecx		; removes Diplomacy (ECX) after fight check

    39 C6		cmp esi,eax		; is our army strength (EAX) >= aggression (ESI)?
    0F 9D 45 0C	setge [ebp+0C]		; if yes, enemy flees if they do not join

    E9 B2D20300	jmp 4E4811		; -> free space (Diplomacy specialty & artifacts)

    ---------	---------------------------------------------------------------------
    0E4802~30	; (EXPANDED SPACE - OVERWRITES DIPLOMACY SPECIALTY & ARTIFACTS)
    ---------	---------------------------------------------------------------------
    8B148D38EA6300	mov edx,[ecx*4+63EA38]	; EDX = surrender discount
    89 55 FC	mov [ebp-04],edx	; store surrender discount
    E9 16010000	jmp 4E4927		; frees space: 0E4811~926

    8B 5D 10	mov ebx,[ebp+10]	; (displaced code)

    8B C1		mov eax,ecx		; EAX = Diplomacy
    6B C0 02	imul eax,02		; EAX * 2
    01 D0		add eax,edx		; EAX + Sympathy (EDX)

    39 C6		cmp esi,eax		; is EAX >= aggression (ESI)?
    0F8F C92DFCFF	jg 4A75EC		; if no -> [no join]

    83 FA 02	cmp edx,02		; is sympathy 2?
    0F8D 332DFCFF	jge 4A755F		; if yes -> [free join]
    E9 7A2DFCFF	jmp 4A75AB		; -> [paid join]

    ---------	-------------------------------------------------------------------------
    01722C~64	; NEW JOIN OFFER FORMULA (VISIONS SPELL)
    ---------	-------------------------------------------------------------------------
    7F 23		jg 417251		; (skip join check if initial fight check fails)
    29 D0		sub eax,edx		; removes Sympathy (EDX) after fight check
    29 F0		sub eax,esi		; removes Diplomacy (ESI) after fight check

    01 F6		add esi,esi		; Diplomacy (ESI) * 2
    EB 05		jmp 41723B		; (skip unusable space)
    90 90 90 90 90	nop			; -
    01 D6		add esi,edx		; Diplomacy + Sympathy (EDX)
    39 F1		cmp ecx,esi		; is ESI >= aggression (ECX)?
    7F 10		jg 417251		; if no -> fight or flee

    31 F6		xor esi,esi		; ESI = 0 (join check)
    83 FA 02	cmp edx,02		; is sympathy 2?
    EB 05		jmp 41724D		; (skip unusable space)
    90 90 90 90 90	nop			; -
    75 13		jne 417262		; if no -> (paid join)
    EB 12		jmp 417263		; -> (free join)

    31 F6		xor esi,esi		; ESI = 0 (fight or flee)
    F7450800000200	test [ebp+08],20000	; is unit flagged as "can't run"?
    75 08		jne 417264		; if yes -> (fight)

    39 C1		cmp ecx,eax		; is army strength (EAX) >= aggression (ECX)?
    7C 05		jl 417265		; if no -> [exit] (flee)
    EB 02		jmp 417264		; -> (fight)
    46		inc esi			; ESI = 3 (paid join)
    46		inc esi			; ESI = 2 (free join)
    46		inc esi			; ESI = 1 (fight)

So, what's happening here? First of all, we're removing the Diplomacy and Sympathy bonuses after running
the initial fight check so that, while they can still allow a stack that would otherwise fight to join,
they can no longer cause it to flee if the join check fails or if the offer is refused. Second, and more
notably, join offers will no longer occur at all without either Diplomacy or Sympathy. Join offers will
always be free with two points of sympathy, otherwise they will always require payment.

You may also notice that we jump over some unusuable bytes at 017236~A and 017248~C. This is something
that we will encounter from time to time and is a consequence of working with HD Mod, which will inject
code during runtime to certain areas of the executable. This makes that space effectively unusable when
modifying the executable file since whatever we change will just get overwritten when the game loads.

On the subject of sympathy, there are two things we need to do with it specifically. First, for any unit
flagged as "compliant", we'll manually set sympathy to 2 for a free join instead of a paid one. Second,
instead of getting the second point of sympathy from having the majority of our army consist of the same
unit, let's have it come from that unit being from the same faction as the hero. These changes will be
more or less inline, only overwriting a totally unncessary check for RoE maps (in which the four basic
elementals are factionless and do not upgrade since Conflux wasn't a thing yet).

    ---------	-------------------------------------------------------------------------
    0A7236~7F	; COMPLIANT UNITS ALWAYS JOIN FOR FREE (OVERWRITES ROE MAP CHECK)
    ---------	-------------------------------------------------------------------------
    8B 45 08	mov eax,[ebp+08]	; EAX = random unit data
    8B 00		mov eax,[eax]		; EAX = aggression
    C1 E0 0F	shl eax,0F		; ""
    C1 F8 1B	sar eax,1B		; ""
    83 C0 06	add eax,06		; EAX + 6
    83 F8 02	cmp eax,02		; is random unit complaint? (-4 aggression)
    75 04		jne 4A724D		; if no -> (optimized code)
    8B E5		mov esp,ebp		; return (sympathy = 2 for free join)
    5D		pop ebp			; ""
    C3		ret			; ""

    53		push ebx		; (optimized code)
    56		push esi		; ""
    57		push edi		; ""
    8B F9		mov edi,ecx		; ""
    8B F2		mov esi,edx		; ""
    31 C9		xor ecx,ecx		; ""
    89 4D FC	mov [ebp-04],ecx	; ""
    89 4D F8	mov [ebp-08],ecx	; ""
    8B 1D B0476700	mov ebx,[6747B0]	; ""
    8B D6		mov edx,esi		; ""
    6B D2 1D	imul edx,1D		; ""
    83 3C 93 FF	cmp [ebx+edx*4],-01	; ""
    75 05		jne 4A7272		; ""
    83 C8 FF	or eax,-01		; ""
    EB 69		jmp 4A72DB		; ""
    8B CE		mov ecx,esi		; ""
    E8 5738FDFF	call 47AAD0		; ""
    83 F8 FF	cmp eax,-01		; ""
    75 5D 		jne 4A72DB		; ""
    EB 54		jmp 4A72D4		; "" (0A7280~D3 is free space)

    ---------	-------------------------------------------------------------------------
    0A72DB~E5	; SECOND SYMAPTHY POINT FROM FACTION ALIGNMENT INSTEAD OF ARMY MAJORITY
    ---------	-------------------------------------------------------------------------
    57		push edi		; push hero onto stack for later use
    81 C7 AD000000	add edi,AD		; (optimized code)
    6A 07		push 07			; ""
    5B		pop ebx			; ""
    90		nop			; -

    ----------	-------------------------------------------------------------------------
    0A72FD~32C	; ""
    ----------	-------------------------------------------------------------------------
    75 05		jne 4A7304		; -> loop code (adjusted jump length)
    31 C0		xor eax,eax		; EAX (sympathy) = 0
    40		inc eax			; EAX +1
    EB 08		jmp 4A730C		; -> EDI = hero

    83 C7 04	add edi,04		; loop code
    4B		dec ebx			; ""
    75 DC		jne 4A72E6		; ""
    31 C0		xor eax,eax		; EAX = 0 (unit is not in our army)

    5F		pop edi			; EDI = hero
    31 DB		xor ebx,ebx		; EBX = 0
    8A 5F 30	mov bl,[edi+30]		; EBX = hero class
    D1 EB		shr ebx,1		; EBX/2 (hero's faction)
    6B F6 74	imul esi,esi,74		; prepare to check unit faction
    81 C6 B8036700	add esi,6703B8		; ""
    8B 36		mov esi,[esi]		; ESI = unit faction
    39 F3		cmp ebx,esi		; same faction?
    75 01		jne 4A7324		; if no -> (cleanup)
    40		inc eax			; EAX +1

    5F		pop edi			; (cleanup)
    5E		pop esi			; ""
    5B		pop ebx			; ""
    8B E5		mov esp,ebp		; ""
    5D		pop ebp			; ""
    C3		ret			; return
    90 90		nop			; -

    In lieu of a diplomacy bonus on easy mode, let's look at providing one for heroes who encounter units in
    which they specialize. The below code uses more of the space from the Diplomacy specialty and artifacts
    section and assumes that we have swapped all unit specialists from type 1 (scaling) to type 4 (static).

    ---------	-------------------------------------------------------------------------
    0A7484~9A	; DIPLOMACY BONUS FOR UNIT SPECIALISTS
    ---------	-------------------------------------------------------------------------
    8B 4F 1A	mov ecx,[edi+1A]	; ECX = Hero ID
    E8 A5D30300	call 4E4831		; -> free space (Diplomacy bonus & artifacts)
    8B DA 		mov ebx,edx		; EBX = diplomacy (EDX will be overwritten)
    89 45 F8	mov [ebp-08],eax	; (optimized code)
    DFE0		fnstsw ax		; ""
    F6 C4 01	test ah,01		; ""
    75 05		jne 004A749D		; ""
    6A 0B		push 0B			; ""
    58		pop eax			; ""

    ---------	-------------------------------------------------------------------------
    0171BD~CD	; DIPLOMACY BONUS FOR UNIT SPECIALISTS (VISIONS SPELL RIGHT-CLICK INFO)
    ---------	-------------------------------------------------------------------------
    8B 4E 1A	mov ecx,[esi+1A]	; ECX = Hero ID
    E8 7ED60C00	call 4E4843		; -> free space (Diplomacy bonus & artifacts)
    89 45 DC	mov [ebp-24],eax	; optimized code
    8B C7		mov eax,edi		; ""
    6B C0 08	imul eax,eax,08		; ""
    90		nop			; -

    ---------	-------------------------------------------------------------------------
    0E4831~A4	; (EXPANDED SPACE - OVERWRITES DIPLOMACY SPECIALTY & ARTIFACTS)
    ---------	-------------------------------------------------------------------------
    0FBE97CD000000	movsx edx,[edi+CD]	; EDX = diplomacy
    57		push edi		; store EDI
    8B 7D F8	mov edi,[ebp-08]	; EDI = enemy unit ID
    E8 0F000000	call 4E4850		; -> free space (Diplomacy specialty & artifacts)
    5F		pop edi			; retrieve EDI
    C3		ret			; return

    0FBE96CD000000	movsx edx,[esi+CD]	; EDX = diplomacy
    E8 01000000	call 4E4850		; -> free space (Diplomacy specialty & artifacts)
    C3		ret			; return

    57		push edi		; store EDI (enemy unit ID)
    8B 1D 809C6700	mov ebx,[679C80]	; EBX = specialty index
    8D 0C 89	lea ecx,[ecx+ecx*4]	; ECX = data range
    8D 0C CB	lea ecx,[ebx+ecx*8]	; ""
    83 39 04	cmp dword [ecx],04	; unit specialist?
    75 2D		jne 4E488F		; if no -> retrieve EDI

    83 FF 70	cmp edi,70		; unit ID 70 (Air Elementals) or higher?
    72 0D		jb 4E4874		; if no -> EDI/2

    81 FF 84000000	cmp edi,84		; unit ID 84 (Azure Dragons) or higher?
    73 14		jae 4E4883		; if yes -> compare EDI to hero specialty unit

    8B 59 04	mov ebx,[ecx+04]	; EBX = hero specialty unit
    EB 07		jmp 4E487B		; -> compare EBX to (lookup table + EDI)

    D1 FF		sar edi,01		; EDI/2 (drops remainder)
    6B FF 02	imul edi,02		; EDI*2
    EB 08		jmp 4E4883		; -> compare EDI to hero specialty unit

    38 9F 21484E00	cmp [edi+4E4821],bl	; compare EBX to (lookup table + EDI)
    74 05		je 4E4888		; if match -> diplomacy bonus
    39 79 04	cmp [ecx+04],edi	; compare EDI to hero specialty unit
    75 07		jne 4E488F		; if no match -> retrieve EDI

    42		inc edx			; Diplomacy (EDX) +1
    83 FA 03	cmp edx,03		; is Diplomacy level now over maximum?
    7E 01		jle 4E488F		; if no -> retrieve EDI
    4A		dec edx			; Diplomacy (EDX) -1

    5F		pop edi			; retrieve EDI
    C3		ret			; return

    81		; Air Elementals accept Energy specialty
    7B		; Earth Elementals accept Ice specialty
    7D		; Fire Elementals accept Magma specialty
    7F		; Water Elementals accept Storm specialty
    20		; Gold Golems accept regular Golem specialty
    20		; Diamond Golems accept regular Golem specialty
    FF		; -
    76		; Sprites accept Pixie specialty
    FF		; -
    78		; Magic Elementals accept Magic specialty
    FF		; -
    73		; Ice Elementals accept Water specialty
    FF		; -
    71		; Magma Elementals accept Earth specialty
    FF		; -
    70		; Storm Elementals accept Air specialty
    FF		; -
    72		; Energy Elementals accept Fire specialty
    FF		; -
    82		; Phoenixes accept Firebird specialty

There's a bit of optimization in the above code that bears explanation. We account for upgraded units by
dividing the unit ID by 2 and then multiplying it by 2; since division in ASM drops any remainder, base
and upgraded units (ex. Griffins [04] and Royal Griffins [05]) will both return the same value. This all
goes to shit starting with Air Elementals since the elemental unit IDs follow no real pattern, so we use
a lookup table at the tail end of the code for unit IDs above 70, which includes Firebirds/Phoenixes.

Finally, as opposed (or in addition) to a discount for surrendering, let's look at the Diplomacy skill
providing a discount for recruiting units from external dwellings. The below code will use the values at
23EA38~47 for the discount. We left an allowance in the join formula edit above to keep the surrender
discount; you can remove it and just have this one by setting 0E4802~8 to 8B 15 38 EA 63 00 90.

    ------		-------------------------------------------------------------------------
    0A8975		; DIPLOMACY REDUCES UNIT COSTS FROM EXTERNAL DWELLINGS
    ------		-------------------------------------------------------------------------
    E9 2BBF0300	jmp 4E48A5		; -> free space (Diplomacy Bonus & Artifacts)

    --------	-------------------------------------------------------------------------
    1507F6~B	; ""
    --------	-------------------------------------------------------------------------
    E8 C040F9FF	call 4E48BB		; -> free space (Diplomacy specialty & artifacts)
    90		nop			; -

    ----------	-------------------------------------------------------------------------
    0E48A5~906	; (EXPANDED SPACE - OVERWRITES DIPLOMACY BONUS & ARTIFACTS)
    ----------	-------------------------------------------------------------------------
    FF 05 013B6700	inc [673B01]		; set "temp" flag
    E8 70CCFBFF	call 4A1520		; -> [external dwelling routine]
    FF 0D 013B6700	dec [673B01]		; unset "temp" flag
    E9 BF40FCFF	jmp 4A897A		; return

    8B 0D 38956900	mov ecx,[699538]	; ECX = main index
    50		push eax		; Store EAX
    A0 013B6700	mov al,[673B01]		; AL = "temp" flag
    A8 01		test al,01		; external dwelling?
    74 37		je 4E4902		; if no -> retrieve EAX

    E8 A09DFEFF	call 4CE670		; (prepare EAX to check hero)
    8B 40 04	mov eax,[eax+04]	; ""
    69 C0 92040000	imul eax,eax,492	; ""
    8D840820160200	lea eax,[eax+ecx+21620]	; EAX = hero
    0FBE88CD000000	movsx ecx, [eax+CD]	; ECX = Diplomacy
    DB 45 F8	fild dword [ebp-08]	; load unit cost
    D9 5D 08	fstp dword [ebp+08]	; store as floating value
    D9 45 08	fld dword [ebp+08]	; load floating value
    D80C8D38EA6300	fmul dword[ecx*4+63EA38]; multiply by discount
    E8 98361300	call 617F94		; convert to integer
    29 45 F8	sub [ebp-08],eax	; subtract discount from unit cost
    8B 4D F8	mov ecx,[ebp-08]	; ECX = unit cost
    58		pop eax			; retrieve EAX
    8D 75 E0	lea esi,[ebp-20]	; (displaced code)
    C3		ret			; return (0E490C~26 is free space)

Worth noting in the above are the commands that modify 673B01(*). We need a temporary variable to tell
us if we're in an external dwelling or not since there's no other way for us to know once we're already
in there. As we'll learn later, the bulk of the space allocated to each unit in the primary data table
is used as in-game memory and there just so happen to be four unused unit slots, thus providing us with
all of the spare memory we could ever need. It's not the most efficient use of space, however, and thus
should only be used when the information we need isn't more readily available somewhere else.

(*We know that incrementing this address will set it to 1 because the game initializes it to 0 when it
first loads - just in case you were thinking about using this block as free space for actual code.)

---------------------------------------------------------------------------------------------------------

### BALLISTICS, ARTILLERY, & FIRST AID

The percentage values for Artillery (you'll notice that the address is not technically part of the skill
table, but it's in the same format) specify the odds of dealing double damage. The skill requirement for
two shots is the value of 01 at 03FFF1 (the following command is "jump if less than or equal to").

The effects of Ballistics can be edited in the Ballist.txt file from the h3bitmap.lod archive.

Part of what makes Ballistics and Artillery useful is that they can allow spellcasting initiative during
siege battles since the Catapult and Arrow Towers will act before anything else does; Ballistics affords
first strike to the attacker unless the defending town has an arrow tower and a hero with the Artillery
skill, which will then take precedence. If desired, the Catapult can be given priority by swapping the
checks for it (edit both: 064B8D, 064B98) with the Arrow Tower (064B6F & 064B7A).

Another option is to merge, at the very least, Ballistics and Artillery into a single skill since they
don't make much sense as separate ones. There are three calls to the Ballistics skill: 0745C7, 0735E7
(both for maanual control of the Catpault/arrow towers), and 045AC6 (for Catapult damage). Setting these
from D3 to DD will use Artillery in all cases, effectively merging the two skills.

Alternatively, you can just remove the skill requirement for war machines to be manually controllable:

	074589 > E9 9C000000 ; Ballista is always controllable (frees 07458E~9E)

	0745C5 > EB 63	; Catapult/arrow tower always controllable (frees 745C7~D6)
	0735E4 > EB 10	; "" (frees 0735E6~F5)

	07391B > 00	; First Aid Tent is always controllable
	074605 > EB	; "" (frees space: 074607~E)

Doing this will highlight just how much these skills suck since they don't really offer much in the way
of benefits otherwise. Let's look at improving them, starting with our combo Ballistics/Artillery skill.
Rather than a mere chance of dealing double damage at basic level that's only guaranteed at expert, the
Ballista and Catapult will always deal double damage and triple at expert.

    ----------	-------------------------------------------------------------------------
    0435DD~605	; BALLISTA TO 2X DAMAGE AT BASIC SKILL & 3X AT EXPERT
    ----------	-------------------------------------------------------------------------
    8B8481CC530000	mov eax,[ecx+eax*4+53CC]; EAX = hero data
    0FBEB8DD000000	movsx edi,[eax+DD]	; EDI = hero's Artillery skill
    85 FF		test edi,edi		; do we have Artillery?
    0F84 9B020000	je 44388E		; if no -> [exit]
    8B 55 08	mov edx,[ebp+08]	; EDX = base damage
    01 55 14	add [ebp+14],edx	; add EDX to total damage
    83 FF 03	cmp edi,03		; expert Artillery?
    7C 03		jl 443601		; if no -> [continue]
    01 55 14	add [ebp+14],edx	; add EDX to total damage
    E9 88020000	jmp 44388E		; -> [continue] (043606~C6 is free)

>(NOTE: the values at 23B810 will no longer be used)

    ---------	-------------------------------------------------------------------------
    045BEC~F7	; CATAPULT TO CUSTOMIZABLE DAMAGE
    ---------	-------------------------------------------------------------------------
    8B 7D 0C	mov edi,[ebp+0C]	; EDI = ballistics data
    0FBE 7F 05	movsx edi,[edi+05]	; EDI = catapult damage
    8B 75 08	mov esi,[ebp+08]	; ESI = target ID
    EB 1F		jmp 445C1A		; -> [continue] (045BF8~C19 is free)

For the damage of the Catapult (and, by extension, Cyclopses), we'll hijack the first "damage" column in
Ballist.txt which, in the original game, specifies the 10% chance for no damage at no Ballistics skill.
Aside from being crappy, this redundant with the chance to miss. If you don't want the Catapult to miss
at all, you can skip the accuracy routine entirely by replacing the jump at the end of the above code
(EB 1F) with E9 B8000000, which will free up a considerable amount of space (045BFB~CB5).

(Somewhat tangentally, the Archery skill also increases the damage of the Ballista - as this is arguably
a bug, we'll look at editing it later on in the Artifacts section along with the Archery artifacts)

As for First Aid, its biggest problem is that the tent is effectively useless except on high-level units
with enough HP to make use of the increased healing. My solution to this problem was to have the skill
allow the tent to also heal negative statuses: physical ailments at basic level, mental statuses at
advanced, and finally all statuses (including purely magical ones like Slow and Curse) at expert.

    ---------	-------------------------------------------------------------------------
    0E4B96~F7	; FIRST AID HEALS STATUSES (OVERWRITES ORIGINAL EFFECT)
    ---------	-------------------------------------------------------------------------
    57		push edi		; store EDI
    85 F6		test esi,esi		; ??? (crash prevention)
    74 58		je 4E4BF3		; -> only heal HP

    0FBE81E4000000	movsx eax,[ecx+E4]	; EAX = First Aid skill
    84 C0		test al,al		; no skill?
    74 4D		je 4E4BF3		; if yes -> only heal HP
    3C 01		cmp al,01		; Basic?
    74 32		je 4E4BDC		; if yes -> physical statuses only
    3C 02		cmp al,02		; Advanced?
    74 17		je 4E4BC5		; if yes -> remove mental statuses

    31 FF		xor edi,edi		; EDI = 0 (remove magic statuses)
    0FBE8798EA6300	movsx eax,[edi+63EA98]	; EAX = status to remove
    50		push eax		; remove status
    8B CE		mov ecx,esi		; ""
    E8 71F6F5FF	call 444230		; ""
    47		inc edi			; EDI + 1
    83 FF 04	cmp edi,04		; have we cleared every magical status?
    7C EB		jl 4E4BB0		; if no  -> EAX = status to remove

    31 FF		xor edi,edi		; EDI = 0 (remove mental statuses)
    0FBE879CEA6300	movsx eax,[edi+63EA9C]	; EAX = status to remove
    50		push eax		; remove status
    8B CE		mov ecx,esi		; ""
    E8 5AF6F5FF	call 444230		; ""
    47		inc edi			; EDI + 1
    83 FF 05	cmp edi,05		; have we cleared every mental status?
    7C EB		jl 4E4BC7		; if no  -> EAX = status to remove

    31 FF		xor edi,edi		; EDI = 0 (remove physical statuses)
    0FBE87A1EA6300	movsx eax,[edi+63EAA1]	; EAX = status to remove
    50		push eax		; remove status
    8B CE		mov ecx,esi		; ""
    E8 43F6F5FF	call 444230		; ""
    47		inc edi			; EDI + 1
    83 FF 05	cmp edi,05		; have we cleared every physical status?
    7C EB		jl 4E4BDE		; if no  -> EAX = status to remove
    5F		pop edi			; (cleanup)
    8B E5		mov esp,ebp		; ""
    5D		pop ebp			; ""
    C3		ret			; return

    ---------	-------------------------------------------------------------------------
    23EA98~A7	; FIRST AID STATUS TABLE (OVERWRITES ORIGINAL FIRST AID HEALTH TABLE)
    ---------	-------------------------------------------------------------------------
    2A 2D 34 36	; magic statuses (Curse, Weakness, Misfortune, Slow)
    32 3B 3C 3D 3E	; mental statuses (Sorrow, Berserk, Hypnotize, Forgetfulness, Blind)
    46 47 49 4A 4B	; physical statuses (Petrify, Poison, Disease, Paralyze, Aging)
    00 00		; -

    07387A > 00	; allows First Aid Tent to heal statuses on units at maximum health
    07609B > 00	; ""

-----------------------------------------------------------------------------------------

    ---------	-------------------------------------------------------------------------
    03383E~4A	; FIRST AID TENT HEALTH RESTORATION BASED ON SKILL (NO RANODMIZATION)
    ---------	-------------------------------------------------------------------------
    0FBE81E4000000	movsx eax,[ecx+E4]	; EAX = First Aid skill
    8A 80 30854700	mov al,[eax+478530]	; EAX = health to restore

    ---------	-------------------------------------------------------------------------
    078521~F	; ""
    ---------	-------------------------------------------------------------------------
    0FBE80E4000000	movsx eax,[eax+E4]	; EAX = First Aid skill
    8A 80 30854700	mov al,[eax+478530]	; EAX = health to restore
    EB 08		jmp 478538		; -> continue

    ---------	-------------------------------------------------------------------------
    078530~7	; FIRST AID HEALTH RESTORATION TABLE
    ---------	-------------------------------------------------------------------------
    XX		; no skill
    XX		; Basic
    XX		; Advanced
    XX		; Expert
    90 90 90 90	; -

While it does keep the First Aid skill tied to the tent, just allowing it to remove status effects isn't
really a sufficient draw to make the skill attractive. So let's take the rest of the space we freed up
earlier with the change to Logistics and have First Aid also buff the health of your hero's units. This
buff will be equal to the hero's First Aid skill level (basic = 1, advanced = 2, expert = 3) times the
unit's level, thus making the skill significantly impactful even on lower-level units.

    ---------	-------------------------------------------------------------------------
    0E671D~22	; FIRST AID HEALTH BUFFS
    ---------	-------------------------------------------------------------------------
    E8 FBE7FFFF	call 4E4F1D		; -> free space (Logistics)
    5F		pop edi			; (displaced code)

    ---------	-------------------------------------------------------------------------
    0E4F1D~46	; (EXPANDED SPACE - OVERWRITES OLD LOGISTICS SPECIALTY)
    ---------	-------------------------------------------------------------------------
    B9 B8036700	mov ecx,6703B8		; ECX = unit data index
    F6 44 39 10 10	test byte[ecx+edi+10],10; is unit living?
    74 15		je 4E4899		; if no -> (displaced code)

    8A 44 39 04	mov al,[ecx+edi+04]	; EAX = unit's level (0~6)
    40		inc eax			; EAX +1
    8B 4D FC	mov ecx,[ebp-04]	; ECX = hero
    50		push eax		; store EAX
    8A 81 E4000000	mov al,[ecx+E4]		; EAX = First Aid skill
    59		pop ecx			; ECX = unit's level (0~6 +1)
    0FAF C1		imul eax,ecx		; EAX * ECX
    01 C3		add ebx,eax		; add EAX to total health bonus (EBX)
    8B 46 4C	mov eax,[esi+4C]	; (displaced code)
    01 D8		add eax,ebx		; ""
    C3		ret			; return (0E489F~926 is free space)

---------------------------------------------------------------------------------------------------------

### WISDOM & SCHOLAR

Like with Eagle Eye, Scholar can be made to allow teaching fifth-level spells by raising its base level
of effectiveness (0A2663: 01 > 02). Aside from that, the only reason that I'm bringing it up here is to
recommend trashing it in favor of a major overhaul to how magic is learned (which also affects Wisdom).
Instead of visiting heroes automatically learning all the spells from a town's mage guild barring those
which a lack of Wisdom precludes, let's turn it into a proper shop where spells can be purchased with no
skill restrictions. Wisdom, then, will no longer be required to learn spells - only to cast them.

The free space we'll be using for this change will come from removing the now-even-more useless Scholar
skill for the primary effect while the Wisdom edit will be taken from Cursed Ground (including its popup
message - line #749 from GenrlTxt.txt - which should be rewritten accordingly) and the Recanter's Cloak
(which, again, we'll look into removing later). Finally, we'll need new captions for the dialogue boxes;
since we're using HD mod, the "army size names" block of ArrayTxt.txt is completely free. We'll be using
the first twelve of them ("immobile" - "quick") as follows:

	#234: (Immobile)...... "Buy this spell for XX gold?"  (Lv.1)
	#235: (Super Slow).... "Buy this spell for XX gold?"  (Lv.2)
	#236: (Ultra Slow).... "Buy this spell for XX gold?"  (Lv.3)
	#237: (Very Slow)..... "Buy this spell for XX gold?"  (Lv.4)
	#238: (Extra Slow).... "Buy this spell for XX gold?"  (Lv.5)
	#239: (Slow).......... "You can't afford this spell." (Lv.1)
	#240: (Swift)......... "You can't afford this spell." (Lv.2)
	#241: (Extra Swift)... "You can't afford this spell." (Lv.3)
	#242: (Very Swift).... "You can't afford this spell." (Lv.4)
	#243: (Ultra Swift)... "You can't afford this spell." (Lv.5)
	#244: (Super Swift)... "You already know this spell."
	#245: (Quick)......... "Only visiting heroes can buy spells."

"XX" are the prices, which are set in the code below. For the sake of optimization, we use one byte per
level and then multiply it by five after loading it (or else we'd be capped at a price of 255). Thus, to
set a price of 25 gold for first-level spells, we set 4A2710 to 05. A value of 0A (10 in hex) at 4A2711
will give us a price of 50 gold for second-level spells, and so on. And now for the actual code:

    ------		-------------------------------------------------------------------------
    1CE919		; INTERACTIVE MAGE GUILDS - SPELLS ARE NOW PURCHASED INDIVIDUALLY
    ------		-------------------------------------------------------------------------
    E9 143DEDFF	jmp 4A2632		; -> free space

    ----------	-------------------------------------------------------------------------
    0A262D~725	; (EXPANDED SPACE - OVERWRITES SCHOLAR ROUTINE)
    ----------	-------------------------------------------------------------------------
    E9 25010000 	jmp 4A2757		; frees space

    83 FA 04	cmp edx,04		; right-click?
    75 0A		jne 4A2641		; if no -> EAX = visiting hero ID
    E8 C4450500	call 4F6C00		; message box
    E9 DDC21200	jmp 5CE91E		; return

    E8 96000000	call 4A26DC		; EAX = visiting hero ID
    74 2C		je 4A2674		; if no hero -> EDX = "no hero" text offset

    E8 9D000000	call 4A26EA		; EAX = hero data
    8B 4C 24 0C	mov ecx,[esp+0C]	; ECX = spell ID
          80BC08EA03000001	cmp byte[eax+ecx+3EA],1	; does hero already know spell?
    74 1C		je 4A2677		; if yes -> EDX = "spell known" text offset

    E8 9E000000	call 4A26FE		; EAX = player data, ECX = cost, EDX = offset
    39 88 B4000000	cmp [eax+B4],ecx	; can player afford spell?
    7C 12		jl 4A267A		; if no -> EDX = "broke bitch" text offset

    B9 D05C6A00	mov ecx,6A5CD0		; ECX = ArrayTxt index (offset to starting point)
    8B 0C 11	mov ecx,[ecx+edx]	; ECX + "buy spell" text offset (EDX)
    6A 02		push 02			; 2 = ok/cancel
    EB 13		jmp 4A2687		; -> pop EDX

    83 C2 04	add edx,04		; EDX = "no hero" text offset
    83 C2 17	add edx,17		; EDX = "spell known" text offset
    83 C2 14	add edx,14		; EDX = "broke bitch" text offset
    B9 D05C6A00	mov ecx,6A5CD0		; ECX = ArrayTxt index
    8B 0C 11	mov ecx,[ecx+edx]	; ECX + text offset (EDX)
    6A 01		push 01			; 1 = ok only
    5A		pop edx			; EDX = 1 (ok only) or 2 (ok/cancel)
    E8 73450500	call 4F6C00		; message box

    A1 D0926900	mov eax,[6992D0]	; was "okay" clicked?
    81783805780000	cmp [eax+38],7805	; ""
    75 3C		jne 4A26D7		; if no (or if no cancel button) -> return

    E8 3C000000	call 4A26DC		; EAX = visiting hero ID
    E8 45000000	call 4A26EA		; EAX = hero data
    8B 8D 28FFFFFF	mov ecx,[ebp-D8]	; ECX = spell ID

          80BC083004000001	cmp byte[eax+ecx+430],1	; is a scroll for this spell equipped?
    75 08		jne 4A26BD		; if no -> increment "spell known" byte
          C68408EA03000001	mov byte[eax+ecx+3EA],1	; set "spell known" byte to 1
    FE8408EA030000	inc byte[eax+ecx+3EA]	; increment "spell known" byte (scroll=2, else=1)
          C684083004000001	mov byte[eax+ecx+430],1	; set "can cast spell" byte to 1

    E8 2D000000	call 4A26FE		; EAX = player data, ECX = cost
    29 88 B4000000	sub [eax+B4],ecx	; subtract spell cost from player's gold
    E9 42C21200	jmp 5CE91E		; return

    A1 4C956900	mov eax,[69954C]	; EAX = town manager
    8B 40 38	mov eax,[eax+38]	; EAX = town data
    8B 40 10	mov eax,[eax+10]	; EAX = visiting hero ID
    3C FF		cmp al,-01		; is there a vistiting hero?
    C3		ret			; return

    8B 0D 38956900	mov ecx,[699538]	; ECX = main index
    69 C0 92040000	imul eax,eax,492	; EAX = data range
    8D840820160200	lea eax,[eax+ecx+21620]	; EAX = hero data
    C3		ret			; return

    A1 A87F6800	mov eax,[687FA8]	; EAX = spell index
    69 C9 88000000	imul ecx,ecx,088	; ECX = data range
    8B 4C 08 18	mov ecx,[eax+ecx+18]	; ECX = spell level
    8B D1		mov edx,ecx		; EDX = ECX
    6B D2 04	imul edx,04		; EDX = "buy spell" text offset (spell level*4)
    8A 89 20274A00	mov cl,[ecx+4A2720]	; ECX = spell cost / 5
    6B C9 05	imul ecx,ecx,05		; ECX * 5
    A1 FCCC6900	mov eax,[69CCFC]	; EAX = active player data
    C3		ret			; return

    05		; Level 1 = 05  (*5 = 25 gold)
    0A		; Level 2 = 10  (*5 = 50 gold)
    14		; Level 3 = 20  (*5 = 100 gold)
    32		; Level 4 = 50  (*5 = 250 gold)
    64		; Level 5 = 100 (*5 = 500 gold)

    Array.txt
    ---------
    #234: (Immobile)...... "Buy this spell for XX gold?"  (Lv.1)
    #235: (Super Slow).... "Buy this spell for XX gold?"  (Lv.2)
    #236: (Ultra Slow).... "Buy this spell for XX gold?"  (Lv.3)
    #237: (Very Slow)..... "Buy this spell for XX gold?"  (Lv.4)
    #238: (Extra Slow).... "Buy this spell for XX gold?"  (Lv.5)
    #239: (Slow).......... "You can't afford this spell." (Lv.1)
    #240: (Swift)......... "You can't afford this spell." (Lv.2)
    #241: (Extra Swift)... "You can't afford this spell." (Lv.3)
    #242: (Very Swift).... "You can't afford this spell." (Lv.4)
    #243: (Ultra Swift)... "You can't afford this spell." (Lv.5)
    #244: (Super Swift)... "You already know this spell."
    #245: (Quick)......... "Only visiting heroes can buy spells."

    --------	-------------------------------------------------------------------------
    1BE576~C	; SKIP AUTOMATIC SPELL LEARNING FOR HUMAN PLAYERS
    --------	-------------------------------------------------------------------------
    E9 AB41EEFF	jmp 4A2726		; -> free space (Scholar)
    90 90 		nop			; -

    ----------	-------------------------------------------------------------------------
    0A2726~744	; (EXPANDED SPACE - OVERWRITES SCHOLAR ROUTINE)
    ----------	-------------------------------------------------------------------------
    A1 FCCC6900	mov eax,[69CCFC]	; EAX = active player data
    8A 80 E1000000	mov al,[eax+E1]		; AL = AI flag
    84 C0		test al,al		; AI player?
    0F85 AFBE1100	jne 5BE5E8		; if no -> [exit]
    0FBE8BD0000000	movsx ecx,[ebx+D0]	; (displaced code)
    E9 38BE1100	jmp 5BE57D		; return (0A2745~56 is free space)

-----------------------------------------------------------------------------------------

    ---------	-------------------------------------------------------------------------
    19EE0B~29	; WISDOM REQUIRED TO CAST LV.3+ COMBAT SPELLS (OVERWRITES CURSED GROUND)
    ---------	-------------------------------------------------------------------------
    8B B5 6CFFFFFF	mov esi,[ebp-94]	; ESI = hero data
    8B 15 809C6700	mov edx,[679C80]	; EDX = specialty index
    8B 4E 1A	mov ecx,[esi+1A]	; ECX = hero ID
    8D 0C 89	lea ecx,[ecx+ecx*4]	; ECX = data range
    8D 0C CA	lea ecx,[edx+ecx*8]	; ""
    EB 48		jmp 59EE6A		; -> free space (Recanter's Cloak)
    E8 BF950000	call 5A83E6		; is Wisdom >= spell level?
    90		nop			; -
    7D 67		jge 59EE91		; if yes -> [allow spell]

    ---------	-------------------------------------------------------------------------
    19EE6A~7F	; (EXPANDED SPACE - OVERWRITES RECANTER'S CLOAK)
    ---------	-------------------------------------------------------------------------
    83 39 03	cmp dword [ecx],03	; spell specialist?
    75 05		jne 59EE74		; if no -> check for scroll

    39 41 04	cmp [ecx+04],eax	; specialist in this spell?
    74 1D		je 59EE91		; if yes -> [allow spell]

          80BC30EA03000001	cmp byte[eax+esi+3EA],01; spell scroll (00 or 02)?
    75 13		jne 59EE91		; if yes -> [allow spell]
    EB A2		jmp 59EE22		; return (19EE80~90 + 19EEAB~F5E is free space)

    ---------	-------------------------------------------------------------------------
    01C551~70	; WISDOM REQUIRED TO CAST LV.3+ MAP SPELLS (OVERWRITES CURSED GROUND)
    ---------	-------------------------------------------------------------------------
    8B 15 D0926900	mov edx,[6992D0]	; get spell ID
    8B 42 38	mov eax,[edx+38]	; ""
          80BC30EA03000001	cmp byte[eax+esi+3EA],01; spell scroll (00 or 02)?
    75 79		jne 41C5DD		; if yes -> [allow spell]

    50		push eax		; store spell ID
    E8 7CBE1800	call 5A83E6		; is Wisdom >= spell level?
    58		pop eax			; retrieve spell ID
    909090909090	nop			; -

    ---------	-------------------------------------------------------------------------
    1A83E1~FB	; (EXPANDED SPACE - OVERWRITES CURSED GROUND & RECANTER'S CLOAK)
    ---------	-------------------------------------------------------------------------
    89 4D F8	mov [ebp-08],ecx	; optimized code
    EB 62		jmp 5A8448		; frees space: 1A83E6~447

    8B 15 A87F6800	mov edx,[687FA8]	; EDX = spell index
    6B C0 11	imul eax,eax,11		; EAX = data range
    8A 8E D0000000	mov cl,[esi+D0]		; CL = Wisdom
    41		inc ecx			; CL + 2
    41		inc ecx			; ""
    3A 4C C2 18	cmp cl,[edx+eax*8+18]	; is CL >= spell level?
    C3		ret			; return

    ---------	-------------------------------------------------------------------------
    0A5459~60	; SHRINES WILL NOT CHECK FOR WISDOM WHEN TEACHING SPELLS
    ---------	-------------------------------------------------------------------------
    8A 45 18	mov al,[ebp+18]		; EAX = AI player?
    E9 E9000000	jmp 4A554A		; -> [continue] (0A5461~549 is free space)

    0A409E > EB	; pyramids don't check for Wisdom when teaching spells (frees 0A40A0~EE)
    17421A > EB 1B	; quests don't check for Wisdom when teaching spells (frees 17421C~36)

-----------------------------------------------------------------------------------------

    --------	-------------------------------------------------------------------------
    0D9894~8	; EQUIP SPELL SCROLL
    --------	-------------------------------------------------------------------------
    E9 63EB0C00	jmp 5A83FC		; -> free space (Cursed Ground/Recanter's Cloak)

    ----------	-------------------------------------------------------------------------
    1A83FC~411	; (EXPANDED SPACE - OVERWRITES CURSED GROUND & RECANTER'S CLOAK)
    ----------	-------------------------------------------------------------------------
          80BC18EA03000001	cmp byte[eax+ebx+3EA],01; does hero already know this spell?
    75 07 		jne 5A840D		; if no -> [continue]
    FF8418EA030000	inc [eax+ebx+3EA]	; set "spell known" byte to 2
    E9 2316F3FF	jmp 4D9A35		; -> [continue]

    --------	-------------------------------------------------------------------------
    0D9860~4	; UNEQUIP SPELL SCROLL
    --------	-------------------------------------------------------------------------
    E8 ADEB0C00	call 5A8412		; -> free space (Cursed Ground/Recanter's Cloak)

    --------	-------------------------------------------------------------------------
    1A8412~F	; (EXPANDED SPACE - OVERWRITES CURSED GROUND & RECANTER'S CLOAK)
    --------	-------------------------------------------------------------------------
    8A 08		mov cl,[eax]		; CL = "spell known" byte
    80 F9 02	cmp cl,02		; does CL = 2?
    75 03		jne 5A841C		; if no -> (displaced code)
    49		dec ecx			; CL = 1
    88 08		mov [eax],cl		; "spell known" byte = 1
    88 0F		mov [edi],cl		; (displaced code)
    47		inc edi			; ""
    C3		ret			; return (1A8420~47 is free space)

    --------	-------------------------------------------------------------------------
    0E5402~6	; SCROLLS CAST AT BASIC LEVEL
    --------	-------------------------------------------------------------------------
    E9 FBCBFAFF	jmp 492002		; -> free space (Cursed Ground, unit casters)

    ---------	-------------------------------------------------------------------------
    092000~1C	; (EXPANDED SPACE - OVERWRITES CURSED GROUND, UNIT CASTERS)
    ---------	-------------------------------------------------------------------------
    EB 1B		jmp 49201D		; frees space: 092009~1C
    83 FE 46	cmp esi,46		; is ESI a spell ID instead of hero data?
    7C 0F		jl 492016		; if yes -> (cleanup)
          80BC3EEA03000001	cmp byte[esi+edi+3EA],1	; spell scroll (00 or 02)?
    74 05		je 492016		; if no -> (cleanup)
    3C 00		cmp al,00		; Unskilled?
    7F 01		jg 492016		; if no -> (cleanup)
    40		inc eax			; Skill +1
    5B		pop ebx			; (cleanup)
    5D		pop ebp			; ""
    C2 0800		ret 08			; return
    90 90		nop			; -

As you can see, fundamentally altering how Wisdom works has mandated that we change several other things
that it ties directly into, such as spell shrines and scrolls. The above is, for the most part, the bare
minimum of changes required to those objects in order for them to respect the new functionality; the one
"rider" effect is that spell scrolls will now cast at a minimum of basic skill. This edit can be omitted
if so desired and is included here primarily because it seemed like the most logical place to put it.

A good learning point here is the use of calls versus jumps. We've seen both used to move to free space
in the code thus far, but haven't really looked at why we use one or the other. In short, we use calls
whenever possible because they're more efficient. A standard return command uses less space than a long
jump, but more importantly they can act as simple ways to execute large portions of code that you would
otherwise need to copy/paste multiple times, as seen in the above example or earlier when we provided a
Diplomacy bonus for unit specialists and ran two diferent routines through the same block of code.

Calls do have a few drawbacks, however. They won't work if your code has multiple possible destinations
and/or no need to return to the point of origin, as seen in the Diplomacy formula rewrite. They also use
the stack to keep track of where they return to, so you can't use them to alter it (push/pop). Finally,
jumps can actually be more optimal if your free space is close by since a short jump is only two bytes
while calls are always five regardless of how far they need to go.

---------------------------------------------------------------------------------------------------------

### RESISTANCE

Resistance is a problematic skill due mostly to a combination of its binary nature and situational use.
Its primary effect is to defend against hostile spells, which only comes into play against other heroes,
and the fact that it provides spell evasion rather than reduction means that it is largely useless at
lower levels and overpowered at higher levels. Let's instead make resistance reduce spell damage using
the rest of the Recanter's Cloak space we freed up above with the Wisdom/mage guild change.

    ---------	-------------------------------------------------------------------------
    04A5AF~B3	; RESISTANCE DOES NOT BLOCK DAMAGE SPELLS
    ---------	-------------------------------------------------------------------------
    E9 F7481500	jmp 59EEAB		; -> free space (Recanter's Cloak)

    ---------	-------------------------------------------------------------------------
    19EEAB~DA	; (EXPANDED SPACE - OVERWRITES RECANTER'S CLOAK)
    ---------	-------------------------------------------------------------------------
    83 7D F0 13	cmp [ebp-10],13		; Chain Lightning? (prevents lockups)
    74 21		je 59EED2		; if yes -> (cleanup)
    8B 3D A87F6800	mov edi,[687FA8]	; EDI = spell index
    8B 75 F0	mov esi,[ebp-10]	; ESI = spell ID
    69 F6 88000000	imul esi,88		; ESI = data range
    8B 5C 3E 0C	mov ebx,[esi+edi+0C]	; EBX = spell flags
    C1 EB 09	shr ebx,09		; EBX = "damage spell" flag
    F6 C3 01	test bl,01		; damage spell?
    74 06		je 59EED2		; if no -> (cleanup)
    D9 05 E0B66300	fld dword ptr [63B6E0]	; spell always hits
    5F		pop edi			; (cleanup)
    5E		pop esi			; ""
    5B		pop ebx			; ""
    8B E5		mov esp,ebp		; ""
    5D		pop ebp			; ""
    C2 0800		ret 0008		; ""

    ---------	-------------------------------------------------------------------------
    1A7F7E~8D	; RESISTANCE LOWERS SPELL DAMAGE
    ---------	-------------------------------------------------------------------------
    A1 20946900	mov eax,[699420]	; EAX = combat manager
    8B 8F F4000000	mov ecx,[edi+F4]	; ECX = unit's owner
    E9 4D6FFFFF	jmp 59EEDB		; -> free space (Recanter's Cloak)

    ---------	-------------------------------------------------------------------------
    19EEDB~F07	; (EXPANDED SPACE - OVERWRITES RECANTER'S CLOAK)
    ---------	-------------------------------------------------------------------------
    8B8C88CC530000	mov ecx,[eax+ecx*4+53CC]; ECX = unit's hero
    85 C9		test ecx,ecx		; does unit have a hero?
    74 1B		je 59EF01		; if no -> EAX = damage
    E8 655AF4FF	call 4E4950		; (Resistance)
    DD 5D F0	fstp qword [ebp-10]	; store Resistance reduction
    DB 45 08	fild dword [ebp+08]	; load damage (integer)
    DD 5D F8	fstp qword [ebp-08]	; store damage as floating value
    DD 45 F8	fld qword [ebp-08]	; load damage (float)
    DC 4D F0	fmul qword [ebp-10]	; apply Resistance reduction
    E8 95900700	call 617F94		; convert result to integer (EAX)
    EB 03		jmp 59EF04		; -> (cleanup)
    8B 45 08	mov eax,[ebp+08]	; EAX = damage
    5D		pop ebp			; (cleanup)
    C2 0C00		ret 0C			; return

More drastically, we can expand our definition of magical damage to include ranged attacks from certain
types of units, such as Mages or Gogs, and use Resistance in place of Armorer to lower their damage. We
use the (maximum) number of shots of a unit in the below code to determine this: anything with a magical
projectile is set to 255 (effectively unlimited) shots, but you can use any value you'd like. For melee
attacks, we restrict this effect solely to Psychic and Magic Elementals lest stacking Resistance allow
you to completely shut down a Conflux opponent with no possible counterplay.

    ---------	-------------------------------------------------------------------------
    043D82~6	; RESISTANCE LOWERS NON-PHYSICAL ATTACK DAMAGE INSTEAD OF ARMORER
    ---------	-------------------------------------------------------------------------
    E8 81B11500	call 59EF08		; -> free space (Recanter's Cloak)

    ---------	-------------------------------------------------------------------------
    19EF08~38	; (EXPANDED SPACE - OVERWRITES RECANTER'S CLOAK)
    ---------	-------------------------------------------------------------------------
    8B 15 B0476700	mov edx,[6747B0]	; EDX = unit index
    8B 43 34	mov eax,[ebx+34]	; EAX = unit ID
    83 7D 10 01	cmp [ebp+10],01		; ranged attack?
    75 0C		jne 59EF23		; if no -> Psychic Elementals?
    6B C0 74	imul eax,74		; EAX = data range
    83 7C 10 64 FF 	cmp [eax+edx+64],-01	; 255 shots?
    75 12		jne 59EF33		; if no -> (Armorer)
    EB 0A		jmp 59EF2D		; -> (Resistance)

    83 F8 78	cmp eax,78		; Psychic Elementals?
    74 05		je 59EF2D		; if yes -> (Resistance)
    83 F8 79	cmp eax,79		; Magic Elementals?
    75 06		jne 59EF33		; if no -> (Armorer)
    E8 1E5AF4FF	call 4E4950		; (Resistance)
    C3		ret			; return
    E8 4856F4FF	call 4E4580		; (Armorer)
    C3		ret			; return

-----------------------------------------------------------------------------------------

Importantly, Resistance also defends against negative statuses set not only by spells, but also by enemy
units. The issue there is that it does so invisibly in the latter case, so players rarely see Resistance
being beneficial. The below code will inform the player whenever Resistance blocks an enemy status:

    ---------	-------------------------------------------------------------------------
    040315~22	; SHOW ANIMATION/BATTLE TEXT WHEN RESISTANCE BLOCKS DISEASE
    ---------	-------------------------------------------------------------------------
    6A 49		push 49			; 49 = Disease
    5E		pop esi			; ""
    E8 03811600	call 5A8420		; -> free space (Cursed Ground/Recanter's Cloak)
    89 B7 EC000000	mov [edi+EC],esi	; set status to be applied
    
    ---------	-------------------------------------------------------------------------
    0404EE~FF	; SHOW ANIMATION/BATTLE TEXT WHEN RESISTANCE BLOCKS PETRIFY
    ---------	-------------------------------------------------------------------------
    6A 46		push 46			; 46 = Petrify
    5E		pop esi			; ""
    E8 2A7F1600	call 5A8420		; -> free space (Cursed Ground/Recanter's Cloak)
    89 B7 EC000000	mov [edi+EC],esi	; set status to be applied
    90 90 90 90	nop			; -
    
    ---------	-------------------------------------------------------------------------
    040385~96	; SHOW ANIMATION/BATTLE TEXT WHEN RESISTANCE BLOCKS FEAR
    ---------	-------------------------------------------------------------------------
    6A 3E		push 3E			; 3E = Fear
    5E		pop esi			; ""
    E8 93801600	call 5A8420		; -> free space (Cursed Ground/Recanter's Cloak)
    89 B7 EC000000	mov [edi+EC],esi	; set status to be applied
    90 90 90 90	nop			; -
    
    ---------	-------------------------------------------------------------------------
    04032D~36	; "" (MOVES MIND RESISTANCE CHECK TO PREVENT FALSE POSITIVES)
    ---------	-------------------------------------------------------------------------
    E9 EA3E1300	jmp 57421C		; -> free space (Wisdom Quest Check)
    5A		pop edx			; (displaced/optimized code)
    31 C9		xor ecx,ecx		; ""
    41		inc ecx			; ""
    90		nop 			; -
    
    ---------	-------------------------------------------------------------------------
    17421C~36	; (EXPANDED SPACE - OVERWRITES WISDOM QUEST CHECK)
    ---------	-------------------------------------------------------------------------
    8B 7D 08	mov edi,[ebp+08]	; EDI = defending stack
    8B 87 84000000	mov eax,[edi+84]	; EAX = unit data
    C1 E8 0A	shr eax,0A		; shift to mind immunity flag
    A8 01		test al,01		; immune?
    0F85 7EC0ECFF	jne 4402AE		; if yes -> [exit]
    6A 64		push 64			; (displaced/optimized code)
    E9 FBC0ECFF	jmp 440332		; return
    
    ---------	-------------------------------------------------------------------------
    0402A0~D	; SHOW ANIMATION/BATTLE TEXT WHEN RESISTANCE BLOCKS AGING
    ---------	-------------------------------------------------------------------------
    6A 4B		push 4B			; 4B = Aging
    5E		pop esi			; ""
    E8 78811600	call 5A8420		; -> free space (Cursed Ground/Recanter's Cloak)
    89 B7 EC000000	mov [edi+EC],esi	; set status to be applied
    
    ---------	-------------------------------------------------------------------------
    0405A4~B5	; SHOW ANIMATION/BATTLE TEXT WHEN RESISTANCE BLOCKS POISON
    ---------	-------------------------------------------------------------------------
    6A 47		push 47			; 47 = Poison
    5E		pop esi			; ""
    E8 747E1600	call 5A8420		; -> free space (Cursed Ground/Recanter's Cloak)
    89 B7 EC000000	mov [edi+EC],esi	; set status to be applied
    90 90 90 90	nop			; -
    
    ---------	-------------------------------------------------------------------------
    040618~2A	; SHOW ANIMATION/BATTLE TEXT WHEN RESISTANCE BLOCKS PARALYZE
    ---------	-------------------------------------------------------------------------
    6A 4A		push 4A			; 4A = Paralyze
    5E		pop esi			; ""
    E8 007E1600	call 5A8420		; -> free space (Cursed Ground/Recanter's Cloak)
    89 B7 EC000000	mov [edi+EC],esi	; set status to be applied
    90 90 90 90	nop			; -
    
    --------	-------------------------------------------------------------------------
    1A8420~D	; (EXPANDED SPACE - OVERWRITES CURSED GROUND/RECANTER'S CLOAK)
    --------	-------------------------------------------------------------------------
    84 C0		test al,al		; was status resisted?
    75 09		jne 5A842D		; if no -> return
    6A 1B		push 1B			; 1B = Shield (graphic only)
    5E		pop esi			; ""
    FF 05 023B6700	inc [673B02]		; set "temp" flag
    C3		ret			; return
    
    --------	-------------------------------------------------------------------------
    1A1393~9	; DO NOT APPLY RESISTED STATUS
    --------	-------------------------------------------------------------------------
    E9 96700000	jmp 5A842E		; -> free space (Cursed Ground/Recanter's Cloak)
    51		push ecx		; (displaced code)
    90		nop			; -
    
    --------	-------------------------------------------------------------------------
    1A18D7~D	; ""
    --------	-------------------------------------------------------------------------
    31 C9		xor ecx,ecx		; (displaced code)
    E9 606B0000	jmp 5A843E		; -> free space (Cursed Ground/Recanter's Cloak)
    
    ---------	-------------------------------------------------------------------------
    1A842E~47	; (EXPANDED SPACE - OVERWRITES CURSED GROUND/RECANTER'S CLOAK)
    ---------	-------------------------------------------------------------------------
    A0 023B6700	mov al,[673B02]		; AL = temp flag
    84 C0		test al,al		; is flag set?
    0F85 698FFFFF	jne 5A13A4		; if yes -> [do not apply status]
    8B 4D EC	mov ecx,[ebp-14]	; (displaced code)
    8B 45 1C	mov eax,[ebp+1C]	; (displaced code)
    E9 528FFFFF	jmp 5A1398		; -> [continue]
    90 90		nop			; -
    
    ----------	-------------------------------------------------------------------------
    1A8EC8~F03	; BATTLE TEXT FOR RESISTED STATUSES
    ----------	-------------------------------------------------------------------------
    74 16		je 5A8EE0		; (optimized code)
    8D 48 FF	lea ecx,[eax-01]	; ""
    8A 40 FF	mov al,[eax-01]		; ""
    84 C0		test al,al		; ""
    74 02		je 5A8ED6		; ""
    3C FF		cmp al,-01		; ""
    0F84 45060000	je 5A9521		; ""
    FE C8		dec al			; ""
    88 01		mov [ecx],al		; ""
    E9 45060000	jmp 5A952A		; ""
    A0 023B6700	mov al,[673B02]		; AL = temp flag
    84 C0		test al,al		; is flag set?
    74 10		je 5A8EFE		; if no -> free space (Recanter's Cloak)
    A1 045D6A00	mov eax,[6A5D04]	; EAX = ArrayTxt, line 246
    FF 0D 023B6700	dec [673B02]		; unset temp flag
    E9 DF000000 	jmp 5A8FDD		; -> [continue]
    E8 3660FFFF	call 59EF39		; -> free space (Recanter's Cloak)
    90		nop 			; -
    
    1A8CDA > 07	; update jump pointer
    
    ---------	-------------------------------------------------------------------------
    19EF39~4F	; (EXPANDED SPACE - OVERWRITES RECANTER'S CLOAK)
    ---------	-------------------------------------------------------------------------
    B9 0A000000	mov ecx,0A		; (displaced/optimized code)
    8B 45 0C	mov eax,[ebp+0C]	; ""
    83 C0 D6	add eax,-2A		; ""
    83 F8 24	cmp eax,24		; ""
    77 06		ja 59EF4F		; ""
    8A 88 D4955A00	mov cl,[eax+5A95D4]	; ""
    C3		ret			; return
