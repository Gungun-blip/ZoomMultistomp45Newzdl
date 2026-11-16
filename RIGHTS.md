# Redistribution, licenses and acknowledgements

**Status — 16 November 2026: rights review incomplete. Not a legal clearance.**

This project is independent from Zoom Corporation, Texas Instruments, and the pedal manufacturers named in `effects.csv`. It is not authorized, sponsored or endorsed by those companies. The `inspired by` field credits sonic influences only and does not imply use of their DSP algorithms, authorization, or a license.

## What is confirmed in the prepared 45-effect release

A binary-level comparison of the exact release ZIP `Zoomms_GitHub_45_Effects_Draft.zip` against archived linker inputs found these identical sequences embedded in the ELF `.text` of the ZDL files:

| Origin indicated by build inputs | Binary length | Matches in the 45 effects |
| --- | ---: | ---: |
| LineSel-derived on/off/edit-handler and runtime segment | 480 bytes | 45 / 45 |
| Floating-point division runtime extracted from a stock effect (TI and Zoom provenance to be resolved) | 640 bytes | 45 / 45 |
| AIR-derived third-knob edit handler | 76 bytes | 11 / 45 |
| NoiseGate-derived DLL entry adapted by the linker (45 unchanged 32-bit words of a 200-byte template; remaining five words vary) | 200-byte template | 45 / 45 |

The prepared ZIP contains **no standalone Zoom firmware image, Zoom stock-effect corpus or TI compiler**, but this does not eliminate the stock-derived executable bytes *inside* the ZDLs. These findings establish technical provenance concerns, not a definitive legal determination.

**No license granted by Zoomms covers these stock-derived components.** Do not assume the binaries are MIT-licensed, open source, or cleared for redistribution because a repository is public, because the effects run on a discontinued product, or because other projects have shipped similar files. Distribution rights and any applicable exceptions require separate assessment. In the meantime, please avoid mirroring or repackaging the ZDL files.

If you already downloaded this repository, be aware that any revision of a GitHub repository may remain available in its commit history even after files are removed in a later commit.

## What is independently licensed

Only the newly authored C files, tests, and documentation **inside [`src/independent/`](src/independent/)** are offered under the MIT license contained in [`src/independent/LICENSE`](src/independent/LICENSE). These are portable reference implementations and **are not wired into the installable ZDLs**.

No repository-wide MIT license is asserted for:
- `Zoom MultiStomp/*.ZDL`, including compiled handlers, DSP and embedded bitmaps;
- the earlier closed or unverified DSP sources or external linker implementations;
- Zoom's stock effects and firmware, Texas Instruments toolchains/runtime, or third-party artwork;
- material authored by upstream contributors without the necessary license and notices.

The project should only license other portions after their authorship, dependencies and redistribution rights have been established.

## Code provenance and artwork

The current private development records include custom C DSP source for some earlier effects. A complete source-to-binary provenance audit of **all 45** was not possible using the sources available in this session. Source for the remaining effects must be examined before claiming a clean fully reproducible build.

All 45 embedded display images were extracted and visually reviewed. They are monochrome LCD graphics, with no visibly identifiable His Dark Materials imagery. Many use *legacy names*, including old commercial-effect or pre-rename names. Their authorship is not independently proven by this visual scan. Bitmap origin, external graphics assets and branding still require verification or replacement.

## Upstream background and acknowledgements

- [themanro/ZoomMultistompZDL](https://github.com/themanro/ZoomMultistompZDL) and [the stock-files disclosure](https://themanro.github.io/ZoomMultistompZDL/docs/STOCK-FILES.html) document the ZDL build interface and openly acknowledge similar stock-derived handler/runtime fragments. **Their existence is not legal authorization for our distribution.**
- [repeat98/ZoomMultistompZDL](https://github.com/repeat98/ZoomMultistompZDL) is an important predecessor for the community research and tooling.
- [ELynx/zoom-fx-modding](https://github.com/ELynx/zoom-fx-modding) is an earlier independent reverse-engineering and patching project.

If we distribute any upstream MIT/GPL/other licensed *source* or compiled material, we must check its precise license, preserve required notices, and satisfy the applicable license terms. Merely citing inspiration is not a substitute for those requirements.

## Work still required before claiming a cleaned release

1. Integrate completely independently built editor/on-off/init handlers with the actual C6000 host callback ABI. **The portable logic implementation alone is insufficient.**
2. Integrate and benchmark an independent `__c6xabi_divf`-compatible implementation (or otherwise remove calls to the stock-sourced runtime). Confirm correct EABI symbol resolution and no copied runtime code.
3. Rebuild **all 45** effect binaries with confirmed-licensed DSP sources and assets.
4. Replace the NoiseGate-derived DLL entry template with a new register/descriptor implementation, and verify host/relocation behavior on hardware.
5. For each ZDL, verify that known stock-derived byte patterns no longer occur in executable sections, then perform Ziddle and native checks, hardware parameter sweeps, patch switching and output-safety QA.
6. Replace/clear inherited bitmap graphics and old branding; finalize an artwork source/rights manifest and any legally required third-party notices.
7. Obtain informed legal advice if you need a definitive statement about distribution of any past or current versions.

See [docs/REBUILD_STATUS.md](docs/REBUILD_STATUS.md) for dated evidence and test limitations.
