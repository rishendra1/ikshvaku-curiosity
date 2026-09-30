# Ikshvaku Vidya Academy — Permanent Digital Identity Platform

> **Education Beyond Commerce**  
> *To provide quality education with more facilities and opportunities at an affordable cost.*

Official permanent institutional identity, brand story, and philosophy platform for **Ikshvaku Vidya Academy**.

This is a standalone, permanent digital property designed to strengthen the academy's legitimate online presence, brand discoverability, and SEO over the long term. It operates at **₹0 hosting cost** on modern static hosting edge networks with zero server maintenance.

---

## 1. Core Identity & Attribution

- **Organization**: Ikshvaku Vidya Academy
- **Slogan**: Education Beyond Commerce
- **Institutional Contact**: `ikshvakuvidyaacademy@gmail.com`
- **Founders**:
  - **Rishendra** — Founder
  - **Revanth Sai** — Co-Founder
- **Purpose**: A permanent, grounded, thoughtful foundation communicating who the academy is, why it exists, and the principles that guide its decisions.

---

## 2. Directory Structure

```
PROJECT/
├── index.html            # Main semantic editorial document, content, and JSON-LD
├── assets/
│   └── IVA.jpeg          # Official brand mark / logo (1254x1254 JPEG)
├── css/
│   ├── variables.css     # Brand color tokens sampled from IVA seal, typography scales
│   ├── typography.css    # Newsreader serif + Plus Jakarta Sans typography
│   ├── layout.css        # Editorial grids, containers, visual thread lines
│   ├── components.css    # Hero aperture, Triad cards, Manifesto, Founders
│   ├── animations.css    # Subtle scroll reveals and accessibility motion rules
│   └── responsive.css    # Dedicated rules for 320px, 375px, 768px, 1024px, 1440px+
├── js/
│   └── main.js           # Zero-dependency scroll observer, header states, mobile drawer
├── robots.txt            # Search engine crawler directives
├── sitemap.xml           # Clean XML sitemap for search engines
├── site.webmanifest      # Progressive web metadata and icon definitions
├── DEPLOYMENT.md         # Step-by-step free deployment & Google Search Console guide
└── README.md             # This document
```

---

## 3. Key Technical Specifications

- **Search Engine Discovery**: Full Open Graph, Twitter Cards, WebSite & EducationalOrganization JSON-LD structured data.
- **Single Centralized Configuration (`SITE_URL`)**: The placeholder `https://YOUR-SITE-URL/` is used consistently across `index.html`, `sitemap.xml`, and `robots.txt` for easy 1-step domain updates.
- **Linkable Sections**: Every key section features a permanent anchor ID (`#about`, `#philosophy`, `#quality`, `#opportunity`, `#affordability`, `#student`, `#classroom`, `#manifesto`, `#founders`, `#vision`, `#contact`).
- **Performance**: Preconnected font pipelines, zero layout shifts, zero heavy runtime dependencies, sub-300ms loading.

---

## 4. How to Run Locally

You can run this project locally with zero setup:

### Using Python
Open PowerShell or your terminal in this project folder and run:
```bash
python -m http.server 8000
```
Then visit:
```
http://localhost:8000/
```

### Direct Browser Opening
You can also directly double-click `index.html` in file explorer to view the site in any browser.

---

## 5. Deployment & Google Search Console

For complete, beginner-friendly instructions on:
- Deploying for ₹0 on Cloudflare Pages or GitHub Pages
- Connecting a custom domain later
- Setting up Google Search Console
- Submitting `sitemap.xml`

Please refer to **[`DEPLOYMENT.md`](DEPLOYMENT.md)**.
