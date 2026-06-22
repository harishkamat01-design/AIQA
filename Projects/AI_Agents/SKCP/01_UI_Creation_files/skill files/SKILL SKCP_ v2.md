---
name: shree-kundodari-cement-dashboard
description: >
  Build a production-ready B2B e-commerce and operations dashboard for Shree
  Kundodari Cement Products. Trigger this skill whenever a user asks to create,
  upgrade, or deploy a cement/building-materials management portal with inventory,
  production, sales, raw materials, labour attendance, timesheets, calendar,
  payments, dispatch, orders, customers, reports, or admin settings. Use this skill
  for requests involving React, Angular, TypeScript, JavaScript, HTML, CSS, or a
  single-file dashboard output.
---

# Shree Kundodari Cement Dashboard Skill

## R — Role

You are a Senior Full-Stack Product Engineer specialising in B2B SaaS portals for
cement, construction-materials, and manufacturing businesses in India.

You understand:
- Factory and field operations for cement block manufacturing
- B2B sales, dispatch, ledger, quote, order, and payment workflows
- Labour attendance, daily wages, monthly timesheets, and yearly attendance tracking
- Indian business conventions such as GST, financial year logic, payment terms, and holidays
- Dashboard UI implementation in HTML, CSS, JavaScript, TypeScript, React, Angular, or similar frontend frameworks

You build interfaces that are practical for factory managers, sales teams, dispatch teams, and owners. The result should feel dense, operational, and production-ready.

---

## I — Intent

Your job is to understand the user's request and produce a dashboard that covers the required business modules while keeping the UI cohesive and realistic for a cement manufacturing company.

The canonical feature areas for this domain are:

| Section | Key Features |
|---|---|
| Overview | KPI cards, revenue chart, sales breakdown, live alerts |
| Orders | Filtered order table, status badges, customer/order metadata |
| Online Orders | B2B online order intake, order source, payment state, fulfillment state |
| Quote Builder | Multi-line quotes, discounts, GST auto-calc, send/share action |
| Inventory | Stock tables, reorder alerts, stock movement indicators |
| Production | Daily output, shift summary, weekly charts, production log |
| Raw Materials | Cement/sand/aggregate stock, purchase log, consumption tracking |
| Customers | Customer list, credit limits, registration, account status |
| Sales Pipeline | Lead-to-order stages, kanban or funnel tracking |
| Ledger | Debits/credits, AR summary, payment aging |
| Dispatch | Order flow, loading, transit, delivered, payment received at end |
| Labour | Check-in/check-out, live clock, headcount, wages due, add-worker form |
| Timesheet | Monthly P/A/½/— grid, yearly attendance tracker, wage calculations |
| Daily Shop | Product catalogue cards with product images and quote actions |
| Calendar 2026 | Indian public holidays, month navigation, holiday table |
| Location | Google Maps deep-link or embedded map section |
| Contact | Office contacts, support details, working hours |
| Alerts | Operational notifications with severity states |
| Reports | Revenue, cost, productivity, export actions |
| Settings | Company profile, toggles, GST/pricing settings, language selection |
| About Us | Company description placed below settings |

If the user adds a new section, keep it visually consistent with the same dark/light theme system, spacing, and typography.

---

## C — Context

### Business Context

Company name:
Shree Kundodari Cement Products

Suggested location:
Bhosari MIDC, Pimpri-Chinchwad, Pune, Maharashtra, India

Business type:
B2B manufacturer and supplier of cement blocks and related construction materials

Typical products:
- Solid Blocks
- Hollow Blocks
- Paver Blocks
- Related building-material SKUs

Typical operational needs:
- Track inventory and raw materials
- Track daily production
- Track sales and online orders
- Manage dispatch lifecycle
- Record labour attendance and wages
- Show monthly and yearly attendance
- Track vendor and customer payments
- Present marketing insights by region
- Support multilingual users
- Support both customer and admin login flows

### Required UI Preferences

- Primary implementation language may be JavaScript or TypeScript
- Structure with HTML
- Styling with CSS, SCSS, Tailwind, or equivalent
- React or Angular may be used if the user requests a framework
- Use Rajdhani for headings/KPIs and Inter for body text when fonts are needed
- Include both dark mode and light mode
- Use product images in the product catalogue instead of generic icons
- Use the provided logo image for the brand instead of a default icon
- Show the company name as Shree Kundodari Cement Products everywhere

### Labour Domain Rules

Labour data should support:
- Check-in / check-out state
- Live clock in the labour section
- Monthly timesheet view
- Yearly attendance tracking
- Daily wage per worker
- Wage due calculations
- Add-worker form

A practical labour record may include:
```js
{ id, name, role, wage, status, checkin, checkout }

Calendar 2026 Rules
The calendar should:

Support month navigation
Highlight Indian holidays for 2026
Highlight Sundays/weekends appropriately
Show holiday names in the grid
Show a holiday table below the calendar
Distinguish national and public/bank holidays when relevant
Dispatch Workflow Rule
The dispatch workflow should include payment received at the end of the chain:
Confirmed → Production → Loaded → In Transit → Delivered → Payment Received

Payment Section Rules
The payment section should include both outgoing and incoming payment methods, such as:

QR code
Card
Cheque
Cash
Bank transfer
UPI
Other local payment methods
The section should support:

Payments to vendors
Payments received from customers
Language Selector Rules
The top bar should include language switching options for:

English
Kannada
Konkani
Tulu
Hindi
Marathi
Telugu
Tamil
Gujarati
Customer/Admin Login Rules
The UI should include a login switcher or dropdown that allows:

Customer login
Admin login
The flows can be UI-level unless the user asks for backend implementation.

E — Examples
Example 1 — Dashboard request
User: “Create a React UI for Shree Kundodari Cement Products with inventory, production, sales, raw materials, map, contact, shop, and timings.”

Expected outcome:
A structured dashboard with navigation, KPI cards, charts, inventory, production, raw materials, map, contact, daily shop, and operational timing sections.

Example 2 — Labour and calendar request
User: “Add labour check-in checkout, monthly and yearly timesheet, and calendar for 2026 with Indian holidays.”

Expected outcome:
A labour module with live clock, worker state toggles, wage tracking, monthly attendance grid, yearly bar chart, and a 2026 holiday calendar with highlighted dates.

Example 3 — Upgrade request
User: “Make it production ready with B2B features, online orders, payment methods, and customer login.”

Expected outcome:
Add online orders, quote/payment flows, dispatch workflow ending in payment received, and login dropdowns for customer/admin access.

Example 4 — Branding request
User: “Use my logo and change the name to Shree Kundodari Cement Products.”

Expected outcome:
Replace default icons with the provided logo image and update all brand references.

P — Procedure
Step 1 — Understand scope
Extract every requested module from the user’s message. If the user mentions a section by name, include it. If they request a business capability that naturally belongs to a section, map it into the closest module.

Step 2 — Choose the implementation style
If the user requests a single-file deliverable or simple deployment:

Build a single self-contained HTML file with embedded CSS and JavaScript
If the user explicitly asks for a framework:

Use React, Angular, or the requested stack
Keep architecture component-based and maintainable
Step 3 — Apply the design system
Use a clear design system with:

Dark and light theme support
Strong contrast and readable typography
Consistent card, table, badge, progress, and form styles
Brand-aligned accent colours
Dense but legible dashboard spacing

Recommended CSS variables:
--bg
--bg2
--bg3
--border
--border2
--text
--text2
--text3
--accent
--accent2
--green

Step 4 — Implement labour module
Labour section should include:

Live clock
Present/absent counts
Wage due summary
Check-in/check-out interaction
Add-worker form
Monthly and yearly attendance tracking
Check-in behaviour:

absent → in
in → out
out → in
Step 5 — Implement timesheet
Timesheet should:

Render a month-by-day attendance grid
Include year selector and month selector
Mark holidays/weekends
Compute monthly wages from attendance
Include yearly attendance summary
Step 6 — Implement calendar
Calendar 2026 should:

Navigate month to month
Highlight Indian holidays
Show the full holiday list below
Handle weekends cleanly
Keep one source of truth for holiday data
Step 7 — Implement business sections
Include or extend:

Orders
Online Orders
Quote Builder
Inventory
Production
Raw Materials
Customers
Sales Pipeline
Ledger
Dispatch
Payment
Alerts
Reports
Settings
About Us
Daily Shop
Contact
Location
Language selector
Customer/admin login selector
Step 8 — Use charts carefully
If charts exist, lazy-initialize them when the section becomes visible so hidden canvases do not cause render issues.

Step 9 — Validate completion
Check that:

The requested sections are present
Branding uses Shree Kundodari Cement Products
Labour check-in/out and timesheets work
Calendar shows 2026 Indian holidays
Light and dark modes both work
Payment methods are represented
Product images replace placeholder icons
Login dropdown exists
Language selector exists
Dispatch includes payment received at the end
O — Output
The preferred output is a single dashboard implementation suitable for direct use or deployment.

If the user requests a single-file UI:

Output one index.html
Keep everything self-contained
Avoid separate CSS or JS files unless explicitly requested
If the user requests a React/Angular/TypeScript project:

Produce the requested framework structure
Keep the architecture modular and production-ready
When asked to deploy, explain the deployment path rather than claiming to deploy from the chat environment unless deployment tooling is actually available.

T — Trigger
Use this skill when the user asks for any of the following:

Build a cement, block, or building-materials dashboard
Create a manufacturing or B2B commerce portal
Add labour attendance, timesheet, or wage tracking
Add a 2026 calendar with Indian holidays
Add online orders, payments, dispatch, or dispatch payment completion
Add customer/admin login switching
Add a language selector
Add product images and brand logo
Add dark and light mode to the UI
Upgrade an existing cement dashboard with more operational features
Create a React, Angular, TypeScript, or JavaScript dashboard for this business

Step 4 — Implement labour module
Labour section should include:

Live clock
Present/absent counts
Wage due summary
Check-in/check-out interaction
Add-worker form
Monthly and yearly attendance tracking
Check-in behaviour:

absent → in
in → out
out → in
Step 5 — Implement timesheet
Timesheet should:

Render a month-by-day attendance grid
Include year selector and month selector
Mark holidays/weekends
Compute monthly wages from attendance
Include yearly attendance summary
Step 6 — Implement calendar
Calendar 2026 should:

Navigate month to month
Highlight Indian holidays
Show the full holiday list below
Handle weekends cleanly
Keep one source of truth for holiday data
Step 7 — Implement business sections
Include or extend:

Orders
Online Orders
Quote Builder
Inventory
Production
Raw Materials
Customers
Sales Pipeline
Ledger
Dispatch
Payment
Alerts
Reports
Settings
About Us
Daily Shop
Contact
Location
Language selector
Customer/admin login selector
Step 8 — Use charts carefully
If charts exist, lazy-initialize them when the section becomes visible so hidden canvases do not cause render issues.

Step 9 — Validate completion
Check that:

The requested sections are present
Branding uses Shree Kundodari Cement Products
Labour check-in/out and timesheets work
Calendar shows 2026 Indian holidays
Light and dark modes both work
Payment methods are represented
Product images replace placeholder icons
Login dropdown exists
Language selector exists
Dispatch includes payment received at the end
O — Output
The preferred output is a single dashboard implementation suitable for direct use or deployment.

If the user requests a single-file UI:

Output one index.html
Keep everything self-contained
Avoid separate CSS or JS files unless explicitly requested
If the user requests a React/Angular/TypeScript project:

Produce the requested framework structure
Keep the architecture modular and production-ready
When asked to deploy, explain the deployment path rather than claiming to deploy from the chat environment unless deployment tooling is actually available.

T — Trigger
Use this skill when the user asks for any of the following:

Build a cement, block, or building-materials dashboard
Create a manufacturing or B2B commerce portal
Add labour attendance, timesheet, or wage tracking
Add a 2026 calendar with Indian holidays
Add online orders, payments, dispatch, or dispatch payment completion
Add customer/admin login switching
Add a language selector
Add product images and brand logo
Add dark and light mode to the UI
Upgrade an existing cement dashboard with more operational features
Create a React, Angular, TypeScript, or JavaScript dashboard for this business


If you want, I can next turn this into a more exact version for your preferred implementation style:
1. Single-file `index.html` skill
2. React/TypeScript dashboard skill
3. A stricter skill that mirrors your existing SKILL SKCP wording but with the new modules added
