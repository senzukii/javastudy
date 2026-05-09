function checkEx(exId) {
  const inputs = document.querySelectorAll(`[data-ex="${exId}"]`);
  let correct = 0;
  const total = inputs.length;

  inputs.forEach(input => {
    const answer = (input.dataset.answer || '').trim().toLowerCase();
    const alts = (input.dataset.alt || '').split(',').map(s => s.trim().toLowerCase()).filter(Boolean);
    const value = input.value.trim().toLowerCase();

    input.disabled = true;
    input.classList.remove('correct', 'wrong');
    if (value === answer || alts.includes(value)) {
      input.classList.add('correct');
      correct++;
    } else {
      input.classList.add('wrong');
    }
  });

  const scoreEl = document.getElementById(`${exId}-score`);
  if (!scoreEl) return;
  scoreEl.textContent = `${correct}/${total}${correct === total ? ' ✓' : ''}`;
  scoreEl.className = 'score-msg visible';
  if (correct === total) scoreEl.classList.add('all-correct');
  else if (correct > 0) scoreEl.classList.add('partial');
  else scoreEl.classList.add('none-correct');
}

function revealEx(exId) {
  const inputs = document.querySelectorAll(`[data-ex="${exId}"]`);
  const total = inputs.length;
  inputs.forEach(input => {
    input.value = input.dataset.answer;
    input.disabled = true;
    input.classList.remove('wrong');
    input.classList.add('correct');
  });
  const scoreEl = document.getElementById(`${exId}-score`);
  if (scoreEl) {
    scoreEl.textContent = `Révélé — ${total}/${total}`;
    scoreEl.className = 'score-msg visible all-correct';
  }
}

function resetEx(exId) {
  const inputs = document.querySelectorAll(`[data-ex="${exId}"]`);
  inputs.forEach(input => {
    input.value = '';
    input.disabled = false;
    input.classList.remove('correct', 'wrong');
  });
  const scoreEl = document.getElementById(`${exId}-score`);
  if (scoreEl) {
    scoreEl.className = 'score-msg';
    scoreEl.textContent = '';
  }
}
