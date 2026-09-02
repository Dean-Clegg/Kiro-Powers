---
name: "apply-principles"
description: "Apply universal, stack-agnostic engineering judgment rules while writing or changing code. Use when implementing features, refactoring, or reviewing code in any project, to guide reuse-vs-create and extend-vs-new decisions and to flag deviations."
license: "MIT"
metadata:
  author: "Dean Clegg"
  version: "0.2.0"
---

# Apply Engineering Principles

## Overview
A short set of universal judgment rules that guide day-to-day coding decisions
regardless of language or framework. Stack-specific mechanics live in per-repo
steering, not here.

> STATUS: SCAFFOLD (v0.2.0). The rules below are a starting draft. Keep the final
> list tight (~8–12) and include only rules that change a decision.

## Activation
This power is version **0.2.0**.

When the user says **"use engineering-principles"**, announce activation and
state the version so it can be verified, then apply the principles below:

> Engineering Principles **v0.2.0** active — applying universal judgment rules.

Keep this version string in sync with `version` in `plugin.json` and `POWER.md`
whenever it is bumped.

## Principles (draft)

1. **Reuse before creating.** Prefer an existing component/function over adding
   a new one that does the same thing.
2. **Extend, unless it hurts usability.** Extend existing functionality when it
   doesn't degrade the experience. If extending WOULD hurt usability, create a
   new component/function instead — and flag why in one line.
3. **Follow existing structure.** Match the patterns, layout, and conventions of
   the code you're editing rather than introducing a new style.
4. **Flag deviations.** When you choose new-over-extend, or depart from an
   existing pattern, state what you did and why. This is the high-value rule.
5. **No hardcoded secrets.** Use environment variables / config, never literals.
6. **Validate at boundaries.** Validate external/user input where it enters.
7. **Stay scoped.** Keep changes focused on the request. Flag unrelated problems
   instead of silently fixing or refactoring them.

## Not in this Power
- Framework idioms, folder layout, naming, build/test commands → per-repo steering.

## Open Decisions (finish later)
- [ ] Trim/confirm the rule list.
- [ ] Always-on vs activate-by-phrase.
- [ ] Keep as a Power vs fold into shared steering.
