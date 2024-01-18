# 7. Buildings

The cost of all buildings can be edited in Building.txt while their descriptions reside in a combination
of BldgNeut.txt, BldgSpec.txt, and Dwelling.txt. Within the .exe file, building data exists primarily in
two arrays: one for dependencies and one stating their animation frames and X/Y coordinates in two bytes
each (AF AF XX XX YY YY). For the time being, we'll concern ourselves mostly with the first one.

The dependency table is... questionably coded, to say the least. Rather than pointing each building for
each town to a specific address where their requirements can be expressed using a bitmask, every faction
instead lists the ID of every building it has access to as a DWORD (4-byte) value, each followed by the
ID(s) of its prerequisite building(s) and finally "FF FF FF FF" to indicate that the next DWORD is a new
building and not an additional requirement. Each faction's building list concludes with "9F FF FF FF" to
indicate the stopping point. This setup is not only inefficient, but it makes modifying it annoying.

Obviously, changing a requirement from one thing to another is easy; adding (or removing) them is where
it starts getting tricky. Most buildings only have one requirement and there's a finite amount of space
allotted to each town without rewriting the entire structure - adding a new requirement for a building
thus means taking one away from somewhere else. The good news is that it doesn't matter what order it's
in so long as it's all there. So you can take one building with, say, two requirements and just swap it
with one that only has one requirement rather than shifting around all of the code between the two.

That said, if you change more than just a few things, it'll probably be a lot easier in the long run to
just rewrite the dependency tables from scratch even if you do stay within the original space for every
faction. If you do need to expand any of them (bearing in mind you'll need to take that space back from
somewhere else to keep the entire structure within its original space allowance), you'll need to adjust
the only things that point to specific addresses within the structure, which is where each town starts:

    EB816 (23EC80 = Castle)	0EB8B3 (23EE24 = Rampart)	0EB971 (23EF34 = Tower)
    EBA39 (23F1A0 = Inferno)	0EBA48 (23F364 = Necropolis)	0EBA5C (23F51C = Dungeon)
    EBA70 (23F6D0 = Stronghold)	0EBA84 (23F870 = Fortress)	0EBA98 (23FA14 = Conflux)

>(As always, the above addresses are expressed as DWORD pointers, i.e. 23EC80 = 80 EC 63 00)

Below is listed every building for every faction followed by its address in the requirements table and
then its address in the graphics table. As mentioned above, most buildings only have one requirement;
those with more (or none) are specifically noted as such beside the first entry.

```
-----------------------------------------------------------------------------------------

				   CASTLE BUILDINGS
				   ----------------

               Fort            23ECF0 (-) 28AA36       Village Hall    ------     28AA48
               Citadel         23ECF8     28AA3C       Town Hall       23ED10     28AA4E
               Castle          23ED04     28AA42       City Hall       23ED1C (4) 28AA54
               ------          ------     ------       Capitol         23ED34 (2) 28AA5A

               Mage Guild 1    23ECA0 (-) 28AA0C       Tavern          23ECB4 (-) 28AA2A
               Mage Guild 2    23EC88     28AA12       Shipyard        23ECAC (-) 28AA30
               Mage Guild 3    23EC94     28AA18       Blacksmith      23ECDC (-) 28AA6C
               Mage Guild 4    23ECA0     28AA1E       Marketplace     23ECC8 (-) 28AA60
               Mage Guild 5    ------     ------       Resource Silo   23ECD0     28AA66

               Lv.1 Dwelling   23ED44     28AAC0       Lv.1 Upgrade    23ED50     28AAEA
               Lv.2 Dwelling   23ED5C     28AAC6       Lv.2 Upgrade    23ED68     28AAEA
               Lv.3 Dwelling   23ED90     28AACC       Lv.3 Upgrade    23EDA8     28AAF6
               Lv.4 Dwelling   23ED74 (2) 28AAD2       Lv.4 Upgrade    23ED84     28AAFC
               Lv.5 Dwelling   23EDE4 (2) 28AAD8       Lv.5 Upgrade    23EDF4     28AB02
               Lv.6 Dwelling   23EDCC     28AADE       Lv.6 Upgrade    23EDD8     28AB08
               Lv.7 Dwelling   23EE00     28AAE4       Lv.7 Upgrade    23EE0C     28AB0E
               Horde Bldg.     23ED9C     28AA78       Horde Upgrade   23EDB4     28AA7E

               Lighthouse      23ECE4     28AA72       Brotherhood     23ECBC     28AA90
               Stables         23EDC0     28AA8A       (Grail Bldg.)   23EE18 (-) 28AAA8

-----------------------------------------------------------------------------------------

				   RAMPART BUILDINGS
				   -----------------

               Fort            23EE24 (-) 28AB3E       Village Hall    ------     28AB50
               Citadel         23EE2C     28AB44       Town Hall       23EEB4     28AB56
               Castle          23EE38     28AB4A       City Hall       23EEC0 (4) 28AB5C
               ------          ------     ------       Capitol         23EED8 (2) 28AB62

               Mage Guild 1    23EE68 (-) 28AB14       Tavern          23EE44 (-) 28AB32
               Mage Guild 2    23EE70     28AB1A       Shipyard        ------     ------
               Mage Guild 3    23EE7C     28AB20       Blacksmith      23EE4C (-) 28AB74
               Mage Guild 4    23EE88     28AB26       Marketplace     23EE54 (-) 28AB68
               Mage Guild 5    23EE94     28AB2C       Resource Silo   23EE5C     28AB6E

               Lv.1 Dwelling   23EEE8     28ABC8       Lv.1 Upgrade    23EEF4     28ABF2
               Lv.2 Dwelling   23EF00     28ABCE       Lv.2 Upgrade    23EF24     28ABF8
               Lv.3 Dwelling   23EF3C     28ABD4       Lv.3 Upgrade    23EF48     28ABFE
               Lv.4 Dwelling   23EF84     28ABDA       Lv.4 Upgrade    23EF90     28AC04
               Lv.5 Dwelling   23EF54     28ABE0       Lv.5 Upgrade    23EF6C     28AC0A
               Lv.6 Dwelling   23EF9C (2) 28ABE6       Lv.6 Upgrade    23EFAC     28AC10
               Lv.7 Dwelling   23EFB8 (2) 28ABEC       Lv.7 Upgrade    23EFC8 (2) 28AC16
               Horde Bldg.A    23EF0C     28AB80       Horde Upg.A     23EF30     28AB86
               Horde Bldg.B    23EF60     28ABA4       Horde Upg.B     23EF78     28ABAA

               Mystic Pond     23EEA0 (-) 28AB7A       Treasury        23EF18     28AB98
               Lucky Fountain  23EEA8     28AB92       (Grail Bldg.)   23EFD8 (-) 28ABB0

-----------------------------------------------------------------------------------------

				   TOWER BUILDINGS
				   ---------------

               Fort            23EFE4 (-) 28AC46       Village Hall    ------     28AC58
               Citadel         23EFF8     28AC4C       Town Hall       23F090     28AC5E
               Castle          23F004     28AC52       City Hall       23F09C (4) 28AC64
               ------          ------     ------       Capitol         23F0B4 (2) 28AC6A

               Mage Guild 1    23F010 (-) 28AC1C       Tavern          23F060 (-) 28AC3A
               Mage Guild 2    23F030     28AC22       Shipyard        ------     ------
               Mage Guild 3    23F03C     28AC28       Blacksmith      23F068 (-) 28AC7C
               Mage Guild 4    23F048     28AC2E       Marketplace     23F070 (-) 28AC70
               Mage Guild 5    23F054     28AC34       Resource Silo   23F078     28AC76

               Lv.1 Dwelling   23F0C4     28ACD0       Lv.1 Upgrade    23F0D0     28ACFA
               Lv.2 Dwelling   23F0DC     28ACD6       Lv.2 Upgrade    23F0F4     28AD00
               Lv.3 Dwelling   23F10C     28ACDC       Lv.3 Upgrade    23F118     28AD06
               Lv.4 Dwelling   23F124 (3) 28ACE2       Lv.4 Upgrade    23F138 (2) 28AD0C
               Lv.5 Dwelling   23F148     28ACE8       Lv.5 Upgrade    23F154     28AD12
               Lv.6 Dwelling   23F160     28ACEE       Lv.6 Upgrade    23F16C     28AD18
               Lv.7 Dwelling   23F178 (2) 28ACF4       Lv.7 Upgrade    23F188     28AD1E
               Horde Bldg.     23F0E8     28AC88       Horde Upgrade   23F100     28AC8E

               Artifact Market 23F084     28AC82       Library         23F018     28ACA0
               Lookout Tower   23EFEC     28AC9A       Knowledge Wall  23F024     28ACA6
               -------------   ------     ------       (Grail Bldg.)   23F194 (-) 28ACB8

-----------------------------------------------------------------------------------------

				   INFERNO BUILDINGS
				   -----------------

               Fort            23F1A0 (-) 28AD4E       Village Hall    ------     28AD60
               Citadel         23F1B4     28AD54       Town Hall       23F240     28AD66
               Castle          23F1CC     28AD5A       City Hall       23F24C (4) 28AD6C
               ------          ------     ------       Capitol         23F264 (2) 28AD72

               Mage Guild 1    23F1FC (-) 28AD24       Tavern          23F1D8 (-) 28AD42
               Mage Guild 2    23F210     28AD2A       Shipyard        ------     ------
               Mage Guild 3    23F21C     28AD30       Blacksmith      23F1E0 (-) 28AD84
               Mage Guild 4    23F228     28AD36       Marketplace     23F1E8 (-) 28AD78
               Mage Guild 5    23F234     28AD3C       Resource Silo   23F1F0     28AD7E

               Lv.1 Dwelling   23F274     28ADD8       Lv.1 Upgrade    23F28C     28AE02
               Lv.2 Dwelling   23F2D4     28ADDE       Lv.2 Upgrade    23F2E0     28AE08
               Lv.3 Dwelling   23F2A4     28ADE4       Lv.3 Upgrade    23F2BC     28AE0E
               Lv.4 Dwelling   23F2EC     28ADEA       Lv.4 Upgrade    23F2F8     28AE14
               Lv.5 Dwelling   23F320     28ADF0       Lv.5 Upgrade    23F32C (2) 28AE1A
               Lv.6 Dwelling   23F304 (2) 28ADF6       Lv.6 Upgrade    23F314     28AE20
               Lv.7 Dwelling   23F33C (2) 28ADFC       Lv.7 Upgrade    23F34C     28AE26
               Horde Bldg.A    23F280     28AD90       Horde Upg.A     23F298     28AD96
               Horde Bldg.B    23F2B0     28ADB4       Horde Upg.B     23F2C8     28ADBA

               Stormclouds     23F1A8     28ADA2       Order Of Fire   23F204     28ADAE
               Castle Gate     23F1C0     28ADA8       (Grail Bldg.)   23F358 (-) 28ADC0

-----------------------------------------------------------------------------------------

				   NECROPOLIS BUILDINGS
				   --------------------

               Fort            23F364 (-) 28AE56       Village Hall    ------     28AE68
               Citadel         23F378     28AE5C       Town Hall       23F400     28AE6E
               Castle          23F384     28AE62       City Hall       23F40C (4) 28AE74
               ------          ------     ------       Capitol         23F424 (2) 28AE7A

               Mage Guild 1    23F3BC (-) 28AE2C       Tavern          23F390 (-) 28AE4A
               Mage Guild 2    23F3D0     28AE32       Shipyard        23F3B4 (-) 28AE50
               Mage Guild 3    23F3DC     28AE38       Blacksmith      23F398 (-) 28AE8C
               Mage Guild 4    23F3E8     28AE3E       Marketplace     23F3A0 (-) 28AE80
               Mage Guild 5    23F3F4     28AE44       Resource Silo   23F3A8     28AE86

               Lv.1 Dwelling   23F434     28AEE0       Lv.1 Upgrade    23F458     28AF0A
               Lv.2 Dwelling   23F48C     28AEE6       Lv.2 Upgrade    23F498     28AF10
               Lv.3 Dwelling   23F474     28AEEC       Lv.3 Upgrade    23F480     28AF16
               Lv.4 Dwelling   23F4A4     28AEF2       Lv.4 Upgrade    23F4B0 (2) 28AF1C
               Lv.5 Dwelling   23F4C0 (2) 28AEF8       Lv.5 Upgrade    23F4D0     28AF22
               Lv.6 Dwelling   23F4DC (2) 28AEFE       Lv.6 Upgrade    23F4EC     28AF28
               Lv.7 Dwelling   23F4F8     28AF04       Lv.7 Upgrade    23F504     28AF2E
               Horde Bldg.     23F44C     28AE98       Horde Upgrade   23F464 (2) 28AE9E

               Darkness Cover  23F36C     28AE92       Transformer     23F440     28AEB0
               Necro Amplifier 23F3C4     28AEAA       (Grail Bldg.)   23F510 (-) 28AEC8

-----------------------------------------------------------------------------------------

				   DUNGEON BUILDINGS
				   -----------------

               Fort            23F51C (-) 28AF5E       Village Hall    ------     28AF70
               Citadel         23F524     28AF64       Town Hall       23F5C0     28AF76
               Castle          23F530     28AF6A       City Hall       23F5CC (4) 28AF7C
               ------          ------     ------       Capitol         23F5E4 (2) 28AF82

               Mage Guild 1    23F57C (-) 28AF34       Tavern          23F54C (-) 28AF52
               Mage Guild 2    23F590     28AF3A       Shipyard        ------     ------
               Mage Guild 3    23F59C     28AF40       Blacksmith      23F554 (-) 28AF94
               Mage Guild 4    23F5A8     28AF46       Marketplace     23F55C (-) 28AF88
               Mage Guild 5    23F5B4     28AF4C       Resource Silo   23F564     28AF8E

               Lv.1 Dwelling   23F5F4     28AFE8       Lv.1 Upgrade    23F60C     28B012
               Lv.2 Dwelling   23F63C     28AFEE       Lv.2 Upgrade    23F648     28B018
               Lv.3 Dwelling   23F624     28AFF4       Lv.3 Upgrade    23F630     28B01E
               Lv.4 Dwelling   23F654 (2) 28B000       Lv.4 Upgrade    23F664     28B02A
               Lv.5 Dwelling   23F670     28B006       Lv.5 Upgrade    23F67C     28B030
               Lv.6 Dwelling   23F688     28B00C       Lv.6 Upgrade    23F694     28B036
               Lv.7 Dwelling   23F6A0 (3) 28AFA0       Lv.7 Upgrade    23F6B4 (2) 28AFA6
               Horde Bldg.     23F600     28AFFA       Horde Upgrade   23F618     28B024

               Artifact Market 23F570     28AF9A       Summons Portal  23F53C (-) 28AFB8
               Mana Vortex     23F584     28AFB2       Battle Academy  23F544 (-) 28AFBE
               -----------     ------     ------       (Grail Bldg.)   23F6C4 (-) 28AFD0

-----------------------------------------------------------------------------------------

				   STRONGHOLD BUILDINGS
				   --------------------

               Fort            23F6D0 (-) 28B066       Village Hall    ------     28B078
               Citadel         23F6F0     28B06C       Town Hall       23F764     28B07E
               Castle          23F6FC     28B072       City Hall       23F770 (4) 28B084
               ------          ------     ------       Capitol         23F788 (2) 28B08A

               Mage Guild 1    23F744 (-) 28B03C       Tavern          23F708 (-) 28B05A
               Mage Guild 2    23F74C     28B042       Shipyard        ------     ------
               Mage Guild 3    23F758     28B048       Blacksmith      23F710 (-) 28B09C
               Mage Guild 4    ------     28B04E       Marketplace     23F724 (-) 28B090
               Mage Guild 5    ------     28B054       Resource Silo   23F72C     28B096

               Lv.1 Dwelling   23F798     28B0F0       Lv.1 Upgrade    23F7B0     28B11A
               Lv.2 Dwelling   23F7C8     28B0F6       Lv.2 Upgrade    23F7D4 (2) 28B120
               Lv.3 Dwelling   23F814     28B0FC       Lv.3 Upgrade    23F820 (2) 28B126
               Lv.4 Dwelling   23F830     28B102       Lv.4 Upgrade    23F83C (2) 28B12C
               Lv.5 Dwelling   23F7E4     28B108       Lv.5 Upgrade    23F7F0     28B132
               Lv.6 Dwelling   23F84C     28B10E       Lv.6 Upgrade    23F858     28B138
               Lv.7 Dwelling   23F7FC     28B114       Lv.7 Upgrade    23F808     28B13E
               Horde Bldg.     23F7A4     28B0A8       Horde Upgrade   23F7BC     28B0AE

               Escape Tunnel   23F6D8     28B0A2       Ballista Yard   23F718     28B0C0
               Freelancers     23F738     28B0BA       Valhalla Hall   23F6E4     28B0C6
               -----------     ------     ------       (Grail Bldg.)   23F864 (-) 28B0D8

-----------------------------------------------------------------------------------------

				   FORTRESS BUILDINGS
				   ------------------

               Fort            23F870 (-) 28B16E       Village Hall    ------     28B180
               Citadel         23F890     28B174       Town Hall       23F8EC     28B186
               Castle          23F89C     28B17A       City Hall       23F908 (4) 28B18C
               ------          ------     ------       Capitol         23F928 (2) 28B192

               Mage Guild 1    23F8CC (-) 28B144       Tavern          23F8A8 (-) 28B162
               Mage Guild 2    23F8D4     28B14A       Shipyard        23F920 (-) 28B168
               Mage Guild 3    23F8E0     28B150       Blacksmith      23F8B0 (-) 28B1A4
               Mage Guild 4    ------     ------       Marketplace     23F8B8 (-) 28B198
               Mage Guild 5    ------     ------       Resource Silo   23F8C0     28B19E

               Lv.1 Dwelling   23F938     28B1F8       Lv.1 Upgrade    23F950 (2) 28B222
               Lv.2 Dwelling   23F96C     28B1FE       Lv.2 Upgrade    23F978     28B228
               Lv.3 Dwelling   23F99C     28B204       Lv.3 Upgrade    23F9A8     28B22E
               Lv.4 Dwelling   23F9B4     28B20A       Lv.4 Upgrade    23F9C0     28B234
               Lv.5 Dwelling   23F9CC (2) 28B210       Lv.5 Upgrade    23F9DC (2) 28B23A
               Lv.6 Dwelling   23F984     28B216       Lv.6 Upgrade    23F990     28B240
               Lv.7 Dwelling   23F9EC (2) 28B21C       Lv.7 Upgrade    23F9FC     28B246
               Horde Bldg.     23F944     28B1B0       Horde Upgrade   23F960     28B1B6

               Warlord Cage    23F8F8 (2) 28B1AA       Blood Obelisk   23F884     28B1C8
               Glyphs Of Fear  23F878     28B1C2       (Grail Bldg.)   23FA08 (-) 28B1E0

-----------------------------------------------------------------------------------------

				   CONFLUX BUILDINGS
				   -----------------

               Fort            23FA14 (-) 28B276       Village Hall    ------     28B288
               Citadel         23FA1C     28B27C       Town Hall       23FAB0     28B28E
               Castle          23FA28     28B282       City Hall       23FABC (4) 28B294
               ------          ------     ------       Capitol         23FAD4 (2) 28B29A

               Mage Guild 1    23FA6C (-) 28B24C       Tavern          23FA3C (-) 28B26A
               Mage Guild 2    23FA74     28B252       Shipyard        23FA34 (-) 28B270
               Mage Guild 3    23FA80     28B258       Blacksmith      23FA44 (-) 28B2AC
               Mage Guild 4    23FA8C     28B25E       Marketplace     23FA4C (-) 28B2A0
               Mage Guild 5    23FA98     28B264       Resource Silo   23FA54     28B2A6

               Lv.1 Dwelling   23FAE4     28B300       Lv.1 Upgrade    23FAFC     28B32A
               Lv.2 Dwelling   23FB14 (2) 28B306       Lv.2 Upgrade    23FB24     28B330
               Lv.3 Dwelling   23FB30 (2) 28B30C       Lv.3 Upgrade    23FB40     28B336
               Lv.4 Dwelling   23FB4C     28B318       Lv.4 Upgrade    23FB58 (2) 28B342
               Lv.5 Dwelling   23FB68     28B31E       Lv.5 Upgrade    23FB74     28B348
               Lv.6 Dwelling   23FB80 (2) 28B324       Lv.6 Upgrade    23FB90 (2) 28B34E
               Lv.7 Dwelling   23FBA0     28B2B8       Lv.7 Upgrade    23FBAC     28B2BE
               Horde Bldg.     23FAF0     28B312       Horde Upgrade   23FB08     28B33C

               Artifact Market 23FA60     28B2B2       Magic Academy   23FAA4     28B2CA
               --------------- ------     ------       (Grail Bldg.)   23FBB8 (-) 28B2E8

---------------------------------------------------------------------------------------------------------

				      UNIT DWELLINGS
				      --------------

In both of the tables discussed above, unit dwellings are not specifically named. Rather, they call on
the dwelling specified as level (X) for (X) town. These specifications exist in a table which starts at
2747B4, listing the seven base unit IDs followed by the seven upgraded unit IDs for each town.

                CASTLE                          RAMPART                           TOWER
    -----------------------------    -----------------------------    -----------------------------
    Lv.1 = 2747B4  Upg.1 = 2747D0    Lv.1 = 2747EC  Upg.1 = 274808    Lv.1 = 274824  Upg.1 = 274840
    Lv.2 = 2747B8  Upg.2 = 2747D4    Lv.2 = 2747F0  Upg.2 = 27480C    Lv.2 = 274828  Upg.2 = 274844
    Lv.3 = 2747BC  Upg.3 = 2747D8    Lv.3 = 2747F4  Upg.3 = 274810    Lv.3 = 27482C  Upg.3 = 274848
    Lv.4 = 2747C0  Upg.4 = 2747DC    Lv.4 = 2747F8  Upg.4 = 274814    Lv.4 = 274830  Upg.4 = 27484C
    Lv.5 = 2747C4  Upg.5 = 2747E0    Lv.5 = 2748FC  Upg.5 = 274818    Lv.5 = 274834  Upg.5 = 274850
    Lv.6 = 2747C8  Upg.6 = 2747E4    Lv.6 = 274800  Upg.6 = 27481C    Lv.6 = 274838  Upg.6 = 274854
    Lv.7 = 2747CC  Upg.7 = 2747E8    Lv.7 = 274804  Upg.7 = 274820    Lv.7 = 27483C  Upg.7 = 274858

               INFERNO                         NECROPOLIS                        DUNGEON
    -----------------------------    -----------------------------    -----------------------------
    Lv.1 = 27485C  Upg.1 = 274878    Lv.1 = 274894  Upg.1 = 2748B0    Lv.1 = 2748CC  Upg.1 = 2748E8
    Lv.2 = 274860  Upg.2 = 27487C    Lv.2 = 274898  Upg.2 = 2748B4    Lv.2 = 2748D0  Upg.2 = 2748EC
    Lv.3 = 274864  Upg.3 = 274880    Lv.3 = 27489C  Upg.3 = 2748B8    Lv.3 = 2748D4  Upg.3 = 2748F0
    Lv.4 = 274868  Upg.4 = 274884    Lv.4 = 2748A0  Upg.4 = 2748BC    Lv.4 = 2748D8  Upg.4 = 2748F4
    Lv.5 = 27486C  Upg.5 = 274888    Lv.5 = 2748A4  Upg.5 = 2748C0    Lv.5 = 2748DC  Upg.5 = 2748F8
    Lv.6 = 274870  Upg.6 = 27488C    Lv.6 = 2748A8  Upg.6 = 2748C4    Lv.6 = 2748E0  Upg.6 = 2748FC
    Lv.7 = 274874  Upg.7 = 274890    Lv.7 = 2748AC  Upg.7 = 2748C8    Lv.7 = 2748E4  Upg.7 = 274900

              STRONGHOLD                        FORTRESS                         CONFLUX
    -----------------------------    -----------------------------    -----------------------------
    Lv.1 = 274904  Upg.1 = 274920    Lv.1 = 27493C  Upg.1 = 274958    Lv.1 = 274974  Upg.1 = 274990
    Lv.2 = 274908  Upg.2 = 274924    Lv.2 = 274940  Upg.2 = 27495C    Lv.2 = 274978  Upg.2 = 274994
    Lv.3 = 27490C  Upg.3 = 274928    Lv.3 = 274944  Upg.3 = 274960    Lv.3 = 27497C  Upg.3 = 274998
    Lv.4 = 274910  Upg.4 = 27492C    Lv.4 = 274948  Upg.4 = 274964    Lv.4 = 274980  Upg.4 = 27499C
    Lv.5 = 274914  Upg.5 = 274930    Lv.5 = 27494C  Upg.5 = 274968    Lv.5 = 274984  Upg.5 = 2749A0
    Lv.6 = 274918  Upg.6 = 274934    Lv.6 = 274950  Upg.6 = 27496C    Lv.6 = 274988  Upg.6 = 2749A4
    Lv.7 = 27491C  Upg.7 = 274938    Lv.7 = 274954  Upg.7 = 274970    Lv.7 = 27498C  Upg.7 = 2749A8

-----------------------------------------------------------------------------------------
```

Where this all comes together is if you want to move units to different levels or towns: in addition to
editing their level in the unit data table (if applicable), you'll also need to edit the above addresses
to reflect your new settings. That will take care of everything mechanically, but not graphically.

Let's assume we want to swap Gnolls (1st-level Fortress unit) with Flies (their 3rd-level unit despite
being the weakest enemy by far in Might & Magic VII). First we swap their levels in the unit data table
as well as in the table above, which gives us what we want except that we're now buying Gnolls from the
Fly Hive and Flies from the Gnoll Hut. We will need to do several things to address this:

- Edit the building descriptions in Dwelling.txt
- Swap the X/Y coordinates for Fortress's 1st and 3rd-level dwellings in the table from earlier(*)
- Swap the DWORD pointers to the Gnoll Hut and Fly Hive building graphics in the .exe

>(*The animation frame values are not used, so there is no need to swap them)

While the first two steps bear no further explanation, the third one is new to us. Earlier in the guide,
I suggested that it was much easier to edit the names of the hero portraits loaded into the .exe rather
than to edit the DWORD pointers due to the uniform length of the filenames and the fact that managing a
set of custom portraits is easier with better names to work with. None of that is true in this case; in
fact, the non-uniform length of the dwelling graphic filenames makes a simple rename job impossible.

Since we now know how DWORD pointers work, however, finding them is a simple task. First, we do a search
in the hex editor for a text string of the filenames (excluding the extension) for the graphic files we
wish to edit. This will include both a "base" graphic file (i.e. TBFRDW_0) and an outline graphic (i.e.
TOFFLY1A) - the easiest way to determine the names of the files you're after is to open h3sprite.lod in
MMArchive and look around at all of the .def files starting with "TB" and "TO". When you locate the file
in the .exe, note the hex address of the first character, which for TBFRDW_0 is 2892F8. Now, we do a hex
search for the DWORD pointer to that address - F8 92 68 00 - and find it at 2435BC.

Unfortunately, we're not out of the woods yet. Were we swapping most other units around, this would be
the end of it. However, one of the units that we're working with here (Gnolls) has a "horde" building
associated with it, so we have a few more steps to go before we're finished.

---------------------------------------------------------------------------------------------------------

## HORDE BUILDINGS

Horde buildings are, for the most part, wholly customizable. There are three tables: one specifying the
(base) unit whose growth to boost and by how much, a second table indicating the level(s) to be affected
by a town's horde building(s), and a third for buildings which replace other buildings (which is mostly
the horde buildings along with a few others). Let's look at the first two tables first:

		     TOWN        UNIT     GROWTH RATE  UNIT LEVEL
		     --------------------------------------------
		     Castle      2887F0   2887F4 (+3)  28A3B4 (2)
		     Rampart     288810   288814 (+4)  28A3B6 (1)
		     Rampart II  288820   288824 (+2)  28A3CA (4)
		     Tower       288830   288834 (+4)  28A3B8 (1)
		     Inferno     288850   288854 (+8)  28A3BA (0)
		     Inferno II  288860   288864 (+3)  28A3CE (2)
		     Necropolis  288870   288874 (+6)  28A3BC (0)
		     Dungeon     288890   288894 (+7)  28A3BE (0)
		     Stronghold  2888B0   2888B4 (+8)  28A3C0 (0)
		     Fortress    2888D0   2888D4 (+6)  28A3C2 (0)
		     Conflux     2888F0   2888F4 (+10) 28A3C4 (0)

The third table starts at 23FCA0 and is laid out like the building code above, with the ID of a building
followed by the one it should replace and then FF FF FF FF with each faction separated with 9C FF FF FF.
Thus, to complete the Gnoll/Fly swap, we need to change 2888D4 to a more reasonable value than 08 for a
3rd-level unit, 28A3C2 from 0 to 2 (level 1 > 3), and then 23FDD4/23FDE from 1E/25 to 20/27 (bearing in
in mind that horde buildings are actually two different buildings for the base and upgraded dwellings).
Finally, we go to BldgSpec.txt and update the horde building descriptions and we're finished at last...

...except for one small issue that I'm still not sure how to fix. For some reason, the trigger for being
offered the "upgraded" horde building instead of the base one will still be the upgraded lv.1 dwelling,
not the upgraded Gnoll (now lv.3) dwelling. Thus, building the Captain's Quarters after upgrading your
Fly Hive will upgrade your Gnoll Hut for free. The best suggestion I have for this is to simply have all
horde buildings require the upgraded dwelling (at least until I can find a proper solution).

-----------------------------------------------------------------------------------------

Let's have another example, wherein we change Necropolis's horde building to raise Zombie growth instead
of Skeletons. This is where the "for the most part" bit up there comes into play since, as you may have
noticed, the Unearthed Graves are kind of attached to the Cursed Temple and we can't change that unless
we're graphic designers (which we aren't). Thus, the only way we have to realistically change this is to
flat-out swap which building produces which unit: Graveyards to Skeletons and Cursed Temple for Zombies.

Using what we've learned thus far, we now know everything that we need to make this switch happen:

	288870 > 3A	; Zombies
	288874 > 04	; horde growth
	28A3BC > 01 08	; horde level
	23FD74 > 1F	; horde building replaces lv. 2 dwelling
	23FD80 > 26	; ""

	2433AC > 1C 99	; Temple > Graveyard (GFX)
	28A714 > 84 B9	; "" (outline)
	28AEE2 > F601DF	; "" (coordinates)

	2433B0 > 28 99	; Graveyard > Temple (GFX)
	28A718 > 90 B9	; "" (outline)
	28AEE8 > 5000DE	; "" (coordinates)

	2433C8 > C8 98	; Upg. Temple > Upg. Graveyard (GFX)
	28A730 > 3C B9	; "" (outline)
	28AF0C > F201E0	; "" (coordinates)

	2433CC > D4 98	; Upg. Graveyard > Upg. Temple (GFX)
	28A734 > 48 B9	; "" (outline)
	28AF12 > 4000DE	; "" (coordinates)

There is actaully one final step in this case, which is to edit the external dwellings to match. This is
a very simple matter of swapping the values at 23D648 and 23D64C; we'll cover external dwellings in more
detail when we get to the "Map Locations" section below. For now, let's continue with town buildings.

---------------------------------------------------------------------------------------------------------

## MAGE GUILDS

One of the more drastic things one might wish to do with the information above is to raise and/or remove
the cap on Castle, Stronghold, and Fortress mage guilds. This is not as simple as adding Mage Guild IV/V
to the dependency table (although that will also need to be done); we also need to add them to the list
of what those towns are able to build in the first place. The code below will remove the cap on Castle's
Mage Guild as well as raising it from level 3 to 4 for Stronghold and Fortress.

	---------	-------------------------------------------------------------------------
	060FA4~ED	; ALLOW STRONGHOLD/FORTRESS MAGE GUILD IV & CASTLE MAGE GUILD V
	---------	-------------------------------------------------------------------------
	74 0F		je 460FB5		; (shortened jump)
	8B 4D 08	mov ecx,[ebp+08]	; ""
	8B 75 FC	mov esi,[ebp-04]	; ""
	C681C04E690003	mov byte [ecx+694EC0],3 ; ""
	EB 76		jmp 46102B		; -> [exit, Mage Guild capped at III]
	8B 86 58010000	mov eax,[esi+158]	; (shifted code)
	8B 1D B0CD6600	mov ebx,[66CDB0]	; ""
	8B 8E 5C010000	mov ecx,[esi+15C]	; ""
	8B 3D B4CD6600	mov edi,[66CDB4]	; ""
	21 D8		and eax,ebx		; ""
	21 F9		and ecx,edi		; ""
	09 C8		or eax,ecx		; ""
	74 50		je 461025		; ""
	8A 46 04	mov al,[esi+04]		; ""
	8B 75 FC	mov esi,[ebp-04]	; ""
	8B 4D 08	mov ecx,[ebp+08]	; ""
	84 C0		test al,al		; ""
	74 0C		je 460FEE		; ""
	3C 06		cmp al,06		; Stronghold?
	74 08		je 460FEE		; if yes -> [exit, Mage Guild capped at IV]
	3C 07		cmp al,07		; Fortress?
	74 04		je 460FEE		; if yes -> [exit, Mage Guild capped at IV]
	42		inc edx			; allow Mage Guild V
	90 90 90	nop			; -

	242EEA > 04	; add Mage Guild V to Castle's build list
	28A3EC > 20C0C8	; outline
	28AA26 > C0024C	; coordinates(*)

	242FF0 > 03	; add Mage Guild IV to Stronghold's build list
	28A808 > 90B768	; outline
	28B050 > D90101	; coordinates

	24301D > 03	; add Mage Guild IV to Fortress's build list
	28A8B8 > 3CB668	; outline
	28B158 > 008700	; coordinates(*)

>(*Again, the animation frame values are not used, so there's no need to add any)

The above code alone takes care of the change from a purely mechanical standpoint (don't forget to add
spell probabilities in SpTraits.txt!), but does nothing graphically. You'll need to export the graphics
for the three highest-level guilds from Castle (TbCsMag4.def), Stronghold (TbStMag3.def), and Fortress
(TbFrMag3.def) and then make copies of them, replacing the numbers in both the component images and the
resulting .def files with one higher. Along with the outline and coordinate edits above - which are just
copies of the values from the levels below them - this will re-use those graphics for the new levels.

If you want to do this change right and include updated building graphics, I'd recommend starting with
Castle since it's the easiest of the three. You'll first need to increase the dimensions of all of the
building images: use the "canvas size" or equivalent option in your photo editing software to add this
space uniformly to the top of the image so that everything remains properly aligned. Now, just do a bit
of cutting and pasting to create a fifth floor; I recommend copying the bottom half of the fourth floor
and inserting it between the top of the fourth floor and the roof.

The next step is to create the "TZ" file, which is a silhouette image of the building graphic which is
used to indicate the building's "hitbox", i.e. where it can be clicked to activate it. This is pretty
easy to do: just screw with the brightness and contrast until the whole building is a single color and
then make sure the background is reset to the transparent color (the first one in the palette list).
Save this file as TZCSM501.bmp and then make a copy of it named TOCSM501.bmp.

TOCSM501.bmp will be our building outline image. Set your paintbrush to the smallest size and the color
to #D2B46E (210 Red, 180 Green, 110 Blue), then simply trace an outline around the building silhouette.
When you're done, fill in the silhouette with the transparent color, leaving only the outline. Now add
both of these images to the h3bitmap.lod archive and we're almost ready to look at it in-game.

The last thing we need is 9 bytes of free space, which we very likely have left over from any countless
number of earlier hacks. In this space, write 54 4F 43 73 4D 35 30 31 00 (TOCSM501). Convert the address
of the first byte to a DWORD pointer (i.e. 0C8A0E -> 0E 8A 4C 00) and write that value to 28A3EC, which
we currently have looking at the town outline for the level below it. This also calls the "TZ" file.

Now for the tricky/fun part. Load up the game and look at your fifth-level Mage Guild in action. You'll
need to fine-tune the Y coordinates until the fifth-level guild is in the same position as level four.
This will vary depending on how big you made the top floor, but for reference I went from 4C to 38.

And now for the final step: getting an image for the build menu. This is actually where Castle is the
hardest of the three due to the position of the Mage Guild in Castle towns. For Stronghold or Fortress,
it's a simple matter of temporarily replacing the adjacent building graphics with transparent images so
that you can get a screenshot of JUST the guild, taking a screenshot, and then cropping/resizing it down
to 150x70 pixels. Unfortunately for Castle, the Mage Guild images contain off-screen background graphics
that don't actually exist in-game. Thus, you'll need to paste your resized screenshot as a new layer on
top of the level four Mage Guild image (ThCsMag4.bmp) and erase everything in that layer but the guild.

HallCstl.def
HallStrn.def
HallFort.def

Stronghold and Fortress will follow the same steps as above, but are both more difficult for different
reasons. Adding another floor to Stronghold's guild is super easy due to the simplicity of its design,
but doing so will cause it to go beyond the bounds of the town screen and will thus require that you
reposition the entire building - I suggest moving it a little bit down the mountain to the left, which
creates a pleasant "twin tower" aesthetic alongside the Hall of Valhalla. Fortress's guild, on the other
hand, won't need to be moved, but its design makes creating a decent fourth level very challenging.

>(If all of this seems like too much work, feel free to steal the graphics I created for my mod)

---------------------------------------------------------------------------------------------------------

## BLACKSMITHS

It's possible to change which war machine (First Aid Tent, Ammo Cart, or Ballista) is sold in each type
of town with just a few edits, starting with the below addresses:

| Faction     | Memory Address |            | Faction     | Memory Address |             | Faction      | Memory Address |
|-------------|----------------|------------|-------------|----------------|-------------|---------------|----------------|
| Castle      | 242EA0         |            | Inferno     | 242EAC         |             | Stronghold   | 242EB8         |
| Rampart     | 242EA4         |            | Necropolis  | 242EB0         |             | Fortress     | 242EBC         |
| Tower       | 242EA8         |            | Dungeon     | 242EB4         |             | Conflux      | 242EC0         |

Along with editing the Blacksmith descriptions in BldgNeut.txt, that'll take care of the visual side of
things and set the correct price (specified in ArTraits.txt). As far as actually getting the machine we
want, we'll need to dig deeper. Ideally, you'll want to preserve the balance of each machine being sold
in three different towns. Assuming this, it's a simple matter of moving around the values shown below:

| BALLISTA                | FIRST AID               | AMMO CART               |
|-------------------------|-------------------------|-------------------------|
| 1C322F (60 = *Castle)   | 1C323E (68 = Rampart)   | 1C3249 (70 = Tower)     |
| 1C326A (88 = Dungeon)   | 1C325F (80 = Necropolis)| 1C3254 (78 = Inferno)   |
| 1C328F (A0 = Conflux)   | 1C3284 (98 = Fortress)  | 1C3279 (90 = Stronghold)|


>(*This address is also used by the Stronghold Ballista Yard)

The obvious elephant in the room is that, since the Ballista Yard uses the same address as the Castle's
blacksmith, you can't just go and make the obvious change of swapping Castle's Ballista with the First
Aid Tent that some imbecile decided to saddle Necropolis with. My personal solution to this was to make
First Aid a starting skill for Clerics so I could justify starting them all out with tents, effectively
sidestepping the issue. But this raises the bigger question of war machine specialists from towns which
don't sell their preferred item being shit out of luck if theirs gets destroyed in combat. In light of
this, you can prevent war machines from being permanently removed from a hero's inventory thusly:

	---------	-------------------------------------------------------------------------
	0D94D0~EB	; WAR MACHINES ARE NOT REMOVED FROM INVENTORY WHEN DESTROYED IN COMBAT
	---------	-------------------------------------------------------------------------
	55		push ebp		; (setup)
	8B EC		mov ebp,esp		; ""
	8B 45 08	mov eax,[ebp+08]	; ""
	05 6FFFFFFF	add eax,FFFFFF6F	; ""

	83 F8 03	cmp eax,03		; ammo cart?
	74 04		je 4D94E4		; if yes -> move catapult to war machine slot 3
	5D		pop ebp			; (cleanup)
	C2 0400		ret 04			; return

	89 81 A5010000	mov [ecx+1A5],eax	; move catapult to war machine slot 3
	EB F4		jmp 4D94E0		; -> (cleanup)

	----------	-------------------------------------------------------------------------
	063DFE~E04	; ""
	----------	-------------------------------------------------------------------------
	E8 E9560700	call 4D94EC		; -> free space (war machine removal)
	90 90		nop			; -

	----------	-------------------------------------------------------------------------
	0D94EC~50E	; (INLINE EDIT - OVERWRITES ORIGINAL WAR MACHINE REMOVAL CODE)
	----------	-------------------------------------------------------------------------
	8BBC81CC530000	mov edi,[ecx+eax*4+53CC]; EDI = hero data
	85 FF		test edi,edi		; was there a hero in this slot?
	74 10		je 4D9507		; if no -> (displaced code)

	80BF9D01000003	cmp byte [edi+19D],03	; catapult in war machine slot 2?
	75 07		jne 4D9507		; if no -> (displaced code)
	C6879D01000005	mov byte [edi+19D],05	; move ammo cart to war machine slot 2

	8B9481BC540000	mov edx,[ecx+eax*4+54BC]; (displaced code)
	C3		ret			; return (0D950F~3F is free space)

What we're doing in the above code is intercepting the routine that removes destroyed artifacts from a
hero's inventory and checking specifically for an ammo cart. Ballistas and first aid tents are disabled
for the remainder of the combat by virtue of simply being dead and thus no longer able to function, but
ammo carts work by checking the player's inventory for an ammo cart rather than the physical object on
the battlefield. To get around this, we invisibly replace the ammo cart with a catapult whenver it gets
destroyed, and then in the post-battle cleanup we replace any catapult in slot 2 with an ammo cart.

Moving on, the Blacksmith code is pretty unoptimized, so we can rewrite it to allow for any combination
of war machine distribution that we wish, as well as uncoupling Stronghold's ballista from Castle:

	---------	-------------------------------------------------------------------------
	1C3220~8F	; OPTIMIZED BLACKSMITH CODE
	---------	-------------------------------------------------------------------------
	6A 04		push 04			; 04 = Ballista
	58		pop eax			; ""
	6A 05		push 05			; 05 = Ammo Cart
	59		pop ecx			; ""
	6A 06		push 06			; 06 = First Aid Tent
	5A		pop edx			; ""

	A3 60AA6A00	mov [6AAA60],eax	; Castle gets a Ballista (EAX)
	90		nop			; -
	89 15 68AA6A00	mov [6AAA68],edx	; Rampart gets a First Aid Tent (EDX)
	89 0D 70AA6A00	mov [6AAA70],ecx	; Tower gets an Ammo Cart
	89 0D 78AA6A00	mov [6AAA78],ecx	; Inferno gets an Ammo Cart
	89 15 80AA6A00	mov [6AAA80],edx	; Necropolis gets a First Aid Tent (EDX)
	A3 88AA6A00	mov [6AAA88],eax	; Dungeon gets a Ballista (EAX)
	90		nop			; -
	89 0D 90AA6A00	mov [6AAA90],ecx	; Stronghold gets an Ammo Cart (EXX)
	89 15 98AA6A00	mov [6AAA98],edx	; Fortress gets a First Aid Tent (EAX)
	A3 A0AA6A00	mov [6AAAA0],eax	; Conflux gets a Ballista (EAX)
	90		nop			; -

	83 C8 FF	or eax,-01		; cleanup (adds terminator to each address)
	A3 64AA6A00	mov [6AAA64],eax	; ""
	A3 6CAA6A00	mov [6AAA6C],eax	; ""
	A3 74AA6A00	mov [6AAA74],eax	; ""
	A3 7CAA6A00	mov [6AAA7C],eax	; ""
	A3 84AA6A00	mov [6AAA84],eax	; ""
	A3 8CAA6A00	mov [6AAA8C],eax	; ""
	A3 94AA6A00	mov [6AAA94],eax	; ""
	A3 9CAA6A00	mov [6AAA9C],eax	; ""
	A3 A4AA6A00	mov [6AAAA4],eax	; ""
	C3		ret			; return

	--------	-------------------------------------------------------------------------
	1D3FB0~4	; CUSTOMIZE WHICH FACTION'S BLACKSMITH THE BALLISTA YARD LOOKS AT
	--------	-------------------------------------------------------------------------
	E8 DBF2FEFF	call 5C3290		; -> free space

	--------	-------------------------------------------------------------------------
	1C3290~C	; (INLINE EDIT - OVERWRITES ORIGINAL BLACKSMITH CODE)
	--------	-------------------------------------------------------------------------
	8B 49 10	mov ecx,[ecx+10]	; (displaced code)
	6A XX		push XX			; XX = Faction ID (presumably one with a Ballista)
	5A		pop edx			; ""
	C3		ret			; return
	909090909090	nop			; -

This optimized code highlights the inherent difficulty of making simpler inline changes to the original
code: moving EAX (the ballista) into position is a shorter opcode than for ECX (ammo cart) or EDX (first
aid tent). Changing an ammo cart into a first aid tent or vise versa is thus a simple one-byte edit, but
you're stuck with three of something even if you change what gets loaded into each register unless you
rewrite the code to include space for editing (note the padding bytes in the above code following each
EAX move). If we were especially strapped for space, we could free up a few more bytes by using EAX for
all three machines, but what we see above is much easier to edit.

We can also look into treating Catapults like other war machines, meaning that they're purchased from a
Blacksmith rather than every hero automatically coming equipped with one. The first thing we'll need to
do in this regard is get rid of the code that gives every hero a Catapult and prevents trading them:

    0D8BDD > EB 08 ; heroes do not come equipped with a Catapult (0D8BDF~E6 is free)
    0DE112 > EB 30 ; do not prevent moving/trading Catapult (0DE114~43 is free)
    1AFA98 > EB 07 ; "" (1AFA9A~A0 is free)

We then need to prevent the game from giving the hero a Catapult in siege battles if they don't actually
have one (the game never originally checked for this for some reason). We do make an exception here for
AI heroes since the AI is retarded enough without potentially denying them a critical piece of hardware.

	--------	-------------------------------------------------------------------------
	063351~7	; DO NOT LOAD CATAPULT FOR SIEGE BATTLES IF HERO DOESN'T HAVE ONE
	--------	-------------------------------------------------------------------------
	E8 BEAD0700	call 4DE114		; -> free space (move/trade Catapult)
	75 F7		jne 46334F		; if no Catapult (human player) -> [exit]

	---------	-------------------------------------------------------------------------
	0DE114~31	; (EXPANDED SPACE - OVERWRITES INABILITY TO MOVE/TRADE CATAPULT)
	---------	-------------------------------------------------------------------------
	A1 FCCC6900	mov eax,[69CCFC]	; EAX = active player data
	8A 80 E1000000	mov al,[eax+E1]		; AL = AI flag
	84 C0		test al,al		; human player?
	75 06		jne 4DE129		; if yes -> check for Catapult

	8B C6		mov eax,esi		; (displaced code)
	6B C0 08	imul eax,eax,08		; ""
	C3		ret			; return

	83B99501000003	cmp [ecx+195],03	; does hero have a Catapult equipped?
	EB F1		jmp 4DE123		; -> (displaced code)

Since it's important for every town to have access to Catapults, they will be sold additionally to that
town's war machine rather than in lieu of it. We'll accomplish this by hijacking Conflux's war machine,
so we'll first set 242EC0 to 91 and then replace the "Conflux gets a Ballista" instruction in the above
code with 48 A3 A0AA6A00 (Conflux gets a Catapult). Then, we simply the Blacksmith routine to run twice:
once for the standard war machine, and then again with the town type set to "08" (Conflux) so we'll get
offered a Catapult. We check for a Conflux town before the first run and then manually set it to another
town type that sells the same type of machine as Conflux does, similar to how the Ballista Yard works.

	--------	-------------------------------------------------------------------------
	1D3D4A~E	; BLACKSMITHS SELL CATAPULTS
	--------	-------------------------------------------------------------------------
	E8 C057F0FF	call 4D950F		; -> free space (war machine removal)

	---------	-------------------------------------------------------------------------
	0D950F~2A	; (EXPANDED SPACE - OVERWRITES WAR MACHINE REMOVAL WHEN DESTROYED
	---------	-------------------------------------------------------------------------
	83 FA 08	cmp edx,08		; Conflux?
	75 03		jne 4D9517		; if no -> buy war machine
	6A XX		push XX			; XX = town type that has Conflux's war machine
	5A		pop edx			; ""
	E8 148C0F00	call 5D2130		; buy war machine
	8B 43 38	mov eax,[ebx+38]	; EAX = ???
	8B 48 10	mov ecx,[eax+10]	; ECX = visiting hero ID
	6A 08		push 08			; EDX = 08 (Conflux - sells Catapults)
	5A		pop edx			; ""
	E8 068C0F00	call 5D2130		; buy catapult
	C3		ret			; return

---------------------------------------------------------------------------------------------------------

## TRADE BUILDINGS

The rates offered by all trade buildings are based on the number of Marketplaces that you control up to
a cap of 10. These values can be edited at the following addresses:

| MARKETPLACES           | ARTIFACT TRADERS        | FREELANCERS GUILD      |
|------------------------|------------------------|------------------------|
| (1) 278348 = 0.10      | (1) 278374 = 0.20      | (1) 2783A0 = 0.30      |
| (2) 27834C = 0.15      | (2) 278378 = 0.25      | (2) 2783A4 = 0.45      |
| (3) 278350 = 0.20      | (3) 27837C = 0.30      | (3) 2783A8 = 0.50      |
| (4) 278354 = 0.25      | (4) 278380 = 0.35      | (4) 2783AC = 0.65      |
| (5) 278358 = 0.30      | (5) 278384 = 0.40      | (5) 2783B0 = 0.70      |
| (6) 27835C = 0.35      | (6) 278388 = 0.45      | (6) 2783B4 = 0.85      |
| (7) 278360 = 0.40      | (7) 27838C = 0.50      | (7) 2783B8 = 0.90      |
| (8) 278364 = 0.45      | (8) 278390 = 0.55      | (8) 2783BC = 1.00      |
| (9) 278368 = 0.50      | (9) 278394 = 0.60      | (9) 2783C0 = 1.00      |
| (+) 27836C = 0.50      | (+) 278398 = 0.60      | (+) 2783C4 = 1.00      |


These values have a "double-dip" effect in that they control both the value you get for what you sell as
well as the markup for anything you buy. At 50%, for example, you'll get a 4:1 exchange rate for similar
resources because anything you buy will be valued at double the base cost while whatever you're selling
will be valued at half. The base costs in gold for artifacts and units are located in ArTraits.txt and
CrTraits.txt, whereas the base values for resources are specified at the following addresses:

    28C4D2 = FA 00 (Wood)	    28C4D4 = F4 01 (Mercury)	    28C4DA = F4 01 (Crystal)
    28C4D6 = FA 00 (Ore)	    28C4D8 = F4 01 (Sulfur)	        28C4DC = F4 01 (Gems)

Bearing the above in mind, there's an easy shortcut to figure out what any value we specfiy will do (and
therefore how to get the results we want). At, say, 0.40, that is the exact value we'll get for anything
we sell - 1 mercury (base value of 500) will get us 200 gold. To obtain the cost of buying it, then, we
just invert the fraction: 2/5 -> 5/2, or 2.50. Were we to trade our mercury for gems, we would pay a 7:1
ratio since each unit we buy will be valued at 1,250 gold while each unit that we sell is worth 200.

Trading Posts, Black Markets, and Freelancers' Guilds on the adventure map offer static exchange rates
equivalent to controlling five marketplaces, meaning that beyond this point they're actually worse than
what you have back at home. It's uncommon on most maps, however, to reach this point until the game is
almost over; in most cases, these objects offer rates so far beyond what you'd otherwise get that many
random map templates simply ban them outright. We could just lower their effectiveness by changing the
values at 1EA4CB (Trading Posts), 1EA517 (Black Markets), and 1EA26B (Freelancers' Guilds), but that's a
band-aid solution at best that fails to address the larger problem of them being obsoleted by your own
markets. So, let's change them to always offer rates one step better than your own markets. We'll need
some free space for this, and I've chosen to obtain that space by reducing the market cap from 10 to a
more reasonable value of 5 - with internal markets capping at 4 so that the external markets will always
be superior. We then compress the data from the above tables and create space there like so:

                MARKETPLACES                 ARTIFACT TRADERS              FREELANCERS GUILD
        ----------------------------   ----------------------------   ----------------------------
        (1) 278348 = 0.25 (0000803E)   (1) 27835C = 0.50 (0000003F)   (1) 278370 = 0.80 (CDCC4C3F)
        (2) 27834C = 0.33 (ABAAAA3E)   (2) 278360 = 0.66 (ABAA2A3F)   (2) 278378 = 0.85 (9A99593F)
        (3) 278350 = 0.40 (CDCCCC3E)   (3) 278364 = 0.80 (CDCC4C3F)   (3) 27837C = 0.90 (1FBA683F)
        (4) 278354 = 0.45 (2FBAE83E)   (4) 278368 = 0.90 (1FBA683F)   (4) 278380 = 0.95 (3333733F)
        (+) 278358 = 0.50 (0000003F)   (+) 27836C = 1.00 (0000803F)   (+) 278384 = 1.00 (0000803F)
        ----------------------------   ----------------------------   ----------------------------
         1EA45A: 0A > 04 (Rate Cap)     1EA1FC: 0A > 04 (Rate Cap)     1EA380: 0A > 04 (Rate Cap)

        1ED2BE > 6C	; update pointer for Freelancer's Guild rates
        124A5D > 58	; update pointer for Artifact Traders/Black Market rates
        1EC10C > 58	; ""
        1EC826 > 58	; ""
        1ED218 > 58 ; ""
        1EDFDA > 58	; ""
        1EE083 > 58	; ""
        1EE64D > 58	; ""
        1EE78A > 58	; ""
        1EE8F6 > 58	; ""

	---------	-------------------------------------------------------------------------
	1EA4C0~F4	; TRADING POST RATES TO PLAYER MARKETS +1
	---------	-------------------------------------------------------------------------
	FF 05 013B6700	inc [673B01]		; set "temp" flag for market count routine
	E8 15FFFFFF	call 5EA3E0		; -> [count player's markets]
	FF 0D 013B6700	dec [673B01]		; clear "temp" flag
	31 C0		xor eax,eax		; (optimized/displaced original code)
	A3 0CAB6A00	mov [6AAB0C],eax	; ""
	40		inc eax			; ""
	A3 2CAB6A00	mov [6AAB2C],eax	; ""
	A1 38956900	mov eax,[699538]	; ""
	05 64F60100	add eax,1F664		; ""
	A3 DCAA6A00	mov [6AAADC],eax	; ""
	FF 05 00AB6A00	inc [6AAB00]		; +1 player markets
	EB 3B		jmp 5EA530		; -> [exit]

	---------	-------------------------------------------------------------------------
	1EA500~2F	; BLACK MARKET RATES TO PLAYER MARKETS +1
	---------	-------------------------------------------------------------------------
	89 0D E0AA6A00	mov [6AAAE0],ecx	; (optimized/displaced original code)
	89 15 DCAA6A00	mov [6AAADC],edx	; ""
	FF 05 013B6700	inc [673B01]		; set "temp" flag for market count routine
	E8 C9FEFFFF	call 5EA3E0		; -> [count player's markets]
	FF 0D 013B6700	dec [673B01]		; clear "temp" flag
	6A 02		push 02			; (optimized/displaced original code)
	58		pop eax			; ""
	A3 2CAB6A00	mov [6AAB2C],eax	; ""
	A3 0CAB6A00	mov [6AAB0C],eax	; ""
	FF 05 00AB6A00	inc [6AAB00]		; +1 player markets

	---------	-------------------------------------------------------------------------
	1EA260~9E	; (EXTERNAL) FREELANCER'S GUILD RATES TO PLAYER MARKETS +1
	---------	-------------------------------------------------------------------------
	89 0D E0AA6A00	mov [6AAAE0],ecx	; (optimized/displaced original code)
	FF 05 013B6700	inc [673B01]		; set "temp" flag for market count routine
	E8 6F010000	call 5EA3E0		; -> [count player's markets]
	FF 0D 013B6700	dec [673B01]		; clear "temp" flag
	6A 03		push 03			; (optimized/displaced original code)
	58		pop eax			; ""
	A3 2CAB6A00	mov [6AAB2C],eax	; ""
	40		inc eax			; ""
	A3 0CAB6A00	mov [6AAB0C],eax	; ""
	A1 38956900	mov eax,[699538]	; ""
	05 64F60100	add eax,1F664		; ""
	A3 DCAA6A00	mov [6AAADC],eax	; ""
	FF 05 00AB6A00	inc [6AAB00]		; +1 player markets
	E9 91020000	jmp 5EA530		; -> [exit]

	---------	-------------------------------------------------------------------------
	1EA453		; EXIT PLAYER MARKET COUNT ROUTINE FOR EXTERNAL BUILDINGS
	---------	-------------------------------------------------------------------------
	E9 2CDF0800     jmp 678384		; -> free space
	90		nop			; -

	---------	-------------------------------------------------------------------------
	278384~AE	; (EXPANDED SPACE - OVERWRITES RATES FOR 6-10 MARKETS)
	---------	-------------------------------------------------------------------------
	8B 0D 00AB6A00	mov ecx,[6AAB00]	; (displaced code)
	A0 013B6700	mov al,[673B01]		; AL = "temp" flag
	A8 01		test al,01		; is this an external market?
	0F84 C220F7FF	je 5EA459		; if no -> [exit to original code]
	83 F9 04	cmp ecx,04		; player markets = 4? (maximum -1)
	EB 04		jmp 6783A0		; (skip next 4 bytes)
	90 90 90 90	nop			; (this space is unusable)
	7E 03		jle 6783A5		; if less or equal -> (cleanup)
	49		dec ecx			; -1 player markets
	EB F2		jmp 678397		; -> player markets = 4?
	89 0D 00AB6A00	mov [6AAB00],ecx	; set market rate
	5F		pop edi			; (cleanup)
	5F		pop edi			; ""
	5E		pop esi			; ""
	C3		ret 			; return (2783AF~C7 is free space)

---------------------------------------------------------------------------------------------------------

## FORT, CITADEL & CASTLE

The growth bonuses of the Citadel and Castle can be changed with the following code:

	------------	-------------------------------------------------------------------------
	1BFFF7~C004F	; CITADEL & CASTLE GROWTH BONUSES
	------------	-------------------------------------------------------------------------
	0F BF 44 90 44	movsx eax,[eax+edx*4+44]; ~~~needs commentary
	8B 96 50010000	mov edx,[esi+150]	;
	89 45 F8	mov [ebp-8],eax		;
	89 D0		mov eax,edx		;
	23 05 E0CD6600	and eax,[66CDE0]	;
	89 F9		mov ecx,edi		;
	23 0D E4CD6600	and ecx,[66CDE4]	;
	09 C8		or eax,ecx		;
	74 0B		je ???			;
	DB 45 F8	fld [ebp-8]		;
	D8 0D 46005C00	fmul [5C0046]		;
	EB 26		jmp ???			;
	A1 D8CD6600	mov eax,[66CDD8]	;
	8B 0D DCCD6600	mov ecx,[66CDDC]	;
	21 C2		and edx,eax		;
	21 CF		and edi,ecx		;
	09 FA		or edx,edi		;
	74 16		je 5C004D		;
	DB 45 F8	fld [ebp-8]		;
	D8 0D 42005C00	fmul [5C0042]		;
	EB 08		jmp 5C004A		;
	XX XX XX XX	(floating value)	;
	YY YY YY YY	(floating value)	;
	DB 4D F8	fstp [ebp-8]		;
	8B 55 F8	mov edx,[ebp-8]		;

"XX XX XX XX" and "YY YY YY YY" in the above example are floating-point values for the growth bonuses of
the Citadel and Castle, respectively. We've seen these several times already now, but like the elemental
orbs we want values of 1.XX% here instead of the usual 0.XX% ones. Thus...

	20% - 9A 99 99 3F	25% - 00 00 A0 3F	 75% - 00 00 E0 3F
	40% - 33 33 B3 3F	33% - AA AA AA 3F	100% - 00 00 00 40
	60% - CD CC CC 3F	50% - 00 00 C0 3F	125% - 00 00 10 40
	80% - 66 66 E6 3F	66% - 50 55 D5 3F	150% - 00 00 20 40

Regarding the defensive structures put in place by these buildings, namely walls and arrow towers, their
HP is specified in Walls.txt and, despite the fact that everything just has a flat 2 HP across the board
by default, not only has independent values for each part, but can also have different values depending
on what type of town it is (i.e. Castle, Rampart). Note that many of the items listed in Walls.txt are
not actually used; see below for the only ones that actually are:

				Upper Tower
				Upper Wall
				Mid-Upper Wall
				Gate
				Mid-Lower Wall
				Lower Wall
				Lower Tower
				Keep

>(Note: the gate and four "wall" segments get +1 HP with a Castle built)

The damage dealt by moats varies depending on the town and can be edited as desired:

	Castle      23BD18	Rampart     23BD1C	Tower       23BD20
	Inferno     23BD24	Necropolis  23BD28	Dungeon     23BD2C
	Stronghold  23BD30	Fortress    23BD34	Conflux     23BD34

Because Tower's "moat" is actually land mines (as the spell), it behaves a little differently. The value
at 23BD20 is a damage minimum that can be surpassed depending on the magic power of the defending hero.
Also like the spell, the mines can not be triggered by any unit native to the terrain and they'll be
removed by Dispel at sufficient expertise without the fix from earlier.

As for the damage dealt by arrow towers, they use a very cryptic damage formula that increases with the
total number of buildings constructed in the town, with the two "side" towers dealing roughly half as
much damage as the main one. It's a good idea in concept since it reflects them getting stronger as the
town grows larger, but it's a pain in the ass to customize and I'd really rather just have a table like
moats do where I can set minimum and maximum damage values for each type of town.

So, that's exactly what I did. We already have the space we need since the moat damage table uses DWORD
(4-byte) values for each faction when it only really needs one (if your idea of fun is moats that deal
over 255 damage, please stop designing games). Thus, we split the moat damage table in half, with it and
arrow towers each getting two bytes per faction. The moat code is slightly modified to account for this
(still using only one byte for static damage) while the arrow towers use both (minimum, maximum).

This will actually end up freeing a large amount of space in the right-click information code since we
end up simplifying it, some of which is used to make water moats (Castle or Conflux) only deal damage to
units with immunity to fire. Fire-immune units, in turn, will not take damage from Inferno's lava moat.
The damage taken by fire-immune units in water moats will be specified in what should be the moat damage
slot for Tower - Tower instead will pull its minimum mine damage from a different location.

Finally, one other thing that you will need to do in addition to implementing the below code is delete
the name "Keep" (unearneath "Lower Tower") for each faction in Walls.txt. This is so we can blank out a
now-unused string in the simplified right-click textbox in the code below. And now, on with the edit:

	0657BD > 45	; adjusted jump length
	0657D1 > 31	; ""

	01E3A4 7D > 4D	; arrow tower damage is now properly reduced by Air Shield & Armorer
	01E4E0 7D > 4D	; ""
	065944 7D > 4D	; ""

	---------	-------------------------------------------------------------------------
	065900~23	; ARROW TOWER DAMAGE
	---------	-------------------------------------------------------------------------
	8B 97 C8530000	mov edx,[edi+53C8]	; EDX = town data
	0FBE 42 04	movsx eax,[edx+04]	; EAX = town type
      0FBE0C452ABD6300	movsx ecx,[eax*2+63BD2A]; ECX = minimum damage
      0FBE14452BBD6300	movsx edx,[eax*2+63BD2B]; EDX = maximum damage
	E8 A16E0A00	call 50C7C0		; (EAX = min~max)
	89 45 08	mov [ebp+08],eax	; store damage
	EB 10		jmp 465934		; -> [exit]

	---------	-------------------------------------------------------------------------
	079C5A-70	; ARROW TOWER DAMAGE (RIGHT CLICK)
	---------	-------------------------------------------------------------------------
	8B 89 C8530000	mov ecx,[ecx+53C8]	; ECX = town data
	31 C0		xor eax,eax		; EAX = 0
	E8 B2000000	call 479D19		; -> free space (same routine)
	31 DB		xor ebx,ebx		; EBX = 0
	6A 00		push 00			; final character of textbox = 0
	50		push eax		; push maximum damage
	56		push esi		; push minimum damage
	8B 75 08	mov esi,[ebp+08]	; ESI = ???
	90		nop			; -

	---------	-------------------------------------------------------------------------
	079D03-3A	; ""
	---------	-------------------------------------------------------------------------
	6A 00		push 00			; Unused
	6A 00		push 00			; ""
	6A 0F		push 0F			; Move to unused slot for string
	8D 55 CC	lea edx,[ebp-34]	; ???
	52		push edx		; ???
	8B CE		mov ecx,esi		; ???
	E8 ECFEFFFF	call 479C00		; ???
	E9 84000000	jmp 479D9D		; frees space: 079D19~9C

	8A 59 04	mov bl,[ecx+04]		; EBX = town type
	8A045D2ABD6300	mov al,[ebx*2+63BD2A]	; EAX = minimum damage
	8B F0		mov esi,eax		; ESI = minimum damage
	8A1C5D2BBD6300	mov bl,[ebx*2+63BD2B]	; EBX = maximum damage
	52		push edx		; store EDX
	B8 67666666	mov eax,66666667	; EDX = maximum damage / 10
	F7 EB		imul ebx		; ""
	C1 FA 02	sar edx,02		; ""
	8B C2		mov eax,edx		; EAX = maximum damage / 10
	5A		pop edx			; retrtieve EDX
	C3		ret			; ret

	--------	-------------------------------------------------------------------------
	069A81~B	; MOAT DAMAGE
	--------	-------------------------------------------------------------------------
	0FBE 5A 04	movsx ebx,[edx+04]	; EBX = town type
	E8 B1020100	call 479D3B		; -> free space (arrow tower right click info)
	90 90		nop			; -

	---------	-------------------------------------------------------------------------
	0B31C9~D3	; MOAT DAMAGE (AI SETTINGS)
	---------	-------------------------------------------------------------------------
	53		push ebx		; store EBX
	0FBE 5A 04	movsx ebx,[edx+04]	; EBX = town type
	E8 5127FBFF	call 465924		; -> free space (old arrow tower damage formula)
	5B		pop ebx			; retrieve EBX

	---------	-------------------------------------------------------------------------
	0B31FD~207	; MOAT DAMAGE (AI SETTINGS)
	---------	-------------------------------------------------------------------------
	53		push ebx		; store EBX
	0FBE 5A 04	movsx ebx,[edx+04]	; EBX = town type
	E8 1D27FBFF	call 465924		; -> free space (old arrow tower damage formula)
	5B		pop ebx			; retrieve EBX

	---------	-------------------------------------------------------------------------
	065924~33	; (INLINE EDIT - OVERWRITES ORIGINAL ARROW TOWER DAMAGE FORMULA)
	---------	-------------------------------------------------------------------------
	57		push edi		; store EDI
	8B FE		mov edi,esi		; EDI = unit stack data
	E8 0F440100	call 479D3B		; -> free space (arrow tower right click info)
	8B D3		mov edx,ebx		; EDX = barricade damage
	5F		pop edi			; retrieve EDI
	C3		ret			; return
	90 90 90 90	nop			; -

	---------	-------------------------------------------------------------------------
	079D3B~6A	; (EXPANDED SPACE - OVERWRITES ARROW TOWER RIGHT CLICK INFO)
	---------	-------------------------------------------------------------------------
	50		push eax		; store EAX
	0FBE 47 34	movsx eax,[edi+34]	; EAX = Unit ID
	2C 10		sub al,10		; AL -10
	3C 77		cmp al,77		; is AL > 77? (table end = Rust Dragons)
	77 06		ja 479D4C		; if yes -> AL = moat damage
	8A A0 58A64400	mov ah,[eax+44A658]	; AH = resistance A
	8A045D18BD6300	mov al,[ebx*2+63BD18]	; AL = moat damage
	80 FC 05	cmp ah,05		; O-Fire?
	75 0F		jne 479D67		; if no -> BL = moat damage
	84 C0		test al,al		; is damage 0? (Castle/Conflux moat)
	75 04		jne 479D60		; if no -> Inferno?
	B3 02		mov bl,02		; BL = 2 (Tower)
	EB EC		jmp 479D4C		; -> AL = moat damage
	80 FB 03	cmp bl,03		; Inferno?
	75 02		jne 479D67		; if no -> BL = moat damage
	31 C0		xor eax,eax		; no damage
	88 C3		mov bl,al		; BL = moat damage
	58		pop eax			; retrieve EAX
	C3		ret			; return (079D6B~9C is free space)

	---------	-------------------------------------------------------------------------
	23BD18~3B	; BARRICADE & TURRET DAMAGE TABLE
	---------	-------------------------------------------------------------------------
	00 00		; Castle Moat (no damage)
	XX 00		; Rampart Brambles
	XX 00		; Castle/Conflux Moat (fire-immune units)
	XX 00		; Inferno Lava
	XX 00		; Necropolis Boneyard
	XX 00		; Dungeon Tar
	XX 00		; Stronghold Spikes
	XX 00		; Fortress Tar
	00 00		; Conflux Moat (no damage)

	XX YY		; Castle Arrow Tower (XX = minimum, YY = maximum)
	XX YY		; Rampart ""
	XX YY		; Tower ""
	XX YY		; Inferno ""
	XX YY		; Necropolis ""
	XX YY		; Dungeon ""
	XX YY		; Stronghold ""
	XX YY		; Fortress ""
	XX YY		; Conflux ""

	065FDD > BE XX 00000090	; Tower Land Mines

------------------------------------------------------------------------------------------

Finally, the units which operate the arrow towers for each town are named below:

	Castle      23CF88	Rampart     23CFA8	Tower       23CFC8
	Inferno     23CFE8	Necropolis  23D008	Dungeon     23D028
	Stronghold  23D048	Fortress    23D068	Conflux     23D088

Note that these are purely graphical settings which don't affect gameplay at all, but they may help you
come up with appropriate values for the damage table above (i.e. Necropolis towers are manned by Liches
and should therefore probably do more damage than towers manned by normal Archers). Also note that arrow
towers use the ranged attack animation of whatever unit is manning them, so the game will crash if you
specify a unit that doesn't have a ranged attack (such as Sprites for Conflux).

Finally, on a completely unrelated note, I suggest renaming both Castles and Arrow Towers to something
less confusable with the factions of the same name (my hack refers to them as "Bastion" and "Turret").
Similarly, since only Castle and Conflux towns have traditional moats (which are named as such), it's a
good idea to replace the generic term with something more all-inclusive (I recommend "Barricade").

---------------------------------------------------------------------------------------------------------

## TOWN INCOME

The income from Halls/Capitol buildingds is specified at the following addresses:

   Village Hall: 1BFA1B (F4 01 00 00 = 500)   City Hall: 1BFA49 (D0 07 00 00 = 2000)
      Town Hall: 1BFA2E (E8 03 00 00 = 1000)    Capitol: 1BFA64 (A0 0F 00 00 = 4000)

-----------------------------------------------------------------------------------------

## RESOURCE SILOS & MYSTIC POND

The yield from Resource Silos per town type is specified by a table starting at 288F04.

	TOWN TYPE	Wood	Merc	Ore	Sulf	Crys	Gems	Gold
	----------------------------------------------------------------------
	Castle		288F04	288F08	288F0C	288F10	288F14	288F18	288F1C
	Rampart		288F20	288F24	288F28	288F2C	288F30	288F34	288F38
	Tower		288F3C	288F40	288F44	288F48	288F4C	288F50	288F54
	Inferno		288F58	288F5C	288F60	288F64	288F68	288F6C	288F70
	Necropolis	288F74	288F78	288F7C	288F80	288F84	288F88	288F8C
	Dungeon		288F90	288F94	288F98	288F9C	288FA0	288FA4	288FA8
	Stronghold	288FAC	288FB0	288FB4	288FB8	288FBC	288FC0	288FC4
	Fortress	288FC8	288FCC	288FD0	288FD4	288FD8	288FDC	288FE0
	Conflux		288FE4	288FE8	288FEC	288FF0	288FF4	288FF8	288FFC

If you wish to remove Resource Silos from the game, set 06101C~22 to 90909090909090 and
0B888C to E9 5C010000. This will free 0B8891~9EC as well as the table above (288F04~FF).
It also frees up 12 bytes in the building dependency table for each town.

The maximum and minimum values of resources produced by the Mystic Ponbd are specified at
0C7E5A and 0C7E62, respectively. The possible resources it can generate are specified at
23E668 (Mercury), 23E66C (Sulfur), 23E670 (Crystal), and 23E674 (Gems).

-----------------------------------------------------------------------------------------

## TAVERNS

Whenever the game initially loads the weekly bartender dialogue, it has a roughly 1 in 3
chance each of a random line from RandTvrn.txt, a random rumor from the map, or one of a
clue about the location of the Grail or a random piece of advice from your Thieves Guild
	(i.e. "X" player makes the most gold). If you wish to change this, the addresses to edit
are 0C0118/0C8A0F (21h) and 0C0126/0C8A1D (42h), which are the odds of a RandTvrn line
and a map rumor, respectively, out of 64h. These are checked in succession, meaning that
a value of 0-20 brings you to one result, 21-41 to another, else you get the grail hint
or thieves guild info. If the map has no rumors, it will fail over to RandTvrn advice,
as will the grail hint if the map has no obelisks.

Personally, I feel that if a map has any rumors, then that's what should always appear.
As for the grail hints, I find them largely unncessary in the original game since they
don't tell you anything that an obelisk or two won't and completely unneccessary if you
require finding them all to dig for the grail in the first place (something we'll learn
how to do later in this guide). The Thieves Guild info is even more useless since it's
all information you can see just by clicking on the Thieves' Guild button yourself. To
that end, we can simplify the code by just always calling the map rumor routine:

	--------	-------------------------------------------------------------------------
	0C0107~F	; TAVERN DIALOGUE TO ALWAYS MAP RUMORS, ELSE RANDOM
	--------	-------------------------------------------------------------------------
	8B CB		mov ecx,ebx		; ECX = main index
	E8 62CB0000	call 4CCC70		; get random map rumor (RandTvrn if none)
	EB 27		jmp 4C0137		; -> [continue] (0C0110~36 is free space)

	----------	-------------------------------------------------------------------------
	0C89FE~A06	; ""
	----------	-------------------------------------------------------------------------
	8B CB		mov ecx,ebx		; ECX = main index
	E8 6B420000	call 4CCC70		; get random map rumor (RandTvrn if none)
	EB 27		jmp 4C8A2E		; -> [continue] (0C8A07~2D is free space)

This removes the grail hint/thieves guild advice routine entirely, freeing up by far the
largest amount of contiguous free space in this guide (0CCE2D~D3CF). Another change that
we can make is to have the tavern advice update daily instead of weekly, which will have
us slightly modify the second code block above like so:

	--------	-------------------------------------------------------------------------
	0C7CB2~7	; DAILY TAVERN DIALOGUE SWAPS
	--------	-------------------------------------------------------------------------
	E8 490D0000	call 4C8A00		; update tavern dialogue
	90		nop			; -

	----------	-------------------------------------------------------------------------
	0C89FE~A0D	; "" (INLINE EDIT) + DIALOGUE IS NEVER THIEVES GUILD INFO
	----------	-------------------------------------------------------------------------
	EB 2E		jmp 4C8A2E		; skip dialogue updates during weekly routine
	8B CB		mov ecx,ebx		; ECX = main index
	E8 69420000	call 4CCC70		; get random map rumor (RandTvrn if none)
	8B 0D 08736900	mov ecx,[697308]	; (displaced code)
	C3		ret 			; return (0C8A0C~2D is free space)

A lesser-known effect of Taverns is that the right-click information you get from other
towns requires that you own two Taverns (set at 016DF7) in order to see even an estimate
of how many units are present. This is a pointless limitation, as well as an unnecessary
double dip since the Thieves' Guild already counts taverns to provide additional info.

On an entirely separate note, the right-click text for the morale boosts provided by the
tavern and brotherhood of the sword are for some reason hard-coded in the .exe instead of
pulled from one of the text files like everything else is. Here's a quick touchup that
adds in the missing line break and some parenthesis around the bonus:

		04BBB1 > 47 (moves pointer to tavern text)
		260B47 > 0A 25 73 20 28 2B 31 29 (tavern text)
		04BC1A > 3E (moves pointer to order text)
		260B3E > 0A 25 73 20 28 2B 32 29 (order text)

See also the "map locations" section below for more tavern-related edits.

-----------------------------------------------------------------------------------------

## SHIPYARDS

Infuriatingly to mapmakers everywhere, towns look south instead of north to determine if
they're on a coast and therefore if a Shipyard can be built. The reasoning for this makes
sense: it's the best way to ensure that the tile where the ship is placed (2 down, 1 left
or right) is actually accessible. Both mechanically and aesthetically, however, this is a
huge flop - it's difficult to make coastal towns in the map editor because the game wants
the coast on the same edge of town as its land entrance, and any town that does qualify
ends up looking super janky because of the awkward cutoff angle.

Let's have towns look to the north for a coastline, instead, by replacing "two tiles down
and one over" with "one tile up and three over". This will put some responsibility on the
mapmaker to ensure that the new tile is accessible, but it's infinitely less of a pain in
the ass (and looks a hell of a lot better) than the original setup.

	------	    ---------------------	------	    ---------------------
	1C0D9E	    ; SHIP COORDS LEFT		1C0DB8	    ; SHIP COORDS RIGHT
	------	    ---------------------	------	    ---------------------
	48	    dec eax	; (Y)-1		49	    dec ecx	; (Y)-1
	83 EA 03    sub edx,03	; (X)-3		83 C2 03    add edx,03	; (X)+3

The much more pressing issue with internal shipyards, however, is that they still offer
little advantage over the external ones in the rare cases in which they can actually be
built. Using some space we'll free later from the Idol of Fortune day 7 check, let's look
at addressing this by allowing internal shipyards to sell boats at a discounted price.

	--------	-------------------------------------------------------------------------
	1D2B57~B	; INTERNAL SHIPYARDS ARE CHEAPER
	--------	-------------------------------------------------------------------------
	E9 29E4ECFF	jmp 4A0F85		; free space (Idol of Fortune, day 7)

	---------	-------------------------------------------------------------------------
	0A0F85~9A	; (EXPANDED SPACE - OVERWRITES IDOL OF FORTUNE, DAY 7)
	---------	-------------------------------------------------------------------------
	FF 05 013B6700	inc [673B01]		; set "temp" flag for external shipyard
	E8 60131300 	call 5D22F0		; displaced code
	FF 0D 013B6700	dec [673B01]		; unset flag
	E9 C11B1300  	jmp 5D2B5C		; return

	---------	-------------------------------------------------------------------------
	1D286D~9A	; CHECK IF PLAYER CAN AFFORD TO PURCHASE A BOAT
	---------	-------------------------------------------------------------------------
	E8 29E7ECFF	call 4A0F9B		  ; -> free space (Idol of Fortune, day 7)
	6B C0 2D	imul eax,eax,2D		  ; EAX = player index
	3994C1840B0200	cmp [ecx+eax*8+20B84],edx ; does player have enough gold?
	7C 1D		jl 5D289B		  ; if no -> [disable buy button]

	E8 5DBEEFFF	call 4CE6E0		  ; ???
	8B 0D 38956900	mov ecx,[699538]	  ; ECX = main index

	E8 21E7ECFF	call 4A0FAF		  ; free space (Idol of Fortune, day 7)
	6B C0 2D	imul eax,eax,2D		  ; EAX = player index
	3994C16C0B0200	cmp [ecx+eax*8+20B6C],edx ; does player have enough wood?
	7D 4D		jge 5D28E7		  ; if no -> [disable buy button]
	90		nop			  ; -

	---------	-------------------------------------------------------------------------
	0A0F9B~BF	; (EXPANDED SPACE - OVERWRITES IDOL OF FORTUNE, DAY 7)
	---------	-------------------------------------------------------------------------
	8A 15 013B6700	mov dl,[673B01]		; DL = "temp" flag
	F6 C2 01	test dl,01		; external?
	BA F4010000	mov edx,1F4		; EDX = 500
	74 03		je 4A0FAE		; if no -> return
	6B D2 04	imul edx,edx,04		; EDX = 2,000
	C3		ret			; return

	8A 15 013B6700	mov dl,[673B01]		; DL = "temp" flag
	F6 C2 01	test dl,01		; external?
	6A 05		push 05			; EDX = 5
	5A		pop edx			; ""
	74 02		je 4A0FBF		; if no -> return
	01 D2 		add edx,edx		; EDX = 10
	C3		ret			; returns

	---------	-------------------------------------------------------------------------
	1D24E0		; GET GOLD COST FOR DIALOGUE WINDOW
	---------	-------------------------------------------------------------------------
	E9 DBEAECFF	jmp 4A0FC0		; free space (Idol of Fortune, day 7)

	------		-------------------------------------------------------------------------
	1D2535		; GET WOOD COST FOR DIALOGUE WINDOW
	------		-------------------------------------------------------------------------
	E9 A2EAECFF	jmp 4A0FDC		; free space (Idol of Fortune, day 7)

	---------	-------------------------------------------------------------------------
	0A0FC0~F8	; (EXPANDED SPACE - OVERWRITES IDOL OF FORTUNE, DAY 7)
	---------	-------------------------------------------------------------------------
	8A 0D 013B6700	mov cl,[673B01]		; DL = "temp" flag
	F6 C1 01	test cl,01		; external?
	74 07		je 4A0FD2		; if no -> push "500"
	68 F6C36800	push 68C3F6		; push "2000"
	EB 05		jmp 4A0FD7		; return
	68 F2C36800	push 68C3F2		; push "500"
	E9 09151300	jmp 5D24E5		; return

	8A 0D 013B6700	mov cl,[673B01]		; DL = "temp" flag
	F6 C1 01	test cl,01		; external?
	74 07		je 4A0FEE		; if no -> push "5"
	68 EFC36800	push 68C3EF		; push "5"
	EB 05		jmp 4A0FF3		; return
	68 EDC36800	push 68C3ED		; push "10"
	E9 42151300	jmp 5D253A		; return
	90		nop			; -

	---------	-------------------------------------------------------------------------
	28C3EC~FB	; DIALOGUE BOX TEXT STRINGS (GOLD & WOOD COSTS)
	---------	-------------------------------------------------------------------------
	00		; -
	35 00		; 68C3EF = "5"
	31 30 00	; 68C3ED = "10"
	35 30 30 00	; 68C3F2 = "500"
	32 30 30 30 00	; 68C3F6 = "2000"
	00		; -

	1D3BD9 > 0CFEFFFF ; -500 Gold (internal shipyards)
	1D3C0A > FB	  ; -5 Wood ("")

	09E1D8 = E8030000 ; 1000 gold (external shipyards)
	09E1EB = 0A	  ; 10 wood ("" - unchanged)

	09E262 = 18FCFFFF ; -1000 gold (external shipyards)
	09E289 = F6	  ; -10 wood ("" - unchanged)

-----------------------------------------------------------------------------------------

## LIGHTHOUSES

This will fix the infamous bug wherein Castle Lighthouses increase ship movement for all
players instead of just the player that controls them. We will need some free space to do
so; I've chosen the space we freeed up earlier with out tavern dialogue edits.

	------		-------------------------------------------------------------------------
	0E4D40		; CASTLE LIGHTHOUSE BUGFIX
	------		-------------------------------------------------------------------------
	E9 CBB3FDFF	jmp 4C0110		; -> free space (tavern dialogue selection)
	90		nop			; -

	---------	-------------------------------------------------------------------------
	0C0110~2B	; (EXPANDED SPACE - OVERWRITES RANDOM SELECTION OF TAVERN DIALOGUE)
	---------	-------------------------------------------------------------------------
	8B 45 FC	mov eax,[ebp-04]	; EAX = hero data
	8A 40 04	mov al,[eax+04]		; AL = hero owner
	8A 51 01	mov dl,[ecx+01]		; DL = town owner
	38 D0		cmp al,dl		; does AL = DL?
	0F85 4B4C0200 	jne 4E4D6C		; if no -> [no bonus from Lighthouse]
	8B 81 50010000	mov eax,[ecx+150]	; (displaced code)
	E9 1A4C0200	jmp 4E4D46		; return (0C012C~36 is free space)

-----------------------------------------------------------------------------------------

## CASTLE GATE

The Inferno Castle Gate is problematic since it requires you to possess at least two
Inferno towns in order to be of any use whatsoever. However, we can allow it to warp us
to any other town we own (a one-way trip, mind, unless it's to another Inferno with a
Castle Gate) with a short edit to HD_SOD.dll: go to 03C2F0 and change 75 5D to EB 34.

Unfortunately, since this plugin is part of HD Mod, which is still being updated, the
above address is subject to change. Make sure that what you're editing is the correct
instruction (75 5D), by checking to see if the code just before it is 83 F8 03.

(Finally, again, this is another building that I'd recommend renaming to something less
confusing - not only does it have the same name as a faction, it's the WRONG faction!)

-----------------------------------------------------------------------------------------

## LOOKOUT TOWER & COVER OF DARKNESS

The radii of effect for these are set at 1BF4F1 (Tower) and 0C78D5 (Cover of Darkness).

-----------------------------------------------------------------------------------------

## SKELETON TRANSFORMER

When a dragon is placed into the Skeleton Transformer, you'll get a Bone Dragon instead
of a Skeleton. Rather than a coded exception, this is handled by a table specifying the
results of EVERY UNIT IN THE GAME when placed inside the transformer:

| Code   | Unit                 | Code    | Unit                    | Code    | Unit                   |
|--------|----------------------|---------|-------------------------|---------|------------------------|
| 4130C  | Pikeman              | 241344  | Centaur                 | 24137C  | Gremlin                |
| 41310  | Halberdier           | 241348  | Centaur Captain         | 241380  | Master Gremlin         |
| 41314  | Archer               | 24134C  | Dwarf                   | 241384  | Stone Gargoyle         |
| 41318  | Marksman             | 241350  | Battle Dwarf             | 241388 | Obsidian Gargoyle      |
| 4131C  | Griffin              | 241354  | Wood Elf                | 24138C  | Stone Golem            |
| 41320  | Royal Griffin        | 241358  | Grand Elf               | 241390  | Iron Golem             |
| 41324  | Swordsman            | 24135C  | Pegasus                 | 241394  | Mage                   |
| 41328  | Crusader             | 241360  | Silver Pegasus          | 241398  | Arch Mage              |
| 4132C  | Monk                 | 241364  | Dendroid                | 24139C  | Genie                  |
| 41330  | Zealot               | 241368  | Dendroid Soldier        | 2413A0  | Master Genie           |
| 41334  | Cavalier             | 24136C  | Unicorn                 | 2413A4  | Naga                   |
| 41338  | Champion             | 241370  | War Unicorn              | 2413A8 | Naga Queen             |
| 4133C  | Angel                | 241374  | Green Dragon            | 2413AC  | Giant                  |
| 41340  | Archangel            | 241378  | Gold Dragon              | 2413B0 | Titan                  |

| Code   | Unit                 | Code    | Unit                    | Code    | Unit                   |
|--------|----------------------|---------|-------------------------|---------|------------------------|
| 413B4  | Imp                  | 2413EC  | Skeleton                | 241424  | Troglodyte             |
| 413B8  | Familiar             | 2413F0  | Skeleton Warrior        | 241428  | Infernal Troglodyte    |
| 413BC  | Gog                  | 2413F4  | Walking Dead             | 24142C | Harpy                  |
| 413C0  | Magog                | 2413F8  | Zombie                  | 241430  | Harpy Hag              |
| 413C4  | Hell Hound           | 2413FC  | Wight                   | 241434  | Beholder               |
| 413C8  | Cerberus             | 241400  | Wraith                  | 241438  | Evil Eye               |
| 413CC  | Demon                | 241404  | Vampire                 | 24143C  | Medusa                 |
| 413D0  | Horned Demon         | 241408  | Vampire Lord             | 241440 | Medusa Queen           |
| 413D4  | Pit Fiend            | 24140C  | Lich                    | 241444  | Minotaur               |
| 413D8  | Pit Lord             | 241410  | Power Lich              | 241448  | Minotaur King          |
| 413DC  | Efreet               | 241414  | Black Knight            | 24144C  | Manticore              |
| 413E0  | Efreet Sultan        | 241418  | Dread Knight            | 241450  | Scorpicore             |
| 413E4  | Devil                | 24141C  | Bone Dragon             | 241454  | Red Dragon             |
| 413E8  | Arch Devil           | 241420  | Ghost Dragon            | 241458  | Black Dragon           |

| Code   | Unit                 | Code    | Unit                    | Code    | Unit                   |
|--------|----------------------|---------|-------------------------|---------|------------------------|
| 4145C  | Goblin               | 241494  | Gnoll                   | 2414E4  | Pixies                 |
| 41460  | Hobgoblin            | 241498  | Gnoll Marauder          | 2414E8  | Sprites                |
| 41464  | Wolf Rider           | 24149C  | Lizardman               | 2414CC  | Air Elemental          |
| 41468  | Wolf Raider          | 2414A0  | Lizard Warrior          | 241508  | Storm Elemental        |
| 4146C  | Orc                  | 2414AC  | Serpent Fly             | 2414D8  | Water Elemental        |
| 41470  | Orc Chieftain        | 2414B0  | Dragonfly               | 2414F8  | Ice Elemental          |
| 41474  | Ogre                 | 2414B4  | Basilisk                | 2414D4  | Fire Elemental         |
| 41478  | Ogre Mage            | 2414B8  | Greater Basilisk        | 241510  | Energy Elemental       |
| 4147C  | Roc                  | 2414A4  | Gorgon                  | 2414D0  | Earth Elemental        |
| 41480  | Thunderbird          | 2414A8  | Mighty Gorgon           | 241500  | Magma Elemental        |
| 41484  | Cyclops              | 2414BC  | Wyvern                  | 2414EC  | Psychic Elemental      |
| 41488  | Cyclops King         | 2414C0  | Wyvern Monarch          | 2414F0  | Magic Elemental        |
| 4148C  | Behemoth             | 2414C4  | Hydra                   | 241514  | Firebird               |
| 41490  | Ancient Behemoth     | 2414C8  | Chaos Hydra             | 241518  | Phoenix                |

| Code   | Unit                 | Code    | Unit                    | Code    | Unit                   |
|--------|----------------------|---------|-------------------------|---------|------------------------|
| 41538  | Peasant              | 241540  | Mummy                   | 24154C  | Troll                  |
| 41534  | Halfling             | 241530  | Sharpshooters            | 241524 | Faerie Dragons          |
| 4153C  | Boar                 | 24152C  | Enchanters              | 241528  | Rust Dragon            |
| 41548  | Rogue                | 2414DC  | Gold Golem              | 241520  | Crystal Dragons         |
| 41544  | Nomad                | 2414E0  | Diamond Golem           | 24151C  | Azure Dragon            |

-----------------------------------------------------------------------------------------

## NECROMANCY BOOSTERS

The 10% boost for the Necromancy Amplifier is specified at 0E4100 (D0 B8 63 00). You can
lower it to 5% (bearing in mind that the bonus is cumulative for each one you control) by
changing it to E4 EA 63 00. The 20% boost from the Soul Prison is specified at 0E411F.

>(For other values, see the skill-boosting artifacts entry from earlier)

Amplifiers don't stack (breaks Grail bonus): 0E4104 > EB 75 90
No Necromancy bonus from grail: 0E411D~22 > 90 90 90 90 90 90

-----------------------------------------------------------------------------------------

## MANA VORTEX

The building that provides this bonus is named at 1BDD08 (40) and 1BDD0E (44) while the
town is named at 1BDCEE. This information on its own isn't very helpful, but we're going
to come back around to it at the end of the next entry. What we can do for now, however,
is remove the "one hero per week" limitation by setting 1BDCFA to 90 90 90 90 90 90.

-----------------------------------------------------------------------------------------

## DEFENSIVE & GRAIL BUILDINGS

`~~~04C141 = 02 (rampart grail?)`

These will be discussed together since there's significant overlap between them. We'll
start by looking at the standard benefits provided by all grail buildings: +50% growth in
the town in which it's built and +5,000 gold per day (NOT week). The static value of the
latter is located at 1BFABE while the former can be disabled by setting 1C01AE from 74 to
EB for the actual effect and 1C63FF from 74 to EB for the right-click text; I have yet to
look into how to actually change the growth bonus to a different value.

The buildings which temporarily boost attributes of defending heroes all run through
one long routine starting at 063927 and can be edited at the following addresses:

	Tower Grail		Brimstone Clouds	Glyphs of Fear		Blood Obelisk
	-----------------	-----------------	-----------------	-----------------
	06392F: 68 = Bldg.	06395C: 40 = Bldg.	063A17: 58 = Bldg.	0639E6: 40 = Bldg.
	06393D: 6C = ""		06396A: 44 = ""		063A1F: 5C = ""		0639F4: 44 = ""
	******: ** = SP		063978: 78 = PWR	063A31: 77 = DEF	0639FE: 76 = ATK
	06394D: 96 = +150	06397C: 02 = +2		063A35: 02 = +2		063A02: 02 = +2

	Dungeon Grail		Stronghold Grail	Fortress Grail A	Fortress Grail B
	-----------------	-----------------	-----------------	-----------------
	06398A: 68 = Bldg.	0639B8: 68 = Bldg.	063A3E: 68 = Bldg.	<---
	063998: 6C = ""		0639C6: 6C = ""		063A44: 6C = ""		""
	0639A6: 78 = PWR	0639D4: 76 = ATK	063A7A: 77 = DEF	063A66: 76 = ATK
	0639AA: 0C = +12	0639D8: 14 = +15	063A63: 0A = +10	063A6E: ""

The Fortress grail uses the same value for both bonuses; to remove the attack bonus and
only boost one stat, NOP out the instructions (write all 90's) from 063A64 to 063A71.

The building IDs specified are relative to the town; i.e. why the Brimstone Stormclouds,
Blood Obelisk, and Mana Vortex (see previous entry) all have the same ID as do all of the
grail buildings. Which town goes to which part of the code is handled by a jump table:

			063C64 = Tower		(27 39 46 00)
			063C68 = Inferno	(54 39 46 00)
			063C6C = (Default)	(98 3A 46 00)
			063C70 = Dungeon	(82 39 46 00)
			063C74 = Stronghold	(B0 39 46 00)
			063C78 = Fortress	(DE 39 46 00)

By now, we should be familiar enough with these to know that each exit is a DWORD pointer
to the appropriate address in the code for each town. We also learned earlier that before
we reach this table, we take our faction ID and subtract the ID of the first faction on
the list (Tower). Thus, Tower becomes 00, Inferno becomes 01, and Necropolis - which has
no buildings that run through this routine - becomes 02, hence why the "default" exit is
positioned in the middle of the table. Castle, Rampart, and Conflux will also end up at
the same destination because subtracting 2 from 00 or 01 (Castle or Rampart) will wrap
around to FF/FE, after which any value higher than 05 (Fortress) is manually sent there.

>(063916 is FE, or -2. We'll look into changing this later.)

-----------------------------------------------------------------------------------------

The Conflux grail effect, widely regarded as the best, can be disabled with a few edits:

	      1BE4F3 > E9 7E000000 ; the actual effect (frees 1BE4F8~575)
	      1D743B > EB 2D       ; graphics (frees 1D743D~69)
	      1CE613 > EB 54       ; description & labels (frees 1CE615~68)
	      1CE81C > E9 B5000000 ; right click text (frees 1CE821~D5)

As you can see, this frees up a substantial amount of space, much of which we'll look
into using to improve the bonuses of other grail buildings.

-----------------------------------------------------------------------------------------

Contrary to the Conflux grail is the Inferno grail, whose effect is widely viewed as the
objective worst of the lot. We can edit the parameters at the following addresses:

	       ------	0C8613: Imp (week) & 0C8C3E (month)
	       Effect	0C861A: Familiar
	       ------	0C861E: +15 growth (replace with: BA XX 00 00 00 90)

	      -------	0CC957: (1C 13 = Imp)
	      Textbox	0CC95D: (90 13 = Familiar)
	      -------	0CC94F: +15 growth (replace with: B9 XX 00 00 00 90)

Changing the unit(s) affected by the grail is a simple ID swap for the actual effect, but
updating the textboxes will require a calculator. As you may remember from looking at the
Halfling luck text earlier, we multiply the desired unit ID by 74h and add 14h to get the
singular unit name (18h would give us plural). We then invert the two bytes when entering
them into the code, which comes out to D4 15 for Demons and 48 16 for Horny Demons.

Of course, one might wonder why we're going to all of this effort to edit a text variable
instead of just replacing the string (%s) in ArrayTxt.txt with the name of the new unit
since the game has a special textbox it calls on just for the weeks caused by the Inferno
grail. The first answer is that the string will not actually go away - textboxes will get
jacked up if you just remove a string. Secondly, who's to say we can't copy this effect?

-----------------------------------------------------------------------------------------

I don't know about you, but when I see the "every week is X week" effect, Inferno is not
the first faction that comes to mind - I think of Necropolis. I think night of the Living
Fucking Dead. Zombies everywhere dude. Just zombies, zombies, zombies fucking everywhere.

Making this happen will require some space, which I'll assume we freed up when we trashed
the Conflux grail effect from earlier. Here's how to make your own Necronomicon:

	------		-------------------------------------------------------------------------
	0C85D3		; INFERNO/NECROPOLIS GRAILS TO "ALWAYS WEEK/MONTH OF DEMON/ZOMBIE"
	------		-------------------------------------------------------------------------
	E9 205F0F00	jmp 5BE4F8		; -> free space (Conflux grail effect)
	90 90 90	nop			; -

	----------	-------------------------------------------------------------------------
	1BE4F8~50C	; (EXPANDED SPACE - OVERWRITES CONFLUX GRAIL EFFECT)
	----------	-------------------------------------------------------------------------
	8A 44 18 04	mov al,[eax+ebx+04]	; AL = town type
	3C 03		cmp al,03		; Inferno?
	74 08		je 5BE508		; if yes -> [continue]
	3C 04		cmp al,04		; Necropolis?
	0F85 F1A0F0FF	jne 4C85F9		; if no -> [exit]
	E9 CEA0F0FF	jmp 4C85DB		; -> [continue]

	---------	-------------------------------------------------------------------------
	0C8602~23	; INFERNO/NECROPOLIS GRAILS TO "ALWAYS WEEK/MONTH OF DEMON/ZOMBIE"
	---------	-------------------------------------------------------------------------
	8B 0D B0476700	mov ecx,[6747B0]	; ???
	8B 55 FC	mov edx,[ebp-04]	; ???
	8B 82 14160200	mov eax,[edx+21614]	; ???
	8A 44 18 04	mov al,[eax+ebx+04]	; AL = town type
	E8 F35E0F00	call 5BE50D		; -> free space (Conflux grail effect)
	89 35 A0776900	mov [6977A0],esi	; store week type
	89 45 F0	mov [ebp-10],eax	; store upgraded unit type
	48		dec eax			; EAX = base unit

	---------	-------------------------------------------------------------------------
	1BE50D~26	; (EXPANDED SPACE - OVERWRITES CONFLUX GRAIL EFFECT)
	---------	-------------------------------------------------------------------------
	3C 04		cmp al,04		; Necropolis?
	74 06		je 5BE517		; if yes -> set "temp" flag
	6A 31		push 31			; 31 = Horny Demons
	6A 07		push 07			; +7
	EB 0A		jmp 5BE521		; -> "grail" growth week

	FF 05 013B6700	inc [673B01]		; set "temp" flag
	6A 3B		push 3B			; 3B = Zombies (Russo-style)
	6A 0E		push 0E			; +15

	6A 02		push 02			; "grail" growth week
	5E		pop esi			; ESI = week type
	5A		pop edx			; EDX = bonus
	58		pop eax			; EAX = unit
	C3		ret			; return

	---------	-------------------------------------------------------------------------
	0CC94F~60	; INFERNO/NECROPOLIS GRAIL TEXTBOX (WEEK)
	---------	-------------------------------------------------------------------------
	E9 D31B0F00	jmp 5BE527		; -> free space (Conflux grail effect)
	90		nop			; -
	8B 90 D4150000	mov edx,[eax+15D4]	; EDX = Demons
	8B 80 48160000	mov eax,[eax+1648]	; EAX = Horny Demons

	---------	-------------------------------------------------------------------------
	1BE527~51	; (EXPANDED SPACE - OVERWRITES CONFLUX GRAIL EFFECT)
	---------	-------------------------------------------------------------------------
	803D013B670001	cmp byte [673B01],01	; Necropolis?
	74 08		je 5BE538		; if yes -> unset "temp" flag

	6A 07		push 07			; ECX = 7 (Demon growth bonus)
	59		pop ecx			; ""
	E9 1DE4F0FF	jmp 4CC955		; -> [return]

	FF 0D 013B6700	dec [673B01]		; unset "temp" flag
	6A 0E		push 0E			; ECX = 15 (Zombie growth bonus)
	59		pop ecx			; ""
	8B 90 5C1A0000	mov edx,[eax+1A5C]	; EDX = Zombies (Romero-style)
	8B 80 D01A0000	mov eax,[eax+1AD0]	; EAX = Zombies (Russo-style)
	E9 0FE4F0FF 	jmp 4CC961		; -> [continue]

	---------	-------------------------------------------------------------------------
	0C8C38~41	; INFERNO/NECROPOLIS GRAIL TEXTBOX (MONTH)
	---------	-------------------------------------------------------------------------
	E8 15590F00	call 5BE552		; -> free space (Conflux grail effect)
	90 90 90 90 90	nop			; -

	---------	-------------------------------------------------------------------------
	1BE552~68	; (EXPANDED SPACE - OVERWRITES CONFLUX GRAIL EFFECT)
	---------	-------------------------------------------------------------------------
	803D013B670001	cmp byte [673B01],01	; Necropolis?
	74 04		je 5BE55F		; if yes -> Zombies
	6A 30		push 30			; Demons
	EB 02		jmp 5BE561		; -> ESI = unit

	6A 3A		push 3A			; Zombies (Romero-style)
	5E		pop esi			; ESI = unit
	89 35 98776900	mov [697798],esi	; store unit
	C3 		ret 			; return (1BE569~75 is free space)

Of course, with the Conflux grail effect trashed, that leaves us with a grail that has no
bonus. Incidentally, we also have a grail - Tower's Skyship - with two effects: it boosts
spell points for defending heroes and it shows the entire map. Trouble is, these effects
both kind of suck: knowledge is the least helpful stat to boost for defending heroes, and
if you've found the grail, you've already seen most of the map. In fact, the spell point
bonus feels more like an effect that you should get from a regular building whereas the
Mana Vortex effect feels like the kind of shit you'd expect to find on a grail building.

So, let's look at moving the Skyship's spell point bonus to Dungeon's Mana Vortex and the
"double your hero's maximum spell points" effect to a grail. I say "a grail" because the
one without an effect right now is Conflux, but it thematically just feels a little off.
There are (now) three grail buildings acting as bonuses to defending heroes: Stronghold,
Fortress, and Dungeon. Number one, it feels more appropriate for those three bonuses to
go to the "neutral" towns while Dungeon - an evil town - gets a more offensively-themed
bonus. Number two, moving the magic power bonus to the Aurora Borealis and then having
Dungeon's Earth Guardian act as the "new" Mana Vortex prevents us from having to move a
bunch of code around to account for Dungeon needing to run through two different sections
of the defensive building routine. All said and done, our edits will look like this:

	063916 > FD ; shifts table up, removing Tower and adding Conflux

	063C64 > 54 39 46 00 ; Inferno (no change)
	063C68 > 98 3A 46 00 ; Necropolis (no change)
	063C6C > 27 39 46 00 ; Dungeon -> (Tower's old exit)
	063C70 > B0 39 46 00 ; Stronghold (no change)
	063C74 > DE 39 46 00 ; Fortress (no change)
	063C78 > 82 39 46 00 ; Conflux -> (Dungeon's old exit)

	06392F > 40	; spell point bonus (Grail -> Mana Vortex)
	06393D > 44	; ""
	06394D > 32	; +50 spell points (seems more reasonable than +150)

	1BDD08 > 68	; double spell points (Mana Vortex -> Grail)
	1BDD0E > 6C	; ""

That just leaves us with Tower's grail, which is now even shittier because we removed the
slightly less shitty of its two shitty effects. We'll leave in the map effect because I
couldn't figure out how to get rid of it, but we'll put in something better to replace
the spell point bonus. Keeping somewhat to the theme of both the other two "good" grails
as well as the Tower grail itself, let's have it allow your units to always recieve the
native terrain bonus in combat (terrain movement costs outside of combat still apply).

	---------	-------------------------------------------------------------------------
	03D544~50	; NEW TOWER GRAIL EFFECT
	---------	-------------------------------------------------------------------------
	89 4B 3C	mov [ebx+3C],ecx	; (rearranged code so we can use ECX)
	E8 D5121900	call 5CE821		; -> free space (Conflux grail, right click)
	8B 45 14	mov eax,[ebp+14]	; (rearranged code so we can use EAX)
	29 C2 		sub edx,eax		; ""

	---------	-------------------------------------------------------------------------
	1CE821~D5	; (EXPANDED SPACE - OVERWRITES CONFLUX GRAIL, RIGHT CLICK)
	---------	-------------------------------------------------------------------------
	53		push ebx		 ; store EBX
	80BBD804000001	cmp byte [ebx+4D8],01	 ; is unit already on native terrain?
	74 30		je 5CE85B		 ; if yes -> (cleanup)

	8B 35 20946900	mov esi,[699420]	 ; ESI = combat manager
	8B 45 14	mov eax,[ebp+14]	 ; EAX = unit's side (attacker = 0, defender = 1)
	8B9C86CC530000	mov ebx,[esi+eax*4+53CC] ; EBX = unit's hero data
	85 DB		test ebx,ebx		 ; is there a hero?
	74 1C		je 5CE85B		 ; if no -> (cleanup)

	8B 35 38956900	mov esi,[699538]	 ; ESI = main index
	8A 4B 22	mov cl,[ebx+22]		 ; ECX = hero's owner
	6B C9 2D	imul ecx,ecx,2D		 ; ECX = data range
	8D9CCED00A0200	lea ebx,[esi+ecx*8+20AD0]; EBX = player data
	8A84CE0E0B0200	mov al,[esi+ecx*8+20B0E] ; EAX = number of towns owned by player

	84 C0		test al,al		 ; do we have any towns?
	74 6C		je 5CE8C9		 ; if no -> (cleanup)

	57		push edi		 ; store number of towns checked (starts at 0)
	50		push eax		 ; store number towns owned by player
	8A 44 3B 40	mov al,[ebx+edi+40]	 ; EAX = town ID owned by player
	3C FF		cmp al,-01		 ; is this a blank slot? (???)
	75 04		jne 5CE86B		 ; if no -> EAX = data range

	31 C0		xor eax,eax		 ; EAX = 0
	EB 15		jmp 5CE880		 ; -> Tower? (~~~this makes no sense)

	69 C0 2D000000	imul eax,eax,2D		 ; EAX = data range
	8B 35 38956900	mov esi,[699538]	 ; ESI = main index
	8B 8E 14160200	mov ecx,[esi+21614]	 ; ECX = town index
	8D 04 C1	lea eax,[ecx+eax*8]	 ; EAX = town data
	80 78 04 02	cmp byte [eax+04],02	 ; Tower?
	75 3C		jne 5CE8C2		 ; if no -> EAX = number towns owned by player

	8B 90 58010000	mov edx,[eax+158]	 ; is grail building built?
	8B 88 5C010000	mov ecx,[eax+15C]	 ; ""
	8B 3D 68CE6600	mov edi,[66CE68]	 ; ""
	8B 35 6CCE6600	mov esi,[66CE6C]	 ; ""
	21 FA		and edx,edi		 ; ""
	21 F1		and ecx,esi		 ; ""
	09 CA		or edx,ecx		 ; ""
	74 1C 		je 5CE8C2		 ; if no -> EAX = number towns owned by player

	8B 7D F8	mov edi,[ebp-08]	 ; EDI = unit data
	C687D804000001	mov byte[edi+4D8],01	 ; unit is on native terrain
	FF 87 C4000000	inc [edi+C4]		 ; Attack +1
	FF 87 C8000000	inc [edi+C8]		 ; Defense +1
	FF 87 CC000000	inc [edi+CC]		 ; Speed +1

	58		pop eax			 ; EAX = number towns owned by player
	5F 		pop edi			 ; EDI = number of towns checked
	47 		inc edi			 ; EDI + 1
	39 F8		cmp eax,edi		 ; have we checked every town this player owns?
	7C 94		jl 5CE85D		 ; if no -> store number of towns checked

	5B		pop ebx			 ; (cleanup)
	31 FF		xor edi,edi		 ; ""
	31 D2		xor edx,edx		 ; ""
	42		inc edx			 ; ""
	C3		ret			 ; return
	909090909090	nop			 ; -
