# 4. SPELLS

Most spell settings can be edited through the SpTraits.txt file, including: name and description, level,
school(s), MP cost (per level), power/effectiveness, and appearance probabilities per town. If any spell
from the game ye wish to remove, simply set the appearance rate to 0 for all towns, unset its school(s),
and set the level to 4 (level 1-3 spells can appear randomly in shrines, while the Spellcaster's Hat and
Pyramids teach lv.5 spells). Also remember that it may still be cast by units and/or artifacts, which
we'll deal with later. When editing appearance rates, remember that in each town the possible results
for each level all add up to 100 - not 112 like the skill probabilities for hero classes.

Several unit abilities also appear at the bottom of SpTraits.txt; these are treated as spells (for the
most part) and are thus subject to being blocked by units with spell immunities. This can be adjusted by
messing with their levels, but any unit with "immunity to lv. 1-5 spells" will block them no matter what
level you set them to. Anti-Magic will behave in a similar manner except that it will ignore any ability
set to level 0. Spell resistance only kicks in for the "Thunderbolt" ability (Thunderbirds), while Acid
Breath, Bind ("Entangle"), and Death Cloud are not treated as spells at all for the purposes of anything
in this paragraph. It's kind of a mess, and I'm only mostly confident that everything I've just stated
here is completely and entirely accurate. Feel free to fact-check me!

As with heroes, there is a table in the .exe file containing various properties for spells beginning at
2854A0, with 88 bytes per spell. There is very little to be done with these, however, as most of those
bytes are dynamically filled during the game's runtime. The few of any interest are the three bytes for
flags, which begin at the following addresses for each spell:

|Name|ID||Name|ID||Name|Id|
|-|-|-|-|-|-|-|-|
Summon Boat|2854AC||Meteor Shower|2860E4||Stoneskin|286D1C
Scuttle Boat|285534||Death Ripple|28616C||Disrupting Ray|286DA4
Visions|2855BC||Destroy Undead|2861F4||Prayer|286E2C
View Earth|285644||Armageddon|28627C||Mirth|286EB4
Disguise|2856CC||Shield|286304||Sorrow|286F3C
View Air|285754||Air Shield|28638C||Fortune|286FC4
Fly|2857DC||Fire Shield|286414||Misfortune|28704C
Water Walk|285864||Resist Air|28649C||Haste|2870D4
Dimension Door|2858EC||Resist Fire|286524||Slow|28715C
Town Portal|285974||Resist Water|2865AC||Slayer|2871E4
Quicksand|2859FC||Resist Earth|286634||Frenzy|28726C
Land Mine|285A84||Anti-Magic|2866BC||Counterstrike|28737C
Force Field|285B0C||Dispel|286744||Berserk|287404
Fire Wall|285B94||Magic Mirror|2867CC||Hypnotize|28748C
Earthquake|285C1C||Cure|286854||Forgetfulness|287514
Magic Arrow|285CA4||Resurrection|2868DC||Blind|28759C
Ice Bolt|285D2C||Animate Dead|286964||Teleport|287624
Lightning Bolt|285DB4||Sacrifice|2869EC||Remove Obstacle|2876AC
Implosion|285E3C||Bless|286A74||Clone|287734
Chain Lightning|285EC4||Curse|286AFC||Summon Fire|2877BC
Frost Ring|285F4C||Bloodlust|286B84||Summon Earth|287844
Fireball|285FD4||Precision|286C0C||Summon Water|2878CC
Inferno|28605C||Weakness|286C94||Summon Air|287954
|||||||||
Petrify|2879DC||Paralyze|287BFC||Dispel(*)|287E1C
Poison|287A64||Age|287C84||Death Stare|287EA4
Bind|287AEC||Death Cloud|287D0C||Acid Breath|287F2C
Disease|287B74||Thunderbolt|287D94||Titan's Bolt|2872F4


>(*This is the Dragonfly dispel effect which only removes positive statuses)

	BYTE 01:				BYTE 02:

	 BIT 1 (01) Battlefield spell		 BIT 1 (01) (*)
	 BIT 2 (02) Adventure spell		 BIT 2 (02) Damage spell
	 BIT 3 (04) Has duration		 BIT 3 (04) Mind spell
	 BIT 4 (08) Unit ability		 BIT 4 (08) Friendly spell
	 BIT 5 (10) Target: stack		 BIT 5 (10) Ineffective on war machines
	 BIT 6 (20) Target: ranged stack	 BIT 6 (20) (*)
	 BIT 7 (40) Mass effect @ expert	 BIT 7 (40) (*)
	 BIT 8 (80) Target: any square		 BIT 8 (80) (*)

			BYTE 03: (AI flags - see notes below)


If the above concept is new to you, a single byte consists of eight "bits", which can be set to 0 or 1.
There are 256 different possible combinations of settings which are ultimately expressed in hexadecimal
format as a byte value between 00 (no bits set) and FF (all bits set). A value of 45, for example, has
bits 1 (01), 3 (04), and 7 (40) set, indicating a combat spell with a duration (so something like Haste
or Stoneskin) which will mass target at expert level.

The major items of note here are the targeting flags, which you can manipulate to make any spell always
target a single unit stack (set ONLY bit 5 or 6 on byte 01), mass target at any skill level (unset all
targeting bits), or only mass target at a certain skill level (set only bit 7) . This threshold can be
globally modified from expert level (02) to advanced (01) or basic (00) at 19E37B. Forgetfulness instead
uses the value at 19E384 (01), which is why it mass-targets at advanced Water Magic rather than expert.

I should also mention that the Implosion spell has the "ineffective on war machines" flag set for some
reason. I believe this to be unintentional/a bug as it's the only direct damage spell with it and there
doesn't seem to be any logical reason why it should (not that you would WANT to use it that way).

Regarding the asterisks above...

`BYTE 2, BIT 1 (01)`
Only used on Remove Obstacle; not sure what it actually does.

`BYTE 2, BIT 6 (20)`
Only used on Titan's Bolt. Indicates an artifact-only spell, and is presumably related to preventing it from appearing via other means (i.e. mage guilds, shrines, tomes).

`BYTE 2, BIT 7 (40)`
Used on (Earth/Air/Fire) Shield, Counterstrike, Anti-Magic, Magic Mirror, and all magic resist spells.
Seems to indicate a defensive/buff spell, but is missing from several of them (i.e. Stoneskin).

`BYTE 2, BIT 8 (80)`
Used on Magic Arrow, Ice Bolt, Frost Ring, Fireball, Lightning/Titan Bolt, Implosion, and Meteor Shower.
This is one of three AI flags for spells which deal damage (see below).

`BYTE 3, BIT 1 (01)`
Used on Chain Lightning and Inferno. The second AI flag for damage spells, seemingly to indicate a spell
with an area of effect. Unsure why Fireball, Frost Ring, and Meteor Shower use the above flag instead.

`BYTE 3, BIT 2 (02)`
Used on Death Ripple, Destroy Undead, and Armageddon. This is the third AI direct damage spell flag.

`BYTE 3, BIT 3 (04)`
Used on most spells which affect units and deal no damage except for the below and Sacrifice.

`BYTE 3, BIT 4 (08)`
Used on Hypnotize, Animate Dead/Resurrection, and summon spells. This flag appears to have something to
do with gaining ownership/control of a unit stack.

`BYTE 3, BIT 5 (10)`
Used only on Earthquake, Summon Boat, Water Walk, Fly, Dimension Door, and Town Portal. Would appear to
indicate an adventure map spell, except we already have a flag for that. Also unsure why Earthquake has
it set (possibly a bug) or what, if anything, this flag is actually used for.

---------------------------------------------------------------------------------------------------------

## SPELL SPECIALTIES

There are seven types of bonuses assigned on a per-spell basis in a single-byte table starting at 0E6358
(Fire Wall) and running to 0E6382 (Slayer). Although this range includes most of the spells in the game,
it doesn't necessarily mean that all of them are eligible due to the bonus failing to interact with the
spell's effects. The default setting for most spells in this range is the "scaling" damage bonus, which
simply has no effect on many of them. Feel free to experiment with other settings.

-----------------------------------------------------------------------------------------

| Spell           | Hex Code | Spell           | Hex Code | Spell           | Hex Code |
|-----------------|----------|-----------------|----------|-----------------|----------|
| Fire Wall       | 0E6358   | Shield          | 0E6366   | Bless           | 0E6374   |
| Earthquake      | 0E6359   | Air Shield      | 0E6367   | Curse           | 0E6375   |
| Magic Arrow     | 0E635A   | Fire Shield     | 0E6368   | Bloodlust       | 0E6376   |
| Ice Bolt        | 0E635B   | Resist Air      | 0E6369   | Precision       | 0E6377   |
| Lightning Bolt  | 0E635C   | Resist Fire     | 0E636A   | Weakness        | 0E6378   |
| Implosion       | 0E635D   | Resist Water    | 0E636B   | Stoneskin       | 0E6379   |
| Chain Lightning | 0E635E   | Resist Earth    | 0E636C   | Disrupting Ray  | 0E637A   |
| Frost Ring      | 0E635F   | Anti-Magic      | 0E636D   | Prayer          | 0E637B   |
| Fireball        | 0E6360   | Dispel          | 0E636E   | Mirth           | 0E637C   |
| Inferno         | 0E6361   | Magic Mirror    | 0E636F   | Sorrow          | 0E637D   |
| Meteor Shower   | 0E6362   | Cure            | 0E6370   | Fortune         | 0E637E   |
| Death Ripple    | 0E6363   | Resurrection    | 0E6371   | Misfortune      | 0E637F   |
| Destroy Undead  | 0E6364   | Animate Dead    | 0E6372   | Haste           | 0E6380   |
| Armageddon      | 0E6365   | Sacrifice       | 0E6373   | Slow            | 0E6381   |
|Slayer           | 0E6382   |||||
										
			00 = +100% damage
			01 = +50% damage
			02 = Tier bonus (Bloodlust, Stoneskin, etc.)
			03 = Static bonus (+2)
			04 = Always expert (Fortune)
			05 = Tier bonus (Slayer)
			06 = Scaling bonus


There are two level-dependent spell bonuses: one used by the Bloodlust, Stoneskin, Haste,
Precision, and Weakness spells (type 2), and the other by Slayer (type 5). Both receive a
static bonus based on the target unit's level as specified at the following addresses:

		      TYPE 2			      TYPE 5
		      ------			      ------
		Tier 1 - 23EAA8 (03)		Tier 1 - 23EAC4 (04)
		Tier 2 - 23EAAC (03)		Tier 2 - 23EAC8 (03)
		Tier 3 - 23EAB0 (02)		Tier 3 - 23EACC (02)
		Tier 4 - 23EAB4 (02)		Tier 4 - 23EAD0 (01)
		Tier 5 - 23EAB8 (01)		Tier 5 - 23EAD4 (00)
		Tier 6 - 23EABC (01)		Tier 6 - 23EAD8 (00)
		Tier 7 - 23EAC0 (00)		Tier 7 - 23EADC (00)

The +2 static bonus is used exclusively by Disrupting Ray and can be modified at 0E62E6.

The bonus for Fortune simply sets the spell to expert-level effect regardless of skill.

The scaling spell bonus uses the same formula as the scaling unit bonus: the effect is
based on the level of the target unit as well as the hero's level. While this can be a
problematic approach to unit bonuses, there is arguably some merit in applying it to
certain spells. The formula for the scaling spell bonus is as follows:

		Bonus = (Spell * 0.03 * Hero Level / (Unit Level + 1))

The multiplier of 0.03 is a DWORD pointer located at 0E631F (08 AC 63 00) which can be
modified if desired, but what this formula really needs is a total rewrite since making
spells more effective on weaker units instead of stronger ones is kind of the opposite of
what one would reasonably expect from a specialty bonus. As we saw with skill specialties
earlier, percentage-based bonuses in general tend to be problematic since any gain which
doesn't bring you up to the next full integer is effectively useless; I thus decided to
simplify this formula to a bonus of (hero level * target unit's level).

	----------	---------------------------------------------------------
	0E62FD~309	; NEW SCALING SPELL BONUS
	----------	---------------------------------------------------------
	0F BF 41 55	movsx eax,[ecx+55]  ; EAX = hero level
	8B 4D 0C	mov ecx,[ebp+0C]    ; ECX = unit's level (0~6)
	41		inc ecx		    ; ECX +1
	0F AF C1	imul eax,ecx	    ; EAX (damage bonus) * ECX
	EB 29		jmp 4E6333	    ; -> (0E630A~32 is free space)


Observant readers may have noticed that the Hypnotize spell is not shown on the above table despite two
heroes in the game specializing in it. What's happening here is that before we get that table, we check
if the spell is within range. If it's not, then we exit to the "default" routine, which in this case is
the scaling bonus. Thus, you can assign a scaling spell specialty to a hero for any spell, regardless of
whether or not it's on the table above, just by editing the hero specialty data.

But what if you want to assign a different kind of specialty to a spell that's off the table, such as
changing the Hypnotize specialty to +50% effectiveness? To do this, we must expand the table, which is
thankfully possible due to the 13 bytes of free space at the end of it - the 90's you see there are the
assembly code for NOP, or "no operation". The code determines if a spell is within the table's range by
taking the spell ID, subtracting the ID of the first spell on the table, and comparing the result to the
length of the table. Any spell ID not on the table will always produce a value greater than the table's
length since the subtraction opcode is a "signed" value, meaning that if we return a result of less than
zero (for any spell that comes before the first one on the table), it wraps around into negative numbers
starting with FF for -01, then FE for -02, FD for -03, and so on.

Thus, to expand the table to include Hypnotize, we need only change the 2A at 0E6296 to 2F. Then, we go
to 0E6383~7 and change the 90's to whatever we want. The first four correspond to Frenzy, Titan's Bolt,
Counterstrike, and Berserk, respectively, and should just be set to the default value of 06 unless you
plan on giving them new bonuses, as well. 0E6387, then, would be the address for the Hypnotize bonus.

-----------------------------------------------------------------------------------------

Another learning point here is how to find the exit pointers on a jump table - in other words, where we
go to depending on what value we find when we look up the spell/unit/whatever that's on the table. If we
look right before this table in the code, we will find 7 DWORD pointers (starting at 0E633C) that direct
us where to go for spell bonuses of 0, 1, 2, 3, 4, 5, and 6, respectively.

Say, for example, that we want to repurpose the Fortune bonus as a secondary static bonus (i.e. type 3).
The fifth DWORD pointer in the list - the exit for the Fortune bonus - is CA 62 4E 00. Remembering that
DWORD pointers are written backwards and runtime will offset all addresses by 400000, this points us to
0E62CA, where we find the code for the Fortune bonus. Looking at the other exits, we see that the next
highest one is actually 00: DB 62 4E 00 (0E62DB). We can thus conclude that the Fortune bonus code ends
just before this, which is confirmed by the C2 OC 00 (Return opcode) at 0E62D8.

Now, we need to get the code for a static bonus by following the fourth exit pointer to 0E62E5:

			    B8 02 00 00 00 5E 8B E5 5D C2 0C 00

This code is substantially shorter than the Fortune bonus code, which is good because it means we won't
need to use any extra space for this change. Copy this hex string over to the Fortune bonus routine at
0E62CA, replacing the second byte (02) with the desired value for the new static bonus. Finally, replace
the remainder of the old Fortune bonus code with 90's like so:

		0E62CA: B8 XX 00 00 00 5E 8B E5 5D C2 0C 00 90 90 90 90 90

Whether or not an edit like this ends up being an easy copy/paste job depends largely on the presence of
certain instructions, namely calls or jumps to data outside of the block we're working with. Neither are
present here, and so an easy job it be. While NOPing the rest of the old (and now partially-overwritten)
code is not strictly necessary, it's a good habit to get into. All coding examples in this document that
leave free space will indicate as much in the comments; NOPing that space out is strongly suggested.

---------------------------------------------------------------------------------------------------------

### VIEW EARTH/AIR, VISIONS, & DISGUISE

The effects at unskilled/basic, advanced, and expert levels can be changed at:

1FC3C5 = 70 (Artifacts, Unskilled)	1FC3E7 = E1 (Resources, Unskilled)
1FC3BE = 98 (Heroes, Advanced)		1FC3E0 = D0 (Mines, Advanced)
1FC3B7 = 7C (Towns, Expert)		1FC3D9 = E0 (Entire Map, Expert)

The above thresholds can be lowered from advanced/expert to basic/advanced by changing
1FC3A6 to 01 and 1FC3AA to 7D (View Air), then 1FC3D1 to 01/1FC3D5 to 7C (View Earth).

As for Visions, the required skill levels to view detailed information about heroes and
towns are set at 016635 and 016DEC, respectively. If you lower the requirement for towns,
you'll also need to change 016DED from 74 to 7D. Finally, we can remove the restriction
on its effective distance by setting 0E6080~4 to B0 01 C2 0400 (freeing up 0E6085~19F).

As for new expert-level effects, let's look into making them free to cast.

The game specifies a minimum SP cost of 1 for any spell at 0E5593, which prevents the
ability of Mages/Archmagi from making a spell free. To make the game respect a 0 SP cost
for adventure map spells, change 0E554B to 4A and then go to 0E558F and change 5F 7D 05
BE 01 00 00 00 to 7D 05 BE 01 00 00 00 5F. The first edit extends a conditional jump for
adventure map spells to bypass this check while the second moves a necessary instruction
(5F) to after the check so that adventure map spells won't miss it.

Additionally or alternatively, we can combine the effects of View Air and Earth into just
one spell (View Air) since having them separate is kind of dumb. The below code will show
all loose resources and artifacts on the map with no skill, all mines at basic level, all
heroes and towns at advanced level, and the entire map at expert. Again, these thresholds
can be modified by changing the addresses like we did above, and we can remove any effect
entirely by NOP'ing out the instruction (replace it with 90's).

    ---------	-------------------------------------------------------------------------
    1FC39C~D4	; MERGE VIEW AIR & EARTH SPELLS (INTO JUST VIEW AIR)
    ---------	-------------------------------------------------------------------------
    75 50		jne 5FC3EC		; If not View Air -> [exit]
    8B 45 0C	mov eax,[ebp+0C]	; EAX = skill level
    85 C0		test eax,eax		; unskilled?
    74 22		je 5FC3C5		; if yes -> show artifacts

    48		dec eax			; basic?
    74 11		je 5FC3B7		; if yes -> show mines

    48		dec eax			; advanced?
    74 07		je 5FC3A9		; if yes -> show towns

    C605E0AC6A0001	mov [6AACE0],01		; show whole map
    C6057CAC6A0001	mov [6AAC7C],01		; show towns
    C60598AC6A0001	mov [6AAC98],01		; show heroes
    C605D0AB6A0001	mov [6AABD0],01		; show mines
    C60570AC6A0001	mov [6AAC70],01		; show artifacts
    C605E1AB6A0001	mov [6AABE1],01		; show resources
    EB 17		jmp 5FC3EC		; continue (1FC3D5~EB is free space)

    1FC36C > F8 05	; Only check for spell 05 (View Air) when loading map

This does leave us with an empty spell - two if you count Disguise, which may as well be
blank. Let's look at using the Disguise code (trashing the spell in the process) in order
to convert View Earth into a "lite" version of Town Portal that warps the caster to their
kingdom's capital city (i.e. whichever city has the Capitol built). For best effect, it
should belong to a different school of magic than Town Portal - I've chosen Air Magic in
the example below. At unskilled level, it will require and consume the caster's maximum
movement points; at expert level, it will have no movement point cost at all.

    ---------	-------------------------------------------------------------------------
    01C74A~7D	; VIEW EARTH -> RECALL (NEW SPELL)
    ---------	-------------------------------------------------------------------------
    E9 172D1100	jmp 52F466		; -> free space (Disguise)
    29 4E 4D	sub [esi+4D],ecx	; subtract movement cost
    80 6E 18 0C	sub byte [esi+18],0C	; subtract spell cost
    8B 40 04	mov eax,[eax+04]	; EAX = capitol coordinates (ZZYYXX--)
    88 E0		mov al,ah		; EAX = ZZYY00XX
    B4 00		mov ah,00		; ""
    6A 01		push 01			; ???
    6A 00		push 00			; ???
    68 F0826800	push 6882F0		; "telepout.vav"
    50		push eax		; push EAX
    80 7C 24 03 00	cmp byte [esp+03],00	; is capitol above ground?
    74 05		je 41C773		; if yes -> push ESI
    C6 44 24 03 04	mov byte [esp+03],04	; ZZ coordinate: 01 -> 04
    56		push esi		; ???
    8B CB		mov ecx,ebx		; ECX = ???
    E8 35130000	call 41DAB0		; teleport routine
    53		push ebx		; (needed to resolve stack)
    90 90		nop			; -

    ----------	-------------------------------------------------------------------------
    12F45B~516	; EXPANDED SPACE (OVERWRITES DISGUISE)
    ----------	-------------------------------------------------------------------------
    83 CA FF	or edx,-01		; frees space: 12F466~57D
    89 55 E8	mov [ebp-18],edx	; ""
    E9 18010000	jmp 52F57E		; ""

    F6860701000004	test byte [esi+107],04	; is hero on a boat?
    0F85 23E2EEFF	jne 41D696		; if yes -> [fail, on a boat]

    8B 4E 49	mov ecx,[esi+49]	; ECX = maximum movement
    83 FF 00	cmp edi,00		; Unskilled?
    74 10		je 52F48B		; if yes -> 100% movement cost
    D1 F9		sar ecx,1		; ECX / 2

    83 FF 01	cmp edi,01		; Basic?
    74 09		je 52F48B		; if yes -> 50% movement cost
    D1 F9		sar ecx,1		; ECX / 2

    83 FF 02	cmp edi,02		; Advanced?
    74 02		je 52F48B		; if yes -> 25% movement cost
    31 C9		xor ecx,ecx		; ECX = 0 (Expert = no movement cost)

    3B 4E 4D	cmp ecx,[esi+4D]	; do we have enough movement left to Recall?
    0F87 DEE0EEFF	ja 41D572		; if no -> [fail, too tired]

    51		push ecx		 ; store ECX
    56		push esi		 ; store ESI
    53		push ebx		 ; store EBX
    31 FF		xor edi,edi		 ; EDI = 0
    8A 56 22	mov dl,[esi+22]		 ; EDX = hero's owner
    6B D2 2D	imul edx,2D		 ; EDX = data range
    8B 35 38956900	mov esi,[699538]	 ; ESI = main index
    8D9CD6D00A0200	lea ebx,[esi+edx*8+20AD0]; EBX = player data
    8A84D60E0B0200	mov al,[esi+edx*8+20B0E] ; EAX = number of towns owned by player
    84 C0		test al,al		 ; does player have any towns?
    74 5B		je 52F512		 ; if no -> [fail, no destination]

    57		push edi		; store number of towns checked (starts at 0)
    50		push eax		; store number towns owned by player
    8A 44 3B 40	mov al,[ebx+edi+40]	; EAX = town ID owned by player
    3C FF		cmp al,-01		; is this a blank slot? (~~~this may not be needed)
    75 04		jne 52F4C5		; if no -> EAX = data range
    31 C0		xor eax,eax		; EAX = 0
    EB 12		jmp 52F4D7		; -> is capitol built?

    6B C0 2D	imul eax,2D		; EAX = data range
    8B 35 38956900	mov esi,[699538]	; ESI = main index
    8B 8E 14160200	mov ecx,[esi+21614]	; ECX = town index
    8D 04 C1	lea eax,[ecx+eax*8]	; EAX = town data

    8B 90 58010000	mov edx,[eax+158]	; is capitol built?
    8B 88 5C010000	mov ecx,[eax+15C]	; ""
    8B 3D 00CE6600	mov edi,[66CE00]	; ""
    8B 35 04CE6600	mov esi,[66CE04]	; ""
    21 FA		and edx,edi		; ""
    21 F1		and ecx,esi		; ""
    09 CA		or edx,ecx		; ""
    74 14		je 52F50B		; if no -> EAX = number towns owned by player

    5F		pop edi			; remove towns checked/owned from the stack
    5F		pop edi			; ""
    83 78 10 FF	cmp [eax+10],-01	; is capitol unoccupied?
    0F85 48E4EEFF	jne 41D94B		; if no -> [fail, destination occupied]

    5B		pop ebx			; retrieve EBX
    5E		pop esi			; retrieve ESI
    59		pop ecx			; retrieve ECX
    E9 44D2EEFF	jmp 41C74F		; return

    58		pop eax			; EAX = number towns owned by player
    5F 		pop edi			; EDI = number of towns checked
    47 		inc edi			; EDI + 1
    39 C7		cmp edi,eax		; have we checked every town this player owns?
    7C A5		jl 5AF4B7		; if no -> store number of towns checked
    E9 26E1EEFF	jmp 41D63D		; -> [fail, no destination] (12F517~7D is free)

---------------

### TOWN PORTAL

The skill level required to select your destination is specified at 01D6D4.

The movement cost for all skill levels below expert is loaded into EAX at 01D51F; this is
then copied into the stack addresses for no, basic, and advanced skill. A different value
(specified at 01D534) is then copied for expert skill. If you want to have no skill cost
more instead of expert costing less, swap the values at 01D52A and 01D533.

Alternatively, we can rewrite the code to make the movement cost a percentage of the
caster's maximum movement rather than a static value like we did with Recall above:

    ---------	-------------------------------------------------------------------------
    01D51E~37	; TOWN PORTAL MOVEMENT COST TO A PERCENTAGE OF THE CASTER'S MAXIMUM
    ---------	-------------------------------------------------------------------------
    8B 46 49	mov eax,[esi+49]	; EAX = caster's maximum movement
    89 45 C0	mov [ebp-40],eax	; Unskilled
    89 45 C4	mov [ebp-3C],eax	; Basic
    D1 F8		sar eax,1		; EAX / 2 (50%)
    89 45 C8	mov [ebp-38],eax	; Advanced
    D1 F8		sar eax,1		; EAX / 2 (25%)
    89 45 CC	mov [ebp-34],eax	; Expert
    56		push esi		; (displaced code)
    57		push edi		; ""
    83 FA FF	cmp edx,-01		; ""
    90 90		nop			; -

The above code assumes you've set basic skill as the requirement to select a destination,
thus providing a benefit for each skill level. This can easily be changed, however, just
by changing the order of the commands as desired. The only drawback is that, due to the
simplicity of the commands being used, the reductions are hard-coded to 50% and 25%.

-----------------------------------------------------------------------------------------

### DIMENSION DOOR

Although effectively identical to Town Portal, the movement cost for Dimension Door is
coded completely differently for some reason. The threshold for movement cost reduction
(03 = expert) is specified at 01D415. The cost at or above this level is specified at
01D41F and the (one byte) value at 01D41C will be added for any skill level below it.

Rather than relying on an arbitrary cap on how many times per day this spell can be cast,
we can enforce it via the same method we used above: make the movement cost a percentage
of the caster's maximum. This will require us to use more of the Disguise free space:

    --------	-------------------------------------------------------------------------
    01D264~A	; DIMENSION DOOR MOVEMENT COST TO A PERCENTAGE OF THE CASTER'S MAXIMUM
    --------	-------------------------------------------------------------------------
    E8 B1221100	call 52F51A		; -> free space (Disguise)
    7D 3F		jge 41D2AA		; if we have enough movement -> [continue]

    ---------	-------------------------------------------------------------------------
    01D40D~16	; ""
    ---------	-------------------------------------------------------------------------
    E8 08211100	call 52F51A		; -> free space (Disguise)
    29 46 4D	sub [esi+4D],eax	; subtract cost from remaining movement
    EB 1A		jmp 41D431		; -> [continue]

    ---------	-------------------------------------------------------------------------
    12F517~3E	; EXPANDED SPACE (OVERWRITES DISGUISE)
    ---------	-------------------------------------------------------------------------
    51		push ecx		; Store ECX
    8B 4D 08	mov ecx,[ebp+08]	; ECX = skill level
    8B 46 49	mov eax,[esi+49]	; EAX = maximum movement

    83 F9 00	cmp ecx,00		; Unskilled?
    74 17		je 52F53A		; if yes -> retrieve ECX

    D1 F8		sar eax,1		; EAX / 2 (50% of maximum)
    83 F9 01	cmp ecx,01		; Basic?
    74 10		je 52F53A		; if yes -> retrieve ECX

    D1 F8		sar eax,1		; EAX / 2 (25% of maximum)
    83 F9 03	cmp ecx,03		; Master?
    74 09		je 52F53A		; if yes -> retrieve ECX

    6B C0 56	imul eax,eax,56		; EAX = 33% of maximum
    C1 F8 09	sar eax,09		; ""
    6B C0 08	imul eax,eax,08		; ""
    59		pop ecx			; retrieve ECX
    39 46 4D	cmp [esi+4D],eax	; do we have enough movement left to Teleport?
    C3		ret			; return (12F53F~7D is free space)

-----------------------------------------------------------------------------------------

### CURE & DISPEL

A bug with the Cure spell is that, while it will remove the Hypnotize status from allied
units, it can't do so at expert level (or whatever your mass effect threshold is set to)
since they're considered to be hostile units at that point and therefore will be ignored
by the mass targeting code. My suggested fix is to disallow Cure from removing the effect
at any level (0462B6: 3C > 3D) and leave the task of removing it to Dispel.

Dispel is a problematic spell due to the fact that it primarily targets friendly units
rather than opponents and so there's no way to dispel enemy buffs without also removing
your own (bearing in mind that the Cure spell effectively serves the function of Dispel
removing negative statuses from your own troops). Changing this is a complicated matter
since Dispel has its own special targeting code that doesn't respect the targeting flags
discussed above. We can make Dispel only target enemy units with the following edits:

    ---------	-------------------------------------------------------------------------
    1A8477~89	; DISPEL TO NORMAL TARGETING (MASS EFFECT AT EXPERT)
    ---------	-------------------------------------------------------------------------
    8B 55 0C	mov edx,[ebp+0C]	; EDX = caster's team (0/1)
    8B 8F F4000000	mov ecx,[edi+F4]	; ECX = unit's team
    39 D1		cmp ecx,edx		; does unit belong to caster?
    0F85 B9000000	jne 5A8541		; if no -> [valid target]
    EB 69		jmp 5A84F3		; -> [invalid target] (1A848A~F2 is free space)

Whenever Dispel mass targets, it also removes any magical obstacles from the battlefield
such as quicksand or land mines (including those used as moats for Tower towns). We can
remove this effect by setting 1A1A0B~F to E9 58090000 (this will free space: 1A1A10~8D).

This does leave us with the problem that Dispel no longer offers any other benefits for
higher skill in Water Magic. Cure is arguably in the same boat due to the fact that it's
useful almost entirely due to the fact that it removes status effects - which it can do
at any level of skill - rather than its ability to restore lost health. My answer to both
of these problems is the separation of statuses into three types just as we did earlier
with the First Aid skill. Unskilled Cure will only remove physical statuses while Dispel
with no Water Magic will remove every status EXCEPT physical ones, which are notably all
negative statuses. At higher levels of skill, Dispel will ignore other negative statuses
on enemy units and instead only remove the positvie ones.

    ---------	-------------------------------------------------------------------------
    046279~DE	; CURE TO REMOVE STATUSES BASED ON WATER MAGIC SKILL
    ---------	-------------------------------------------------------------------------
    8B 00		mov eax,[eax]		; (rearranged code)
    89 46 58	mov [esi+58],eax	; ""
    57		push edi		; ""
    80 7D 08 02	cmp byte [ebp+08],02	; Advanced?
    7C 34		jl 4462B7		; if less -> physical statuses only
    80 7D 08 03	cmp byte [ebp+08],03	; Expert?
    7C 17		jl 4462A1		; if less -> mental statuses

    31 FF		xor edi,edi		; EDI = 0 (remove magic statuses)
    0FBE87D2624400	movsx eax,[edi+4462D2]	; EAX = status to remove
    50		push eax		; remove status
    8B CE		mov ecx,esi		; ""
    E8 94DFFFFF	call 444230		; ""
    47		inc edi			; EDI + 1
    83 FF 04	cmp edi,04		; have we cleared every magical status?
    7C EB		jl 44628D		; if no  -> EAX = status to remove

    31 FF		xor edi,edi		; EDI = 0 (remove mental statuses)
    0FBE87D6624400	movsx eax,[edi+4462D6]	; EAX = status to remove
    50		push eax		; remove status
    8B CE		mov ecx,esi		; ""
    E8 7DDFFFFF	call 444230		; ""
    47		inc edi			; EDI + 1
    83 FF 04	cmp edi,04		; have we cleared every mental status?
    7C EB		jl 4462A3		; if no  -> EAX = status to remove

    31 FF		xor edi,edi		; EDI = 0 (remove physical statuses)
    0FBE87DA624400	movsx eax,[edi+4462DA]	; EAX = status to remove
    50		push eax		; remove status
    8B CE		mov ecx,esi		; ""
    E8 66DFFFFF	call 444230		; ""
    47		inc edi			; EDI + 1
    83 FF 05	cmp edi,05		; have we cleared every physical status?
    7C EB		jl 4462B9		; if no  -> EAX = status to remove
    EB 2B		jmp 4462FD		; -> [continue]

    2A 2D 34 36	; magic statuses (Curse, Weakness, Misfortune, Slow)
    32 3B 3D 3E	; mental statuses (Sorrow, Berserk, Forgetfulness, Blind)
    46 47 49 4A 4B	; physical statuses (Petrify, Poison, Disease, Paralyze, Aging)

    ------		-------------------------------------------------------------------------
    1A18F7		; DISPEL TO IGNORE DEBUFFS BASED ON WATER MAGIC SKILL
    ------		-------------------------------------------------------------------------
    E8 8E6B0000	call 5A848A		; -> free space (Dispel targeting)

    ------		-------------------------------------------------------------------------
    1A1985		; ""
    ------		-------------------------------------------------------------------------
    E8 006B0000	call 5A848A		; -> free space (Dispel targeting)

    ---------	-------------------------------------------------------------------------
    1A848A-B5	; (INLINE EDIT - OVERWRITES DISPEL TARGETING)
    ---------	-------------------------------------------------------------------------
    80 7D BC 02	cmp byte [ebp-44],02	; Advanced?
    7C 25		jl 5A84B5		; if less -> return
    80 7D BC 03	cmp byte [ebp-44],03	; Expert?
    7C 0F		jl 5A84A5		; if less -> skip mental statuses (Sorrow?)

    83 FF 2A	cmp edi,2A		; Curse?
    74 19		je 5A84B4		; if yes -> skip
    83 FF 2D 	cmp edi,2D		; Weakness?
    74 14		je 5A84B4		; if yes -> skip
    83 FF 36	cmp edi,36		; Slow?
    74 0F		je 5A84B4		; if yes -> skip

    83 FF 32	cmp edi,32		; Sorrow?
    74 0A		je 5A84B4		; if yes -> skip
    83 FF 3B	cmp edi,3B		; Berserk?
    74 05		je 5A84B4		; if yes -> skip
    83 FF 3E	cmp edi,3E		; Blind?
    75 01		jne 5A84B5		; if no -> return
    47		inc edi			; skip this status
    C3		ret			; return

    1A1907 > 3E	; stop removing statuses at Blind (always skip physical statuses)
    1A1995 > 3E	; ""

-----------------------------------------------------------------------------------------

### BLESS/CURSE

Due to how the game's damage formula works, Bless and Curse are just as effective or, in
most cases, objectively better than the supposedly more powerful Bloodlust/Precision and
Weakness spells. The problem is that it completely eliminates rather than simply reducing
a unit's damage variance. The below code will make these effects lower damage variance by
either increasing minimum or reducing maximum damage by a magnitude of 12.5%, 25%, or 50%
of a unit's range (maximum damage - minimum). Effectiveness is determined by the spell's
"power" setting in SpTraits.txt (previously used for bonus damage at higher expertise);
the above percentages coorespond to power settings of 1, 2, and 3, respectively.

A critical detail is that the new code sets a minimum increase or decrease of 1 per unit
in the stack. This is the difference between the minimum damage of a stack of 100 Pikemen
being raised from 100 to 200 and from 100 to 112 at zero expertise. This means that Bless
and Curse, which are low-level spells, remain effective on lower-level units as they were
presumably intended to while higher-level units benefit more from higher-level spells.

The code also allows for both Bless and Curse specialists by doubling the spell's effects
to 25%, 50%, and the original effect of 100% (no variance). For this to work as intended,
both spells must be set to "00" in the specialty table (+100% damage). Also note that the
code assumes that the global mass effect threshold has been lowered from expert to basic
level and thus applies the same effects to both basic and unskilled Bless/Curse; this can
be changed if desired by adjusting the power comparison values from 6/3/2 to 3/2/1.

    ---------	-------------------------------------------------------------------------
    042F64~B2	; NEW BLESS/CURSE CODE
    ---------	-------------------------------------------------------------------------
    8B 81 3C020000	mov eax,[ecx+23C]	; EAX = Bless flag
    85 C0		test eax,eax		; blessed?
    74 0A		je 442F78		; if no -> (EAX = Curse)
    6A 01		push 01			; push temp flag (01 = Bless)
    8B 81 58040000	mov eax,[ecx+458]	; EAX = Bless power
    EB 12		jmp 442F8A		; -> Max Damage * # of Units

    8B 81 40020000	mov eax,[ecx+240]	; EAX = Curse flag
    85 C0		test eax,eax		; cursed?
    74 37		je 442FB9		; if no -> [exit]
    6A 00		push 00			; push temp flag (00 = Curse)
    8B 81 5C040000	mov eax,[ecx+45C]	; EAX = Curse power

    0FAF DA		imul ebx,edx		; Maximum damage (EBX) * # of units (EDX)
    0FAF F2		imul esi,edx		; Minimum damage (ESI) * # of units (EDX)
    53		push ebx		; push maximum damage
    29 F3		sub ebx,esi		; EBX = damage range
    E8 13F5FFFF	call 4424AB		; -> free space (old Bless/Curse AI code)

    5A		pop edx			; EDX = Maximum damage
    8B CE		mov ecx,esi		; ECX = Minimum damage
    58		pop eax			; EAX = 1 (Bless) or 0 (Curse)

    85 C0		test eax,eax		; Bless?
    74 04		je 442FA4		; if no -> subtract EBX from EDX
    01 D9		add ecx,ebx		; add EBX to ECX
    EB 02		jmp 442FA6		; -> (displaced code)
    29 DA		sub edx,ebx		; subtract EBX from EDX

    5F		pop edi			; (displaced code)
    5E		pop esi			; ""
    5B		pop ebx			; ""
    51		push ecx		; store ECX
    52		push edx		; store EDX
    E8 10980C00	call 50C7C0		; (EAX = min~max)
    5A		pop edx			; retrieve EDX
    59		pop ecx			; retrieve ECX
    90		nop			; -

    ---------	-------------------------------------------------------------------------
    0424A9~C6	; (INLINE EDIT - OVERWRITES OLD BLESS/CURSE AI CODE)
    ---------	-------------------------------------------------------------------------
    EB 4F		jmp 4424FA		; frees space: 0424AB~F9

    83 F8 06	cmp eax,06		; Expert specialist?
    7D 16		jge 4424C6		; if yes -> return
    D1 EB		shr ebx,1		; EBX/2

    83 F8 03	cmp eax,03		; Expert or Advanced specialist?
    7D 09		jge 4424C0		; if yes -> return
    D1 EB		shr ebx,1		; EBX/2 (total: 1/4)

    83 F8 02	cmp eax,02		; Advanced or Basic specialist?
    7D 02		jge 4424C0		; if yes -> return
    D1 EB		shr ebx,1		; EBX/2 (total: 1/8)

    39 D3		cmp ebx,edx		; compare damage range (EBX) to # of units (EDX)
    7F 02		jg 4424C6		; if higher -> return
    8B DA		mov ebx,edx		; EBX = EDX (minimum effect of +/-1 per unit)
    C3		ret			; return (0424C7~F9 is free space)

    ---------	-------------------------------------------------------------------------
    09301D~21	; NEW BLESS/CURSE CODE (CONT.)
    ---------	-------------------------------------------------------------------------
    8B DA		mov ebx,edx		; EBX = Maximum damage
    8B F9		mov edi,ecx		; EDI = Minimum damage

    ---------	-------------------------------------------------------------------------
    044809~30	; APPLY NEW BLESS & CURSE SPECIALTY BONUSES
    ---------	-------------------------------------------------------------------------
    E8 B9DCFFFF	call 4424C7		; -> free space (old AI routine)
    6A 2A		push 2A			; (optimized code)
    E8 1BFAFFFF	call 444230		; ""
    89 BE 58040000	mov [esi+458],edi	; ""
    EB E7		jmp 444804		; ""
    E8 A5DCFFFF	call 4424C7		; -> free space (old AI routine)
    6A 29		push 29			; (optimized code)
    E8 07FAFFFF	call 444230		; ""
    89 BE 5C040000	mov [esi+45C],edi	; ""
    EB D3		jmp 444804		' ""

    ---------	-------------------------------------------------------------------------
    0424C7~D9	; (INLINE EDIT - OVERWRITES OLD BLESS/CURSE AI CODE)
    ---------	-------------------------------------------------------------------------
    8B 4D 14	mov ecx,[ebp+14]	; ECX = hero
    8B 55 08	mov edx,[ebp+08]	; EDX = spell ID
    57		push edi		; push spell power (EDI)
    57		push edi		; (unit level/unused)
    52		push edx		; push spell ID
    E8 8B3D0A00	call 4E6260		; spell specialty routine
    01 C7		add edi,eax		; add specialty bonus (EAX) to spell power
    8B CE		mov ecx,esi		; (displaced code)
    C3		ret 			; return (0424DA~F9 is free space)

    043488 > EB	; skip old Bless/Curse specialty routine (04348A~9C is free space)

>(IMPORTANT: Bless will need to be removed from Enchanters; see later for how to do so)

-----------------------------------------------------------------------------------------

### FRENZY, BLIND, & COUNTERSTRIKE

There are many things we need to look at here. The first is that Frenzy adds the target
unit's Defense stat to its Attack rather than just, say, doubling its Attack. To change
it to use the unit's Attack as a base instead, change 04223A from 45 to 5D. It should be
noted, however, that double Attack does not equal double DAMAGE, which we'll look into
doing a little further below when addressing the issues with Counterstrike.

Next is the drawback of it setting the unit's defense to zero, which is (probably) why
its duration is hard-coded to one turn. Rather than increasing Frenzy's effect for each
level of expertise, I instead opted to have basic Fire Magic remove the defense penalty
while further advancement increases the duration with the magnitude remaining static.

To set this up, we first need to go to SpTraits.txt and set the power of unskilled Frenzy
to 0 and then 1 for basic, advanced, and expert skill; this is how we'll know whether or
not to zero out our defense. The actual attack bonus begins at 042239 and, if you wish to
simply double the target unit's attack, can be simplified to 01 C0 EB 26 (this will free
space: 04223D~62). Alternatively, you can replace it with 2x damage as seen further down.

    --------	-------------------------------------------------------------------------
    0422C7~A	; FRENZY TO NO DEFENSE PENALTY AT BASIC FIRE MAGIC
    --------	-------------------------------------------------------------------------
    EB DC		jmp 4422A5		; -> free space (unused in original game)

    --------	-------------------------------------------------------------------------
    0422A5~F	; (EXPANDED SPACE - UNUSED IN ORIGINAL GAME)
    --------	-------------------------------------------------------------------------
    80BF9804000000	cmp byte [edi+498],00	; Frenzy power (from SpTraits.txt) = 0?
    74 1B		je 4422C9		; if yes -> [Defense = 0]
    EB 1E		jmp 4422CE		; -> [Defense unaffected]

    ---------	-------------------------------------------------------------------------
    04463B~58	; FRENZY TO INCREASE DURATION AT ADVANCED & EXPERT LEVEL
    ---------	-------------------------------------------------------------------------
    8B 45 10	mov eax,[ebp+10]	; EAX = skill level (this will be the duration)
    85 C0		test eax,eax		; is skill level 0?
    75 06		jne 444648		; if no -> ECX = unit data
    40		inc eax			; EAX = 1
    EB 03		jmp 444648		; -> ECX = unit data

    8B 45 0C	mov eax,[ebp+0C]	; EAX = duration (*all other spells, see below)
    8B 8E 84000000	mov ecx,[esi+84]	; ECX = unit data
    C1 E9 1A	shr ecx,1A		; shift to "has moved" flag
    F6 C1 01	test cl,01		; has unit already moved this turn?
    74 28		je 44467E		; if no -> [continue]
    40		inc eax			; ECX + 1 (will decrease at start of next round)
    EB 25		jmp 44467E		; -> [continue]

Of particular note in the above code is that we check to see if the target stack has
moved this turn and, if so, increase the spell's duration by 1. This is because status
durations are decremented and the status removed if the duration is zero at the start of
each combat round, and so casting a spell on a unit that has already moved effectively
wastes a turn. Frenzy was the only spell in the original game that made this check since
it was hard-coded to only last a single turn, but there's a lot of sense in applying it
globally. The above code allows us to do this with the following additional edits:

		ALL DURATION SPELLS TO CHECK IF TARGET STACK HAS MOVED
		------------------------------------------------------
				044624 > 20
				0450EF > 1
				0450F0 > 1
				0450D4 > 45

Blind has the oppposite problem from Frenzy: rather than being underpowered for having a
static duration, it's greatly overpowered due to being a completely disabling spell that
lasts longer depending on the caster's magic power. We can apply the same rules to it as
we did with Frenzy above: 1 round at unskilled and basic levels (assuming the difference
between them is no retaliation), 2 at advanced, and 3 at expert by setting 0450E7 to 01.

As for Counterstrike, rather than increasing the number of retaliations for each skill
level, let's look into having it set infinite retaliations at any skill level along with
a damage boost to retaliations that increases with skill. We'll specify the total damage
per level in 25% increments in SpTraits.txt, so 5 = 125% damage, 6 = 150% damage, and so
on. I'd recommend unsetting Counterstrike as a mass effect spell if you go this route for
hopefully obvious reasons. The free space that we'll be using for this will be Frenzy's
original attack bonus code and will include the change for it to instead deal 2x damage.

    ---------	-------------------------------------------------------------------------
    041B5D~61	; SET RETALIATION FLAG FOR COUNTERSTRIKE
    ---------	-------------------------------------------------------------------------
    E8 C2060000	call 442224		; -> free space (original Frenzy bonus)

    041B4D > 90 90	; NOP out pushes to be moved to free space

    --------	-------------------------------------------------------------------------
    041733~8	; DAMAGE BONUSES FOR COUNTERSTRIKE RETALIATIONS & FRENZY
    --------	-------------------------------------------------------------------------
    E8 FB0A0000	call 442233		; -> free space (original Frenzy attack bonus)
    50		push eax		; (displaced code)

    ---------	-------------------------------------------------------------------------
    042221~60	; EXPANDED SPACE (OVERWRITES ORIGINAL FRENZY ATTACK BONUS)
    ---------	-------------------------------------------------------------------------
    5F		pop edi			; (displaced code)
    EB 3D		jmp 442261		; -> [no ATK bonus] (frees space: 042224~60)

    53		push ebx		; (displaced code)
    57		push edi		; ""
    80B65704000001	xor byte [esi+457],01	; toggle "temp" flag before calling damage routine
    E8 FEF0FFFF	call 441330		; damage routine (retaliation)
    C3 		ret			; return

    8A 8E 57040000	mov cl,[esi+457]	; CL = "temp" flag
    84 C9		test cl,cl		; is this a retaliation?
    74 10		je 44224D		; if no -> Frenzy?

    8B 8E 94040000	mov ecx,[esi+494]	; ECX = Counterstrike level
    85 C9		test ecx,ecx		; do we have counterstrike?
    74 06		je 44224D		; if no -> (displaced code)
    0FAF C1		imul eax,ecx		; damage * Counterstrike level
    C1 F8 02	sar eax,02		; damage / 2 (result: 125%/150%/175%/200%)

    8B 8E 78020000	mov ecx,[esi+278]	; ECX = Frenzy duration
    85 C9		test ecx,ecx		; do we have Frenzy?
    74 02		je 442259		; if no -> (displaced code)
    01 C0		add eax,eax		; Damage * 2

    8B CF		mov ecx,edi		; (displaced code)
    89 45 F0	mov [ebp-10],eax	; ""
    C3		ret			; return
    90 90		nop			; -

    --------	-------------------------------------------------------------------------
    093021~6	; FRENZY DOUBLES DAMAGE (STATUS BAR HOVER TEXT)
    --------	-------------------------------------------------------------------------
    E8 3316FBFF	call 444659		; -> free space (original Frenzy duration code)
    90		nop			; -

    ---------	-------------------------------------------------------------------------
    044659~71	; EXPANDED SPACE (OVERWRITES ORIGINAL DURATION CODE)
    ---------	-------------------------------------------------------------------------
    8B 4D 0C	mov ecx,[ebp+0C]	; ECX = (01 for ranged attack, 00 for melee)
    85 C9		test ecx,ecx		; ranged attack?
    75 0E		jne 44466E		; if yes -> (displaced code)

    8B 86 78020000	mov eax,[esi+278]	; EAX = Frenzy duration
    85 C0		test eax,eax		; is unit Frenzied?
    74 04		je 44465A		; if no -> (displaced code)

    01 DB		add ebx,ebx		; 2x damage
    01 FF		add edi,edi		; ""
    8B 45 10	mov eax,[ebp+10]	; (displaced code)
    C3		ret			; return (044672~A is free space)

    ---------	-------------------------------------------------------------------------
    041B78~92	; UNSET RETALIATION FLAG
    ---------	-------------------------------------------------------------------------
    FF 8E 54040000	dec [esi+454]		; (optimized code)
    31 C0		xor eax,eax		; ""
    8986C0040000	mov [esi+4C0],eax	; ""
    C6865704000000	mov byte [esi+457],00	; unset "temp" retaliation flag
    909090909090	nop			; -

    041AE3 > 97	; update jump pointer
    041AFB > 7F	; ""
    041B0C > 71	; ""
    041B16 > 67	; ""
    041B20 > 5D	; ""
    041B24 > 59	; ""

    ---------	-------------------------------------------------------------------------
    046EA4~B7	; COUNTERSTRIKE ALWAYS ALLOWS INFINITE RETALIATIONS
    ---------	-------------------------------------------------------------------------
    8B 86 94040000	mov eax,[esi+494]	; EAX = counterstrike level
    6B C0 69	imul eax,eax,69		; EAX * obscenely high number (nice)
    01 86 54040000	add [esi+454],eax	; add EAX to stack's retaliations
    90 90 90 90 90	nop			; -

    28737C > 15	; Counterstrike no longer mass effect at expert level

-----------------------------------------------------------------------------------------

### ANTI-MAGIC

To remove the effect of Anti-Magic clearing all negative status effects from the target
unit(s), set 0447C4 to EB 3E (this will free 0447C6~803). This change notwithstanding,
Anti-Magic is one of those spells that straddles the line between being overpowered and
useless due to the combination of its single-stack targeting and excessive duration at
higher magic levels. We can address this by setting it to the routine that we set up for
Frenzy earlier, where the duration is based on skill level and caps at three rounds.

You may also want to set Anti-Magic to mass effect at the standard level threshold now
that doing so will no longer make it ridiculously overpowered, but that brings us to an
important point. The Frenzy/Blind duration code that we set up earlier assumes that the
non-duration skill bonus comes at basic level rather than expert, meaning that this edit
will also assume that the standard mass effect threshold has been lowered from expert
level to basic. If it hasn't, the duration code may need to be edited to compensate.

    --------	-------------------------------------------------------------------------
    04461D~F	; ANTI-MAGIC TO SAME DURATION ROUTINE AS FRENZY
    --------	-------------------------------------------------------------------------
    EB 53		jmp 444672		; -> free space (Frenzy duration)
    90		nop			; -

    --------	-------------------------------------------------------------------------
    044672~A	; (EXPANDED SPACE - INLINE WITH FRENZY DURATION EDIT ABOVE)
    --------	-------------------------------------------------------------------------
    8D 43 D1	lea eax,[ebx-2F]	; (displaced code)
    3C F3		cmp al,-0D		; Anti-Magic?
    74 C2		je 44463B		; if yes -> [Frenzy duration routine]
    EB A5		jmp 444620		; return

    2866BC > 45	; Anti-Magic to mass effect at level threshold

-----------------------------------------------------------------------------------------

### BERSERK

The settings in SpTraits.txt have no effect on Berserk's effect radius, as seen below.

242274 = Unskilled
242278 = Basic
24227C = Advanced
242280 = Expert

Note that values larger than 2 will cause (harmless) GFX bugs with the targeting shadow.

By default, the AI is unable to cast Berserk. Changing 287404 from 85 to 15 (changing the
targeting code from "any tile" to "single stack") will allow them to with no ill effects.

-----------------------------------------------------------------------------------------

### PRAYER

To remove the speed bonus from this spell and make it just an Attack/Defense buff, go to
044956 and write E9 01 04 00 00 90 and then to 04440D and write E9 CF 00 00 00 90.

-----------------------------------------------------------------------------------------

### TELEPORT

The skill level required to cross moats is specified at 1A3AA5 and 1A3AB7 for walls.

-----------------------------------------------------------------------------------------

### FIRE WALL & FORCE FIELD

The static duration of 2 rounds is set at 1A0C19 (Fire Wall) and 1A0ADE (Force Field).

The required skill level for a larger fire/barrier is specified at 1A0B65 (Fire Wall)
and 1A0A86 (Force Field). However, I don't yet know how to edit the targeting shadow
for Fire Wall to follow suit with any changes. Note that Force Field lacks a targeting
shadow entirely due to a bug (which, again, I don't know how to fix).

-----------------------------------------------------------------------------------------

### QUICKSAND & LAND MINES

The quantity of each placed per skill level are specified at the following addresses:

	           QUICKSAND			      LAND MINES
	    -----------------------		-----------------------
	    242224 = 04 (Unskilled)		242234 = 04 (Unskilled)
	    242228 = 04 (Basic)			242238 = 04 (Basic)
	    24222C = 06 (Advanced)		24223C = 06 (Advanced)
	    242230 = 08 (Expert)		242240 = 08 (Expert)

-----------------------------------------------------------------------------------------

### DEATH RIPPLE & DESTROY UNDEAD

Death Ripple checks the "undead" flag for immunity instead of the "living" flag, causing
it to be effective on things that it arguably shouldn't be (i.e. Golems and elementals).
To fix this, change 04A372~6 from 00 00 04 00 75 to 10 00 00 00 74.

Unlike Death Ripple, Destroy Undead makes more sense as a single-target spell instead of
a battlefield nuke. One might assume that this change would be as simple as setting the
appropriate targeting flag (2861F4 > 11), but there's actually a bit more to it...

    ---------	-------------------------------------------------------------------------
    1A118E~F1	; DESTROY UNDEAD TO SINGLE TARGET DAMAGE
    ---------	-------------------------------------------------------------------------
    8B CB		mov ecx,ebx		; (mostly a copy/paste of Magic Arrow's routine)
    E8 EB8EECFF	call 46A080		; ""
    84 C0		test al,al		; ""
    0F85 33FBFFFF	jne 5A0CD0		; ""
    68 6C226400	push 64226C		; Disrupting Ray shot GFX
    68 70226400	push 642270		; ""
    6A 05		push 05			; (more copypasta)
    8B CF		mov ecx,edi		; ""
    E8 A051EAFF	call 446350		; ""
    50		push eax		; ""
    8B CF		mov ecx,edi		; ""
    E8 C851EAFF	call 446380		; ""
    8B 55 18	mov edx,[ebp+18]	; ""
    50		push eax		; ""
    8B 45 D0	mov eax,[ebp-30]	; ""
    52		push edx		; ""
    50 		push eax		; ""
    8B CB		mov ecx,ebx		; ""
    E8 C867ECFF	call 467990		; ""
    A1 A87F6800	mov eax,[687FA8]	; ""
    8B 55 C4	mov edx,[ebp-3C]	; ""
    6A 01		push 01			; ""
    57		push edi		; ""
    8B 88 780D0000	mov ecx,[eax+D78]	; load Destroy Undead data
    8BB4B07C0D0000	mov esi,[eax+esi*4+D7C]	; ""
    0FAF 4D 1C	imul ecx,[ebp+1C]	; (more copypasta)
    8B 45 EC	mov eax,[ebp-14]	; ""
    01 CE		add esi,ecx		; ""
    52		push edx		; ""
    50		push eax		; ""
    6A 19		push 19			; 19 = Destroy Undead
    E9 03FBFFFF	jmp 5A0CF5		; -> [continue] (1A11F2~37D is free)

-----------------------------------------------------------------------------------------

### ANIMATE DEAD & RESURRECTION

Setting 1A1C89 from 09 to 00 causes Animate Dead to run the same magic skill check for
permanence as Resurrection; the required level is specified at 1A1C8C.

-----------------------------------------------------------------------------------------

### EARTHQUAKE

The 1 damage dealt by Earthquake is hard-coded and not affected by the power setting in
SpTraits.txt. The "bonus" settings per level are respected, however, and increasing them
to larger values will result in a more powerful - albeit janky and inconsistent - spell.
The below code modifies Earthquake to destroy fort sections outright instead of simply
damaging them, with SpTraits.txt specifying how many hits to make at each skill level.

    ----------	-------------------------------------------------------------------------
    1A80A8~106	; EARTHQUAKE DESTROYS INSTEAD OF DAMAGES FORT SECTIONS
    ----------	-------------------------------------------------------------------------
    31 C9		xor ecx,ecx		; ECX = 0
    89 4D 08	mov [ebp+08],ecx	; no hits have been made yet
    85 F6		test esi,esi		; do we have any hits? (from SpTraits.txt)
    0F8E B4020000	jle 5A8369		; if no -> [exit]

    6A 07		push 07			; EDX = 7
    5A		pop edx			; ""
    E8 0347F6FF	call 50C7C0		; EAX = 0~7 (random fort section)
    8D 54 85 B0	lea edx,[ebp+eax*4-50]	; EDX = address in memory for section
    6B C0 0C	imul eax,eax,0C		; EAX = data range
    8D 88 68BE6300	lea ecx,[eax+63BE68]	; ECX = section data
    31 C0		xor eax,eax		; EAX = 0

    83 3A 01	cmp dword ptr [edx],01	; have we already hit this section?
    74 0C		je 5A80DD		; if yes -> EAX +1
    8B 39		mov edi,[ecx]		; EDI = section ID
         83BCBB603F010000	cmp [ebx+edi*4+13F60],0	; has this section already been destroyed?
    7F 1E		jg 5A80FB		; if no -> hit section

    40		inc eax			; EAX +1
    83 C2 04	add edx,04		; EDX = next section
    83 C1 0C	add ecx,0C		; ECX = data for next section
    81 F9 C8BE6300	cmp ecx,63BEC8		; have we passed the last section?
    75 08		jne 5A80F4		; if no -> are we out of sections to check?
    8D 55 B0	lea edx,[ebp-50]	; EDX = first section (upper turret)
    B9 68BE6300	mov ecx,63BE68		; ECX = data for upper turret
    83 F8 08	cmp eax,08		; are we out of sections to check?
    7E D3		jle 5A80CC		; if no -> have we already hit this section?
    EB 2D		jmp 5A8128		; -> [continue]

    FF 02		inc [edx]		; hit section
    FF 45 08	inc [ebp+08]		; we have made at least one hit
    31 C9		xor ecx,ecx		; ECX = 0
    4E		dec esi			; subtract one hit
    7F B0		jg 5A80B5		; if any are left -> loop (EDX = 7)
    EB 21		jmp 5A8128		; -> [continue] (1A8107~27 is free)

    --------	-------------------------------------------------------------------------
    1A8281~D	; ""
    --------	-------------------------------------------------------------------------
    8B 4D F8	mov ecx,[ebp-08]	; (shifted code)
    8B 45 F4	mov eax,[ebp-0C]	; EAX = section HP
    6A 69		push 69			; push lethal damage (nice)
    50		push eax		; push section HP
    90 90 90 90	nop			; -

-----------------------------------------------------------------------------------------

### SUMMON ELEMENTAL

The IDs for the units summoned by the four elemental spells are specified at:

    1A2042 = Fire
    1A2057 = Earth
    1A206C = Water
    1A2081 = Air

A caveat to this is that the "push" instruction used (6A XX) is signed and thus limits us
to a maximum ID of 7F; anything higher (which includes Energy Elementals) will be read as
a negative number and will crash the game. We can push higher values than 7F, but it will
need a longer opcode (68 XX 00 00 00), meaning we have to jump to free space to do it.

>(NOTE: the above issue will be extremely important as we move into the next section)

You can also get rid of the completely arbitrary rule specifying that only one type of
elemental may be summoned at a time by going to 19F8BF and changing 0F to 00.

---------------------------------------------------------------------------------------------------------

Finally, let's look at how we can improve the spellbook interface. HD Mod does us a favor by enlarging
the book to include more spells per page - enough so, in fact, that each school can fit on a single set
of two pages without the need to flip to a new one. We can finish the job by changing the interface to
behave like the one from the mainline games, removing the "all spells" tab and the separation of battle
and adventure map spells. This in turn will allow us to have a designated position for each spell in the
book rather than a condensed list, making it easier to tell at a glance which ones we have (or don't).

The one caveat to this is that it will necessitate we standardize the costs of all spells since the cost
will be how we determine the position of each spell. By this I mean that, as in the mainline games, each
school will have one spell that costs 1 spell point, one spell that costs 2 spell points, one that costs
8 spell points, and so forth. It will also overwrite a code block that checks for Armageddon's Blade and
Titan's Thunder for the purposes of spell costs (expert level for Armageddon, 0 for Titan's Bolt).

    19CB82 > 01	; default landing page to Air Magic instead of "all spells"
    19CB87 > 00	; ""

    19E24C > 20	; spells sorted by (unskilled) cost instead of alphabetically
    19E24F > 20	; ""
    19E2A6 > 20	; ""
    19E2AD > 20	; ""

    ---------	-------------------------------------------------------------------------
    19D81F~27	; DISABLE "ALL SPELLS" TAB (ON CLICK)
    ---------	-------------------------------------------------------------------------
    74 E3 		je 59D804		; if switching to all spells, do nothing
    31 C0		xor eax,eax		; (optimized code)
    40		inc eax			; ""
    8B CF		mov ecx,edi		; ""
    D3 E0		shl eax,cl		; "" (19D828~30 is 9h free space)

    ---------	-------------------------------------------------------------------------
    19CD75~8D	; DISABLE "ALL SPELLS" TAB (ON CTRL+UP/DOWN) & COMBINE MAP/COMBAT SPELLS
    ---------	-------------------------------------------------------------------------
    50		push eax		; (displaced code)
    E8 B586F4FF	call 4E5430		; ""
    EB 11		jmp 59CD8E		; frees space: 19CD7D~8D

    6A 04		push 04			; load water magic instead of all spells
    6A 02		push 02			; ""
    EB 04		jmp 59CD87		; -> (cleanup)

    6A 01		push 01			; load air magic instead of all spells
    6A 00		push 00			; ""

    5F		pop edi			; (cleanup)
    58		pop eax			; ""
    C3		ret			; return
    90 90 90 90	nop			; -

    19D5A9 > E8 D5F7FFFF ; (choose one) CTRL+Up on air magic does nothing
    19D5A9 > E8 CFF7FFFF ; (choose one) CTRL+Up on air magic -> water magic

    19D5E7 > E8 91F7FFFF ; (choose one) CTRL+Down on water magic does nothing
    19D5E7 > E8 97F7FFFF ; (choose one) CTRL+Down on water magic -> air magic

    ---------	-------------------------------------------------------------------------
    19CF97~E	; UNCONDENSE SPELL LIST
    ---------	-------------------------------------------------------------------------
    E9 2085F4FF	jmp 4E54BC		; -> free space (titan's bolt/armageddon checks)
    8B 4D C4	mov ecx,[ebp-3C]	; moved to after jump so we can use ECX there

    ----------	-------------------------------------------------------------------------
    0E54BA~513	; (EXPANDED SPACE - OVERWRITES CHECKS FOR TITAN'S BOLT/ARMAGEDDON)
    ----------	-------------------------------------------------------------------------
    EB 58		jmp 4E5514		; frees space: 0E54BC~513

    E8 747F0B00	call 59D435		; -> free space (right click table)
    83 FF 16	cmp edi,16		; end of spell list?
    77 48 		ja 4E550E		; if yes -> exit

    80BFADCE590000	cmp byte[edi+59CEAD],00	; check for empty slot
    75 0C		jne 4E54DB		; if no -> lea eax,[edi-02]
    FF 05 283B6700	inc [673B28]		; leave current slot blank
    FF 45 E0	inc [ebp-20]		; ""
    47		inc edi			; ""
    EB D0		jmp 4E54AB		; -> [next spell slot] (hop to long jump)

    8D 47 FE	lea eax,[edi-02]	; prepare EAX to get spell ID
    2B 05 283B6700	sub eax,[673B28]	; ""
    6B C0 0C	imul eax,eax,0C		; ""
    8B 04 18	mov eax,[eax+ebx]	; EAX = spell ID
    83 F8 45	cmp eax,45		; is this a valid spell/do we have any left?
    77 1F		ja 4E550E		; if no -> exit

    8B 0D A87F6800	mov ecx,[687FA8]	; ECX = spell index
    6B C0 11	imul eax,eax,11		; EAX = data range
    8B 44 C1 20	mov eax,[ecx+eax*8+20]	; EAX = spell cost (unskilled)
    3A 87 ADCE5900	cmp al,[edi+59CEAD]	; does this spell go in this slot?
    75 CB		jne 4E54CF		; if no -> leave current slot blank

    B8 ABAAAA2A	mov eax,2AAAAAAB	; (displaced code)
    E9 8E7A0B00	jmp 59CF9C		; -> [continue]
    E9 597D0B00	jmp 59D26C		; -> [exit]
    90		nop			; -

    0E54AB > E9 DC7A0B00 ; next spell slot

    --------	-------------------------------------------------------------------------
    19D331~6	; CHECK FOR MORE SPELLS AFTER RUNNING "CLEAR SPELL SLOT" ROUTINE
    --------	-------------------------------------------------------------------------
    E9 0F010000	jmp 59D445		; -> free space (right click table)

    19D2B5 > EB 7A	; hop to long jump above

    ---------	-------------------------------------------------------------------------
    19D42C~7A	; (INLINE EDIT - USES RIGHT CLICK TABLE SPACE)
    ---------	-------------------------------------------------------------------------
    31 C0		xor eax,eax		; optimized code
    FF24BDFCDD5900	jmp dword[edi*4+59DDFC]	; ""

    FF 05 013B6700	inc [673B01]		; set "temp" flag
    53		push ebx		; store EBX
    57		push edi		; store EDI
    E8 2AFEFFFF	call 59D26C		; clear current spell slot
    5F 		pop edi			; retrieve EDI
    5B		pop ebx			; retrieve EBX
    C3		ret			; return

    A0 013B6700	mov al,[673B01]		; AL = "temp" flag
    3C 01		cmp al,01		; is flag set? (if yes, we're not done yet)
    75 07		jne 59D455		; if no -> displaced code
    FF 0D 013B6700	dec [673B01]		; unset "temp" flag
    C3		ret			; return

    83 FB 60	cmp ebx,60		; (displaced code)
    0F8C 19FEFFFF	jl 59D277		; ""
    C605283B670000	mov byte [673B28],00	; reset "temp" variable we used earlier
    E9 50FEFFFF	jmp 59D2BA		; -> [continue]
    90 90 90 90 90	nop			; ""

    31 C0		xor eax,eax		; EAX = EDI (see jump table pointers below)
    40		inc eax			; (A)
    40		inc eax			; (9)
    40		inc eax			; (-)
    40		inc eax			; (7)
    40		inc eax			; (6)
    40		inc eax			; (5)
    40		inc eax			; (4)
    40		inc eax			; -
    40		inc eax			; -
    40		inc eax			; (1)

    19D41C > 52    ; (EDI = A)
    19DDFC > 77    ; (EDI = 4)
    19DE00 > 76    ; (EDI = 5)
    19DE04 > 75    ; (EDI = 6)
    19DE08 > 74    ; (EDI = 7)
    19DE0C > 82 D9 ; disables "all spells" tab
    19DE10 > 82 D9 ; disables combat spells
    19DE14 > 82 D9 ; disables adventure spells
    19DE18 > 72    ; (EDI = 9)
    19DE1C > 7B    ; (EDI = 0)
    19DE20 > 7A    ; (EDI = 1)

    ---------	-------------------------------------------------------------------------
    19CE9D~C4	; SPELL COST LIST (OVERWRITES ANOTHER "ALL SPELLS" TAB CHECK)
    ---------	-------------------------------------------------------------------------
    89 45 EC	mov [ebp-14],eax	; optimized code
    8B 86 B8000000	mov eax,[esi+B8]	; ""
    80 48 16 06	or byte [eax+16],06	; ""
    8B 56 70	mov edx,[esi+70]	; ""
    EB 2C		jmp 59CEDB		; frees space: 19CEAF~DA

    00		; (blank)
    01		; Spell Cost = 1
    02		; Spell Cost = 2
    03		; Spell Cost = 3
    04		; Spell Cost = 4
    06		; Spell Cost = 6
    08		; Spell Cost = 8
    00		; (blank)
    0A		; Spell Cost = 10
    00		; (blank)
    00		; (blank)
    00		; (blank)
    00		; (blank)
    0C		; Spell Cost = 12
    0F		; Spell Cost = 15
    12		; Spell Cost = 18
    14		; Spell Cost = 20
    18		; Spell Cost = 24
    19		; Spell Cost = 25
    00		; (blank)
    1E		; Spell Cost = 30
    00		; (blank - 19CEC5~DA is free space)

    19CFD4 > 84 E4 90 ; needed for water magic to show up correctly (~~~I forget why)
    19CFDE > 90 90	  ; ""

-----------------------------------------------------------------------------------------

	    With the above code, our resulting spellbook will look like this:

			o----------------+----------------o-o
			|  --   --   --  |  --   --   --  |||=
			|                |                |||=
			|  01   02   03  |  12   15   18  |||=
			|                |                |||=
			|  04   06   08  |  20   24   25  |||
			|                |                |||
			|  --   10   --  |  --   30   --  |||
			o----------------+----------------o-o

By default, the original code skips the first two spell slots to leave space for the elemental graphic,
hence why we only have one blank spot in the above table but three in the book. Since this example comes
from my own hack, which has only 14 spells per scool, there are several blank spots in the bottom row.
However, simply setting Visions to fire instead of every element will reduce all four schools to an even
count of eighteen spells each - meaning the top row can go completely unusued.

That brings us back to the subject of graphics editing, which we will need to do a bit of to close this
overhaul out. For the top row, we can center the elemental graphic on the top of the left page and then
duplicate it on the right page. This can be achieved by editing the four images from the "Schools.def"
archive from H3Sprites.lod. Begin by widening the graphic to a width of 523 pixels (i.e. adding more of
the cyan transparent color, not actually stretching out the graphic itself). Then, move the graphic 45
pixels from the left edge of the image. Finally, place a copy of it on the far right edge.

The other thing we'll need to do is remove the "all spells" tab from the spellbook, which is much easier
to do. Simply open all of the images in the SpelTab.def archive and erase the bottom tab from each one.