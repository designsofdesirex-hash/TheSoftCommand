import os

css_append = """
/* ==========================================================================
   Age Gate Modal
   ========================================================================== */
.age-gate-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(8, 8, 8, 0.95);
  backdrop-filter: blur(8px);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 1;
  transition: opacity 0.6s ease;
}

.age-gate-overlay.fade-out {
  opacity: 0;
  pointer-events: none;
}

.age-gate-content {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  padding: 3rem 2rem;
  max-width: 500px;
  width: 90%;
  text-align: center;
  border-radius: 2px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.8);
  position: relative;
  overflow: hidden;
}

.age-gate-content::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, var(--accent-1), transparent);
}

.age-gate-content h2 {
  margin-bottom: 1rem;
  font-size: clamp(1.8rem, 4vw, 2.4rem);
}

.age-gate-content p {
  opacity: 0.8;
  margin-bottom: 2.5rem;
}

.age-gate-btns {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.age-gate-btns .btn {
  min-width: 140px;
}

body.no-scroll {
  overflow: hidden;
}
"""

with open('assets/css/styles-upgrade.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

js_append = """
  // 9. Age Gate Modal
  if (!localStorage.getItem('ageVerified')) {
    const ageGateHTML = `
      <div id="age-gate-modal" class="age-gate-overlay">
        <div class="age-gate-content reveal active">
          <p class="section-eyebrow cinzel gold-gradient-text">Verification Required</p>
          <h2 class="cormorant gold-gradient-text">Are you 18 or older?</h2>
          <p class="jost">This website contains adult themes. By entering, you confirm you are at least 18 years of age and consent to viewing such content.</p>
          <div class="age-gate-btns">
            <button id="btn-over-18" class="btn btn--primary cinzel">I am 18+</button>
            <button id="btn-under-18" class="btn btn--ghost cinzel">Exit</button>
          </div>
        </div>
      </div>
    `;
    document.body.insertAdjacentHTML('beforeend', ageGateHTML);
    document.body.classList.add('no-scroll');

    document.getElementById('btn-over-18').addEventListener('click', () => {
      localStorage.setItem('ageVerified', 'true');
      const modal = document.getElementById('age-gate-modal');
      modal.classList.add('fade-out');
      document.body.classList.remove('no-scroll');
      setTimeout(() => modal.remove(), 600);
    });

    document.getElementById('btn-under-18').addEventListener('click', () => {
      window.location.href = 'https://www.google.com';
    });
  }
});
"""

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

if '});' in js_content and 'Age Gate Modal' not in js_content:
    js_parts = js_content.rsplit('});', 1)
    new_js_content = js_parts[0] + js_append + js_parts[1]
    with open('assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(new_js_content)
