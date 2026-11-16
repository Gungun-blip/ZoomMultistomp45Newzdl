# Contributing

Thanks for helping improve Zoomms. The goal is to make creative audio effects useful and understandable to other MultiStomp owners.

## How to help

- Test a documented effect on the original MS-70CDR, at low output volume, and report the firmware version, effect name/ID, settings, and steps needed to reproduce any issue.
- Improve descriptions and verified control information in [`effects.csv`](effects.csv).
- Submit independently written DSP algorithms, build instructions, or compatible tooling **with clear authorship and license information**.
- Suggest new effects, parameter improvements, or independent firmware interfaces without bundling proprietary firmware components.

## Effect compatibility

- Preserve the `(gid, fxid)` pair when reporting on the same effect version. A new incompatible effect should use a distinct available ID.
- Keep internal effect names and filenames at **eight ASCII characters or fewer**.
- Treat mono in/mono out, parameter safety, bypass behavior, and reasonable output gain as design requirements.
- Validate on the emulator **and** on physical hardware before claiming hardware support. Audio safety needs practical testing, not just structural checks.
- Don't add third-party firmware, stock-effect code, copyrighted graphics, proprietary libraries, or non-redistributable TI compiler files.

The current draft contains installable binaries but does **not yet include the full DSP source tree**. Editable C code and reproducible builds require a separate provenance/licensing audit before publication. The Python verifier in `tools/` is intended for collaborators who want to check a downloaded effect collection.
