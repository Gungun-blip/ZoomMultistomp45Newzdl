# Zoomms — effects for Zoom MultiStomp

**45 independently designed / adapted audio effects for the original Zoom MultiStomp MS-70CDR.**

Explore reverbs, delays, loopers, modulation, pitch effects, fuzz, and digital textures. The complete effect list is in **[effects.csv](effects.csv)**, including each effect’s controls (where documented), inspiration, compatibility IDs, filename, and SHA-256 checksum.

> **Publication status:** This repository is a **draft**, not cleared for public distribution. The included `.ZDL` binaries are provided here for private project review only until their code, handler, and artwork provenance is fully audited. Do not make this ZIP or its binary folder public yet. See [RIGHTS.md](RIGHTS.md).

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
