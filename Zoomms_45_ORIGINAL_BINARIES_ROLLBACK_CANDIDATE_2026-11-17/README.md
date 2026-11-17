# Zoomms – original-binary 45-effect recovery candidate (2026-11-17)

This is a rollback/recovery collection reconstructed from ORIGINAL, unchanged archived ZDLs, NOT an independently confirmed hardware-working 45-effect release.

- 41 original, byte-for-byte unchanged selected beta binaries from `Zoomms_BETA_FINAL_G1_25_G2_16_ZDL_2026-11-15(2).zip` (Gen1 25 + Gen2 16).
- 4 original, byte-for-byte unchanged Gen2 alpha binaries: AACollag, AASweet, AAPerco, AALore recovered from `Zoomms_GEN2_ALPHA_ALL16_AA_ZDL_INSTALL_2026-11-13.zip` inside the supplied continuation archive.
- Original firmware aliases, original Dll symbol names, original metadata. No cosmetic renames, DSP-cost recalibration, artwork changes, or DSP code modifications were applied.
- 45 unique (gid,fxid) pairs, filenames <=8 letters, ELF loadable headers validated; no (9,256) stock Cave ID; audio `.text` sections of all 45 match public archive by byte comparison.
- Four recovered additions were historically experimental; no proof of 45/45 hardware validation. The 41 selected beta had varying hardware validation as described in the original beta docs.

All 41 original selected-beta files had their display name and ELF symbol metadata modified when building the 41 normal-name archive. It is worth isolating whether this metadata rename breaks hardware lookup.

This ZIP does NOT prove that installing it will resolve a Cave-on-pedal symptom. That symptom also affected 19 ZDLs in the public ZIP that were byte-identical to the preceding 41-repository ZIP, pointing to installation/firmware state as a possible cause.

To diagnose safely, back up your pedal and patches; check that Zoom Effect Manager 2.3.3+ reads files from folder, that `From Folder` is enabled, and that conflicting old versions of the same IDs are removed. Test one familiar ORIGINAL ZDL first on a blank patch at low monitoring volume. Do not flash all 45 at once.

Contents:
- `ZDL/`: 45 original .ZDL binaries
- `AUDIT.csv`: full effect-ID, filename, hash, and DSP-code comparison vs public 45
- `README.md`: this file

This package preserves historical binaries for the owner's troubleshooting, not an assurance of redistribution rights.
