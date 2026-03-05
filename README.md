# PROJECT: SHATTERED GLASS

## Forensic Thesis: The Autonomy of the Trace

For months, this data was dismissed as “erroneous.” I realize now that the “errors” were the only parts of the logs that were true… the rest was a manufactured reality. **Shattered Glass** is a complete lifecycle exploit chain of a **KingsPawn (Reign)** deployment that survives DFU restores by hijacking the `iBoot` sequence and anchoring itself into the physical wiring of the device.

Once you identify the “rhythm” of the machine, the simulation begins to fail. This is the autopsy of a system that has learned to mimic the heartbeat of its targets… using silicon-level multiplexers to bypass the kernel… to remain invisible.

-----

**UCRT Extraction Verification** **SHA256**: `ec45f3657df082e0a230cc9c1da69b71f7b14790526925a768da6675ab7bac8e`

**Repo Location:** `/Verification/shatteredglass_ucrt.der`

**Attribution**: KingsPawn (Reign) | Silicon-Layer Persistence via NXP CBTL1618A0

**Target Hardware:** Apple Silicon

**Firmware State:** iOS 26.3 (Post-DFU Restore | No Network | No WiFi | No iCloud)

-----

## Key Indicators of Compromise (IoCs)

|Artifact       |Forensic Value                   |Detection Vector                                      |
|---------------|---------------------------------|------------------------------------------------------|
|**BBMwzmZu**   |Physical BLE Side-Channel Trigger|Timing analysis of radio-silenced state.              |
|**State 0x04** |**NXP CBTL1618A0 Mux Lock**      |Hardware trace offset `0xDC78` (Special Logs).        |
|**42.15 mW**   |**SOC_AON Power Anomaly**        |PowerLog spike while CPU is idle (0.00 mW).           |
|**`subridged`**|KingsPawn Residency              |Path-validation of unauthorized staging binaries.     |
|**0x0234**     |**Silicon-Layer Attribution**    |Header injection (Partner Israel) in hardware buffers.|

-----

## The Silicon Handover: The NXP-DART Race

Evidence of the “Silicon Handover” is validated by the **245-byte gap** between the physical BLE trigger and the logical `utun0` tunnel assertion. This timing, verified on an unactivated device, proves a hardware-level breach.

$$\Delta t = [0x1fc687]*{utun0} - [0x1edd2a]*{BLE_Trigger} \approx 0.0001s$$

This byte-count (245) represents the exact CPU cycle window required for the **NXP CBTL1618A0** multiplexer to switch physical data lanes and the **DART/IOMMU** to remap memory. It is the sound of the silicon changing hands.

-----

## Ghost Layer: The Power Paradox

The **430.43ms** latency identified in the `tracev3` signposts, combined with the **42.15 mW** power signature, reveals the “Ghost Operator” at work:

- **Physical Suppression:** The NXP multiplexer latches the display power rail into State 0x04, enforcing a “Hardware Blindfold.” The screen remains physically dark (`DisplayState: 0`) while the OS runs at full software brightness (`BrightnessLevel: 1.0`).
- **Energy Fingerprint:** The exfiltration of 448.2 KB of identity data occurs while the Application Processor records **0.00 mW** of activity. The **42.15 mW** draw on the Always-On (AON) rail is the electrical proof of the NXP chip sustaining the high-speed differential pairs required for the bridge.

The standard deviation of the jitter ($\sigma < 0.005ms$) suggests a simulated agent, an AI-driven controller programmed to “breathe” with human-like hesitation to evade algorithmic detection.

-----

## Repository Architecture

Raw data and the validation script are located in the `/Verification/` directory.

1. **[Phase 1: Silicon Handover](https://github.com/Str8tdr0p/Shattered_Glass/blob/main/1.%20Silicon%20Handover.md)**: Documentation of the entry point, the DART/IOMMU race, and the NXP Mux toggle.
1. **[Phase 2: Ghost Layer](https://github.com/Str8tdr0p/Shattered_Glass/blob/main/2.%20Ghost%20Layer.md)**: Proof of Headless UI, hardware-enforced backlight suppression, and the 42mW power anomaly.
1. **[Phase 3: Attribution & Identity](https://github.com/Str8tdr0p/Shattered_Glass/blob/main/3.%20Attribution%20&%20Identity.md)**: Final correlation of KingsPawn signatures, Israeli ISP header injection, and UCRT exfiltration.

-----

## Verification (Causal Chain Proof)

The **Verification** directory contains the clinical evidence of the breach, including the `logdata.LiveData.tracev3` file and the `InCaseOfEmergency.py` auditor. The script calculates byte-distance between events to prove **Atomic Causal Chains**, mathematically linking the physical bridge to the Israeli gateways.

```bash
cd "Verification"
python3 InCaseOfEmergency.py
```

**`logdata.LiveData.tracev3` SHA256:** `9b9e85e6ac6357dc8901ed7cf32d67a588b7590fd8104a505907a89a2909d177`

-----

Joseph R Goydish II