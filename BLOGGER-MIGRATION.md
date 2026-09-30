# Ikshvaku Vidya Academy — Blogger Migration & Setup Guide

> **Education Beyond Commerce**  
> *Permanent Institutional Identity, Philosophy, and Educational Journal on Blogger*

This guide explains step-by-step how to launch **Ikshvaku Vidya Academy** on Google Blogger using the custom institutional theme (`blogger-template.xml`).

---

## 1. Project Context & Independence

- **100% Standalone**: This website is completely independent of the separate website being developed by your friend. It does not share repositories, databases, APIs, or hosting.
- **Purpose**: A permanent public presence establishing the academy's official identity, philosophy, founders, educational vision, and long-term SEO journal.
- **₹0 Hosting**: Hosted entirely on Google's globally distributed Blogger infrastructure with zero server maintenance, free SSL, and unlimited bandwidth.

---

## 2. File Overview

- **`blogger-template.xml`**: The production-ready Blogger XML theme containing the full editorial design system, typography, responsive layout, homepage narrative flow, and journal article template.
- **`assets/IVA.jpeg`**: The official, unaltered brand seal.
- **`index.html` / `css/` / `js/`**: Preserved as your local standalone reference and testing playground.

---

## 3. Step 1: Create the Blogger Blog

1. Visit [blogger.com](https://www.blogger.com/) and sign in with your Google account (`ikshvakuvidyaacademy@gmail.com`).
2. Click **Create Blog** (or New Blog in the top left menu).
3. **Title**: Enter `Ikshvaku Vidya Academy`.
4. **URL**: Choose an initial free address (e.g., `ikshvaku-vidya-academy.blogspot.com` or `ikshvakuacademy.blogspot.com`). You can connect a custom domain later.
5. Click **Save**.

---

## 4. Step 2: Upload & Host the Official Seal (`IVA.jpeg`)

To let Google serve your high-resolution logo at maximum speed:

1. In the Blogger dashboard, click **Pages** → **New page**.
2. Title this draft page `Assets (Do Not Delete)`.
3. Click the **Insert image** icon → **Upload from computer** → select `assets/IVA.jpeg`.
4. In the post editor, right-click the uploaded image and choose **Copy Image Address** (it will look like `https://blogger.googleusercontent.com/img/b/...`).
5. Save the page as a **Draft** (no need to publish it).
6. Open `blogger-template.xml` in any text editor and replace:
   ```
   https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivaLogoPlaceholder/s320/IVA.jpeg
   ```
   and
   ```
   https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivaLogoPlaceholder/s160/IVA.jpeg
   ```
   with your copied image address.

---

## 5. Step 3: Install the Custom Theme (`blogger-template.xml`)

1. In the Blogger dashboard, click **Theme** in the left sidebar.
2. Next to the orange "Customize" button, click the **drop-down arrow (⋮)**.
3. Select **Edit HTML**.
4. Press `Ctrl + A` (or `Cmd + A`) to select all the existing default template code and press `Delete`.
5. Open `blogger-template.xml`, select all contents, and paste them into the Blogger HTML editor.
6. Click the **Save icon (disk)** in the top right corner.
7. Click **Back**, then click the drop-down arrow next to "Customize" again, select **Mobile settings**, and make sure it is set to **Desktop** (this ensures Blogger serves our custom responsive theme to mobile phones instead of an old default mobile layout).

---

## 6. Step 4: Separate Institutional Pages from Blog Posts

Blogger provides two distinct content types:
1. **Pages** (for static institutional statements that do not change)
2. **Posts** (for ongoing educational articles in the Ikshvaku Journal)

### Create These 9 Static Pages:
Go to **Pages** → **New page** and create each page with its title:

| Page Title | Purpose / Content Summary |
| :--- | :--- |
| **Home** | The central landing page displaying the full institutional narrative. |
| **Our Story** | The humble beginning: two people, one conviction, and a bigger vision. |
| **What We Believe** | The 8 declarations of the Ikshvaku Manifesto. |
| **Education Beyond Commerce** | Full essay on sustainable education versus transactional extraction. |
| **Quality • Facilities • Affordability** | Detailed breakdown of the core triad commitments. |
| **The Student We See** | Profiles of the curious, persistent, and untested learners. |
| **Founders** | Attribution for **Rishendra** (Founder) and **Revanth Sai** (Co-Founder). |
| **Vision** | "Start Small. Think Far." & "One Day, We Hope...". |
| **Contact** | Institutional dialogue and email: `ikshvakuvidyaacademy@gmail.com`. |

*(Note: On the homepage, these sections are already seamlessly sequenced for visitors. Creating individual pages gives you permanent, shareable standalone URLs for each topic).*

---

## 7. Step 5: Recommended Navigation Structure

The theme header and mobile drawer include these primary links:

```
[Logo: Ikshvaku Vidya Academy]
  ├── About (#about)
  ├── Philosophy (#philosophy)
  ├── The Student (#student)
  ├── Affordability (#affordability)
  ├── Manifesto (#manifesto)
  ├── Founders (#founders)
  ├── Journal (#journal)
  └── Contact (mailto:ikshvakuvidyaacademy@gmail.com)
```

---

## 8. Step 6: Publishing to the Ikshvaku Journal

To publish an article:
1. In Blogger, click **Posts** → **New Post**.
2. Enter the article title and write your content using the rich text or HTML editor.
3. In the right sidebar, assign one or more **Labels** (e.g., `Mathematics`, `Thinking & Curiosity`, `Learning`).
4. Click **Publish**. The article automatically appears in the **Ikshvaku Journal** grid on your homepage and in the permanent article archive.

### Recommended First 10 Journal Article Topics

These topics build authentic search authority and educational credibility without keyword stuffing:

1. **Why Learning Needs Curiosity More Than Memorization**
   - *Premise*: Exploring why understanding first principles builds lasting confidence compared to formula cramming.
   - *Label*: `Educational Philosophy`
2. **The Importance of Mathematical Confidence**
   - *Premise*: Practical approaches for students who feel anxious about numbers and problem-solving.
   - *Label*: `Mathematics`
3. **Can High-Quality Education Actually Be Affordable?**
   - *Premise*: An honest examination of how modern technology and focused curriculum reduce waste without compromising quality.
   - *Label*: `Education Beyond Commerce`
4. **Learning How to Think: An Introduction to Analytical Reasoning**
   - *Premise*: Breaking down complex problems into manageable logical components.
   - *Label*: `Thinking & Curiosity`
5. **Beyond the Marksheet: Why Unmeasured Potential Matters**
   - *Premise*: A message of encouragement for students whose strengths aren't reflected in standardized tests.
   - *Label*: `Student Life`
6. **Understanding Systems: How Computer Science Trains the Mind**
   - *Premise*: Viewing programming not just as a job skill, but as a discipline of structured thought.
   - *Label*: `Technology`
7. **The Power of Starting Small: Habits for Independent Learning**
   - *Premise*: Actionable guidance on self-study and building daily intellectual momentum.
   - *Label*: `Learning`
8. **Pattern Recognition in Everyday Problems**
   - *Premise*: Exploring number sequences, puzzles, and real-world patterns.
   - *Label*: `Mathematics`, `Thinking & Curiosity`
9. **Why Mentorship Matters When Resources Are Limited**
   - *Premise*: The role of guidance in helping students overcome early hurdles.
   - *Label*: `Opportunities`
10. **Education as Possibility: The Long-Term Horizon**
    - *Premise*: Reflections on what an open, student-centered learning environment can achieve.
    - *Label*: `Educational Philosophy`

---

## 9. Step 7: SEO Settings in Blogger

Configure these settings inside the **Blogger Dashboard** → **Settings**:

### Basic
- **Title**: `Ikshvaku Vidya Academy`
- **Description**: `Ikshvaku Vidya Academy is an independent education initiative dedicated to providing quality education with more facilities and opportunities at an affordable cost. Education Beyond Commerce.`
- **Blog language**: English (United Kingdom / United States)

### Privacy
- **Visible to search engines**: **Yes** (Enable)

### HTTPS
- **HTTPS availability**: **Yes** (Enable)
- **HTTPS redirect**: **Yes** (Enable)

### Crawlers and Indexing (Critical for SEO)
- **Enable search description**: **Yes**
- **Custom robots.txt**: Enable and paste:
  ```txt
  User-agent: *
  Disallow: /search
  Allow: /

  Sitemap: https://YOUR-BLOG-NAME.blogspot.com/sitemap.xml
  ```
  *(Replace `YOUR-BLOG-NAME.blogspot.com` with your live address).*
- **Custom robots header tags**: Enable
  - Home page tags: `all`, `noodp`
  - Archive and search page tags: `noindex`, `nofollow`
  - Post and page tags: `all`, `noodp`

---

## 10. Step 8: Connect Google Search Console

1. In Blogger **Settings** → **Crawlers and indexing**, click **Google Search Console**.
2. Sign in with the same Google account.
3. Click **Add Property** → enter your blog address (e.g. `https://ikshvakuacademy.blogspot.com/`).
4. Because Blogger and Search Console are both Google products, **ownership is verified instantly**.
5. In Search Console, click **Sitemaps** in the left menu.
6. Enter `sitemap.xml` and click **Submit**. Google will crawl your blog automatically.

---

## 11. Step 9: Connecting a Custom Domain (Later)

When you decide to purchase a domain (e.g., `ikshvakuvidyaacademy.org`):

1. Go to Blogger **Settings** → **Publishing** → **Custom domain**.
2. Enter your domain (e.g. `www.ikshvakuvidyaacademy.org`).
3. Blogger will display two CNAME DNS records:
   - Record 1: Name `www`, Destination `ghs.google.com`
   - Record 2: Name `<unique-security-token>`, Destination `<unique-google-verify-code>`
4. Add these two CNAME records at your domain registrar (GoDaddy, Namecheap, Cloudflare, etc.).
5. Also add Google's 4 standard A-records for naked domain redirect:
   - `216.239.32.21`
   - `216.239.34.21`
   - `216.239.36.21`
   - `216.239.38.21`
6. In Blogger Settings, toggle **Redirect domain** (`ikshvakuvidyaacademy.org` to `www.ikshvakuvidyaacademy.org`) and enable **HTTPS Redirect**.
7. Your custom domain is live with free Google SSL in under an hour.

---

## 12. Comparison: What Was Preserved vs. Adapted

| Feature | Original Static Website | Blogger Version |
| :--- | :--- | :--- |
| **Visual Identity & Palette** | Oxford Navy, Warm Ivory, Muted Gold | **100% Identical** |
| **Typography** | Newsreader serif + Plus Jakarta Sans | **100% Identical** |
| **Institutional Narrative** | Hero, Triad, Student, Manifesto, Founders | **100% Preserved on Homepage** |
| **Mobile Navigation Drawer** | Vanilla JS accessible drawer | **100% Preserved** |
| **Educational Articles** | Static placeholders | **Upgraded to live Blogger CMS** |
| **Article Management** | Editing HTML code | **Simple visual editor in Blogger** |
| **Comments / Community** | None | **Optional Blogger comments** |
| **RSS / Atom Feeds** | None | **Automatic RSS feed built-in** |
