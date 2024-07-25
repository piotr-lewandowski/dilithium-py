model;

# additional hints about some variables
# hint that s[j] = s_hint[j] or s[j] = s_hint[j] + 1
set HINTS within INDICES;
param s_hint{HINTS} integer;
# hint that s[j] = s_exact[j]
set EXACT within INDICES;
param s_exact{EXACT} integer;

subject to exact_hint {j in EXACT}:
  s[j] = s_exact[j];

subject to approximate_hint {j in HINTS}:
  s_hint[j] <= s[j] <= s_hint[j] + 1;