import re
import xml.etree.ElementTree as ET

def integrate():
    # 1. Read base blogger template (reset from git HEAD~1 if needed or clean up)
    with open('blogger-template.xml', 'r', encoding='utf-8') as f:
        b_text = f.read()

    with open('curiosity-machine.html', 'r', encoding='utf-8') as f:
        c_text = f.read()

    # Extract CSS
    style_match = re.search(r'<style>(?:/\*<!\[CDATA\[\*/)?(.*?)(?:/\*\]\]>\*/)?</style>', c_text, re.DOTALL)
    c_css = style_match.group(1).strip() if style_match else ''

    # Extract JS
    script_match = re.search(r'<script>(?://<!\[CDATA\[)?(.*?)(?://\]\]>)?</script>', c_text, re.DOTALL)
    c_js = script_match.group(1).strip() if script_match else ''

    # Extract HTML
    c_html = c_text
    if style_match:
        c_html = c_html.replace(style_match.group(0), '')
    if script_match:
        c_html = c_html.replace(script_match.group(0), '')
    c_html = c_html.strip()

    # Clean existing curiosity machine injections if any
    b_text = re.sub(r'/\* ==========================================================================\s+IKSHVAKU CURIOSITY MACHINE STYLES.*?(?=\]\]></b:skin>)', '', b_text, flags=re.DOTALL)
    b_text = re.sub(r'<!-- =====================================================================\s+6\.5 THE CURIOSITY MACHINE.*?<!-- 7\. QUIET PAUSE', '<!-- 7. QUIET PAUSE', b_text, flags=re.DOTALL)
    b_text = re.sub(r'<script type=\x27text/javascript\x27>\s*//<!\[CDATA\[\s*\(function\(\)\s*\{[\s\S]*?ivaSimSliderVal[\s\S]*?//\]\]>\s*</script>\s*', '', b_text)

    # Clean redundant curiosity machine links from drawer/nav
    b_text = re.sub(r'<a class=\x27nav-link\x27 [^>]*Curiosity Machine ✦</a>\s*', '', b_text)

    # 1. Fix root tag attributes for maximum Blogger compatibility
    b_text = b_text.replace("b:layoutsVersion='3'", "b:layoutsversion='3'")
    b_text = b_text.replace("b:defaultwidgetversion='2'", "b:defaultwidgetversion='1'")

    # 2. Fix all expr:href with '+' to standard, bulletproof anchor links
    b_text = b_text.replace('expr:href=\'data:blog.homepageUrl + "#about"\'', 'href="#about"')
    b_text = b_text.replace('expr:href=\'data:blog.homepageUrl + "#contact"\'', 'href="#contact"')
    b_text = b_text.replace('expr:href=\'data:blog.homepageUrl + "#curiosity-machine"\'', 'href="#curiosity-machine"')

    # 3. Fix fonts link in head to include JetBrains Mono
    if 'JetBrains+Mono' not in b_text:
        b_text = b_text.replace(
            'family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap',
            'family=JetBrains+Mono:wght@400;500;600&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap'
        )

    # 4. Insert Curiosity Machine CSS before closing </b:skin>
    skin_end = b_text.find(']]></b:skin>')
    if skin_end != -1:
        curiosity_css_block = '\n\n/* ==========================================================================\n   IKSHVAKU CURIOSITY MACHINE STYLES\n   ========================================================================== */\n' + c_css + '\n'
        b_text = b_text[:skin_end] + curiosity_css_block + b_text[skin_end:]

    # 5. Add Nav links in Desktop Nav and Mobile Drawer cleanly
    nav_desktop_target = '<a class=\'btn btn-primary\' href="#contact"'
    curiosity_nav_link = '<a class=\'nav-link\' href="#curiosity-machine" style=\'color: var(--color-accent-gold); font-weight: 600;\'>Curiosity Machine ✦</a>\n          '
    b_text = b_text.replace(nav_desktop_target, curiosity_nav_link + nav_desktop_target)

    drawer_target = "id='mobileDrawer'>\n      <a class='nav-link' href=\"#about\">About Academy</a>"
    drawer_replacement = "id='mobileDrawer'>\n      <a class='nav-link' href=\"#about\">About Academy</a>\n      <a class='nav-link' href=\"#curiosity-machine\" style=\"color: var(--color-accent-gold); font-weight: 600;\">Curiosity Machine ✦</a>"
    b_text = b_text.replace(drawer_target, drawer_replacement)

    # 6. Change <b:if cond='data:view.isHomepage'> to <b:if cond='!data:view.isPost'> so it displays in Preview and Landing
    b_text = b_text.replace("<b:if cond='data:view.isHomepage'>", "<b:if cond='!data:view.isPost'>")

    # 7. Insert Curiosity Machine Section after classroom section
    curiosity_section = '\n        <!-- =====================================================================\n             6.5 THE CURIOSITY MACHINE (Interactive First-Principles Inquiry Engine)\n             ===================================================================== -->\n        <section aria-labelledby=\'curiosityMachineTitle\' class=\'section\' id=\'curiosity-machine\' style=\'padding: 0; background: #060913;\'>\n' + c_html + '\n        </section>\n'

    pause_target = '<!-- 7. QUIET PAUSE (Breathing Moment) -->'
    b_text = b_text.replace(pause_target, curiosity_section + '\n        ' + pause_target)

    # 8. Ensure Blog1 widget is version='1' and showaddelement='no' for universal Blogger compatibility
    b_text = re.sub(r'<b:widget id=\x27Blog1\x27 locked=\x27true\x27 title=\x27Ikshvaku Journal\x27 type=\x27Blog\x27 version=\x27\d+\x27>', "<b:widget id='Blog1' locked='true' title='Ikshvaku Journal' type='Blog' version='1'>", b_text)
    b_text = b_text.replace("showaddelement='false'", "showaddelement='no'")

    # 9. Insert Curiosity Machine JS before </body>
    script_tag = "\n  <script type='text/javascript'>\n  //<![CDATA[\n" + c_js + "\n  //]]>\n  </script>\n"

    body_end = b_text.find('</body>')
    b_text = b_text[:body_end] + script_tag + b_text[body_end:]

    # 10. Validate with XML parser
    try:
        ET.fromstring(b_text)
        print('SUCCESS: blogger-template.xml is 100% valid XML!')
        with open('blogger-template.xml', 'w', encoding='utf-8') as out:
            out.write(b_text)
        print(f'Successfully wrote updated blogger-template.xml ({len(b_text)} bytes)')
    except Exception as e:
        print('XML Validation FAILED on blogger-template.xml:', e)

    # 11. Also build bulletproof standalone curiosity-theme.xml
    build_standalone(c_css, c_html, c_js)

def build_standalone(c_css, c_html, c_js):
    standalone_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='1' b:layoutsversion='3' b:responsive='true' expr:dir='data:blog.languageDirection' expr:lang='data:blog.locale' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
  <meta charset='UTF-8'/>
  <meta content='width=device-width, initial-scale=1.0' name='viewport'/>
  <title><data:blog.pageTitle/></title>
  
  <b:include data='blog' name='all-head-content'/>

  <meta content='Ikshvaku Curiosity Machine — 500,000 Questions of First-Principles Inquiry' name='title'/>
  <meta content='Explore 500,000 algorithmic first-principles questions across 8 disciplines with live physics simulators and celestial audio.' name='description'/>
  <meta content='#060913' name='theme-color'/>

  <link href='https://fonts.googleapis.com' rel='preconnect'/>
  <link crossorigin='anonymous' href='https://fonts.gstatic.com' rel='preconnect'/>
  <link href='https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap' rel='stylesheet'/>

  <b:skin><![CDATA[
html, body {{
  margin: 0;
  padding: 0;
  background: #060913;
  color: #f8fafc;
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  overflow-x: hidden;
}}

/* Curiosity Machine Styles */
{c_css}
  ]]></b:skin>
</head>
<body>
  {c_html}

  <!-- Minimal Required Blogger Section and Widget -->
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

    try:
        ET.fromstring(standalone_xml)
        print('SUCCESS: curiosity-theme.xml is 100% valid XML!')
        with open('curiosity-theme.xml', 'w', encoding='utf-8') as out:
            out.write(standalone_xml)
        print(f'Successfully wrote curiosity-theme.xml ({len(standalone_xml)} bytes)')
    except Exception as e:
        print('XML Validation FAILED on curiosity-theme.xml:', e)

if __name__ == '__main__':
    integrate()
