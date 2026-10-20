"""Run with: python reference_impl/reproduce.py (standard library only)."""
from mws import Candidate, choose, threshold
CASES=[Candidate('A',.82,.18,.35),Candidate('B',.74,.32,.05),Candidate('C',.69,.22,.02)]
print('Four-way ablation | A B C | winner')
for label,m,g in [('Base only',0,0),('Memory only',.8,0),('Governor only',0,1.5),('Full',.8,1.5)]:
    win,s=choose(CASES,m,g)
    print(label, *(f'{s[c.name]:.3f}' for c in CASES), win)
    assert win == ('A' if label=='Base only' else 'B')
assert abs(threshold(CASES,0)-4/7)<1e-10
assert threshold(CASES,1.5) is None
assert choose([Candidate('X',1,1,0,False)])[0] is None
print('Base-only strict crossover:',round(threshold(CASES,0),6))
print('Governed winner-change threshold: none (B already wins)')
print('PASS: sample arithmetic, strict veto and crossover conditions')
