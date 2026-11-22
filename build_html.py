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
    <svg viewBox="0 0 320 140" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="68" fill="oklch(0.90 0.03 85)"/>
      <rect y="68" width="320" height="72" fill="oklch(0.75 0.07 225)"/>
      <path d="M0 78 L108 78 L92 140 L0 140 Z" fill="oklch(0.77 0.06 80)"/>
      <path d="M204 140 L320 96 L320 140 Z" fill="oklch(0.77 0.06 80)"/>
      <rect x="38" y="62" width="28" height="24" rx="2" fill="oklch(0.48 0.02 250)"/>
      <path d="M46 66 L58 34 L70 66 Z" fill="oklch(0.58 0.20 35)"/>
      <circle cx="62" cy="34" r="10" fill="oklch(0.42 0.01 260)" opacity="0.85"/>
      <circle cx="74" cy="24" r="12" fill="oklch(0.50 0.01 260)" opacity="0.75"/>
      <text x="14" y="114" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="11" fill="oklch(0.30 0.04 75)">BAHRAIN</text>
      <text x="234" y="130" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="9" fill="oklch(0.30 0.04 75)">KHASAB, OMAN</text>
      <g transform="translate(172,62)">
        <polygon points="0,12 52,12 46,21 6,21" fill="oklch(0.22 0.01 260)"/>
        <rect x="8" y="6" width="24" height="6" fill="oklch(0.48 0.18 24)"/>
        <polygon points="16,12 22,-3 28,12" fill="oklch(0.72 0.18 65)"/>
      </g>
      <g transform="translate(234,78)">
        <polygon points="0,12 54,12 48,21 6,21" fill="oklch(0.22 0.01 260)"/>
        <rect x="8" y="6" width="26" height="6" fill="oklch(0.48 0.18 24)"/>
        <polygon points="18,12 24,-2 30,12" fill="oklch(0.72 0.18 65)"/>
      </g>
      <rect x="132" y="6" width="176" height="26" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="220" y="24" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="15" fill="white">2 TANKERS HIT</text>
    </svg>""",
    'eu_indonesia': """
    <svg viewBox="0 0 320 140" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="140" fill="oklch(0.96 0.005 85)"/>
      <rect x="10" y="22" width="94" height="58" rx="2" fill="oklch(0.36 0.17 262)"/>
      <g fill="oklch(0.84 0.17 92)" transform="translate(57,51)">
        <circle cx="0" cy="-19" r="2.2"/><circle cx="9.5" cy="-16.4" r="2.2"/><circle cx="16.4" cy="-9.5" r="2.2"/>
        <circle cx="19" cy="0" r="2.2"/><circle cx="16.4" cy="9.5" r="2.2"/><circle cx="9.5" cy="16.4" r="2.2"/>
        <circle cx="0" cy="19" r="2.2"/><circle cx="-9.5" cy="16.4" r="2.2"/><circle cx="-16.4" cy="9.5" r="2.2"/>
        <circle cx="-19" cy="0" r="2.2"/><circle cx="-16.4" cy="-9.5" r="2.2"/><circle cx="-9.5" cy="-16.4" r="2.2"/>
      </g>
      <text x="57" y="96" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="9.5" fill="oklch(0.36 0.17 262)">EU · 98.5% CUT</text>
      <rect x="216" y="22" width="94" height="29" fill="oklch(0.50 0.21 25)"/>
      <rect x="216" y="51" width="94" height="29" fill="white" stroke="oklch(0.84 0.008 85)"/>
      <text x="263" y="96" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="9.5" fill="oklch(0.50 0.21 25)">ID · 90.4% CUT</text>
      <text x="160" y="18" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="11" fill="oklch(0.18 0.01 260)">CEPA</text>
      <rect x="132" y="26" width="56" height="54" rx="3" fill="oklch(0.93 0.03 230)" stroke="oklch(0.50 0.13 240)" stroke-width="1.5"/>
      <line x1="142" y1="38" x2="178" y2="38" stroke="oklch(0.50 0.13 240)" stroke-width="2"/>
      <line x1="142" y1="48" x2="178" y2="48" stroke="oklch(0.50 0.13 240)" stroke-width="2"/>
      <line x1="142" y1="58" x2="168" y2="58" stroke="oklch(0.50 0.13 240)" stroke-width="2"/>
      <circle cx="172" cy="68" r="5.5" fill="oklch(0.48 0.18 24)"/>
      <rect x="10" y="108" width="300" height="25" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="160" y="125" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="13.5" fill="white">TARIFFS CUT: 98.5% EU · 90.4% ID</text>
    </svg>""",
    'mexico_sinaloa': """
    <svg viewBox="0 0 320 140" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="66" fill="oklch(0.28 0.04 145)"/>
      <rect y="66" width="320" height="74" fill="oklch(0.40 0.05 140)"/>
      <line x1="88" y1="36" x2="212" y2="36" stroke="oklch(0.15 0.01 260)" stroke-width="2.5"/>
      <ellipse cx="150" cy="50" rx="28" ry="10" fill="oklch(0.20 0.02 145)"/>
      <line x1="176" y1="50" x2="218" y2="45" stroke="oklch(0.20 0.02 145)" stroke-width="3"/>
      <g fill="oklch(0.20 0.02 145)" transform="translate(0,14)">
        <circle cx="38" cy="54" r="4"/><rect x="33" y="59" width="10" height="22" rx="2"/>
        <circle cx="58" cy="54" r="4"/><rect x="53" y="59" width="10" height="22" rx="2"/>
        <circle cx="78" cy="54" r="4"/><rect x="73" y="59" width="10" height="22" rx="2"/>
      </g>
      <rect x="276" y="64" width="9" height="18" fill="oklch(0.45 0.14 150)"/>
      <rect x="285" y="64" width="9" height="18" fill="white"/>
      <rect x="294" y="64" width="9" height="18" fill="oklch(0.50 0.21 25)"/>
      <text x="150" y="112" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="11" fill="oklch(0.93 0.01 90)">GUASAVE, SINALOA</text>
      <rect x="8" y="6" width="188" height="26" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="102" y="24" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="15" fill="white">11 DEAD IN SINALOA</text>
    </svg>""",
    'finland_ship': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="44" fill="oklch(0.86 0.03 230)"/>
      <rect y="44" width="188" height="34" fill="oklch(0.48 0.08 235)"/>
      <polygon points="34,54 108,54 100,64 40,64" fill="oklch(0.22 0.01 260)"/>
      <rect x="44" y="46" width="18" height="8" fill="white"/>
      <polygon points="68,54 78,34 88,54" fill="oklch(0.60 0.20 35)"/>
      <circle cx="84" cy="32" r="8" fill="oklch(0.46 0.01 260)" opacity="0.85"/>
      <circle cx="96" cy="26" r="9" fill="oklch(0.56 0.01 260)" opacity="0.75"/>
      <text x="122" y="64" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="11" fill="white">16 SAFE</text>
      <rect x="4" y="4" width="96" height="14" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="52" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">FINLAND: SHIP ABLAZE</text>
    </svg>""",
    'bitcoin_chart': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="78" fill="oklch(0.22 0.02 250)"/>
      <circle cx="24" cy="42" r="11" fill="oklch(0.72 0.16 70)"/>
      <text x="24" y="46" text-anchor="middle" font-family="Libre Baskerville, Georgia, serif" font-weight="700" font-size="13" fill="white">₿</text>
      <polyline points="42,34 78,58 118,48 158,36" fill="none" stroke="oklch(0.75 0.16 70)" stroke-width="2.5" stroke-linejoin="round"/>
      <circle cx="78" cy="58" r="3" fill="oklch(0.58 0.20 24)"/>
      <circle cx="158" cy="36" r="3" fill="oklch(0.70 0.15 150)"/>
      <text x="126" y="68" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="11" fill="oklch(0.78 0.14 75)">$60,190</text>
      <rect x="4" y="4" width="88" height="14" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="48" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">BITCOIN: 8% SWING</text>
    </svg>""",
    'cop31_clock': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="78" fill="oklch(0.94 0.02 85)"/>
      <text x="20" y="54" font-family="Libre Baskerville, Georgia, serif" font-weight="700" font-size="17" fill="oklch(0.22 0.02 250)">DAY 13</text>
      <circle cx="136" cy="46" r="16" fill="white" stroke="oklch(0.18 0.01 260)" stroke-width="2"/>
      <line x1="136" y1="46" x2="136" y2="35" stroke="oklch(0.18 0.01 260)" stroke-width="2" stroke-linecap="round"/>
      <line x1="136" y1="46" x2="144" y2="51" stroke="oklch(0.48 0.18 24)" stroke-width="2" stroke-linecap="round"/>
      <rect x="4" y="4" width="82" height="14" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="45" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">COP31: OVERTIME</text>
    </svg>""",
    'bepicolombo': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="78" fill="oklch(0.18 0.03 260)"/>
      <circle cx="150" cy="44" r="17" fill="oklch(0.62 0.02 250)"/>
      <circle cx="144" cy="38" r="4" fill="oklch(0.52 0.02 250)"/>
      <circle cx="156" cy="50" r="3" fill="oklch(0.52 0.02 250)"/>
      <rect x="48" y="38" width="22" height="14" fill="oklch(0.86 0.01 250)"/>
      <rect x="20" y="42" width="28" height="6" fill="oklch(0.55 0.15 245)"/>
      <rect x="70" y="42" width="28" height="6" fill="oklch(0.55 0.15 245)"/>
      <polygon points="70,43 98,40 98,50" fill="oklch(0.72 0.18 65)"/>
      <text x="122" y="70" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="9" fill="white">MERCURY</text>
      <rect x="4" y="4" width="84" height="14" rx="2" fill="oklch(0.24 0.01 260)"/>
      <text x="46" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">SPACE: MERCURY</text>
    </svg>""",
    'peru_quake': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="78" fill="oklch(0.95 0.015 85)"/>
      <line x1="0" y1="46" x2="188" y2="46" stroke="oklch(0.86 0.01 85)" stroke-width="1"/>
      <polyline points="8,46 26,46 34,28 42,64 50,24 58,62 66,36 74,46 114,46" fill="none" stroke="oklch(0.48 0.18 24)" stroke-width="2.2" stroke-linejoin="round"/>
      <text x="124" y="54" font-family="Libre Baskerville, Georgia, serif" font-weight="700" font-size="16" fill="oklch(0.18 0.01 260)">M6.7</text>
      <rect x="4" y="4" width="84" height="14" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="46" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">PERU: M6.7 QUAKE</text>
    </svg>""",
    'taiwan_jets': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="78" fill="oklch(0.90 0.03 230)"/>
      <line x1="94" y1="0" x2="94" y2="78" stroke="oklch(0.48 0.18 24)" stroke-width="2" stroke-dasharray="4 3"/>
      <g fill="oklch(0.30 0.03 250)" transform="translate(0,8)">
        <polygon points="34,22 54,27 34,32 39,27"/>
        <polygon points="62,33 82,38 62,43 67,38"/>
        <polygon points="34,44 54,49 34,54 39,49"/>
      </g>
      <text x="124" y="60" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="11" fill="oklch(0.18 0.01 260)">21 JETS</text>
      <rect x="4" y="4" width="76" height="14" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="42" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">TAIWAN: 21 JETS</text>
    </svg>""",
    'ust_luga': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="54" fill="oklch(0.20 0.03 255)"/>
      <rect y="54" width="188" height="24" fill="oklch(0.32 0.05 245)"/>
      <rect x="28" y="38" width="22" height="16" fill="oklch(0.40 0.02 250)"/>
      <rect x="58" y="34" width="22" height="20" fill="oklch(0.45 0.02 250)"/>
      <polygon points="64,38 76,22 88,38" fill="oklch(0.62 0.20 35)"/>
      <polygon points="108,30 122,34 108,38" fill="oklch(0.75 0.16 70)"/>
      <text x="122" y="68" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="10" fill="white">UST-LUGA</text>
      <rect x="4" y="4" width="84" height="14" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="46" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">RUSSIA: DRONES</text>
    </svg>""",
    'bolsonaro_icu': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="78" fill="oklch(0.95 0.015 230)"/>
      <rect x="22" y="46" width="84" height="10" rx="2" fill="white" stroke="oklch(0.48 0.03 250)" stroke-width="2"/>
      <line x1="22" y1="36" x2="22" y2="66" stroke="oklch(0.48 0.03 250)" stroke-width="3"/>
      <line x1="106" y1="42" x2="106" y2="66" stroke="oklch(0.48 0.03 250)" stroke-width="3"/>
      <text x="124" y="56" font-family="Libre Baskerville, Georgia, serif" font-weight="700" font-size="16" fill="oklch(0.48 0.18 24)">ICU</text>
      <rect x="4" y="4" width="70" height="14" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="39" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">BRAZIL: ICU</text>
    </svg>""",
    'cricket_nz': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="78" fill="oklch(0.93 0.03 145)"/>
      <line x1="34" y1="30" x2="48" y2="64" stroke="oklch(0.55 0.08 55)" stroke-width="5" stroke-linecap="round"/>
      <circle cx="62" cy="58" r="6" fill="oklch(0.48 0.18 24)"/>
      <text x="96" y="58" font-family="Libre Baskerville, Georgia, serif" font-weight="700" font-size="17" fill="oklch(0.18 0.01 260)">486-4</text>
      <rect x="4" y="4" width="76" height="14" rx="2" fill="oklch(0.24 0.01 260)"/>
      <text x="42" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">CRICKET: 486-4</text>
    </svg>""",
    'un_robots': """
    <svg viewBox="0 0 188 78" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="78" fill="oklch(0.94 0.01 250)"/>
      <rect x="28" y="32" width="32" height="24" rx="4" fill="oklch(0.48 0.03 250)"/>
      <circle cx="38" cy="42" r="3" fill="white"/>
      <circle cx="50" cy="42" r="3" fill="white"/>
      <circle cx="44" cy="44" r="20" fill="none" stroke="oklch(0.48 0.18 24)" stroke-width="3"/>
      <line x1="30" y1="30" x2="58" y2="58" stroke="oklch(0.48 0.18 24)" stroke-width="3"/>
      <text x="86" y="54" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="11" fill="oklch(0.18 0.01 260)">128 STATES</text>
      <rect x="4" y="4" width="88" height="14" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="48" y="14" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="8.5" fill="white">UN: KILLER ROBOTS</text>
    </svg>""",
}


def badge_html(status: str, kind: str, overlay: bool = False) -> str:
    cls = 'badge-official' if kind == 'official' else 'badge-confirmed'
    pos = 'badge-overlay' if overlay else ''
    return f'<span class="badge {cls} {pos}">{html.escape(status)}</span>'


def build_world_map_svg(pins: list[dict]) -> str:
    w, h = 290, 152

    def proj(lon: float, lat: float) -> tuple[float, float]:
        px = ((lon + 180.0) / 360.0) * w
        py = ((82.0 - lat) / 142.0) * h
        return max(8, min(w - 8, px)), max(8, min(h - 8, py))

    continents = [
        [(-165, 65), (-130, 70), (-80, 62), (-55, 50), (-75, 28), (-100, 16), (-122, 36)],
        [(-80, 11), (-50, 5), (-35, -8), (-54, -36), (-70, -52), (-80, -15)],
        [(-10, 36), (0, 50), (15, 58), (35, 68), (55, 65), (50, 45), (30, 38), (5, 36)],
        [(-16, 35), (10, 37), (34, 31), (50, 12), (40, -10), (28, -34), (15, -30), (10, 5), (-16, 15)],
        [(35, 38), (60, 38), (75, 20), (105, 10), (122, 24), (142, 44), (165, 64), (100, 72), (55, 68)],
        [(114, -22), (145, -12), (153, -28), (138, -38), (115, -34)],
    ]
    polys = ''.join(
        '<polygon points="'
        + ' '.join(f'{proj(lo, la)[0]:.1f},{proj(lo, la)[1]:.1f}' for lo, la in poly)
        + '" fill="oklch(0.87 0.015 85)" stroke="oklch(0.76 0.015 85)" stroke-width="0.8"/>'
        for poly in continents
    )
    pin_els = ''
    for p in pins:
        px, py = proj(p['lon'], p['lat'])
        col = REGION_OKLCH.get(p['r'], 'oklch(0.24 0.01 260)')
        pin_els += (
            f'<g transform="translate({px:.1f},{py:.1f})">'
            f'<circle r="6.2" fill="{col}" stroke="white" stroke-width="1"/>'
            f'<text y="2.8" text-anchor="middle" font-family="Libre Franklin, Arial Narrow, sans-serif" font-weight="900" font-size="7.5" fill="white">{p["id"]}</text>'
            f'</g>'
        )
    return f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg"><rect width="{w}" height="{h}" fill="oklch(0.955 0.006 85)"/>{polys}{pin_els}</svg>'


def generate_html(data_path: Path, out_html: Path) -> None:
    data = json.loads(data_path.read_text(encoding='utf-8'))

    timeline_html = ''.join(
        f'<div class="tl-item"><div class="tl-time">{html.escape(t["time"])}</div><div class="tl-lbl">{html.escape(t["label"])}</div></div>'
        for t in data['timeline']
    )

    kpi_html = ''.join(
        f'<div class="kpi-item" style="border-left:3px solid {k["color"]}"><div class="kpi-num">{html.escape(k["num"])}</div><div class="kpi-lbl">{html.escape(k["label"])}</div></div>'
        for k in data['kpi_stats']
    )

    total_reg = sum(r['count'] for r in data['region_bar'])
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
        for b in data['briefs'][:5]
    )
    col2 = ''.join(
        f'<div class="brief"><span class="b-id">{b[0]}</span> <span class="b-loc">{html.escape(b[1])}:</span> {html.escape(b[2])}</div>'
        for b in data['briefs'][5:]
    )

    legend_html = ''.join(
        f'<span class="leg-item"><i style="background:{col}"></i>{name.title()}</span>'
        for name, col in REGION_OKLCH.items()
    )

    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<style>
  @font-face {{
    font-family: "Playfair Display";
    font-style: normal;
    font-weight: 700 900;
    font-display: block;
    src: url("./fonts/playfair-900.woff2") format("woff2");
  }}
  @font-face {{
    font-family: "Libre Baskerville";
    font-style: normal;
    font-weight: 400 700;
    font-display: block;
    src: url("./fonts/libre-baskerville.woff2") format("woff2");
  }}
  @font-face {{
    font-family: "Libre Franklin";
    font-style: normal;
    font-weight: 400 900;
    font-display: block;
    src: url("./fonts/libre-franklin-900.woff2") format("woff2");
  }}
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
    font-family: nyt-cheltenham, "Libre Baskerville", cheltenham-fallback-georgia, cheltenham-fallback-noto, georgia, "times new roman", times, serif;
    text-rendering: optimizeLegibility;
  }}
  .page {{
    width: 1024px;
    height: 1024px;
    padding: 8px 18px 6px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 2px;
  }}
  .eyebrow {{
    display: flex;
    justify-content: space-between;
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 12px;
    letter-spacing: 0.03em;
    padding-bottom: 2px;
    border-bottom: 1px solid var(--ink-primary);
  }}
  .eyebrow-left {{ color: var(--scarlet); }}
  .eyebrow-right {{ color: var(--ink-primary); }}
  h1.masthead {{
    font-family: nyt-cheltenham, "Playfair Display", "Libre Baskerville", georgia, serif;
    font-weight: 900;
    font-size: 38px;
    line-height: 1.02;
    text-align: center;
    letter-spacing: -0.015em;
    padding: 4px 0;
    border-bottom: 2px solid var(--ink-primary);
  }}
  .timeline {{
    display: grid;
    grid-template-columns: 64px repeat(5, 1fr);
    align-items: center;
    border-bottom: 1px solid var(--rule);
    padding: 3px 0;
  }}
  .kpi-strip {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 6px;
    padding: 3px 0;
    border-bottom: 1px solid var(--rule);
  }}
  .kpi-item {{
    padding-left: 6px;
  }}
  .kpi-num {{
    font-family: nyt-cheltenham, "Libre Baskerville", georgia, serif;
    font-weight: 700;
    font-size: 20px;
    line-height: 1.05;
    color: var(--scarlet);
  }}
  .kpi-lbl {{
    font-family: nyt-franklin, "Libre Franklin", helvetica, arial, sans-serif;
    font-weight: 600;
    font-size: 12px;
    line-height: 1.15;
    color: var(--ink-secondary);
    margin-top: 1px;
  }}
  .reg-bar {{
    display: flex;
    gap: 2px;
    margin-top: 3px;
  }}
  .reg-seg {{
    color: white;
    font-family: nyt-franklin, "Libre Franklin", "Arial Narrow", sans-serif;
    font-weight: 700;
    font-size: 12px;
    text-align: center;
    white-space: nowrap;
    padding: 2px 6px;
    border-radius: 1px;
  }}
  .tl-badge {{
    background: var(--scarlet);
    color: white;
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 12px;
    line-height: 1.1;
    text-align: center;
    padding: 3px 2px;
    border-radius: 2px;
  }}
  .tl-item {{
    text-align: center;
    border-left: 1px solid var(--rule);
    padding: 0 3px;
  }}
  .tl-time {{
    font-family: Georgia, serif;
    font-weight: 700;
    font-size: 13px;
    color: var(--scarlet);
  }}
  .tl-lbl {{
    font-size: 12px;
    color: var(--ink-secondary);
    white-space: nowrap;
  }}
  .leads {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    padding: 3px 0 4px;
    border-bottom: 1px solid var(--rule);
  }}
  .lead-art {{
    height: 112px;
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
    margin: 3px 0 2px;
  }}
  .kicker {{
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 12px;
    color: var(--scarlet);
  }}
  .badge {{
    font-family: "Arial Narrow", Arial, sans-serif;
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
    top: 4px;
    right: 4px;
  }}
  .lead-card h2 {{
    font-family: nyt-cheltenham, "Playfair Display", "Libre Baskerville", georgia, serif;
    font-weight: 900;
    font-size: 21px;
    line-height: 1.08;
    margin-bottom: 3px;
  }}
  .lead-card p {{
    font-family: nyt-cheltenham, "Libre Baskerville", cheltenham-fallback-georgia, cheltenham-fallback-noto, georgia, "times new roman", times, serif;
    font-size: 12px;
    line-height: 1.28;
    color: var(--ink-secondary);
  }}
  .cards {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px 14px;
    padding: 3px 0 5px;
    border-bottom: 2px solid var(--ink-primary);
  }}
  .mini-art {{
    position: relative;
    height: 62px;
    border: 1px solid var(--ink-secondary);
    overflow: hidden;
  }}
  .kicker-sm {{
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 12px;
    color: var(--scarlet);
    margin-top: 2px;
  }}
  .mini-card h3 {{
    font-family: nyt-cheltenham, "Playfair Display", "Libre Baskerville", georgia, serif;
    font-weight: 900;
    font-size: 16.5px;
    line-height: 1.10;
    margin: 1px 0 2px;
  }}
  .mini-card p {{
    font-family: nyt-franklin, "Libre Franklin", helvetica, arial, sans-serif;
    font-weight: 500;
    font-size: 12px;
    line-height: 1.25;
    color: var(--ink-secondary);
  }}
  .bottom {{
    display: grid;
    grid-template-columns: 290px 1fr;
    gap: 14px;
    align-items: start;
  }}
  .sec-hd {{
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 12px;
    color: var(--scarlet);
    margin-bottom: 3px;
  }}
  .map-box {{
    border: 1px solid var(--rule);
    line-height: 0;
  }}
  .legend {{
    display: flex;
    flex-wrap: wrap;
    gap: 2px 8px;
    margin-top: 3px;
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
    gap: 0 12px;
    border-top: 1px solid var(--ink-primary);
    padding-top: 3px;
  }}
  .brief {{
    font-family: nyt-franklin, "Libre Franklin", helvetica, arial, sans-serif;
    font-weight: 500;
    font-size: 12px;
    line-height: 1.25;
    padding: 2.5px 0;
    border-bottom: 1px solid var(--rule);
    color: var(--ink-primary);
  }}
  .b-id {{
    font-family: nyt-franklin, "Libre Franklin", "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    color: var(--scarlet);
  }}
  .b-loc {{
    font-family: nyt-cheltenham, "Libre Baskerville", cheltenham-fallback-georgia, cheltenham-fallback-noto, georgia, "times new roman", times, serif;
    font-weight: 700;
    color: var(--ink-primary);
  }}
  .date-check {{
    margin-top: 4px;
    background: var(--bg-panel);
    border: 1px solid var(--rule);
    border-top: 2px solid var(--scarlet);
    padding: 4px 8px;
    font-size: 12px;
    line-height: 1.28;
    color: var(--ink-primary);
  }}
  .footer {{
    display: flex;
    justify-content: space-between;
    border-top: 1px solid var(--ink-primary);
    padding-top: 3px;
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
      <div class="timeline">
        <div class="tl-badge">THE DAY<br/>IN UTC</div>
        {timeline_html}
      </div>
      <div class="kpi-strip">{kpi_html}</div>
      <div class="reg-bar">{reg_html}</div>
    </div>

    <div class="leads">{leads_html}</div>

    <div class="cards">{cards_html}</div>

    <div class="bottom">
      <div>
        <div class="sec-hd">WHERE IT HAPPENED</div>
        <div class="map-box">{build_world_map_svg(data["pins"])}</div>
        <div class="legend">{legend_html}</div>
      </div>
      <div>
        <div class="sec-hd">ALSO ON SATURDAY 21 NOVEMBER · 10 MORE STORIES</div>
        <div class="briefs-grid">
          <div>{col1}</div>
          <div>{col2}</div>
        </div>
        <div class="date-check">{html.escape(data["date_check"])}</div>
      </div>
    </div>

    <div class="footer">
      <span>Every story happened or was first reported on Sat 21 Nov 2026; claims attributed.</span>
      <span>Sources: AP, Reuters, AFP, BBC, USGS, ESA, UKMTO · Original vector drawings</span>
    </div>
  </div>
</body>
</html>'''
    out_html.write_text(page, encoding='utf-8')


if __name__ == '__main__':
    base = Path(__file__).resolve().parent
    generate_html(base / 'edition-data.json', base / 'index.html')
    print('Wrote index.html')
