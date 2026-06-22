shree-kundodari-cement-products/
│
├── backend/                # Node.js + Express API
│   ├── src/
│   │   ├── config/         # DB connection, environment configs
│   │   ├── controllers/    # Business logic (e.g., customerController.js)
│   │   ├── models/         # Database schemas (e.g., Customer.js, User.js)
│   │   ├── routes/         # API routes (e.g., customerRoutes.js)
│   │   ├── middleware/     # Auth, validation, error handling
│   │   └── server.js       # Express app entry point
│   ├── package.json
│   └── .env                # Secrets (DB URL, JWT secret)
│
├── frontend/               # React + TypeScript UI
│   ├── public/             # Static assets (logo, favicon)
│   ├── src/
│   │   ├── components/     # Reusable UI blocks (Sidebar, Header, Forms)
│   │   ├── pages/          # Dashboard pages (Inventory, Customers, Payments)
│   │   ├── services/       # API calls (axios/fetch)
│   │   ├── context/        # Auth context, theme context
│   │   └── App.tsx
│   ├── package.json
│   └── .env                # API base URL
│
├── database/               # SQL scripts or migrations
│   └── schema.sql
│
└── README.md