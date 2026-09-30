import re
import xml.etree.ElementTree as ET

def integrate():
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

    # 1. Update fonts link in head to include JetBrains Mono
    b_text_new = b_text.replace(
        'family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap',
        'family=JetBrains+Mono:wght@400;500;600&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap'
    )

    # 2. Add Curiosity Machine CSS before closing </b:skin>
    skin_end = b_text_new.find(']]></b:skin>')
    if skin_end != -1:
        curiosity_css_block = '\n\n/* ==========================================================================\n   IKSHVAKU CURIOSITY MACHINE STYLES\n   ========================================================================== */\n' + c_css + '\n'
        b_text_new = b_text_new[:skin_end] + curiosity_css_block + b_text_new[skin_end:]
    else:
        print('Error: ]]></b:skin> not found')
        return

    # 3. Add Nav links in Desktop Nav and Mobile Drawer
    nav_desktop_target = '<a class=\'btn btn-primary\' expr:href=\'data:blog.homepageUrl + "#contact"\''
    curiosity_nav_link = '<a class=\'nav-link\' expr:href=\'data:blog.homepageUrl + "#curiosity-machine"\' style=\'color: var(--color-accent-gold); font-weight: 600;\'>Curiosity Machine ✦</a>\n          '
    b_text_new = b_text_new.replace(nav_desktop_target, curiosity_nav_link + nav_desktop_target)

    drawer_target = "id='mobileDrawer'>\n      <a class='nav-link' expr:href='data:blog.homepageUrl + \"#about\"'>About Academy</a>"
    drawer_replacement = "id='mobileDrawer'>\n      <a class='nav-link' expr:href='data:blog.homepageUrl + \"#about\"'>About Academy</a>\n      <a class='nav-link' expr:href='data:blog.homepageUrl + \"#curiosity-machine\"' style='color: var(--color-accent-gold); font-weight: 600;'>Curiosity Machine ✦</a>"
    b_text_new = b_text_new.replace(drawer_target, drawer_replacement)

    # 4. Insert Curiosity Machine Section after classroom section
    curiosity_section = '\n        <!-- =====================================================================\n             6.5 THE CURIOSITY MACHINE (Interactive First-Principles Inquiry Engine)\n             ===================================================================== -->\n        <section aria-labelledby=\'curiosityMachineTitle\' class=\'section\' id=\'curiosity-machine\' style=\'padding: 0; background: #060913;\'>\n' + c_html + '\n        </section>\n'

    pause_target = '<!-- 7. QUIET PAUSE (Breathing Moment) -->'
    b_text_new = b_text_new.replace(pause_target, curiosity_section + '\n        ' + pause_target)

    # 5. Insert Curiosity Machine JS before </body>
    script_tag = "\n  <script type='text/javascript'>\n  //<![CDATA[\n" + c_js + "\n  //]]>\n  </script>\n"

    body_end = b_text_new.find('</body>')
    b_text_new = b_text_new[:body_end] + script_tag + b_text_new[body_end:]

    # 6. Validate with XML parser
    try:
        ET.fromstring(b_text_new)
        print('XML Validation PASSED! Zero errors.')
        with open('blogger-template.xml', 'w', encoding='utf-8') as out:
            out.write(b_text_new)
        print(f'Successfully wrote updated blogger-template.xml ({len(b_text_new)} bytes)')
    except Exception as e:
        print('XML Validation FAILED:', e)

    # 7. Also build curiosity-theme.xml (standalone theme)
    build_standalone_curiosity_theme(c_css, c_html, c_js)

def build_standalone_curiosity_theme(c_css, c_html, c_js):
    standalone_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' expr:dir='data:blog.languageDirection' expr:lang='data:blog.locale' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
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
/* Reset & Base */
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
    <b:section class='main-section' id='main' showaddelement='false'>
      <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog' version='2'>
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
        print('Standalone curiosity-theme.xml XML Validation PASSED! Zero errors.')
        with open('curiosity-theme.xml', 'w', encoding='utf-8') as out:
            out.write(standalone_xml)
        print(f'Successfully wrote curiosity-theme.xml ({len(standalone_xml)} bytes)')
    except Exception as e:
        print('Standalone XML Validation FAILED:', e)

if __name__ == '__main__':
    integrate()
