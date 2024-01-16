## 1. INTRODUCTION

SHAMELESS SELF-PROMOTION

[http://ngplus.net/index.php?/files/file/56-another-heroes-3-mod-ah3m/](http://ngplus.net/index.php?/files/file/56-another-heroes-3-mod-ah3m/)

-----------------------------------------------------------------------------------------

This guide is a compilation of all of the information I have for modding Heroes of Might and Magic III,
ranging from the basics to customized assembly hacks. The information here should be a useful reference
tool for modders of all skill levels; knowledge of coding is not needed or expected to make use of this
guide, but you can learn quite a bit purely through the examples it provides.

Something that will be covered heavily throughout this guide is hex editing; although many changes are
possible through simply editing the game's internal text files, many more will require directly editing
the main .exe file. Simple changes will just indicate which hex addresses to edit, while more in-depth
ones will also show the corresponding ASM commands with commentary; it's not something you will have to
read or understand in order to use the code provided, it's just there to help you see what the new code
is doing and/or modify it to your liking should you wish to do so.

One thing you will need to keep in mind when editing the .exe file is that all values and addresses will
be in hexadecimal format (base 16) instead of decimal (base 10). Also note that any address specified in
this document will be as they would appear in a hex editor; runtime will offset by 400000. Thus, 23EA68
in a hex editor will actually be 63EA68 when the game is running. Any code example will use the runtime
addresses because it needs to, but the commentary will refer to them as they would be seen in an editor.

Finally, these edits will frequently include the game's internal IDs for spells, units, et al - the last
section of this document serves as a quick reference guide for all of these values.

Before we get started, let's set you up with all of the tools you'll want/need.

### Heroes 3 HD+ (REQUIRED - SEE BELOW)

The HD+ fan mod (NOT to be confused with the official HD mod, which should never, under
any circumstances, ever be used) upgrades the game's graphics as well as its interface.
It's important from a modding perspective since the new .exe file that it generates will
restructure some of the internal code, making several of the hex edits discussed in this
file possible. The unofficial "Horn of the Abyss" patch is based on the structure of HD+
and so will also work... sort of. HotA externally patches a lot of things covered by this
guide with .dll files and so will undo many changes that you make to them.

>THIS GUIDE MAKES ABSOLUTELY NO GUARANTEE ABOUT EDITING HOTA

[https://sites.google.com/site/heroes3hd/](https://sites.google.com/site/heroes3hd/)

-----------------------------------------------------------------------------------------

### MMArchive

This tool allows you to view - and more importantly, extract - the files contained inside
the game's .lod archives. Contrary to what the name suggests, all of the game's rules and
basic settings can be found in "H3bitmap.lod". For ease of use, you can set a filter for
a given file extension; just set it to .txt and extract everything in there.

MMArchive can also insert new or updated files into a .lod archive, which isn't necessary
for .txt files (as we'll get into below) but will be for other file types. Note that any
.pcx files will be extracted as .bmp files while any .bmp files that are inserted will be
converted back into .pcx format, so there is no need for you to convert them manually.

[https://github.com/GrayFace/Misc/releases/download/MMArchive-1.3.1/MMArchive.rar](https://github.com/GrayFace/Misc/releases/download/MMArchive-1.3.1/MMArchive.rar)


### TxtEdit

If you attempt to open one of the .txt files you extracted above, you will find that they
are structured in a spreadsheet-like format that renders them nearly impossible to read,
let alone edit. This program was specifically designed to work with them.

[https://github.com/GrayFace/Misc/releases/download/TxtEdit-1.4.1/TxtEdit.rar](https://github.com/GrayFace/Misc/releases/download/TxtEdit-1.4.1/TxtEdit.rar)


### H3DefTool

Another file type you may be working with in the .lod archives are .def files, which are
themselves archives of bitmap images. This program is able to both edit .def archives as
well as re-insert them into the .lod files from whence they came. Even if you don't want
to edit the game's graphics, you'll need to use this tool if you change any of the hero
specialties or else their associated images will be incorrect.

(You'll also need something like Photo/Paintshop or GIMP to edit images as needed.)

[http://sites.google.com/site/sergroj/wog/H3DefTool.rar](http://sites.google.com/site/sergroj/wog/H3DefTool.rar)

### LODMerge

This is a command-line utility that can merge the contents of two .lod files. While many
file types (namely .txt) will be automatically "soft"-patched into the game just by being
placed into the "data" folder, .def or .h3c (campaign) files will not. HD Mod also has an
annoying debug window that appears whenever it soft-patches .pcx files, so I'd recommend
hard-patching those, as well. To do this, use MMArchive	to generate a new .lod file with
all of your modified files and then LODMerge to insert them with the following command:

		"lodmerge.exe" "(EXISTING FILE).lod" "(NEW FILE).lod" /b

[https://grayface.github.io/mm/#LodMerge](https://grayface.github.io/mm/#LodMerge)

-----------------------------------------------------------------------------------------

### HxD64

Many edits cannot be made via .lod editing and will require the .exe file to be directly
modified. Any hex editor will do; this is simply the one that I use.

[https://mh-nexus.de/en/downloads.php?product=HxD20](https://mh-nexus.de/en/downloads.php?product=HxD20)

### Floating IPS

This utility will create a patch containing all of your .exe edits for easy distribution.
While there are many IPS patchers available, I recommend this one specifically due to its
command-line compatibility. Along with LodMerge, this will allow you to distribute your
changes as a complete package with a simple installation script.

[https://dl.smwcentral.net/11474/floating.zip](https://dl.smwcentral.net/11474/floating.zip)

### Cheat Engine

As you begin to learn more about the code, you may want to dig deeper into it than this
guide will cover and will thus need a debugger/disassembler. There is a steep learning
curve and I would not recommend this to someone who is just getting started, but it's an
invaluable tool for advanced hackers who are looking to progress further.

[https://www.cheatengine.org/](https://www.cheatengine.org/)

