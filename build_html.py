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
    <svg viewBox="0 0 320 112" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="54" fill="oklch(0.90 0.03 85)"/>
      <rect y="54" width="320" height="58" fill="oklch(0.75 0.07 225)"/>
      <path d="M0 62 L108 62 L92 112 L0 112 Z" fill="oklch(0.77 0.06 80)"/>
      <path d="M204 112 L320 76 L320 112 Z" fill="oklch(0.77 0.06 80)"/>
      <rect x="38" y="48" width="28" height="22" rx="2" fill="oklch(0.48 0.02 250)"/>
      <path d="M46 52 L58 20 L70 52 Z" fill="oklch(0.58 0.20 35)"/>
      <circle cx="62" cy="20" r="10" fill="oklch(0.42 0.01 260)" opacity="0.85"/>
      <circle cx="74" cy="12" r="12" fill="oklch(0.50 0.01 260)" opacity="0.75"/>
      <text x="14" y="90" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="11" fill="oklch(0.30 0.04 75)">BAHRAIN</text>
      <text x="234" y="104" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="9" fill="oklch(0.30 0.04 75)">KHASAB, OMAN</text>
      <!-- Tanker 1 & 2 -->
      <g transform="translate(172,48)">
        <polygon points="0,12 52,12 46,21 6,21" fill="oklch(0.22 0.01 260)"/>
        <rect x="8" y="6" width="24" height="6" fill="oklch(0.48 0.18 24)"/>
        <polygon points="16,12 22,-3 28,12" fill="oklch(0.72 0.18 65)"/>
      </g>
      <g transform="translate(234,62)">
        <polygon points="0,12 54,12 48,21 6,21" fill="oklch(0.22 0.01 260)"/>
        <rect x="8" y="6" width="26" height="6" fill="oklch(0.48 0.18 24)"/>
        <polygon points="18,12 24,-2 30,12" fill="oklch(0.72 0.18 65)"/>
      </g>
      <rect x="150" y="5" width="136" height="17" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="218" y="17" text-anchor="middle" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="10" fill="white">2 TANKERS HIT</text>
    </svg>""",
    'eu_indonesia': """
    <svg viewBox="0 0 320 112" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="112" fill="oklch(0.96 0.005 85)"/>
      <rect x="10" y="14" width="96" height="62" rx="2" fill="oklch(0.36 0.17 262)"/>
      <g fill="oklch(0.84 0.17 92)" transform="translate(58,45)">
        <circle cx="0" cy="-20" r="2.2"/><circle cx="10" cy="-17.3" r="2.2"/><circle cx="17.3" cy="-10" r="2.2"/>
        <circle cx="20" cy="0" r="2.2"/><circle cx="17.3" cy="10" r="2.2"/><circle cx="10" cy="17.3" r="2.2"/>
        <circle cx="0" cy="20" r="2.2"/><circle cx="-10" cy="17.3" r="2.2"/><circle cx="-17.3" cy="10" r="2.2"/>
        <circle cx="-20" cy="0" r="2.2"/><circle cx="-17.3" cy="-10" r="2.2"/><circle cx="-10" cy="-17.3" r="2.2"/>
      </g>
      <text x="58" y="88" text-anchor="middle" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="10" fill="oklch(0.36 0.17 262)">EU</text>
      <rect x="214" y="14" width="96" height="31" fill="oklch(0.50 0.21 25)"/>
      <rect x="214" y="45" width="96" height="31" fill="white" stroke="oklch(0.84 0.008 85)"/>
      <text x="262" y="88" text-anchor="middle" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="10" fill="oklch(0.50 0.21 25)">INDONESIA</text>
      <text x="160" y="14" text-anchor="middle" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="11" fill="oklch(0.18 0.01 260)">CEPA</text>
      <rect x="132" y="19" width="56" height="58" rx="3" fill="oklch(0.93 0.03 230)" stroke="oklch(0.50 0.13 240)" stroke-width="1.5"/>
      <line x1="142" y1="32" x2="178" y2="32" stroke="oklch(0.50 0.13 240)" stroke-width="2"/>
      <line x1="142" y1="42" x2="178" y2="42" stroke="oklch(0.50 0.13 240)" stroke-width="2"/>
      <line x1="142" y1="52" x2="168" y2="52" stroke="oklch(0.50 0.13 240)" stroke-width="2"/>
      <circle cx="172" cy="64" r="6" fill="oklch(0.48 0.18 24)"/>
      <rect x="20" y="92" width="280" height="16" rx="2" fill="oklch(0.18 0.01 260)"/>
      <text x="160" y="103" text-anchor="middle" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="9" fill="white">TARIFFS CUT ON 98.5% OF EU LINES</text>
    </svg>""",
    'mexico_sinaloa': """
    <svg viewBox="0 0 320 112" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="52" fill="oklch(0.28 0.04 145)"/>
      <rect y="52" width="320" height="60" fill="oklch(0.40 0.05 140)"/>
      <line x1="88" y1="22" x2="212" y2="22" stroke="oklch(0.15 0.01 260)" stroke-width="2.5"/>
      <ellipse cx="150" cy="36" rx="28" ry="10" fill="oklch(0.20 0.02 145)"/>
      <line x1="176" y1="36" x2="218" y2="31" stroke="oklch(0.20 0.02 145)" stroke-width="3"/>
      <g fill="oklch(0.20 0.02 145)">
        <circle cx="38" cy="54" r="4"/><rect x="33" y="59" width="10" height="22" rx="2"/>
        <circle cx="58" cy="54" r="4"/><rect x="53" y="59" width="10" height="22" rx="2"/>
        <circle cx="78" cy="54" r="4"/><rect x="73" y="59" width="10" height="22" rx="2"/>
      </g>
      <rect x="276" y="48" width="9" height="18" fill="oklch(0.45 0.14 150)"/>
      <rect x="285" y="48" width="9" height="18" fill="white"/>
      <rect x="294" y="48" width="9" height="18" fill="oklch(0.50 0.21 25)"/>
      <text x="150" y="88" text-anchor="middle" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="11" fill="oklch(0.93 0.01 90)">GUASAVE, SINALOA</text>
      <rect x="8" y="5" width="136" height="17" rx="2" fill="oklch(0.48 0.18 24)"/>
      <text x="76" y="17" text-anchor="middle" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="10" fill="white">11 DEAD IN SINALOA</text>
    </svg>""",
    'finland_ship': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="36" fill="oklch(0.86 0.03 230)"/>
      <rect y="36" width="188" height="28" fill="oklch(0.48 0.08 235)"/>
      <polygon points="34,42 108,42 100,52 40,52" fill="oklch(0.22 0.01 260)"/>
      <rect x="44" y="34" width="18" height="8" fill="white"/>
      <polygon points="68,42 78,22 88,42" fill="oklch(0.60 0.20 35)"/>
      <circle cx="84" cy="20" r="8" fill="oklch(0.46 0.01 260)" opacity="0.85"/>
      <circle cx="96" cy="13" r="10" fill="oklch(0.56 0.01 260)" opacity="0.75"/>
      <text x="122" y="50" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="11" fill="white">16 SAFE</text>
    </svg>""",
    'bitcoin_chart': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="64" fill="oklch(0.22 0.02 250)"/>
      <circle cx="24" cy="28" r="11" fill="oklch(0.72 0.16 70)"/>
      <text x="24" y="32" text-anchor="middle" font-family="Georgia, serif" font-weight="700" font-size="13" fill="white">₿</text>
      <polyline points="42,22 78,48 118,38 158,24" fill="none" stroke="oklch(0.75 0.16 70)" stroke-width="2.5" stroke-linejoin="round"/>
      <circle cx="78" cy="48" r="3" fill="oklch(0.58 0.20 24)"/>
      <circle cx="158" cy="24" r="3" fill="oklch(0.70 0.15 150)"/>
      <text x="126" y="54" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="11" fill="oklch(0.78 0.14 75)">$60,190</text>
    </svg>""",
    'cop31_clock': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="64" fill="oklch(0.94 0.02 85)"/>
      <text x="20" y="40" font-family="Georgia, serif" font-weight="700" font-size="17" fill="oklch(0.22 0.02 250)">DAY 13</text>
      <circle cx="136" cy="34" r="17" fill="white" stroke="oklch(0.18 0.01 260)" stroke-width="2"/>
      <line x1="136" y1="34" x2="136" y2="22" stroke="oklch(0.18 0.01 260)" stroke-width="2" stroke-linecap="round"/>
      <line x1="136" y1="34" x2="145" y2="40" stroke="oklch(0.48 0.18 24)" stroke-width="2" stroke-linecap="round"/>
    </svg>""",
    'bepicolombo': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="64" fill="oklch(0.18 0.03 260)"/>
      <circle cx="150" cy="32" r="18" fill="oklch(0.62 0.02 250)"/>
      <circle cx="144" cy="26" r="4" fill="oklch(0.52 0.02 250)"/>
      <circle cx="156" cy="38" r="3" fill="oklch(0.52 0.02 250)"/>
      <rect x="48" y="25" width="22" height="14" fill="oklch(0.86 0.01 250)"/>
      <rect x="20" y="29" width="28" height="6" fill="oklch(0.55 0.15 245)"/>
      <rect x="70" y="29" width="28" height="6" fill="oklch(0.55 0.15 245)"/>
      <polygon points="70,30 98,27 98,37" fill="oklch(0.72 0.18 65)"/>
      <text x="122" y="56" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="9" fill="white">MERCURY</text>
    </svg>""",
    'peru_quake': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="64" fill="oklch(0.95 0.015 85)"/>
      <line x1="0" y1="34" x2="188" y2="34" stroke="oklch(0.86 0.01 85)" stroke-width="1"/>
      <polyline points="8,34 26,34 34,14 42,54 50,10 58,52 66,24 74,34 114,34" fill="none" stroke="oklch(0.48 0.18 24)" stroke-width="2.2" stroke-linejoin="round"/>
      <text x="124" y="42" font-family="Georgia, serif" font-weight="700" font-size="16" fill="oklch(0.18 0.01 260)">M6.7</text>
    </svg>""",
    'taiwan_jets': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="64" fill="oklch(0.90 0.03 230)"/>
      <line x1="94" y1="0" x2="94" y2="64" stroke="oklch(0.48 0.18 24)" stroke-width="2" stroke-dasharray="4 3"/>
      <g fill="oklch(0.30 0.03 250)">
        <polygon points="34,16 54,21 34,26 39,21"/>
        <polygon points="62,28 82,33 62,38 67,33"/>
        <polygon points="34,40 54,45 34,50 39,45"/>
      </g>
      <text x="124" y="50" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="11" fill="oklch(0.18 0.01 260)">21 JETS</text>
    </svg>""",
    'ust_luga': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="44" fill="oklch(0.20 0.03 255)"/>
      <rect y="44" width="188" height="20" fill="oklch(0.32 0.05 245)"/>
      <rect x="28" y="28" width="22" height="16" fill="oklch(0.40 0.02 250)"/>
      <rect x="58" y="24" width="22" height="20" fill="oklch(0.45 0.02 250)"/>
      <polygon points="64,28 76,10 88,28" fill="oklch(0.62 0.20 35)"/>
      <polygon points="108,16 122,20 108,24" fill="oklch(0.75 0.16 70)"/>
      <text x="122" y="56" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="10" fill="white">UST-LUGA</text>
    </svg>""",
    'bolsonaro_icu': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="64" fill="oklch(0.95 0.015 230)"/>
      <rect x="22" y="34" width="84" height="10" rx="2" fill="white" stroke="oklch(0.48 0.03 250)" stroke-width="2"/>
      <line x1="22" y1="24" x2="22" y2="54" stroke="oklch(0.48 0.03 250)" stroke-width="3"/>
      <line x1="106" y1="30" x2="106" y2="54" stroke="oklch(0.48 0.03 250)" stroke-width="3"/>
      <text x="124" y="45" font-family="Georgia, serif" font-weight="700" font-size="16" fill="oklch(0.48 0.18 24)">ICU</text>
    </svg>""",
    'cricket_nz': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="64" fill="oklch(0.93 0.03 145)"/>
      <line x1="34" y1="16" x2="48" y2="50" stroke="oklch(0.55 0.08 55)" stroke-width="5" stroke-linecap="round"/>
      <circle cx="62" cy="44" r="6" fill="oklch(0.48 0.18 24)"/>
      <text x="96" y="44" font-family="Georgia, serif" font-weight="700" font-size="17" fill="oklch(0.18 0.01 260)">486-4</text>
    </svg>""",
    'un_robots': """
    <svg viewBox="0 0 188 64" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="188" height="64" fill="oklch(0.94 0.01 250)"/>
      <rect x="28" y="20" width="32" height="24" rx="4" fill="oklch(0.48 0.03 250)"/>
      <circle cx="38" cy="30" r="3" fill="white"/>
      <circle cx="50" cy="30" r="3" fill="white"/>
      <circle cx="44" cy="32" r="21" fill="none" stroke="oklch(0.48 0.18 24)" stroke-width="3"/>
      <line x1="29" y1="17" x2="59" y2="47" stroke="oklch(0.48 0.18 24)" stroke-width="3"/>
      <text x="86" y="42" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="11" fill="oklch(0.18 0.01 260)">128 STATES</text>
    </svg>""",
}


def badge_html(status: str, kind: str, overlay: bool = False) -> str:
    cls = 'badge-official' if kind == 'official' else 'badge-confirmed'
    pos = 'badge-overlay' if overlay else ''
    return f'<span class="badge {cls} {pos}">{html.escape(status)}</span>'


def build_world_map_svg(pins: list[dict]) -> str:
    w, h = 340, 232

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
            f'<text y="2.8" text-anchor="middle" font-family="Arial Narrow, sans-serif" font-weight="700" font-size="7.5" fill="white">{p["id"]}</text>'
            f'</g>'
        )
    return f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg"><rect width="{w}" height="{h}" fill="oklch(0.955 0.006 85)"/>{polys}{pin_els}</svg>'


def generate_html(data_path: Path, out_html: Path) -> None:
    data = json.loads(data_path.read_text(encoding='utf-8'))

    timeline_html = ''.join(
        f'<div class="tl-item"><div class="tl-time">{html.escape(t["time"])}</div><div class="tl-lbl">{html.escape(t["label"])}</div></div>'
        for t in data['timeline']
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
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
    text-rendering: geometricPrecision;
  }}
  .page {{
    width: 1024px;
    height: 1024px;
    padding: 10px 20px 8px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .eyebrow {{
    display: flex;
    justify-content: space-between;
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 10.5px;
    letter-spacing: 0.04em;
    padding-bottom: 3px;
    border-bottom: 1px solid var(--ink-primary);
  }}
  .eyebrow-left {{ color: var(--scarlet); }}
  .eyebrow-right {{ color: var(--ink-primary); }}
  h1.masthead {{
    font-family: Didot, Georgia, serif;
    font-weight: 700;
    font-size: 51px;
    line-height: 1.05;
    text-align: center;
    letter-spacing: -0.01em;
    padding: 4px 0 3px;
    border-bottom: 2px solid var(--ink-primary);
  }}
  .timeline {{
    display: grid;
    grid-template-columns: 64px repeat(7, 1fr);
    align-items: center;
    border-bottom: 1px solid var(--rule);
    padding: 4px 0;
  }}
  .tl-badge {{
    background: var(--scarlet);
    color: white;
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 10px;
    line-height: 1.15;
    text-align: center;
    padding: 4px 2px;
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
    font-size: 11px;
    color: var(--scarlet);
  }}
  .tl-lbl {{
    font-size: 9px;
    color: var(--ink-secondary);
    white-space: nowrap;
  }}
  .leads {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    padding-bottom: 6px;
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
    margin: 4px 0 2px;
  }}
  .kicker {{
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 9.5px;
    color: var(--scarlet);
  }}
  .badge {{
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 8px;
    color: white;
    padding: 1.5px 5px;
    border-radius: 2px;
    letter-spacing: 0.02em;
  }}
  .badge-confirmed {{ background: var(--badge-confirmed); }}
  .badge-official {{ background: var(--badge-official); }}
  .badge-overlay {{
    position: absolute;
    top: 4px;
    right: 4px;
  }}
  .lead-card h2 {{
    font-family: Georgia, serif;
    font-weight: 700;
    font-size: 14px;
    line-height: 1.15;
    margin-bottom: 3px;
  }}
  .lead-card p {{
    font-size: 9.5px;
    line-height: 1.25;
    color: var(--ink-secondary);
  }}
  .cards {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 8px 10px;
    padding-bottom: 6px;
    border-bottom: 2px solid var(--ink-primary);
  }}
  .mini-art {{
    position: relative;
    height: 64px;
    border: 1px solid var(--ink-secondary);
    overflow: hidden;
  }}
  .kicker-sm {{
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 8.5px;
    color: var(--scarlet);
    margin-top: 3px;
  }}
  .mini-card h3 {{
    font-family: Georgia, serif;
    font-weight: 700;
    font-size: 11.5px;
    line-height: 1.15;
    margin: 1px 0 2px;
  }}
  .mini-card p {{
    font-size: 9.2px;
    line-height: 1.22;
    color: var(--ink-secondary);
  }}
  .bottom {{
    display: grid;
    grid-template-columns: 340px 1fr;
    gap: 14px;
    align-items: start;
  }}
  .sec-hd {{
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    font-size: 10px;
    color: var(--scarlet);
    margin-bottom: 4px;
  }}
  .map-box {{
    border: 1px solid var(--rule);
    line-height: 0;
  }}
  .legend {{
    display: flex;
    flex-wrap: wrap;
    gap: 3px 9px;
    margin-top: 4px;
    font-size: 8.5px;
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
    gap: 0 14px;
    border-top: 1px solid var(--ink-primary);
    padding-top: 4px;
  }}
  .brief {{
    font-size: 9.2px;
    line-height: 1.28;
    padding: 3.5px 0;
    border-bottom: 1px solid var(--rule);
    color: var(--ink-secondary);
  }}
  .b-id {{
    font-family: "Arial Narrow", Arial, sans-serif;
    font-weight: 700;
    color: var(--scarlet);
  }}
  .b-loc {{
    font-family: Georgia, serif;
    font-weight: 700;
    color: var(--ink-primary);
  }}
  .date-check {{
    margin-top: 7px;
    background: var(--bg-panel);
    border: 1px solid var(--rule);
    border-top: 2px solid var(--scarlet);
    padding: 6px 8px;
    font-size: 9.5px;
    line-height: 1.3;
    color: var(--ink-primary);
  }}
  .footer {{
    display: flex;
    justify-content: space-between;
    border-top: 1px solid var(--ink-primary);
    padding-top: 4px;
    font-size: 8.5px;
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
        <div class="sec-hd">ALSO ON SATURDAY 21 NOVEMBER · 14 MORE STORIES</div>
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
