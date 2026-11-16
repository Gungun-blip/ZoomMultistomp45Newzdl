# Installing effects

Target hardware: **original Zoom MultiStomp MS-70CDR**, not the Plus series. Actual compatibility can depend on firmware and your effect-manager version.

1. **Back up** existing patches and effect files before making any changes.
2. Find the effect in [`effects.csv`](effects.csv) and locate its `.ZDL` file in [`Zoom MultiStomp/`](Zoom%20MultiStomp).
3. Use a compatible Zoom MultiStomp effect manager to install the selected `.ZDL` file. Follow the manager's own instructions for your specific device and firmware.
4. Do not install different versions of the **same effect ID** simultaneously, even if their file names differ.
5. First test in an empty patch, with output volume and amplifier levels low. Check switching, bypass, each control over its range, sustained feedback, signal level, and unexpected pops.
6. If an effect produces a loud pop, distorted noise, missing audio, or unstable behavior, stop using it and restore the backup.

These effects are experimental modifications. Software loading checks and emulator audio tests do not guarantee safe behavior on the real pedal. Four additions (Patchwork, Sweetroll, Percolator, Fablewell) were recovered from earlier experimental builds, and do not have equivalent documented physical acceptance to the later selected set.
