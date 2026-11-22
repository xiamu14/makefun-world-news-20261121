from __future__ import annotations

import html
import json
from pathlib import Path

REGION_OKLCH = {
    'EUROPE': 'oklch(0.46 0.13 245)',
    'ASIA': 'oklch(0.48 0.12 195)',
    'MIDDLE EAST': 'oklch(0.46 0.15 310)',
    'AFRICA': 'oklch(0.46 0.13 150)',
    'N. AMERICA': 'oklch(0.48 0.18 24)',
    'S. AMERICA': 'oklch(0.50 0.14 70)',
    'OCEANIA': 'oklch(0.46 0.12 170)',
    'GLOBAL': 'oklch(0.24 0.01 260)',
}

SVGS: dict[str, str] = {
    'bahrain_hormuz': """
    <svg viewBox="0 0 318 112" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="bhsky" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="oklch(0.93 0.025 85)"/>
          <stop offset="100%" stop-color="oklch(0.86 0.045 78)"/>
        </linearGradient>
        <linearGradient id="bhsea" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="oklch(0.74 0.08 228)"/>
          <stop offset="100%" stop-color="oklch(0.60 0.09 232)"/>
        </linearGradient>
      </defs>
      <rect width="318" height="54" fill="url(#bhsky)"/>
      <rect y="54" width="318" height="58" fill="url(#bhsea)"/>
      <path d="M0 58 L98 58 L80 112 L0 112 Z" fill="oklch(0.78 0.06 78)"/>
      <path d="M204 112 L254 80 L318 68 L318 112 Z" fill="oklch(0.78 0.06 78)"/>
      <rect x="28" y="48" width="32" height="18" rx="2" fill="oklch(0.44 0.02 250)"/>
      <polygon points="40,52 52,24 64,52" fill="oklch(0.62 0.21 35)"/>
      <polygon points="45,52 52,32 59,52" fill="oklch(0.82 0.18 75)"/>
      <circle cx="56" cy="22" r="9" fill="oklch(0.38 0.01 260)" opacity="0.85"/>
      <circle cx="68" cy="14" r="10" fill="oklch(0.48 0.01 260)" opacity="0.72"/>
      <text x="12" y="102" font-family="Roboto, sans-serif" font-weight="900" font-size="10.5" fill="oklch(0.24 0.04 75)">BAHRAIN</text>
      <text x="232" y="104" font-family="Roboto, sans-serif" font-weight="900" font-size="9.5" fill="oklch(0.24 0.04 75)">KHASAB, OMAN</text>
      <g transform="translate(154,48)">
        <path d="M0,14 L58,14 L50,22 L8,22 Z" fill="oklch(0.20 0.015 260)"/>
        <rect x="6" y="12" width="46" height="2" fill="oklch(0.48 0.18 24)"/>
        <rect x="8" y="6" width="12" height="6" fill="oklch(0.95 0.01 90)"/>
        <polygon points="26,12 32,-2 38,12" fill="oklch(0.64 0.21 35)"/>
      </g>
      <g transform="translate(222,68)">
        <path d="M0,14 L56,14 L48,22 L8,22 Z" fill="oklch(0.20 0.015 260)"/>
        <rect x="6" y="12" width="44" height="2" fill="oklch(0.48 0.18 24)"/>
        <rect x="8" y="6" width="11" height="6" fill="oklch(0.95 0.01 90)"/>
        <polygon points="24,12 30,-1 36,12" fill="oklch(0.64 0.21 35)"/>
      </g>
      <rect x="118" y="7" width="192" height="23" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="214" y="23" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="13" fill="white">2 TANKERS HIT</text>
    </svg>""",
    'eu_indonesia': """
    <svg viewBox="0 0 318 112" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="318" height="112" fill="oklch(0.96 0.008 85)"/>
      <rect x="12" y="18" width="84" height="50" rx="2" fill="oklch(0.36 0.17 262)"/>
      <g fill="oklch(0.84 0.17 92)" transform="translate(54,43)">
        <circle cx="0" cy="-16" r="2"/><circle cx="8" cy="-13.8" r="2"/><circle cx="13.8" cy="-8" r="2"/>
        <circle cx="16" cy="0" r="2"/><circle cx="13.8" cy="8" r="2"/><circle cx="8" cy="13.8" r="2"/>
        <circle cx="0" cy="16" r="2"/><circle cx="-8" cy="13.8" r="2"/><circle cx="-13.8" cy="8" r="2"/>
        <circle cx="-16" cy="0" r="2"/><circle cx="-13.8" cy="-8" r="2"/><circle cx="-8" cy="-13.8" r="2"/>
      </g>
      <text x="54" y="79" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9" fill="oklch(0.36 0.17 262)">EU · 98.5% CUT</text>
      <rect x="222" y="18" width="84" height="25" fill="oklch(0.50 0.21 25)"/>
      <rect x="222" y="43" width="84" height="25" fill="white" stroke="oklch(0.84 0.008 85)"/>
      <text x="264" y="79" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9" fill="oklch(0.50 0.21 25)">ID · 90.4% CUT</text>
      <text x="159" y="14" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="10.5" fill="oklch(0.18 0.01 260)">CEPA TRADE PACT</text>
      <g transform="translate(126,20)">
        <rect width="66" height="50" rx="3" fill="white" stroke="oklch(0.46 0.13 245)" stroke-width="1.5"/>
        <polygon points="52,0 66,14 52,14" fill="oklch(0.90 0.03 240)"/>
        <line x1="9" y1="13" x2="44" y2="13" stroke="oklch(0.46 0.13 245)" stroke-width="2.2"/>
        <line x1="9" y1="22" x2="57" y2="22" stroke="oklch(0.65 0.04 250)" stroke-width="2"/>
        <line x1="9" y1="31" x2="46" y2="31" stroke="oklch(0.65 0.04 250)" stroke-width="2"/>
        <circle cx="52" cy="39" r="6" fill="oklch(0.48 0.18 24)"/>
      </g>
      <rect x="12" y="85" width="294" height="22" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="159" y="100" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="12.5" fill="white">TARIFFS CUT: 98.5% EU · 90.4% ID</text>
    </svg>""",
    'mexico_sinaloa': """
    <svg viewBox="0 0 318 112" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="318" height="58" fill="oklch(0.26 0.04 145)"/>
      <path d="M0 58 L48 38 L98 50 L158 34 L224 48 L278 36 L318 46 L318 58 Z" fill="oklch(0.33 0.04 145)"/>
      <rect y="58" width="318" height="54" fill="oklch(0.40 0.05 140)"/>
      <polygon points="150,48 116,96 184,96" fill="oklch(0.86 0.08 90)" opacity="0.18"/>
      <line x1="92" y1="34" x2="210" y2="34" stroke="oklch(0.14 0.01 260)" stroke-width="2.5"/>
      <ellipse cx="150" cy="46" rx="26" ry="9" fill="oklch(0.18 0.02 145)"/>
      <line x1="175" y1="46" x2="214" y2="41" stroke="oklch(0.18 0.02 145)" stroke-width="3"/>
      <g fill="oklch(0.18 0.02 145)" transform="translate(0,10)">
        <circle cx="38" cy="54" r="4"/><rect x="33" y="59" width="10" height="20" rx="2"/>
        <circle cx="58" cy="54" r="4"/><rect x="53" y="59" width="10" height="20" rx="2"/>
        <circle cx="78" cy="54" r="4"/><rect x="73" y="59" width="10" height="20" rx="2"/>
      </g>
      <rect x="272" y="52" width="10" height="20" fill="oklch(0.45 0.14 150)"/>
      <rect x="282" y="52" width="10" height="20" fill="white"/>
      <rect x="292" y="52" width="10" height="20" fill="oklch(0.50 0.21 25)"/>
      <text x="150" y="102" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="11" fill="oklch(0.95 0.01 90)">GUASAVE, SINALOA</text>
      <rect x="8" y="7" width="186" height="23" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="101" y="23" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="13" fill="white">11 DEAD IN SINALOA</text>
    </svg>""",
    'finland_ship': """
    <svg viewBox="0 0 236 80" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="236" height="44" fill="oklch(0.86 0.03 230)"/>
      <rect y="44" width="236" height="36" fill="oklch(0.48 0.08 235)"/>
      <polygon points="34,54 128,54 118,68 42,68" fill="oklch(0.22 0.01 260)"/>
      <rect x="46" y="43" width="22" height="11" fill="white"/>
      <polygon points="78,54 90,30 102,54" fill="oklch(0.62 0.21 35)"/>
      <circle cx="96" cy="28" r="9" fill="oklch(0.44 0.01 260)" opacity="0.85"/>
      <circle cx="110" cy="22" r="10" fill="oklch(0.54 0.01 260)" opacity="0.72"/>
      <text x="176" y="64" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="14" fill="white">16 SAFE</text>
      <rect x="6" y="5" width="122" height="16" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="67" y="16.5" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9.5" fill="white">FINLAND: SHIP ABLAZE</text>
    </svg>""",
    'bitcoin_chart': """
    <svg viewBox="0 0 236 80" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="236" height="80" fill="oklch(0.20 0.02 250)"/>
      <circle cx="32" cy="46" r="14" fill="oklch(0.72 0.16 70)"/>
      <text x="32" y="51" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="16" fill="white">₿</text>
      <polyline points="56,36 96,62 146,50 198,36" fill="none" stroke="oklch(0.75 0.16 70)" stroke-width="2.8" stroke-linejoin="round"/>
      <circle cx="96" cy="62" r="3.5" fill="oklch(0.58 0.20 24)"/>
      <circle cx="198" cy="36" r="3.5" fill="oklch(0.70 0.15 150)"/>
      <text x="176" y="70" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="14" fill="oklch(0.78 0.14 75)">$60,190</text>
      <rect x="6" y="5" width="112" height="16" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="62" y="16.5" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9.5" fill="white">BITCOIN: 8% SWING</text>
    </svg>""",
    'cop31_clock': """
    <svg viewBox="0 0 236 80" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="236" height="80" fill="oklch(0.94 0.02 85)"/>
      <text x="68" y="56" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="22" fill="oklch(0.20 0.02 250)">DAY 13</text>
      <circle cx="172" cy="48" r="18" fill="white" stroke="oklch(0.18 0.01 260)" stroke-width="2.2"/>
      <line x1="172" y1="48" x2="172" y2="35" stroke="oklch(0.18 0.01 260)" stroke-width="2.2" stroke-linecap="round"/>
      <line x1="172" y1="48" x2="182" y2="54" stroke="oklch(0.48 0.18 24)" stroke-width="2.2" stroke-linecap="round"/>
      <rect x="6" y="5" width="106" height="16" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="59" y="16.5" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9.5" fill="white">COP31: OVERTIME</text>
    </svg>""",
    'bepicolombo': """
    <svg viewBox="0 0 236 80" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="236" height="80" fill="oklch(0.18 0.03 260)"/>
      <circle cx="186" cy="46" r="20" fill="oklch(0.62 0.02 250)"/>
      <circle cx="178" cy="39" r="4.5" fill="oklch(0.52 0.02 250)"/>
      <circle cx="194" cy="53" r="3.5" fill="oklch(0.52 0.02 250)"/>
      <rect x="60" y="38" width="26" height="16" fill="oklch(0.86 0.01 250)"/>
      <rect x="26" y="42" width="34" height="7" fill="oklch(0.55 0.15 245)"/>
      <rect x="86" y="42" width="34" height="7" fill="oklch(0.55 0.15 245)"/>
      <polygon points="86,43 122,39 122,52" fill="oklch(0.72 0.18 65)"/>
      <text x="150" y="72" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="10.5" fill="white">MERCURY</text>
      <rect x="6" y="5" width="106" height="16" rx="2" fill="oklch(0.24 0.01 260)"/>
      <text x="59" y="16.5" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9.5" fill="white">SPACE: MERCURY</text>
    </svg>""",
    'peru_quake': """
    <svg viewBox="0 0 236 80" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="236" height="80" fill="oklch(0.95 0.015 85)"/>
      <line x1="0" y1="48" x2="236" y2="48" stroke="oklch(0.86 0.01 85)" stroke-width="1"/>
      <polyline points="10,48 30,48 40,28 50,68 60,24 70,66 80,36 90,48 136,48" fill="none" stroke="oklch(0.48 0.18 24)" stroke-width="2.5" stroke-linejoin="round"/>
      <text x="180" y="58" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="21" fill="oklch(0.18 0.01 260)">M6.7</text>
      <rect x="6" y="5" width="108" height="16" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="60" y="16.5" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9.5" fill="white">PERU: M6.7 QUAKE</text>
    </svg>""",
    'taiwan_jets': """
    <svg viewBox="0 0 236 80" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="236" height="80" fill="oklch(0.90 0.03 230)"/>
      <line x1="118" y1="0" x2="118" y2="80" stroke="oklch(0.48 0.18 24)" stroke-width="2.2" stroke-dasharray="4 3"/>
      <g fill="oklch(0.30 0.03 250)" transform="translate(8,8)">
        <polygon points="34,22 58,27 34,32 40,27"/>
        <polygon points="68,34 92,39 68,44 74,39"/>
        <polygon points="34,46 58,51 34,56 40,51"/>
      </g>
      <text x="176" y="58" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="15" fill="oklch(0.18 0.01 260)">21 JETS</text>
      <rect x="6" y="5" width="102" height="16" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="57" y="16.5" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9.5" fill="white">TAIWAN: 21 JETS</text>
    </svg>""",
    'ust_luga': """
    <svg viewBox="0 0 236 80" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="236" height="54" fill="oklch(0.20 0.03 255)"/>
      <rect y="54" width="236" height="26" fill="oklch(0.32 0.05 245)"/>
      <rect x="30" y="36" width="24" height="18" fill="oklch(0.40 0.02 250)"/>
      <rect x="64" y="32" width="26" height="22" fill="oklch(0.45 0.02 250)"/>
      <polygon points="70,36 84,18 98,36" fill="oklch(0.62 0.20 35)"/>
      <polygon points="126,28 144,33 126,38" fill="oklch(0.75 0.16 70)"/>
      <text x="166" y="70" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="12" fill="white">UST-LUGA</text>
      <rect x="6" y="5" width="108" height="16" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="60" y="16.5" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9.5" fill="white">RUSSIA: DRONES</text>
    </svg>""",
    'cricket_nz': """
    <svg viewBox="0 0 236 80" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="236" height="80" fill="oklch(0.93 0.035 145)"/>
      <line x1="36" y1="30" x2="52" y2="66" stroke="oklch(0.55 0.09 55)" stroke-width="5.5" stroke-linecap="round"/>
      <circle cx="68" cy="60" r="6.5" fill="oklch(0.48 0.18 24)"/>
      <text x="154" y="58" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="25" fill="oklch(0.18 0.01 260)">486–4</text>
      <rect x="6" y="5" width="104" height="16" rx="2" fill="oklch(0.24 0.01 260)"/>
      <text x="58" y="16.5" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="9.5" fill="white">CRICKET: 486-4</text>
    </svg>""",
}


def badge_html(status: str, kind: str, overlay: bool = False) -> str:
    cls = 'badge-official' if kind == 'official' else 'badge-confirmed'
    pos = 'badge-overlay' if overlay else ''
    return f'<span class="badge {cls} {pos}">{html.escape(status)}</span>'


def build_world_map_svg(pins: list[dict]) -> str:
    w, h = 286, 146

    def proj(lon: float, lat: float) -> tuple[float, float]:
        px = ((lon + 180.0) / 360.0) * w
        py = ((82.0 - lat) / 142.0) * h
        return max(8, min(w - 8, px)), max(8, min(h - 8, py))

    landmasses = [
        [
            (-168, 65), (-162, 71), (-140, 70), (-125, 71), (-110, 74), (-95, 72), (-82, 68),
            (-78, 62), (-92, 60), (-90, 54), (-79, 52), (-76, 60), (-64, 60), (-55, 52),
            (-60, 46), (-67, 45), (-70, 42), (-75, 38), (-81, 31), (-80, 25), (-82, 27),
            (-85, 30), (-90, 29), (-97, 26), (-96, 19), (-90, 21), (-87, 21), (-84, 15),
            (-83, 10), (-78, 8), (-80, 9), (-86, 11), (-92, 14), (-105, 19), (-110, 24),
            (-114, 31), (-117, 32), (-122, 38), (-124, 48), (-132, 54), (-140, 60),
            (-152, 60), (-162, 55), (-166, 60),
        ],
        [(-56, 76), (-42, 82), (-20, 81), (-18, 70), (-36, 65), (-44, 60), (-52, 65)],
        [
            (-78, 9), (-72, 12), (-62, 10), (-52, 4), (-48, 0), (-35, -6), (-38, -14),
            (-41, -22), (-48, -28), (-54, -34), (-62, -40), (-66, -46), (-68, -54),
            (-74, -52), (-74, -42), (-71, -30), (-70, -18), (-77, -12), (-81, -5), (-79, 2),
        ],
        [
            (-9, 37), (-9, 43), (-2, 44), (-4, 48), (2, 51), (8, 54), (8, 57), (12, 56),
            (10, 60), (5, 62), (14, 68), (25, 71), (32, 70), (42, 67), (58, 70), (72, 73),
            (102, 77), (138, 73), (170, 68), (178, 64), (162, 59), (156, 51), (142, 54),
            (136, 44), (129, 40), (126, 35), (129, 35), (124, 39), (118, 39), (122, 31),
            (118, 24), (109, 20), (109, 12), (104, 10), (103, 2), (100, 6), (98, 14),
            (94, 16), (91, 22), (85, 19), (80, 13), (77, 8), (73, 18), (68, 23), (62, 25),
            (56, 26), (51, 25), (49, 30), (56, 23), (59, 21), (53, 16), (44, 13), (40, 19),
            (35, 29), (33, 31), (36, 36), (27, 37), (26, 41), (22, 37), (20, 40), (14, 45),
            (16, 40), (12, 42), (9, 44), (4, 43), (0, 39), (-5, 36),
        ],
        [(-6, 50), (1, 51), (1, 53), (-2, 57), (-6, 58), (-7, 54)],
        [(-10, 52), (-6, 52), (-6, 55), (-10, 54)],
        [
            (-6, 36), (10, 37), (12, 33), (25, 32), (32, 31), (36, 26), (42, 12), (51, 12),
            (48, 4), (41, -2), (40, -11), (35, -20), (32, -28), (26, -34), (18, -34),
            (15, -26), (12, -16), (12, -6), (9, 4), (2, 6), (-8, 5), (-15, 11),
            (-17, 15), (-16, 22), (-10, 30),
        ],
        [(44, -25), (47, -25), (50, -15), (48, -12), (44, -18)],
        [(130, 32), (136, 34), (141, 36), (142, 41), (145, 44), (140, 43), (136, 37), (130, 34)],
        [(120, 18), (123, 14), (126, 7), (122, 6), (120, 13)],
        [(109, 2), (118, 6), (117, -3), (110, -3)],
        [(95, 5), (104, -2), (114, -8), (106, -7), (98, 1)],
        [
            (114, -22), (122, -17), (130, -12), (136, -12), (137, -15), (142, -11),
            (146, -18), (153, -26), (150, -36), (145, -38), (138, -36), (130, -32),
            (122, -34), (115, -34), (113, -27),
        ],
        [(173, -35), (178, -38), (175, -42), (167, -46), (170, -42), (174, -39)],
    ]

    grid_lines = ''
    for lat in (-30, 0, 30, 60):
        _, gy = proj(0, lat)
        grid_lines += f'<line x1="0" y1="{gy:.1f}" x2="{w}" y2="{gy:.1f}" stroke="oklch(0.88 0.015 225)" stroke-width="0.6" stroke-dasharray="2 2"/>'
    for lon in (-120, -60, 0, 60, 120):
        gx, _ = proj(lon, 0)
        grid_lines += f'<line x1="{gx:.1f}" y1="0" x2="{gx:.1f}" y2="{h}" stroke="oklch(0.88 0.015 225)" stroke-width="0.6" stroke-dasharray="2 2"/>'

    polys = ''.join(
        '<polygon points="'
        + ' '.join(f'{proj(lo, la)[0]:.1f},{proj(lo, la)[1]:.1f}' for lo, la in poly)
        + '" fill="oklch(0.91 0.018 85)" stroke="oklch(0.68 0.02 85)" stroke-width="0.75" stroke-linejoin="round"/>'
        for poly in landmasses
    )
    pin_els = ''
    for p in pins:
        px, py = proj(p['lon'], p['lat'])
        col = REGION_OKLCH.get(p['r'], 'oklch(0.24 0.01 260)')
        pin_els += (
            f'<g transform="translate({px:.1f},{py:.1f})">'
            f'<circle r="6.2" fill="{col}" stroke="white" stroke-width="1"/>'
            f'<text y="2.8" text-anchor="middle" font-family="Roboto, sans-serif" font-weight="900" font-size="7.5" fill="white">{p["id"]}</text>'
            f'</g>'
        )
    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="oklch(0.955 0.014 225)"/>{grid_lines}{polys}{pin_els}</svg>'
    )


def generate_html(data_path: Path, out_html: Path) -> None:
    data = json.loads(data_path.read_text(encoding='utf-8'))

    kpi_html = ''.join(
        f'<div class="kpi-item" style="border-left:3px solid {k["color"]}"><div class="kpi-num">{html.escape(k["num"])}</div><div class="kpi-lbl">{html.escape(k["label"])}</div></div>'
        for k in data['kpi_stats']
    )

    reg_html = ''.join(
        f'<div class="reg-seg" style="flex:{r["count"]} 0 auto;background:{r["color"]}">{html.escape(r["name"])}</div>'
        for r in data['region_bar']
    )

    leads_html = ''.join(
        f'''<article class="lead-card">
          <div class="lead-art">{SVGS[l["art"]]}</div>
          <div class="meta-row">
            <span class="kicker">{html.escape(l["kicker"])}</span>
            {badge_html(l["status"], l["status_kind"])}
          </div>
          <h2>{html.escape(l["title"])}</h2>
          <p>{html.escape(l["body"])}</p>
        </article>'''
        for l in data['leads']
    )

    cards_html = ''.join(
        f'''<article class="mini-card">
          <div class="mini-art">
            {SVGS[c["art"]]}
            {badge_html(c["status"], c["status_kind"], overlay=True)}
          </div>
          <div class="kicker-sm">{html.escape(c["kicker"])}</div>
          <h3>{html.escape(c["title"])}</h3>
          <p>{html.escape(c["sub"])}</p>
        </article>'''
        for c in data['cards']
    )

    col1 = ''.join(
        f'<div class="brief"><span class="b-id">{b[0]}</span> <span class="b-loc">{html.escape(b[1])}:</span> {html.escape(b[2])}</div>'
        for b in data['briefs'][:7]
    )
    col2 = ''.join(
        f'<div class="brief"><span class="b-id">{b[0]}</span> <span class="b-loc">{html.escape(b[1])}:</span> {html.escape(b[2])}</div>'
        for b in data['briefs'][7:]
    )

    legend_html = ''.join(
        f'<span class="leg-item"><i style="background:{col}"></i>{name.title()}</span>'
        for name, col in REGION_OKLCH.items()
    )

    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-paper: oklch(0.992 0.004 90);
    --bg-panel: oklch(0.955 0.006 85);
    --ink-primary: oklch(0.18 0.01 260);
    --ink-secondary: oklch(0.30 0.01 260);
    --ink-muted: oklch(0.46 0.01 260);
    --rule: oklch(0.84 0.008 85);
    --scarlet: oklch(0.48 0.18 24);
    --badge-confirmed: oklch(0.42 0.12 152);
    --badge-official: oklch(0.46 0.13 65);
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 1024px;
    height: 1024px;
    overflow: hidden;
    background: var(--bg-paper);
    color: var(--ink-primary);
    font-family: "Roboto", sans-serif;
    text-rendering: optimizeLegibility;
  }}
  .page {{
    width: 1024px;
    height: 1024px;
    padding: 6px 18px 5px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 2px;
  }}
  .eyebrow {{
    display: flex;
    justify-content: space-between;
    font-weight: 700;
    font-size: 12px;
    letter-spacing: 0.02em;
    padding-bottom: 2px;
    border-bottom: 1px solid var(--ink-primary);
  }}
  .eyebrow-left {{ color: var(--scarlet); }}
  .eyebrow-right {{ color: var(--ink-primary); }}
  h1.masthead {{
    font-weight: 900;
    font-size: 33px;
    line-height: 1.02;
    text-align: center;
    letter-spacing: -0.015em;
    padding: 2px 0 1px;
  }}
  .deck {{
    text-align: center;
    font-size: 12px;
    font-weight: 500;
    color: var(--scarlet);
    padding-bottom: 2px;
    border-bottom: 2px solid var(--ink-primary);
  }}
  .kpi-strip {{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 6px;
    padding: 2px 0;
    border-bottom: 1px solid var(--rule);
  }}
  .kpi-item {{
    padding-left: 5px;
  }}
  .kpi-num {{
    font-weight: 900;
    font-size: 19px;
    line-height: 1.04;
    color: var(--scarlet);
  }}
  .kpi-lbl {{
    font-weight: 600;
    font-size: 12px;
    line-height: 1.15;
    color: var(--ink-secondary);
    margin-top: 1px;
  }}
  .reg-bar {{
    display: flex;
    gap: 2px;
    margin-top: 2px;
  }}
  .reg-seg {{
    color: white;
    font-weight: 700;
    font-size: 12px;
    text-align: center;
    white-space: nowrap;
    padding: 2px 6px;
    border-radius: 1px;
  }}
  .leads {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    padding: 2px 0 3px;
    border-bottom: 1px solid var(--rule);
  }}
  .lead-art {{
    height: 102px;
    border: 1px solid var(--ink-secondary);
    overflow: hidden;
  }}
  .lead-art svg, .mini-art svg {{
    display: block;
    width: 100%;
    height: 100%;
  }}
  .meta-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 2px 0 1.5px;
  }}
  .kicker {{
    font-weight: 700;
    font-size: 12px;
    color: var(--scarlet);
  }}
  .badge {{
    font-weight: 700;
    font-size: 12px;
    color: white;
    padding: 1px 6px;
    border-radius: 2px;
  }}
  .badge-confirmed {{ background: var(--badge-confirmed); }}
  .badge-official {{ background: var(--badge-official); }}
  .badge-overlay {{
    position: absolute;
    top: 3px;
    right: 3px;
  }}
  .lead-card h2 {{
    font-weight: 900;
    font-size: 22px;
    line-height: 1.06;
    margin-bottom: 2px;
  }}
  .lead-card p {{
    font-weight: 400;
    font-size: 12px;
    line-height: 1.22;
    color: var(--ink-secondary);
  }}
  .cards {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 5px 14px;
    padding: 2px 0 4px;
    border-bottom: 2px solid var(--ink-primary);
  }}
  .mini-art {{
    position: relative;
    height: 72px;
    border: 1px solid var(--ink-secondary);
    overflow: hidden;
  }}
  .kicker-sm {{
    font-weight: 700;
    font-size: 12px;
    color: var(--scarlet);
    margin-top: 2px;
  }}
  .mini-card h3 {{
    font-weight: 900;
    font-size: 17px;
    line-height: 1.07;
    margin: 1px 0;
  }}
  .mini-card p {{
    font-weight: 500;
    font-size: 12px;
    line-height: 1.22;
    color: var(--ink-secondary);
  }}
  .bottom {{
    display: grid;
    grid-template-columns: 286px 1fr;
    gap: 12px;
    align-items: start;
  }}
  .sec-hd {{
    font-weight: 700;
    font-size: 12px;
    color: var(--scarlet);
    margin-bottom: 2px;
  }}
  .map-box {{
    border: 1px solid var(--rule);
    line-height: 0;
  }}
  .legend {{
    display: flex;
    flex-wrap: wrap;
    gap: 2px 8px;
    margin-top: 2px;
    font-size: 12px;
    font-weight: 600;
    color: var(--ink-secondary);
  }}
  .leg-item {{
    display: inline-flex;
    align-items: center;
    gap: 3px;
  }}
  .leg-item i {{
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
  }}
  .briefs-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0 10px;
    border-top: 1px solid var(--ink-primary);
    padding-top: 2px;
  }}
  .brief {{
    font-weight: 400;
    font-size: 12px;
    line-height: 1.22;
    padding: 2px 0;
    border-bottom: 1px solid var(--rule);
    color: var(--ink-primary);
  }}
  .b-id {{
    font-weight: 700;
    color: var(--scarlet);
  }}
  .b-loc {{
    font-weight: 700;
    color: var(--ink-primary);
  }}
  .date-check {{
    background: var(--bg-panel);
    border: 1px solid var(--scarlet);
    border-left: 3px solid var(--scarlet);
    padding: 3px 7px;
    font-size: 12px;
    line-height: 1.22;
    color: var(--ink-primary);
  }}
  .footer {{
    display: flex;
    justify-content: space-between;
    border-top: 1px solid var(--ink-primary);
    padding-top: 2px;
    font-size: 12px;
    color: var(--ink-muted);
  }}
</style>
</head>
<body>
  <div class="page">
    <div>
      <div class="eyebrow">
        <span class="eyebrow-left">{html.escape(data["eyebrow_left"])}</span>
        <span class="eyebrow-right">{html.escape(data["eyebrow_right"])}</span>
      </div>
      <h1 class="masthead">{html.escape(data["masthead"])}</h1>
      <div class="deck">{html.escape(data["deck"])}</div>
      <div class="kpi-strip">{kpi_html}</div>
      <div class="reg-bar">{reg_html}</div>
    </div>

    <div class="leads">{leads_html}</div>

    <div class="cards">{cards_html}</div>

    <div class="bottom">
      <div>
        <div class="sec-hd">WHERE IT HAPPENED · PINS 1–13</div>
        <div class="map-box">{build_world_map_svg(data["pins"])}</div>
        <div class="legend">{legend_html}</div>
      </div>
      <div>
        <div class="sec-hd">ALSO ON SATURDAY 21 NOVEMBER · 14 MORE STORIES</div>
        <div class="briefs-grid">
          <div>{col1}</div>
          <div>{col2}</div>
        </div>
      </div>
    </div>

    <div class="date-check">{html.escape(data["date_check"])}</div>

    <div class="footer">
      <span>CONFIRMED = 2+ outlets; OFFICIAL = on the record. All Sat 21 Nov 2026.</span>
      <span>Sources: AP, Reuters, AFP, BBC, USGS, ESA, UKMTO, RNZ · Original vector art</span>
    </div>
  </div>
</body>
</html>'''
    out_html.write_text(page, encoding='utf-8')


if __name__ == '__main__':
    base = Path(__file__).resolve().parent
    generate_html(base / 'edition-data.json', base / 'index.html')
    print('Wrote index.html')
