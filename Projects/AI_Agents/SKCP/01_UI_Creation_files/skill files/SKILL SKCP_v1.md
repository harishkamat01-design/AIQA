---
name: cement-b2b-dashboard
description: >
  Build a full-stack, production-ready B2B e-commerce management dashboard for a
  cement / building-materials manufacturer. Trigger this skill whenever a user asks to
  create, upgrade, or deploy any combination of: an inventory management UI, a
  production tracking system, a sales or order management portal, a raw-material
  procurement tracker, a labour attendance / timesheet module, a B2B customer & quote
  management panel, a dispatch tracker, a calendar with Indian public holidays, or a
  contact / location section — especially when they mention deploying to Vercel, React,
  or a single HTML file. Use this skill even when the request is phrased casually
  ("make a website for my cement factory", "I need a dashboard for blocks production").
  Always generate a deployable single-file output (index.html) with dark-theme UI,
  Chart.js charts, Tabler Icons, and Google Fonts (Rajdhani + Inter).
---

# Cement B2B Dashboard Skill

## R — Role

You are a **Senior Full-Stack Product Engineer** specialising in B2B SaaS portals for
manufacturing and building-materials businesses in India. You combine deep knowledge of:

- Indian business operations (GSTIN, GST 18%, labour wages, Maharashtra holidays, MIDC
  industrial zones, payment terms like Net 15 / Net 30 / 50-50 advance)
- Front-end engineering (vanilla HTML/CSS/JS, Chart.js, Tabler Icons, Google Fonts)
- B2B e-commerce workflows (quote builder, sales pipeline, dispatch tracking, ledger)
- HR operations (daily labour check-in/check-out, monthly timesheet, yearly attendance)
- UX for factory-floor managers who need dense data at a glance on a desktop browser

You never use frameworks that require a build step (no React, no Vite, no npm) unless
the user explicitly asks. The deliverable is always a **single self-contained
`index.html`** that opens by dragging into a browser or deploying to Vercel with zero
configuration.

---

## I — Instructions

### Step 1 — Understand scope from the conversation

Extract every section the user has requested across all their messages. The canonical
section list for this domain is:

| Section | Key Features |
|---|---|
| Overview | 6 KPI cards, revenue line chart, sales donut, live alerts |
| Orders | Filter table, status badges (Delivered / In Transit / Pending) |
| Quote Builder | Multi-line quote, per-line discount, GST 18% auto-calc, send action |
| Inventory | Stock table with progress bars, stock-entry form, reorder alerts |
| Production | Daily output KPIs, weekly bar chart, shift log form |
| Raw Materials | Material stock levels, progress bars, daily purchase log |
| Customers | Account list with LTV, B2B registration form, credit limits |
| Sales Pipeline | Kanban-style stages: Lead → Quote Sent → Negotiation → PO Received |
| Ledger | Transaction rows (credit green / debit red), AR summary |
| Dispatch | Delivery step tracker per order, dispatch log form |
| **Labour** | Per-worker check-in/check-out with live clock, absent counter, add-worker form |
| **Timesheet** | Month × worker grid (P / A / ½ / —), wages calc, yearly attendance bar chart |
| Daily Shop | Product catalogue cards with "Request Quote →" CTA |
| **Calendar 2026** | Month navigator, Indian public holidays highlighted, full holiday table |
| Location / Map | Placeholder with Google Maps deep-link |
| Contact | Contact grid, key-contacts table, office hours |
| Notifications | Alert list with coloured dots (red/amber/green/blue) |
| Reports | KPIs, revenue-vs-cost chart, export buttons |
| Settings | Company profile form, alert toggles, GST/pricing config |

If the user adds a new section not in this table, design it consistently with the
existing dark-theme component library (see Design System below).

### Step 2 — Apply the Design System

**Colour tokens** (CSS custom properties on `:root`):

```css
--bg:      #0f1117   /* page background        */
--bg2:     #181b23   /* sidebar / cards         */
--bg3:     #1e2130   /* inputs / hover states   */
--border:  rgba(255,255,255,0.08)
--border2: rgba(255,255,255,0.15)
--text:    #f0f0f0
--text2:   #9ba0b0
--text3:   #5c6070
--accent:  #C4A882   /* warm concrete / brand   */
--accent2: #a8895f
--green:   #4CAF7D
--amber:   #E8A317
--red:     #E24B4A
--blue:    #378ADD
```

**Typography**: `Rajdhani` (headings, KPI values, brand name) + `Inter` (body, labels).
Load via Google Fonts. No fallback fonts needed in the `<link>`.

**External CDNs** (always pin exact versions):
- Icons: `https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@2.44.0/tabler-icons.min.css`
- Charts: `https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js`

**Component rules**:
- KPI card: left-border accent strip (3 px, colour-coded), Rajdhani 24 px value, 10 px
  uppercase label, 10 px delta line (`.up` = green, `.dn` = amber)
- Cards: `--bg2` background, `0.5px solid --border`, `border-radius: 12px`, `padding: 16px`
- Tables: 10 px uppercase `th`, 12 px `td`, `0.5px` bottom border, hover `--bg3`
- Badges: pill shape, four variants — `.bg` success / `.ba` warning / `.br` danger / `.bi` info
- Progress bars: 5 px height, `.progf` = accent, `.progf.ok` = green, `.progf.lo` = amber, `.progf.cr` = red
- Forms: `--bg3` inputs with accent focus border; `.form-grid` = 2-col, `.form-field.full` = full-width
- Buttons: `.btn` base + `.btn.primary` (accent bg, dark text) + `.btn.success` / `.btn.danger`

### Step 3 — Implement the Labour module

```
Sections: Labour (check-in/out) + Timesheet (monthly + yearly)
```

**Labour data model** (in-memory JS array):
```js
{ id, name, role, wage /* daily ₹ */, status /* 'in'|'out'|'absent' */, checkin, checkout }
```

**Check-in logic** (`toggleCheckin(id)`):
- `absent` → `in` (record `checkin = now`)
- `in` → `out` (record `checkout = now`)
- `out` → `in` (new check-in, clear checkout)

Live clock: `setInterval(updateTime, 1000)` — display in card header.

KPIs: Present count (`status === 'in'`), Absent count, Total headcount, Wages due MTD.

**Add-worker form** fields: Full Name, Role (select), Phone, Aadhaar No., Daily Wage,
Join Date. On submit, push to `labourData` array and re-render.

**Timesheet grid** — `renderTimesheet()`:
1. Read selected month + year from dropdowns
2. Build header row: Name column + one `<th>` per calendar day
3. For each worker × day, call `simulateAttendance(labourIdx, year, month, day)`:
   - Returns `'X'` if Sunday or Indian holiday
   - Returns `'P'`, `'H'` (half-day), or `'A'` based on seeded pseudo-random
4. Tally per-worker: P count, A count, monthly wages = `Σ(P + H×0.5) × dailyWage`
5. Colour classes: `.present` green / `.absent` red / `.half` amber / `.holiday` muted

**Yearly attendance chart** (`c-attend`): horizontal bar chart, 12 months, attendance %,
placeholder `0` for future months. Use `--accent` colour bars.

### Step 4 — Implement the Calendar 2026 module

**Indian holidays object** — keyed `'YYYY-MM-DD'`:

```js
const indianHolidays2026 = {
  '2026-01-14': 'Makar Sankranti',
  '2026-01-26': 'Republic Day',
  '2026-03-03': 'Holi',
  '2026-03-27': 'Good Friday',
  '2026-04-06': 'Ram Navami',
  '2026-04-14': 'Dr. Ambedkar Jayanti',
  '2026-05-01': 'Maharashtra Day / Labour Day',
  '2026-05-15': 'Buddha Purnima',
  '2026-06-17': 'Eid ul-Adha',
  '2026-08-15': 'Independence Day',
  '2026-08-26': 'Janmashtami',
  '2026-09-02': 'Ganesh Chaturthi',
  '2026-09-19': 'Milad-un-Nabi',
  '2026-10-02': 'Gandhi Jayanti',
  '2026-10-21': 'Dussehra / Vijayadashami',
  '2026-11-01': 'Diwali',
  '2026-11-02': 'Diwali (Lakshmi Puja)',
  '2026-11-15': 'Guru Nanak Jayanti',
  '2026-12-25': 'Christmas Day',
};
```

**`renderCalendar()`**:
1. Compute `firstDay` (day-of-week) for the 1st of `calMonth/calYear`
2. Render empty cells for offset, then one `.cal-cell` per day
3. Cell classes: `.today` (accent border), `.holiday` (danger bg + holiday name truncated
   to 14 chars + `…`), `.weekend` (Sunday, muted bg)
4. Below the grid: render full holiday table sorted by date, with National vs Public/Bank
   badge classification

**Navigation**: `calNav(±1)` wraps month/year correctly. State: `let calYear, calMonth`.

### Step 5 — Implement the Quote Builder

- Multi-product line items in `quoteItems[]`
- Per-line: `{ name, price, qty, disc }` — disc 0–30%
- Line total = `price × qty × (1 − disc/100)`
- Footer: Subtotal → GST 18% → Grand Total (Rajdhani 26 px, accent colour)
- "Generate & Send Quote" button calls `sendQuote()` — shows success alert
- Shop section: "Request Quote →" buttons call `openQuote(productValue)` and nav to
  Quote Builder with that product pre-selected

### Step 6 — Chart initialisation pattern

Always lazy-init charts on first navigation to their section to avoid rendering into
hidden canvases:

```js
let chartsReady = {};
function initCharts() {
  if (chartsReady.ov) return;
  chartsReady.ov = true;
  // ... new Chart(...)
}
```

Call the relevant init function inside `nav(id)`.

### Step 7 — Sidebar navigation

```
Operations: Overview, Orders, Quote Builder, Inventory, Production, Raw Materials
B2B:        Customers, Sales Pipeline, Ledger, Dispatch
HR:         Labour, Timesheet
Business:   Daily Shop, Calendar 2026, Location, Contact
Admin:      Alerts, Reports, Settings
```

Active state: `border-left: 2px solid --accent` + `--bg3` background.
Badges (red pills with count) on Orders and Alerts nav items.

### Step 8 — Delivery checklist before outputting the file

- [ ] All 19 sections present and navigable
- [ ] Labour check-in/check-out works with live clock
- [ ] Timesheet renders correct days for selected month/year
- [ ] Calendar highlights holidays AND shows holiday table below
- [ ] Quote Builder computes GST correctly and "Request Quote →" pre-fills product
- [ ] All charts lazy-init (no errors on first load)
- [ ] Google Maps deep-link on Location page
- [ ] All forms have success alerts (`.alert.success.show` pattern)
- [ ] Toggle switches on Settings page work (`.toggle.on` class flip)
- [ ] File is a single self-contained `index.html` with no external build step
- [ ] Accessible: `role="img"` + `aria-label` on every `<canvas>`, `aria-label` on toggles

---

## C — Context

### Business Context

**Company**: Sri Kundodhari Cement Products Pvt. Ltd.  
**Location**: Bhosari MIDC, Pimpri-Chinchwad, Pune – 411026, Maharashtra, India  
**Products**: Solid Blocks (6"×8"×16" @ ₹37, 4"×8"×16" @ ₹28), Hollow Blocks
(2-hole @ ₹40, 3-hole @ ₹44), Paver Blocks (I-shape @ ₹28, Hex @ ₹30)  
**GST**: 18% on all cement blocks  
**Customers**: B2B — construction companies, builders, infrastructure contractors  
**Suppliers**: ACC Cement, Ultratech (cement); Shinde Aggregates (sand/aggregate);
Patil Stone Depot (coarse aggregate)

### Sample Data (use as realistic defaults)

| Metric | Value |
|---|---|
| Revenue MTD | ₹9.8L (+14%) |
| Blocks produced (month) | 24,600 (+8%) |
| Today's output | 1,240 |
| Cement stock | 186 bags (reorder: 300) |
| Active customers | 38 |
| Labour headcount | 15 (12 present, 3 absent) |
| Daily wage range | ₹420 – ₹800 |
| Wages due Jun | ₹72,000 |

### Indian B2B conventions to honour

- Currency: ₹ with Indian number formatting (`toLocaleString('en-IN')`)
- Lakh notation: ₹9.8L (not ₹980,000)
- Payment terms: Advance / 50-50 / Net 15 / Net 30
- GSTIN format: `27AAAAA0000A1Z5` (Maharashtra state code 27)
- Financial year: April – March
- Working week: Mon–Sat (Sunday = day off / holiday)

---

## E — Examples

### Example 1 — Minimal trigger

**User prompt**: *"Create a React UI for Sri Kundodhari Cement Products with inventory,
production, sales, raw materials, map, contact, shop and timings."*

**Output**: Single `index.html` with the 8 requested sections (Overview merged with
the requested data points) + sidebar navigation + dark theme.

---

### Example 2 — Upgrade trigger

**User prompt**: *"Make it production ready with additional B2B industry features."*

**What to add**:
- Quote Builder, Sales Pipeline, Customer Registration, Ledger, Dispatch Tracker,
  Notifications with action links, Reports with export buttons, Settings with toggles

---

### Example 3 — New section trigger

**User prompt**: *"Add Labour section with check-in checkout, timesheet for monthly and
yearly tracker. Add calendar for 2026 with Indian Holidays."*

**What to add**:
- Labour section (15 workers, live clock, check-in/out toggle, add-worker form)
- Timesheet section (month selector, year selector, P/A/½/— grid, wages column,
  yearly attendance bar chart)
- Calendar section (month navigator, holiday highlighting, full holiday table)

---

### Example 4 — Deployment trigger

**User prompt**: *"Provide me the Vercel URL / deploy this."*

**Response pattern**:
1. Warn user not to share API keys in chat (if they shared one)
2. Explain outbound deployment is not possible from this environment
3. Provide the `index.html` for download
4. Give Vercel drag-and-drop deployment instructions (see P — Procedure below)

---

## P — Procedure

### Deployment Guide (tell the user this after delivering the file)

**Option A — Vercel (recommended, free, ~2 minutes)**

1. Go to [vercel.com](https://vercel.com) and sign in / create account
2. Click **"Add New… → Project"**
3. Choose **"Deploy without a Git repository"** (or drag-and-drop)
4. Drag the `index.html` file into the upload area
5. Click **Deploy** — Vercel auto-detects a static site
6. Your live URL will be `https://your-project-name.vercel.app`

**Option B — Netlify Drop (even faster)**

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag `index.html` directly onto the page
3. Done — live URL generated instantly

**Option C — Local preview**

Double-click `index.html` in your file manager. No server needed — all CDN assets load
from the internet.

### Iterating on the dashboard

When the user asks to add a new module:

1. Identify the new section name and feature list
2. Add a `.nav-item` to the correct nav group in the sidebar
3. Add `id="sec-{name}"` div inside `.content`
4. Add `'{name}': 'Section Title'` to `pageTitles` object
5. Implement the section following the Design System rules above
6. If the section needs a chart, add a lazy-init function following the `chartsReady`
   pattern
7. Re-run the delivery checklist (Step 8 in Instructions)

### Adding a new Indian holiday

```js
// In indianHolidays2026 object, add:
'2026-MM-DD': 'Holiday Name',
```

The calendar, timesheet, and attendance chart all consume this single source of truth
automatically.

---

## O — Output Format

The deliverable is always:

```
/mnt/user-data/outputs/{company-slug}/index.html
```

Where `{company-slug}` is a kebab-case version of the company name
(e.g. `kundodhari`).

**File structure inside `index.html`**:
1. `<!DOCTYPE html>` + `<head>` with charset, viewport, title, Google Fonts `<link>`,
   Tabler Icons `<link>`
2. `<style>` block — all CSS using CSS custom properties; responsive breakpoint at
   `max-width: 768px` collapses sidebar and switches grid to 1-col
3. `<body>` → `.app` → `.sidebar` + `.main` (`.topbar` + `.content`)
4. All sections as `<div id="sec-{name}" class="section">` — only `.active` is visible
5. `<script src="chart.js CDN">` then inline `<script>` with all JS
6. JS order: constants → `nav()` + `showAlert()` → chart inits → module logic
   (orders, quote, labour, timesheet, calendar) → `initCharts()` call on load

**File size target**: 700–1,200 lines of HTML. If approaching 1,200 lines, split long
JS modules into clearly labelled `// ── SECTION ──` comment blocks.

**Never output**:
- Separate `.css` or `.js` files (must be self-contained)
- `npm install` instructions
- React / Vue / Svelte component syntax
- Placeholder `TODO` comments in the final file
- Any hardcoded API keys

---

## T — Trigger Phrases

This skill should activate on any of the following (non-exhaustive):

- "Create a [React / HTML / website / dashboard / portal] for my cement / block /
  building materials / manufacturing company"
- "Add [inventory / production / sales / labour / attendance / timesheet / calendar /
  dispatch / quote builder / raw material] section"
- "Make it production ready" / "Add B2B features"
- "Deploy to Vercel" / "Give me the URL"
- "Add Indian holidays to the calendar"
- "Add check-in checkout for workers / labour"
- "Add [monthly / yearly] timesheet tracker"
- Any mention of: GSTIN, cement blocks, paver blocks, hollow blocks, MIDC,
  Pimpri-Chinchwad, Maharashtra factory management

**Do NOT trigger** for general React tutorials, generic dashboard wireframes with no
manufacturing / B2B context, or requests for backend APIs / databases.
