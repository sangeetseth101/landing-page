import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Add btn-ghost and reveal-item to CSS
css_additions = """
    .btn-ghost{background:transparent;border:1.5px solid rgba(232,69,60,.5);color:var(--accent);font-family:var(--font-head);font-size:15px;font-weight:700;padding:14px 28px;border-radius:10px;display:inline-flex;align-items:center;transition:border-color .2s,background .2s,transform .2s;text-decoration:none}
    .btn-ghost:hover{border-color:var(--accent);background:rgba(232,69,60,.08);transform:translateY(-2px)}
    .reveal-item{opacity:0;transform:translateY(40px);transition:opacity 0.7s cubic-bezier(0.2,0.8,0.2,1), transform 0.7s cubic-bezier(0.2,0.8,0.2,1)}
    .reveal-item.revealed{opacity:1;transform:translateY(0)}
    .cta-container{margin-top:48px;display:flex;justify-content:center;width:100%}
"""
if ".btn-ghost" not in html:
    html = html.replace(".btn-sm{padding:11px 22px;font-size:14px}", ".btn-sm{padding:11px 22px;font-size:14px}\n" + css_additions)

# 2. Update PROBLEM CSS
old_prob_css = """    /* PROBLEM */
    #problem{padding:100px 0;position:relative}
    .problem-header{text-align:center;margin-bottom:56px}
    .problem-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:48px}
    .problem-card{background:var(--card-bg);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:var(--radius);padding:28px 28px 28px 32px;transition:border-color .25s,transform .25s}
    .problem-card:hover{border-top-color:rgba(255,255,255,.12);border-right-color:rgba(255,255,255,.12);border-bottom-color:rgba(255,255,255,.12);transform:translateY(-3px)}
    .problem-num{font-family:var(--font-head);font-size:13px;font-weight:700;color:var(--accent);letter-spacing:.08em;margin-bottom:12px}
    .problem-text{font-size:16px;font-weight:500;color:var(--white);line-height:1.55}
    .problem-footer{text-align:center;font-family:var(--font-head);font-size:20px;font-weight:700;color:var(--white);max-width:600px;margin:0 auto;padding:32px 28px;background:var(--card-bg2);border:1px solid var(--border);border-radius:var(--radius)}"""

new_prob_css = """    /* PROBLEM */
    #problem{padding:100px 0;position:relative}
    .problem-header{text-align:center;margin-bottom:56px}
    .problem-grid{display:flex;flex-direction:column;gap:20px;max-width:820px;margin:0 auto 56px}
    .problem-card{background:var(--card-bg);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:var(--radius);padding:32px 36px;transition:border-color .25s,box-shadow .25s}
    .problem-card.reveal-item:hover{border-top-color:rgba(255,255,255,.12);border-right-color:rgba(255,255,255,.12);border-bottom-color:rgba(255,255,255,.12);transform:translateY(-4px);transition:border-color .2s, transform .2s}
    .problem-num{font-family:var(--font-head);font-size:14px;font-weight:700;color:var(--accent);letter-spacing:.08em;margin-bottom:12px;transform-origin:left center;transform:scale(0.85);transition:transform 0.7s cubic-bezier(0.2,0.8,0.2,1)}
    .problem-card.revealed .problem-num{transform:scale(1)}
    .problem-text{font-size:18px;font-weight:500;color:var(--white);line-height:1.6}
    .problem-footer{text-align:center;font-family:var(--font-head);font-size:22px;font-weight:700;color:var(--white);max-width:820px;margin:0 auto;position:relative;border-radius:18px;padding:3px;background:var(--card-bg2)}
    .problem-footer::before{content:'';position:absolute;inset:-2px;border-radius:20px;background:conic-gradient(from var(--angle,0deg),transparent 40%,var(--accent) 50%,var(--amber) 55%,transparent 65%);animation:spin 4s linear infinite}
    @supports not (background: conic-gradient(from 0deg, red, blue)){ .problem-footer::before{background:linear-gradient(var(--accent),var(--amber));opacity:.6} }
    .problem-footer::after{content:'';position:absolute;inset:2px;border-radius:16px;background:var(--card-bg2);z-index:0}
    .problem-footer-content{position:relative;z-index:1;padding:36px;display:flex;flex-direction:column;align-items:center;gap:28px}"""
html = html.replace(old_prob_css, new_prob_css)

# 3. Update the PROBLEM HTML
old_prob_html = """    <div class="problem-grid">
      <div class="problem-card">
        <div class="problem-num">01</div>
        <p class="problem-text">You spend more time on admin than on actual client work.</p>
      </div>
      <div class="problem-card">
        <div class="problem-num">02</div>
        <p class="problem-text">You've tried AI tools. The output was generic. Nothing stuck.</p>
      </div>
      <div class="problem-card">
        <div class="problem-num">03</div>
        <p class="problem-text">Session prep, proposals, follow-ups, onboarding. Same tasks, every day, from scratch.</p>
      </div>
      <div class="problem-card">
        <div class="problem-num">04</div>
        <p class="problem-text">Your expertise is trapped in your head. Nothing runs without you.</p>
      </div>
    </div>
    <div class="problem-footer">
      You don't need another tool. You need someone to build the system for you.
    </div>"""

new_prob_html = """    <div class="problem-grid">
      <div class="problem-card reveal-item">
        <div class="problem-num">01</div>
        <p class="problem-text">Are you spending more time on admin than on actual client work?</p>
      </div>
      <div class="problem-card reveal-item">
        <div class="problem-num">02</div>
        <p class="problem-text">Have you tried AI tools, only to get generic output that never stuck?</p>
      </div>
      <div class="problem-card reveal-item">
        <div class="problem-num">03</div>
        <p class="problem-text">Are you still doing session prep, proposals, follow-ups, and onboarding from scratch - every single day?</p>
      </div>
      <div class="problem-card reveal-item">
        <div class="problem-num">04</div>
        <p class="problem-text">Is your expertise trapped in your head, so nothing runs without you?</p>
      </div>
    </div>
    <div class="problem-footer reveal-item">
      <div class="problem-footer-content">
        <p>You don't need another tool.<br>You need someone to build the system for you.</p>
        <a href="#booking" class="btn-ghost">Save +360 Hours Per Year →</a>
      </div>
    </div>"""
html = html.replace(old_prob_html, new_prob_html)

# 4. Meet Sangeet photo zoom out
old_meet_photo_css = ".meet-photo{position:relative;z-index:1;width:100%;border-radius:16px;object-fit:cover;display:block;filter:drop-shadow(0 20px 50px rgba(0,0,0,.55))}"
new_meet_photo_css = ".meet-photo{position:relative;z-index:1;width:100%;height:100%;min-height:480px;border-radius:16px;object-fit:cover;object-position:center top;transform:scale(0.85);display:block;filter:drop-shadow(0 20px 50px rgba(0,0,0,.55))}\n    .meet-frame-inner{overflow:hidden}"
html = html.replace(old_meet_photo_css, new_meet_photo_css)
html = html.replace(".meet-frame-inner{position:relative;border-radius:18px;padding:3px;background:var(--card-bg2)}", ".meet-frame-inner{position:relative;border-radius:18px;padding:3px;background:var(--card-bg2);overflow:hidden;display:flex;align-items:center;justify-content:center;height:100%}")

# 5. Add JavaScript for animations
js_str = """
  /* SCROLL REVEAL ANIMATIONS */
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
  revealElements.forEach(el => revealObserver.observe(el));
"""
if "/* SCROLL REVEAL ANIMATIONS */" not in html:
    html = html.replace("/* STICKY NAV */", js_str + "\n  /* STICKY NAV */")

# 6. Hero CTA update
html = html.replace("Take the Free Friction Audit →", "Book Your Free Friction Audit →")

# 7. Insert missing CTAs into sections
# How it works
hiw_close = "    </div>\n  </div>\n</section>\n\n<!-- CASE STUDIES -->"
hiw_new = "    </div>\n    <div class=\"cta-container\"><a href=\"#booking\" class=\"btn\">Book Your Free Friction Audit →</a></div>\n  </div>\n</section>\n\n<!-- CASE STUDIES -->"
html = html.replace(hiw_close, hiw_new)

# Case Studies
cs_close = "    <p class=\"cs-disclaimer\">Case studies include both named clients (with permission) and anonymized composites representing typical results.</p>\n  </div>\n</section>\n\n<!-- MEET SANGEET -->"
cs_new = "    <p class=\"cs-disclaimer\">Case studies include both named clients (with permission) and anonymized composites representing typical results.</p>\n    <div class=\"cta-container\"><a href=\"#booking\" class=\"btn-ghost\">Save +360 Hours Per Year →</a></div>\n  </div>\n</section>\n\n<!-- MEET SANGEET -->"
html = html.replace(cs_close, cs_new)

# Meet Sangeet
meet_close = "linkedin.com/in/sangeet-seth/\n        </a>\n      </div>"
meet_new = "linkedin.com/in/sangeet-seth/\n        </a>\n        <div style=\"margin-top:32px\"><a href=\"#booking\" class=\"btn\">Book Your Free Friction Audit →</a></div>\n      </div>"
html = html.replace(meet_close, meet_new)

# FAQ
faq_close = "    </div>\n  </div>\n</section>\n\n<!-- FINAL CTA + CAL.COM BOOKING -->"
faq_new = "    </div>\n    <div class=\"cta-container\"><a href=\"#booking\" class=\"btn-ghost\">Save +360 Hours Per Year →</a></div>\n  </div>\n</section>\n\n<!-- FINAL CTA + CAL.COM BOOKING -->"
html = html.replace(faq_close, faq_new)

# 8. Floating Cal.com button restyle
# The float button is injected. We add global CSS overrides
cal_css = """
/* Cal.com floating button overrides */
<style>
  [data-cal-namespace="friction-audit"] button, .cal-floating-button {
    background-color: #E8453C !important;
    color: #000 !important;
    bottom: 5vh !important;
    transform: scale(0.85) !important;
    position: relative !important;
  }
  .cal-floating-btn-wrap {
    position: fixed;
    bottom: 5vh;
    right: 20px;
    z-index: 99999;
  }
  .cal-glow-wrap::before {
    content:'';position:absolute;inset:-3px;border-radius:100px;
    background:conic-gradient(from var(--angle,0deg),transparent 40%,var(--accent) 50%,var(--amber) 55%,transparent 65%);
    animation:spin 4s linear infinite;z-index:-1;
    pointer-events:none;
  }
</style>
"""
# Since Cal dynamically adds the button, injecting CSS might be tricky if it lives in shadow DOM or iframe.
# Actually, Cal.com popup button is inserted into the main DOM.
# We will just append the CSS before </head>. 
# But wait, to put a glowing border around it, we can't easily add a wrapper around their injected button if it's dynamic.
# Actually, their button is just a DOM element. The glowing border might be achieved using `box-shadow` animation instead of a wrapper?
# Wait! Animated conic gradient requires a pseudo element. Let's add the basic style override first.
html = html.replace("/* RESPONSIVE */", """
    /* CAL.COM OVERRIDES */
    body [id^="cal-floating-button"] { background: #E8453C !important; bottom: 5vh !important; transform: scale(0.85) !important; transform-origin: bottom right !important; }
    body [id^="cal-floating-button"] span { color: #0A0A0A !important; font-weight: 700 !important }
    body [id^="cal-floating-button"] svg { fill: #0A0A0A !important; stroke: #0A0A0A !important }
    /* Approximate the glow with animated box-shadow since we can't easily add ::before to their button if we don't control its HTML */
    @keyframes pulseGlow { 0% { box-shadow: 0 0 0 0 rgba(232,69,60,0.7); } 70% { box-shadow: 0 0 0 15px rgba(232,69,60,0); } 100% { box-shadow: 0 0 0 0 rgba(232,69,60,0); } }
    body [id^="cal-floating-button"] { animation: pulseGlow 2s infinite !important; }

    /* RESPONSIVE */""")

# Also change floating button text
html = html.replace('"buttonText":"Book my Friction Audit"', '"buttonText":"Book your Audit"')

with open("index.html", "w") as f:
    f.write(html)

print("HTML transformations applied successfully.")
