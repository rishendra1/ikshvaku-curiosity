import re
import xml.etree.ElementTree as ET

def build_standalone_curiosity_platform():
    # 1. Read base curiosity-machine.html
    with open('curiosity-machine.html', 'r', encoding='utf-8') as f:
        c_text = f.read()

    # 2. Extract base64 logo from blogger-template.xml
    with open('blogger-template.xml', 'r', encoding='utf-8') as f:
        b_text = f.read()
    logo_match = re.search(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', b_text)
    base64_logo = logo_match.group(0) if logo_match else 'https://rishendra1.github.io/ikshvaku-curiosity/assets/IVA.jpeg'

    # 3. Extract CSS, JS, HTML
    style_match = re.search(r'<style>(?:/\*<!\[CDATA\[\*/)?(.*?)(?:/\*\]\]>\*/)?</style>', c_text, re.DOTALL)
    script_match = re.search(r'<script>(?://<!\[CDATA\[)?(.*?)(?://\]\]>)?</script>', c_text, re.DOTALL)

    c_css = style_match.group(1).strip() if style_match else ''
    c_js = script_match.group(1).strip() if script_match else ''

    c_html = c_text
    if style_match:
        c_html = c_html.replace(style_match.group(0), '')
    if script_match:
        c_html = c_html.replace(script_match.group(0), '')
    c_html = c_html.strip()

    # 4. Replace logo src with base64 logo so it never breaks, maintaining XML self-closing
    c_html = c_html.replace('src="assets/IVA.jpeg"', f'src="{base64_logo}"')

    # 5. Update logo text & mentions:
    # "an idea / initiative from Ikshvaku Vidya Academy"
    old_logo_markup = """<div class="iva-logo-title">IKSHVAKU CURIOSITY MACHINE</div>
          <div class="iva-logo-sub">Education Beyond Commerce</div>"""
    new_logo_markup = """<div class="iva-logo-title">IKSHVAKU CURIOSITY MACHINE</div>
          <div class="iva-logo-sub">An Initiative by Ikshvaku Vidya Academy • Education Beyond Commerce</div>"""
    c_html = c_html.replace(old_logo_markup, new_logo_markup)

    # 6. Add the Top Institutional Bar above the machine
    top_institutional_header = f"""
  <!-- Official Ikshvaku Vidya Academy Header -->
  <header class="iva-top-banner" role="banner">
    <div class="iva-top-container">
      <div class="iva-top-left">
        <img src="{base64_logo}" alt="Ikshvaku Vidya Academy Official Seal" class="iva-top-logo" />
        <div class="iva-top-titles">
          <div class="iva-top-name">IKSHVAKU VIDYA ACADEMY</div>
          <div class="iva-top-initiative">First-Principles Educational Initiative • Education Beyond Commerce</div>
        </div>
      </div>
      <div class="iva-top-right">
        <span class="iva-top-badge">✦ Official Curiosity Platform</span>
      </div>
    </div>
  </header>
"""
    # Insert top_institutional_header right after <div id="iva-curiosity-machine">
    c_html = c_html.replace('<div id="iva-curiosity-machine">', '<div id="iva-curiosity-machine">\n' + top_institutional_header)

    # 7. Add dedicated responsive CSS for top banner & phone/computer perfection
    banner_css = """
/* ── TOP INSTITUTIONAL BANNER ── */
#iva-curiosity-machine .iva-top-banner {
  background: linear-gradient(180deg, #071b36 0%, #060913 100%);
  border-bottom: 1px solid rgba(179, 134, 66, 0.35);
  padding: 14px 20px;
  position: relative;
  z-index: 10;
}
#iva-curiosity-machine .iva-top-container {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
#iva-curiosity-machine .iva-top-left {
  display: flex;
  align-items: center;
  gap: 14px;
}
#iva-curiosity-machine .iva-top-logo {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 1.5px solid #b38642;
  box-shadow: 0 0 12px rgba(179, 134, 66, 0.4);
  object-fit: cover;
  flex-shrink: 0;
}
#iva-curiosity-machine .iva-top-titles {
  display: flex;
  flex-direction: column;
}
#iva-curiosity-machine .iva-top-name {
  font-family: 'Newsreader', Georgia, serif;
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: #faf8f5;
}
#iva-curiosity-machine .iva-top-initiative {
  font-size: 0.78rem;
  color: #b38642;
  font-weight: 500;
  letter-spacing: 0.02em;
}
#iva-curiosity-machine .iva-top-badge {
  background: rgba(179, 134, 66, 0.15);
  border: 1px solid rgba(179, 134, 66, 0.4);
  color: #e5c07b;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 999px;
  letter-spacing: 0.03em;
  white-space: nowrap;
}

/* ── PHONE & COMPUTER RESPONSIVENESS ── */
@media (max-width: 768px) {
  #iva-curiosity-machine .iva-top-banner {
    padding: 10px 14px;
  }
  #iva-curiosity-machine .iva-top-name {
    font-size: 1.05rem;
  }
  #iva-curiosity-machine .iva-top-initiative {
    font-size: 0.7rem;
  }
  #iva-curiosity-machine .iva-top-badge {
    display: none;
  }
  #iva-curiosity-machine .iva-header-inner {
    flex-direction: column;
    align-items: stretch;
    gap: 12px;
  }
  #iva-curiosity-machine .iva-header-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    justify-content: flex-start;
  }
  #iva-curiosity-machine .iva-categories-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 8px !important;
  }
  #iva-curiosity-machine .iva-category-chip {
    padding: 12px 10px !important;
    font-size: 0.8rem !important;
    flex-direction: column;
    text-align: center;
    gap: 6px;
  }
  #iva-curiosity-machine .iva-hero-title {
    font-size: clamp(1.75rem, 6vw, 2.4rem) !important;
  }
  #iva-curiosity-machine .iva-curiosity-card {
    padding: 1.25rem 1rem !important;
  }
  #iva-curiosity-machine .iva-hero-actions,
  #iva-curiosity-machine .iva-card-actions {
    flex-direction: column;
    width: 100%;
  }
  #iva-curiosity-machine .iva-btn {
    width: 100%;
    justify-content: center;
  }
  #iva-curiosity-machine .iva-modal-content {
    width: 95vw !important;
    max-height: 90vh !important;
    padding: 1rem !important;
  }
}

@media (max-width: 420px) {
  #iva-curiosity-machine .iva-categories-grid {
    grid-template-columns: 1fr !important;
  }
}
"""
    full_css = banner_css + '\n' + c_css

    # 8. Build Standalone Blogger XML Theme (For Theme -> Edit HTML)
    # 100% ONLY Curiosity Machine + Header. NO About page, NO Manifesto, NO Journal!
    blogger_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='1' b:layoutsversion='3' b:responsive='true' expr:dir='data:blog.languageDirection' expr:lang='data:blog.locale' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
  <meta charset='UTF-8'/>
  <meta content='width=device-width, initial-scale=1.0, maximum-scale=5.0' name='viewport'/>
  <title>Curiosity Machine — An Initiative by Ikshvaku Vidya Academy</title>
  
  <b:include data='blog' name='all-head-content'/>

  <!-- Primary Meta Tags -->
  <meta content='Ikshvaku Curiosity Machine — An Initiative by Ikshvaku Vidya Academy' name='title'/>
  <meta content='Explore 500,000 algorithmic first-principles questions across 8 disciplines with live physics simulators and celestial harmonic audio. An initiative by Ikshvaku Vidya Academy — Education Beyond Commerce.' name='description'/>
  <meta content='#071b36' name='theme-color'/>

  <!-- Typography: Newsreader & JetBrains Mono & Plus Jakarta Sans -->
  <link href='https://fonts.googleapis.com' rel='preconnect'/>
  <link crossorigin='anonymous' href='https://fonts.gstatic.com' rel='preconnect'/>
  <link href='https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap' rel='stylesheet'/>

  <b:skin><![CDATA[
/* Reset & Base Canvas */
html, body {{
  margin: 0;
  padding: 0;
  background: #060913;
  color: #f8fafc;
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}}

{full_css}
  ]]></b:skin>
</head>
<body>

  {c_html}

  <!-- Minimal Required Blogger Section for 100% Strict Schema Validation -->
  <div style='display: none;'>
    <b:section class='main-section' id='main' showaddelement='no'>
      <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog' version='1'>
        <b:includable id='main'>
          <b:loop values='data:posts' var='post'>
            <article>
              <h2><data:post.title/></h2>
              <div><data:post.body/></div>
            </article>
          </b:loop>
        </b:includable>
      </b:widget>
    </b:section>
  </div>

  <script type='text/javascript'>
  //<![CDATA[
{c_js}
  //]]>
  </script>
</body>
</html>"""

    # 9. Verify XML Validity
    try:
        ET.fromstring(blogger_xml)
        print('SUCCESS: blogger_xml is 100% valid XML!')
        with open('curiosity-theme.xml', 'w', encoding='utf-8') as f:
            f.write(blogger_xml)
        with open('blogger-template.xml', 'w', encoding='utf-8') as f:
            f.write(blogger_xml)
        print(f'Wrote curiosity-theme.xml and blogger-template.xml ({len(blogger_xml)} bytes)')
    except ET.ParseError as e:
        print('ERROR in XML validation:', e)
        l, c = e.position
        b_lines = blogger_xml.splitlines()
        for i in range(max(0, l-5), min(len(b_lines), l+5)):
            print(f'{i+1}: {b_lines[i]}')

    # 10. Build Standalone HTML Component for Blogger -> Pages -> New Page
    standalone_html = f"""<!-- 
  IKSHVAKU CURIOSITY MACHINE
  An Initiative by Ikshvaku Vidya Academy — Education Beyond Commerce
  For Blogger Pages: Paste in Pages -> New Page -> HTML view (<>)
-->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet" />

<style>
{full_css}
</style>

{c_html}

<script>
{c_js}
</script>
"""
    with open('curiosity-page.html', 'w', encoding='utf-8') as f:
        f.write(standalone_html)
    print('Wrote curiosity-page.html for Pages -> New Page')

if __name__ == '__main__':
    build_standalone_curiosity_platform()
