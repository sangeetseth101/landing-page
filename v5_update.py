import re

with open("index.html", "r") as f:
    html = f.read()

# --- 1. Trust Stats Bar (mobile font size) ---
css_mobile = """    @media(max-width:768px){
      #hero{padding:130px 0 64px}
      #problem,#how-it-works,#case-studies,#meet,#what-you-get,#pricing,#faq,#booking{padding:64px 0}
      .trust-bar{flex-direction:column;align-items:flex-start;gap:24px;padding-left:16px}
      .trust-item{align-items:flex-start;text-align:left;gap:4px}
      .trust-num{font-size:28px}
      .trust-label{font-size:17px;font-weight:500;color:#ddd}
      .trust-divider{display:none}"""

# Replace the old mobile block for 768px
old_mobile_768 = """    @media(max-width:768px){
      #hero{padding:130px 0 64px}
      #problem,#how-it-works,#case-studies,#meet,#what-you-get,#pricing,#faq,#booking{padding:64px 0}
      .trust-bar{flex-direction:column;align-items:flex-start;gap:20px;padding-left:12px}
      .trust-item{align-items:flex-start;text-align:left;gap:2px}
      .trust-num{font-size:22px}
      .trust-label{font-size:16px}
      .trust-divider{display:none}"""
html = html.replace(old_mobile_768, css_mobile)

# --- 2. Problem Section (scroll animation stagger) ---
html = html.replace(
    ".reveal-item{opacity:0;transform:translateY(40px);transition:opacity 0.7s cubic-bezier(0.2,0.8,0.2,1), transform 0.7s cubic-bezier(0.2,0.8,0.2,1)}",
    ".reveal-item{opacity:0;transform:translateY(40px);transition:all 0.7s ease-out}"
)

old_js = """  /* SCROLL REVEAL ANIMATIONS */
  const revealElements = document.querySelectorAll('.reveal-item');
  const revealOptions = { threshold: 0.25, rootMargin: "0px 0px -50px 0px" };
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, revealOptions);
  revealElements.forEach(el => revealObserver.observe(el));"""

new_js = """  /* SCROLL REVEAL ANIMATIONS */
  const revealElements = document.querySelectorAll('.reveal-item');
  const revealOptions = { threshold: 0.2, rootMargin: "0px 0px -20px 0px" };
  const revealObserver = new IntersectionObserver((entries, observer) => {
    // Add staggering if multiple enter at once, but primarily base on intersection
    let delay = 0;
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('revealed');
        }, delay);
        delay += 150; // stagger 150ms
        observer.unobserve(entry.target);
      }
    });
  }, revealOptions);
  revealElements.forEach(el => revealObserver.observe(el));"""
html = html.replace(old_js, new_js)

# --- 3. Highlighted Box reduce font size ---
html = html.replace("font-size:22px;font-weight:700;color:var(--white);max-width:820px;margin:0 auto;position:relative;border-radius:18px;padding:3px;background:var(--card-bg2)", "font-size:18px;font-weight:700;color:var(--white);max-width:820px;margin:0 auto;position:relative;border-radius:18px;padding:3px;background:var(--card-bg2)")
# Add mobile font size to problem-footer
if ".problem-footer{font-size:16px}" not in html:
    html = html.replace(".trust-divider{display:none}", ".trust-divider{display:none}\n      .problem-footer{font-size:16px}\n      .problem-footer-content .btn{font-size:14px;padding:12px 24px}")

# --- 4. All CTA Buttons consistent orange ---
# Remove btn-ghost references. Just replace class="btn-ghost" with class="btn"
html = html.replace('class="btn-ghost"', 'class="btn"')
# Also remove btn-outline if it's there
html = html.replace('class="btn btn-outline"', 'class="btn"')
# And style the font size of buttons
html = html.replace(".btn{display:inline-flex", ".btn{display:inline-flex;color:#fff!important")

# --- 5. Floating Cal.com button with glow ---
# Delete old CSS overrides
old_cal_css = """    /* CAL.COM OVERRIDES */
    [data-cal-namespace="friction-audit"] button, .cal-floating-button, [class*="cal-floating"] {
      background-color: #E8453C !important;
      bottom: 5vh !important;
      transform: scale(0.82) !important;
      transform-origin: bottom right !important;
      position: relative !important;
      overflow: visible !important;
      border: 3px solid transparent !important;
      background-clip: padding-box !important;
      z-index: 10000 !important;
    }
    [data-cal-namespace="friction-audit"] button * { color: #000 !important; fill: #000 !important; font-weight: 700 !important; stroke: #000 !important; }
    
    [data-cal-namespace="friction-audit"] button::before, .cal-floating-button::before {
      content: '';
      position: absolute;
      inset: -3px; 
      border-radius: inherit;
      background: conic-gradient(from var(--angle, 0deg), transparent 40%, var(--accent) 50%, var(--amber) 55%, transparent 65%);
      animation: spin 4s linear infinite;
      z-index: -2 !important;
      pointer-events: none;
    }
    [data-cal-namespace="friction-audit"] button::after, .cal-floating-button::after {
      content: '';
      position: absolute;
      inset: -1px;
      background-color: #E8453C;
      border-radius: inherit;
      z-index: -1 !important;
      pointer-events: none;
    }"""
html = html.replace(old_cal_css, "")

# Remove Cal floating button script call
cal_script_regex = re.compile(r'Cal\.ns\["friction-audit"\]\("floatingButton", [^\)]+\);\n')
html = cal_script_regex.sub("", html)

# Insert pure HTML custom floating button just before </body>
custom_float_btn = """
<!-- CUSTOM FLOATING CAL BUTTON -->
<div class="custom-float-wrap" onclick="Cal.ns['friction-audit']('ui', {'command':'open', 'calLink':'sangeet-seth-vcxo8u/friction-audit'})">
  <div class="custom-float-inner">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
    Book your Audit
  </div>
</div>
"""
html = html.replace("</body>", custom_float_btn + "\n</body>")

# Add CSS for custom float button
custom_float_css = """
    /* CUSTOM FLOATING BUTTON */
    .custom-float-wrap {
      position: fixed;
      bottom: 5vh;
      right: 24px;
      z-index: 9999;
      cursor: pointer;
      border-radius: 100px;
      padding: 3px;
      background: var(--card-bg2);
      transform: scale(0.85);
      transform-origin: bottom right;
      transition: transform 0.2s;
    }
    .custom-float-wrap:hover { transform: scale(0.88); }
    .custom-float-wrap::before {
      content: '';
      position: absolute;
      inset: -1px;
      border-radius: 100px;
      background: conic-gradient(from var(--angle, 0deg), transparent 40%, var(--accent) 50%, var(--amber) 55%, transparent 65%);
      animation: spin 3.5s linear infinite;
      z-index: 0;
    }
    .custom-float-wrap::after {
      content: ''; position: absolute; inset: 2px; border-radius: 100px; background: #E8453C; z-index: 0;
    }
    .custom-float-inner {
      position: relative;
      z-index: 1;
      display: flex;
      align-items: center;
      gap: 10px;
      background: #E8453C;
      color: #fff;
      font-family: var(--font-head);
      font-weight: 700;
      font-size: 16px;
      padding: 14px 24px;
      border-radius: 100px;
    }
    @media(max-width:768px) { .custom-float-wrap { transform: scale(0.75); right: 16px; bottom: 20px; } .custom-float-wrap:hover { transform: scale(0.75); } }
"""
html = html.replace("/* RESPONSIVE */", custom_float_css + "\n    /* RESPONSIVE */")


# --- 6. Meet Sangeet Photo ---
old_meet_css = ".meet-photo{position:relative;z-index:1;width:100%;height:100%;min-height:480px;border-radius:16px;object-fit:cover;object-position:center top;transform:scale(0.85);display:block;filter:drop-shadow(0 20px 50px rgba(0,0,0,.55))}"
new_meet_css = ".meet-photo{position:relative;z-index:1;width:100%;height:100%;min-height:400px;border-radius:16px;object-fit:cover;object-position:70% center;display:block;filter:drop-shadow(0 20px 50px rgba(0,0,0,.55))}"
html = html.replace(old_meet_css, new_meet_css)

# Reduce frame size slightly by limiting max-width of meet-frame
if ".meet-frame{max-width:320px;margin:0 auto}" in html:
    # Desktop frame reduction
    html = html.replace(".meet-frame{position:relative;display:flex;justify-content:center}", ".meet-frame{position:relative;display:flex;justify-content:center;max-width:82%;margin:0 auto}")

with open("index.html", "w") as f:
    f.write(html)

print("HTML transformations applied successfully.")
