---
name: "engineering-principles"
displayName: "Engineering Principles"
description: "Portable, stack-agnostic engineering judgment rules. Encodes universal decisions like reuse before creating, extend existing functionality when it doesn't hurt usability (otherwise create new and flag it), follow the existing structure, and never hardcode secrets. Applies across any project; stack-specific mechanics belong in per-repo steering."
keywords: ["coding-standards", "engineering-principles", "code-quality", "reuse", "conventions", "best-practices"]
author: "Dean Clegg"
---

# Engineering Principles

> **Status: early scaffold (v0.1.0).** The rule list is a starting draft and
> still being tightened. See `POWER-INTENT.md` for the design intent and open
> decisions.

## Overview

**Engineering Principles** is a small, portable set of **universal** engineering
judgment rules — the ones that apply the same whether you are in a TypeScript
backend, a Flutter app, or a Next.js web app. It captures your "house philosophy"
so it travels to any project, guiding the reuse-vs-create and extend-vs-new
decisions and, crucially, making the agent **flag** when it deviates.

Stack-specific mechanics (folder layout, naming, build/test commands, framework
idioms) deliberately live in per-repo steering, **not** here.

## The Principles (draft)

1. **Reuse before creating.** Prefer an existing component/function over a new
   one that does the same thing.
2. **Extend, unless it hurts usability.** Extend existing functionality when it
   doesn't degrade the experience; if extending would hurt usability, create new
   instead — and flag why in one line.
3. **Follow existing structure.** Match the patterns and conventions of the code
   you're editing rather than introducing a new style.
4. **Flag deviations.** When you choose new-over-extend or depart from a pattern,
   state what you did and why. This is the high-value rule.
5. **No hardcoded secrets.** Use environment variables / config, never literals.
6. **Validate at boundaries.** Validate external/user input where it enters.
7. **Stay scoped.** Keep changes focused on the request; flag unrelated problems
   instead of silently fixing them.

## Design Notes

The value is in rules that **change a decision**. Truisms every model already
follows ("use meaningful names") are deliberately left out to keep the list tight
(~8–12 rules) so it gets followed rather than diluted.

## Skills

- **apply-principles** — applies the universal judgment rules while writing,
  changing, or reviewing code in any project.

## Getting Started

After installing, the principles guide code work automatically. You can also
invoke them explicitly, e.g. **"apply engineering principles to this change."**

## Structure

```
plugin.json                              # agent-plugins manifest (loader)
POWER.md                                 # metadata + overview (this file)
POWER-INTENT.md                          # design intent + open decisions
skills/
  apply-principles/SKILL.md              # universal engineering judgment rules
```

## License

MIT. See [LICENSE](../LICENSE).
