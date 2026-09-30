# Permanent Deployment & Long-Term SEO Guide
## Ikshvaku Vidya Academy — Digital Identity Platform

This guide walks you through deploying this website for **₹0 long-term cost**, configuring your domain, and setting up **Google Search Console** for long-term search engine discovery.

---

### Central Configuration Value: `SITE_URL`

To keep migration simple and avoid broken links, this website uses one standard placeholder:

```
https://YOUR-SITE-URL/
```

This placeholder appears in only 3 files:
1. `index.html` (canonical link, Open Graph metadata, Twitter card, and JSON-LD schema)
2. `sitemap.xml` (the public XML sitemap)
3. `robots.txt` (the search crawler map location)

All other assets (styles, logo, scripts) use **relative paths** (`assets/IVA.jpeg`, `css/...`, `js/...`), which means the website will load and look right on any URL without extra configuration.

---

## Step-by-Step Deployment Roadmap

### Phase 1: Deploy to Free Hosting (Cloudflare Pages Recommended)

Cloudflare Pages provides free hosting with unmetered bandwidth, global edge caching, and free SSL certificates.

1. **Upload your code to GitHub**:
   - Create a free GitHub account if you do not have one.
   - Create a new repository named `ikshvaku-academy` (can be public or private).
   - Push or upload all files in this project folder into that repository.

2. **Connect to Cloudflare Pages**:
   - Go to [dash.cloudflare.com](https://dash.cloudflare.com/) and create a free account.
   - In the left sidebar, click **Workers & Pages**.
   - Click **Create application** → select the **Pages** tab → click **Connect to Git**.
   - Select your `ikshvaku-academy` repository.

3. **Configure the deployment settings**:
   - **Project name**: `ikshvaku-academy` (or your choice)
   - **Production branch**: `main`
   - **Framework preset**: `None`
   - **Build command**: *(leave completely blank)*
   - **Build output directory**: `/` (root directory)

4. **Click "Save and Deploy"**:
   - Within 30 seconds, Cloudflare will deploy your site and provide a free live URL (e.g., `https://ikshvaku-academy.pages.dev`).

*(Alternative: You can also use **GitHub Pages** under repository **Settings** → **Pages** → **Deploy from branch `main` / `/root`.)*

---

### Phase 2: Test the Public URL

Once deployed, visit your live URL:
- Check that the official seal (`IVA.jpeg`) appears clearly in the hero, header, and footer.
- Verify that navigation links jump smoothly to sections: `#about`, `#philosophy`, `#student`, `#affordability`, `#classroom`, `#manifesto`, `#founders`, `#vision`, and `#contact`.
- Open the site on your smartphone to confirm mobile menu navigation and readability.
- Send the URL via WhatsApp or LinkedIn to verify that the Open Graph title, description, and logo preview display cleanly.

---

### Phase 3: Connect a Custom Domain (When You Choose to Get One)

You do **not** need to buy a domain immediately. Your free Cloudflare Pages or GitHub Pages address works indefinitely.

When you do acquire a custom domain (e.g., `ikshvakuvidyaacademy.org` from any registrar like Cloudflare Registrar, Namecheap, or GoDaddy):

1. Go to your **Cloudflare Pages project dashboard**.
2. Click **Custom domains** → **Set up a custom domain**.
3. Type your domain (e.g., `ikshvakuvidyaacademy.org` or `identity.ikshvakuvidyaacademy.org`).
4. Cloudflare will give you simple DNS instructions:
   - For a root domain: add a CNAME or ALIAS record pointing to your `*.pages.dev` address.
   - Cloudflare handles free SSL certificates automatically.
5. No code rebuilding is required.

---

### Phase 4: Update `SITE_URL`

Once your permanent domain (or chosen free subdomain) is active:

1. Open `index.html` and search for:
   ```
   https://YOUR-SITE-URL/
   ```
   Replace every occurrence with your live domain (e.g., `https://ikshvaku-academy.pages.dev/` or `https://ikshvakuvidyaacademy.org/`).
2. Open `sitemap.xml` and update the URL.
3. Open `robots.txt` and update the `Sitemap:` URL.
4. Commit and push the changes to GitHub. Cloudflare updates automatically in 15 seconds.

---

### Phase 5: Google Search Console Setup

Google Search Console ensures Google discovers, understands, and indexes the academy's official identity.

1. Visit [search.google.com/search-console](https://search.google.com/search-console) and sign in with `ikshvakuvidyaacademy@gmail.com`.
2. Click **Add property**.
3. Choose **URL prefix** and enter your live URL (e.g., `https://ikshvaku-academy.pages.dev/`).
4. **Verification**:
   - Google offers several verification methods. The simplest is **HTML tag**.
   - Copy the meta tag provided by Google (e.g., `<meta name="google-site-verification" content="..."/>`).
   - Paste it inside the `<head>` section of `index.html`.
   - Push to GitHub and click **Verify** in Search Console.

---

### Phase 6: Submit `sitemap.xml`

1. In Google Search Console, navigate to the **Sitemaps** section in the left sidebar.
2. In the "Add a new sitemap" box, type:
   ```
   sitemap.xml
   ```
3. Click **Submit**.
4. Google will report a "Success" status after fetching your sitemap.

---

### Phase 7: Verify Indexing

- **Inspection**: You can use the "URL Inspection" tool at the top of Search Console to check how Google crawls your homepage.
- **Timeline**: Legitimate search indexing takes time (often a few days to a few weeks for new sites). Google will gradually associate "Ikshvaku Vidya Academy" and "Education Beyond Commerce" with your permanent web property.

---

### Phase 8: Long-Term Maintenance

This platform is intentionally designed with **no short-term content, no changing prices, and no expiration dates**.

You only need to visit the code if:
- You acquire a new permanent domain (see Phase 4).
- Official leadership details or contact email changes.
- You wish to add links to future initiatives when they are ready.

Otherwise, the website will continue running on the edge network with **zero maintenance and ₹0 hosting cost**.
