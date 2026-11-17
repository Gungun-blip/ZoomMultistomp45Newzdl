# 45 effects for Zoom MultiStomp

**45 "designed" / adapted audio effects for the original Zoom MultiStomp, taking it to new heights.**
Welcome to this repository! I've spent the last weeks and many hours developing these effects.

IF YOU WANT TO TEST THESE EFFECTS BEWARE AND PROTECT YOUR EARS!
There can still be a lot of bugs, so I recommend using an audio interface, preferably with a limiter.
I encountered bugs of extreme loudness during development and you WILL need to protect your ears.

I have only hardware tested on a zoom ms50g. All 45 effects are something I found very nice and usable, but not necessarily perfect yet.
I especially liked the granular delays, one-tap clock looper, the afterneath-esque reverb and the tape effects like the deco. 
Also the phaser mode 3 is awesome.
The ranges of the knobs are poorly defined. For instance, I only run the Afterneath with all knobs maxed, except the drag which was at 35.
This is the first beta, and I'll be making many revisions going forth.
I have also not tested the effects together with more than 1-2 effects at a time. The DSP load of each effect is not precise.

# Installation

I have set up my folder structure on my computer exactly as themanros repository, and I copy the contents of "Zoom Multistomp" from this repository into the /dist folder

I recommend and have only tested these using zoom midistomp 2.0: https://www.reddit.com/r/zoommultistomp/comments/1xlwm57/midistomp_v20_my_free_custom_firmware_for_the/

I also recommend installing another repository first as a test, such as themanro: https://github.com/themanro/ZoomMultistompZDL?utm_source=chatgpt.com

I use the Zoom Effects manager 2 for installation: https://zoomeffectmanager.com/en/

## Known bugs by 17/11/2026

The effects may load in with all knobs at 0, even though the display says otherwise. Wiggle all knobs of the effect and it should function.

The first upload "45BBetaZDL" didn't work for some people, so rollback is added

# Notes and more 

Bear in mind - these are NOT direct ports of existing software, but interpretations.
the main goal was to make something I can work with musically in my own creative practice. 
ATM I am ready to take my CBA Mood MkII and Red Panda Tensor as well as Walrus Ambient and DBA Reverberation Machine off my board.

I used my knowledge and ears as a musician and guitarist having played a ton of pedals over the years, but I haven't done 1:1 testing.
The main issue I have is not having enough money to own the pedals I need, and not having enough space on my board and hopefully these patches can help others in the same position.

Feel free to grab these off of here and start tuning them to your own liking.
I claim no ownership as such.
If you enjoy this work I spent hours and hours of tuning, feel free to buy me a coffee: https://buymeacoffee.com/silvertongue12
Also totally fair if you don't want to.

# AI Disclaimer! (and tips)
I'm only decent at programming in python, and have no rust or C experience.
I prompted with the specific audio goals - "grain delay with random splices" "modelled asymmetric drive with a low q 3 db boost at 120 hz" and so on.
It then generated the prompted effects in C, inhouse rewrote it as .zdls and used ziddle, a multistomp emulator to test it.

I used a Chatgpt project because I randomly got a month free. It took a long time to make it learn the software and workflow.
I also tried using github copilot, but it burned all my tokens in a day and didn't make anything functioning.

While AI has a LOT of inherent problems regarding creative/licensing abuse, I think as a software development tool it makes some sense to me.
I feel somewhat ok using it in this case, as I've not spent money on it, and I'm not asking money for anything or claim that I created this myself.
At least in this case where I can tailor something with an effect I already own, and relatively simple C audio manipulation programming.
I continue to oppose the use of AI in creative processes, such as generating artwork for profit, or creating AI works of art that have been trained unlawfully on others work.
If you think this unfair, I can also handle some criticism, so feel free to write it.

The complete effect list is in **[effects.csv](effects.csv)**, including each effect’s controls (where documented), inspiration, compatibility IDs, filename, and SHA-256 checksum.
The repository does **not** contain a standalone Zoom firmware image or TI compiler, but stock-derived code is embedded inside the effect binaries. Permission or another lawful basis for redistribution has **not** been established. Please avoid mirroring or redistributing the ZDLs while we investigate. See [RIGHTS.md](RIGHTS.md) and [the remediation status](docs/REBUILD_STATUS.md).


## Repository contents

```text
Zoomms/
├── README.md
├── effects.csv
├── Zoom MultiStomp/
│   ├── BlkMrdn.ZDL
│   ├── ... (45 effects total)
│   └── Wolfrm.ZDL
├── INSTALL.md
├── CONTRIBUTING.md
├── RIGHTS.md
└── tools/
    └── verify.py
```

### Finding an effect

Browse **[effects.csv](effects.csv)** and locate the value under `zdl file`, then get that file from **[Zoom MultiStomp](Zoom%20MultiStomp)**. Full effect names can be longer than the Zoom's eight-character filename/identifier limit.

The `inspired by` field acknowledges musical design influences; these are original implementations or interpretations, **not official software by the named manufacturers**. An inspiration is not a claim of identical circuitry or sound.

## Installation

See [INSTALL.md](INSTALL.md). Back up your patches and effects first, and test each effect in an empty patch at low output volume. The original **MS-70CDR** is the target; other models, including the MS-70CDR+, have not been confirmed compatible. Device firmware, CPU usage, and safe levels are not guaranteed by emulator tests.

## Verification and contribution

```bash
python tools/verify.py
```

This checks that the files match the catalog, that their SHA-256 hashes are correct, and that effect IDs do not conflict. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to help improve the project.

These files use the same compiled audio-processing code as the selected project builds; naming metadata was updated separately. Some legacy embedded LCD labels may still differ from the names in the catalog. **A passed file check does not establish physical device safety.**

Not affiliated with or endorsed by Zoom or any of the manufacturers named in the catalog.
