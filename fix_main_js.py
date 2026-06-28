import re

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Let's fix the broken main.js by removing the botched age gate first
if '// 9. Age Gate Modal' in js_content:
    js_content = js_content.split('// 9. Age Gate Modal')[0]
    # Now js_content has the broken end of initCustomSelects
    js_content = js_content.rstrip()
    if not js_content.endswith('});\\n}'):
        if not js_content.endswith('}'):
            js_content += '\n  });\n}'

age_gate_logic = """
document.addEventListener('DOMContentLoaded', () => {
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

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content + '\n' + age_gate_logic)
