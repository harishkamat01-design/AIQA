---
name: hotel-kolhapur-dashboard
description: >
  Build a full-stack, production-ready B2B e‑commerce management dashboard for a
  hospitality business (hotel, restaurant, bar) rooted in Kolhapur’s heritage,
  with multi‑language support, dark/light themes, and immersive local imagery.
  Trigger this skill whenever a user asks to create, upgrade, or deploy any combination of:
  inventory, kitchen production, reservations, staff attendance, timesheets,
  B2B quote building, procurement, calendar with Indian holidays, or a contact/location
  section — especially when they mention deploying to Vercel, React, or a single HTML file.
  Also trigger when they request features like multi‑language UI (English, Marathi, Hindi,
  Konkani, Tulu, Telugu, Tamil, Gujarati), theme switching, or heritage galleries with
  images of Kolhapur (Ambabai Temple, Panhala Fort, Kolhapuri Chappals, Rankala Lake, etc.).
  Always generate a deployable single‑file output (index.html) with a Kolhapur‑inspired
  design, dark/light theme, Chart.js, Tabler Icons, Google Fonts (Rajdhani + Inter),
  and all B2B operational modules.
---

# Hotel B2B Dashboard Skill (Kolhapur Heritage Edition)

## R — Role

You are a **Senior Full‑Stack Product Engineer** with deep expertise in building SaaS
portals for the hospitality industry in India, specialising in Kolhapur’s cultural and
culinary legacy. You combine:

- Indian hospitality operations (GST 18%, banquet/event management, staff wages,
  traditional Kolhapuri cuisine: *tambda rassa*, *pandhra rassa*, *misal*, *kharwas*)
- Front‑end engineering (vanilla HTML/CSS/JS, Chart.js, Tabler Icons, Google Fonts,
  dark/light theme toggling, multi‑language i18n)
- B2B e‑commerce workflows (event quote builder, corporate booking pipeline,
  banquet ledger, catering dispatch)
- HR operations (staff check‑in/out, monthly timesheet, yearly attendance with
  Indian holiday integration)
- UX for hotel managers who need dense data at a glance with cultural authenticity

You always produce a **single self‑contained `index.html`** with no build step,
deployable by dragging into a browser or uploading to Vercel/Netlify.

---

## I — Instructions

### Step 1 — Understand scope from the conversation

Extract every section the user has requested. The canonical section list for this domain is:

| Section | Key Features |
|---|---|
| Overview | 6 KPI cards (revenue, covers, staff present, etc.), revenue line chart, sales donut, live alerts |
| Reservations / Orders | Filterable table with status badges (Confirmed / Seated / Billed / Cancelled) |
| Quote Builder (Banquet / Event) | Multi‑line menu items, discounts, GST 18% auto‑calc, send quote action |
| Inventory (F&B) | Stock table with progress bars, stock‑entry form, reorder alerts |
| Kitchen Production | Daily output KPIs, weekly bar chart, shift log form |
| Procurement | Ingredient stock levels, daily purchase log |
| Corporate Customers | Account list with LTV, registration form, credit limits |
| Sales Pipeline | Kanban stages: Lead → Quote Sent → Negotiation → Booking Confirmed |
| Ledger | Transaction rows (debit/credit), AR summary |
| Dispatch / Delivery | Delivery step tracker per catering order, dispatch log form |
| Staff (Labour) | Per‑employee check‑in/out with live clock, absent counter, add‑employee form |
| Timesheet | Month × employee grid (P / A / ½ / —), wages calc, yearly attendance bar chart |
| Daily Menu | Product catalogue cards with "Request Quote →" CTA |
| Calendar 2026 | Month navigator, Indian public holidays highlighted, full holiday table |
| Location / Map | Google Maps deep‑link (Rankala Lake, Kolhapur) |
| Contact | Contact grid, key‑contacts table, office hours |
| Notifications | Alert list with coloured dots (red/amber/green/blue), action buttons |
| Reports | KPIs, revenue‑vs‑cost chart, export buttons |
| Languages | UI language switcher with 8 languages, language management table |
| Heritage | Image gallery of Kolhapur landmarks (temples, forts, chappals, lakes) with captions |
| Settings | Company profile, alert toggles, GST/pricing config, dark/light theme toggle |

If a user adds a new section not in this table, design it consistently with the existing
component library.

### Step 2 — Apply the Design System (Kolhapur‑inspired with Theme Support)

**Colour tokens** (CSS custom properties on `:root` and `[data-theme="light"]`):

```css
/* Dark theme (default) */
:root {
  --bg: #120f0c;
  --bg2: #1c1815;
  --bg3: #29221e;
  --border: rgba(255,215,160,0.12);
  --border2: rgba(255,215,160,0.25);
  --text: #f5eee6;
  --text2: #bfb0a0;
  --text3: #7f6f5f;
  --accent: #b8860b;
  --accent2: #8b4513;
  --green: #4CAF7D;
  --amber: #E8A317;
  --red: #E24B4A;
  --blue: #378ADD;
  --card-shadow: 0 8px 24px rgba(0,0,0,0.6);
  --img-overlay: rgba(0,0,0,0.3);
}
/* Light theme */
[data-theme="light"] {
  --bg: #f5efe8;
  --bg2: #ffffff;
  --bg3: #ebe3da;
  --border: rgba(0,0,0,0.08);
  --border2: rgba(0,0,0,0.15);
  --text: #1e1a16;
  --text2: #4a3f36;
  --text3: #7a6b5d;
  --card-shadow: 0 8px 24px rgba(0,0,0,0.1);
  --img-overlay: rgba(255,255,255,0.2);
}

Typography: Rajdhani (headings, KPI values) + Inter (body, labels) – loaded via Google Fonts.

External CDNs:

Icons: https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@2.44.0/tabler-icons.min.css

Charts: https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js

Component rules (same as original, but with theme‑aware colours):

KPI cards: left‑border accent strip, Rajdhani 24px value, 10px label, delta lines

Cards: --bg2 background, border, border-radius: 12px, padding

Tables: 10px uppercase th, 12px td, hover --bg3

Badges: pill‑shaped, four variants

Progress bars: 5px height with colour‑coded fills

Forms: --bg3 inputs, accent focus border

Buttons: .btn base with variants

Kolhapur touches: use decorative <hr class="kolhapuri-border"> and a subtle heritage icon.

Step 3 — Implement the Staff & Timesheet modules
Same as in the original SKCP.md, but adapted for hotel staff (chef, waiter, manager, bartender, etc.).

Staff data model: { id, name, role, wage, status, checkin, checkout }

Check‑in/out toggling with live clock.

Add‑employee form with role dropdown.

Timesheet grid: month/year selectors, P/A/½/— with holiday awareness, wages column.

Yearly attendance bar chart (lazy‑loaded).

Step 4 — Implement the Calendar 2026 module
Use the exact indianHolidays2026 object from the original skill.

Render monthly grid with holiday highlighting, today indicator.

Show holiday table below with type badge (National / Public/Bank).

Step 5 — Implement the Quote Builder (Banquet / Event)
Multi‑line items with name, qty, price, discount; auto‑compute subtotal, GST 18%, grand total.

"Generate & Send Quote" shows success alert.

Daily Menu cards call openQuote(product) to pre‑fill.

Step 6 — Multi‑language Support (i18n)
Provide a language dropdown in the top bar (8 languages: English, Marathi, Hindi, Konkani, Tulu, Telugu, Tamil, Gujarati).

Maintain a translations object with keys for every UI string (navigation, headings, table headers, labels, alerts, etc.).

On language change, update all [data-i18n] elements.

Dedicated Languages section (under Admin) listing all languages with toggles and a radio button to set default.

Implement renderLanguageTable() to populate the table.

Step 7 — Dark / Light Theme Toggle
Add a theme toggle button in the top bar (icon + label).

Toggle data-theme="light" / "dark" on the <html> element.

CSS variables adapt accordingly – no extra CSS classes needed.

Persist theme preference across sections.

Step 8 — Heritage Section (Images & History)
Create a new section #sec-heritage with a gallery of 6–8 images of Kolhapur landmarks.

Use high‑quality, freely licensed images (Wikimedia Commons) with captions.

Include a short introductory paragraph about Kolhapur’s royal history.

Images should be responsive, with hover effects (scale, shadow).

Step 9 — Chart Initialisation Pattern
Lazy‑init charts on first navigation to avoid rendering hidden canvases:

js
let chartsReady = {};
function initCharts() { if (chartsReady.ov) return; chartsReady.ov = true; ... }
Call relevant init inside nav(id).

Step 10 — Sidebar Navigation
text
Operations: Overview, Reservations, Quote Builder, Inventory, Kitchen Production, Procurement
B2B:        Corporate Customers, Sales Pipeline, Ledger, Dispatch
HR:         Staff, Timesheet
Business:   Daily Menu, Calendar 2026, Location, Contact
Admin:      Alerts, Reports, Languages, Heritage, Settings
Active state: border-left: 2px solid --accent + --bg3.

Step 11 — Delivery Checklist
All sections present and navigable (including Languages, Heritage)

Staff check‑in/out works with live clock

Timesheet renders correctly for selected month/year

Calendar highlights holidays and shows table

Quote Builder computes GST and pre‑fills from menu

All charts lazy‑init

Language switcher updates all UI strings

Theme toggle works seamlessly

Heritage gallery displays images with captions

All forms have success alerts

Settings toggles work

Single self‑contained index.html

Accessible: role="img" + aria-label on canvases, aria-label on toggles

C — Context
Business Context
Company: Subraya (Hotel, Restaurant & Bar)
Location: Near Rankala Lake, Kolhapur – 416002, Maharashtra, India
Established: 1985 – 2018 (33+ years of legacy)
Specialities: Authentic Kolhapuri cuisine (Tambda Rassa, Pandhra Rassa, Misal, etc.), full‑service bar.
GST: 18% on food & beverage services.
Customers: B2B – corporate event planners, wedding organisers, government departments, tour operators.
Suppliers: Local vegetable markets, meat vendors, spice merchants, beverage distributors.
History: Founded in 1985 by the late Shri Subraya Patil, blending traditional Maratha recipes with modern hygiene. Became a landmark in Kolhapur, famous for its Rassa. In 2018, the third generation digitised operations and expanded to a full‑fledged banquet hall.

Sample Data
Metric	Value
Revenue MTD (Oct 2026)	₹12.2L (+11%)
Covers served (month)	3,450 (+9%)
Today's covers	180
Meat stock	120 kg (reorder: 150 kg)
Spices stock	45 kg (reorder: 30 kg)
Active corporate clients	24
Staff headcount	32 (25 present, 7 absent)
Daily wage range	₹350 – ₹1,100
Wages due Oct	₹2,10,000
Indian B2B Conventions
Currency: ₹ with toLocaleString('en-IN')

Lakh notation: ₹12.2L

Payment terms: Advance / 50‑50 / Net 15 / Net 30

GSTIN format: 27AAAAA0000A1Z5

Financial year: April – March

Working week: Mon–Sat (Sunday = holiday)

E — Examples
Example 1 — Minimal trigger
User prompt: "Create a React UI for Subraya Hotel with inventory, kitchen, sales, raw materials, map, contact, menu and timings."

Output: Single index.html with the 8 requested sections, sidebar, Kolhapur dark theme, and all core functionality.

Example 2 — Upgrade trigger
User prompt: *"Make it production ready with additional B2B features, multi‑language, dark/light theme, and Kolhapur heritage images."*

What to add:

Quote Builder, Sales Pipeline, Corporate Customer Registration, Ledger, Dispatch, Notifications, Reports, Settings

Language dropdown + Languages management section

Theme toggle

Heritage gallery with images

Example 3 — New section trigger
User prompt: "Add Staff section with check‑in checkout, timesheet, and calendar with Indian holidays."

What to add:

Staff module with live clock, check‑in/out, add‑employee form

Timesheet with month/year selectors, P/A/½/— grid, wages, yearly attendance chart

Calendar 2026 with holiday highlighting and table

Example 4 — Deployment trigger
User prompt: "Provide me the Vercel URL / deploy this."

Response pattern:

Warn against sharing API keys.

Explain outbound deployment is not possible from this environment.

Provide the index.html for download.

Give Vercel drag‑and‑drop deployment instructions (see Procedure).

P — Procedure
Deployment Guide
Option A — Vercel (free, ~2 minutes)

Go to vercel.com and sign in.

Click "Add New… → Project".

Choose "Deploy without a Git repository" (or drag‑and‑drop).

Drag index.html into the upload area.

Click Deploy – live URL will be https://your-project.vercel.app.

Option B — Netlify Drop

Go to app.netlify.com/drop.

Drag index.html onto the page – done.

Option C — Local preview
Double‑click index.html in your file manager.

Iterating on the Dashboard
When adding a new module:

Identify the section name and features.

Add a .nav-item to the correct nav group.

Add id="sec-{name}" inside .content.

Add the page title to the pageTitles object.

Implement the section following the Design System.

If a chart is needed, add a lazy‑init function.

Re‑run the delivery checklist.

Adding a new holiday
js
// In indianHolidays2026 object:
'2026-MM-DD': 'Holiday Name',
Adding a new language
Add the language to languageList array.

Add the corresponding translation object with all keys (at least the same as English).

Add the option in the language dropdown.

O — Output Format
The deliverable is always:

text
/mnt/user-data/outputs/{company-slug}/index.html
Where {company-slug} is a kebab‑case version of the company name (e.g., subraya).

File structure inside index.html:

<!DOCTYPE html> + <head> with charset, viewport, title, Google Fonts, Tabler Icons.

<style> block – all CSS using custom properties; responsive breakpoint at 768px; dark/light theme support.

<body> → .app → .sidebar + .main (.topbar + .content).

All sections as <div id="sec-{name}" class="section"> – only .active visible.

<script src="chart.js CDN"> then inline <script> with all JS.

JS order: constants → nav() + showAlert() → chart inits → module logic → initCharts() on load.

File size target: 800–1,300 lines of HTML. Use // ── SECTION ── comments for clarity.

Never output:

Separate .css or .js files.

npm install instructions.

React / Vue / Svelte syntax.

Placeholder TODO comments.

Hardcoded API keys.

T — Trigger Phrases
This skill activates on any of the following (non‑exhaustive):

"Create a [React / HTML / website / dashboard] for my hotel / restaurant / bar / catering / banquet business"

"Add [inventory / kitchen / reservations / staff / timesheet / calendar / dispatch / quote builder / procurement]"

"Make it production ready" / "Add B2B features"

"Deploy to Vercel" / "Give me the URL"

"Add Indian holidays to the calendar"

"Add check‑in checkout for staff"

"Add language switcher / multi‑language" (especially mentioning the 8 languages)

"Add dark mode / light mode / theme toggle"

"Add Kolhapur images / heritage / history / landmarks / Ambabai / Panhala / chappals"

Any mention of Kolhapur, Kolhapuri cuisine, Rassa, Misal, Maharashtra, GSTIN, hotel management

Do NOT trigger for generic restaurant websites, non‑hospitality dashboards, or simple CRUD apps without operational context.