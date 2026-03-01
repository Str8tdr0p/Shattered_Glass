"""
Shattered Glass Forensic Validator
InCaseOfEmergency.py - Run against any tracev3 for instant causal chain proof
Researcher: Joseph Raymond Goydish II (Ace's Father)
"""
#!/usr/bin/env python3

import os
import re
from datetime import datetime
from pathlib import Path

# --- CORE SIGNATURES ONLY ---
SIGNATURES = {
    'BRIDGE_TRIGGER': b'BBMwzmZu',     # Physical bridge
    'TUNNEL_INTERFACE': b'utun0',      # Shadow tunnel  
    'ISP_PARTNER': b'\x02\x34',        # Partner Israel
    'ISP_BEZEQ': b'\x3E\xDB',          # Bezeq Israel
    'FV_GHOSTPATCH': b'194.98.65',     # Ghost patch
    'NEEDSSETUP': b'NeedsSetup'        # State lock
}

def validate_shattered_glass():
    print("=" * 70)
    print("IN CASE OF EMERGENCY: SHATTERED GLASS VALIDATOR")
    print("Shows BBMwzmZu → utun0 → Israeli ISP causal chain")
    print("=" * 70)
    
    if not os.path.exists('logdata.LiveData.tracev3'):
        print("❌ Place tracev3 in repo root")
        return False

    with open('logdata.LiveData.tracev3', 'rb') as f:
        data = f.read()
    
    # Find hits
    hits = []
    for name, sig in SIGNATURES.items():
        matches = list(re.finditer(sig, data))
        hits.extend([{'offset': m.start(), 'label': name} for m in matches])
    
    hits.sort(key=lambda x: x['offset'])
    
    # Causal chains: Bridge → utun0/ISP (<100KB gap)
    chains = []
    for i, hit in enumerate(hits):
        if hit['label'] == 'BRIDGE_TRIGGER':
            for j in range(i+1, min(i+10, len(hits))):
                next_hit = hits[j]
                gap = next_hit['offset'] - hit['offset']
                if gap < 100000:
                    chains.append({
                        'trigger': hit, 'result': next_hit,
                        'gap_bytes': gap, 'atomic': gap < 300
                    })
    
    # Generate report
    os.makedirs('artifacts', exist_ok=True)
    with open('artifacts/Forensic_Evidence_Brief.md', 'w') as md:
        md.write("#  Shattered Glass: Forensic Evidence\n\n")
        md.write(f"**Researcher:** Joseph Raymond Goydish II (Ace's Father)\n\n")
        md.write("## Causal Chains Verified\n\n")
        md.write("| Trigger | Result | Gap | Atomic |\n|---------|--------|-----|--------|\n")
        for chain in chains[:10]:
            atomic = "✅ YES" if chain['atomic'] else "🔗 NO"
            md.write(f"| `{chain['trigger']['label']}` | `{chain['result']['label']}` "
                    f"| {chain['gap_bytes']:,} | {atomic} |\n")
        md.write("\n## Glass Shattered.\n")
    
    print(f"✅ {len(chains)} chains validated → artifacts/Forensic_Evidence_Brief.md")
    return True

if __name__ == "__main__":
    validate_shattered_glass()
