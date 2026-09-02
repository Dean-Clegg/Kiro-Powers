# engineering-principles — Power Intent

> Design/intent doc, not part of the plugin spec. Ignored by the plugin loader.

## Purpose

A small, portable set of UNIVERSAL engineering judgment rules — the ones that
apply the same whether you're in the TypeScript backend, the Flutter app, or the
Next.js web app. It captures your "house philosophy" so it travels to any repo.

## The dividing line (important)

- **Universal judgment rules → this Power.** Stack-agnostic decisions.
- **Stack-specific mechanics → per-repo steering.** Folder layout, naming,
  build/test commands, framework idioms. Do NOT put those here.

## Anti-bloat rule

Only include rules that CHANGE A DECISION. Drop truisms every model already
follows ("use meaningful names", "write good code") — they add noise and dilute
the rules that matter. Aim for ~8–12 real rules, kept short. A tight list gets
followed; a long one gets ignored.

## Candidate rules (refine later — draft in SKILL.md)

- Reuse before creating: prefer an existing component/function over a new one.
- Extend existing functionality when it doesn't hurt usability; if extending
  WOULD hurt usability, create new instead — and flag why in one line.
- Follow the existing structure and patterns of the file/module you're in.
- When you deviate from an existing pattern or choose new-over-extend, state
  what you did and why (the "flag it" behavior — this is the valuable part).
- Never hardcode secrets/keys; use env/config.
- Validate inputs at boundaries.
- Keep changes scoped to the request; flag unrelated issues instead of fixing
  them silently.

## Open decisions
- [ ] Final rule list (keep it tight).
- [ ] Should it always be on, or activate by phrase like "use engineering-principles"?
- [ ] Does this stay a Power, or fold into shared steering? (Power only pays off
      if you want it across unrelated repos / to share it.)

## Status
Scaffold only. Finish the rule list in SKILL.md later.
