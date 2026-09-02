# Kiro Powers

A collection of [Kiro Powers](https://kiro.dev/docs/powers/) by Dean Clegg.
Each power lives in its own directory and can be installed independently.

## Powers

| Power | Description |
|-------|-------------|
| [`ui-architect`](./ui-architect) | UI/UX architect that designs and reviews UI one screen at a time, building from your own design system. |
| [`research-desk`](./research-desk) | Evidence-first research assistant that cites every claim and can export findings to Markdown, CSV, or PDF. |
| [`engineering-principles`](./engineering-principles) | Portable, stack-agnostic engineering judgment rules (reuse before create, extend-or-flag, follow existing structure). |

> `research-desk` and `engineering-principles` are early scaffolds (v0.1.0).
> See each power's `POWER-INTENT.md` for the design intent and open decisions.

## Installing a power

In Kiro, open the Powers panel, choose **Add Custom Power → Import from GitHub**,
and provide this repository. A single repository can contain multiple powers,
each in its own directory.

Repository: https://github.com/Dean-Clegg/Kiro-Powers

## Repository layout

```
Kiro-Powers/
├── ui-architect/
│   └── plugin.json
├── research-desk/
│   └── plugin.json
└── engineering-principles/
    └── plugin.json
```

Each power has its own `plugin.json` at its directory root, per the
[Agent Plugins specification](https://agent-plugins.org/).

## Versioning

Each power is versioned independently via the `version` field in its
`plugin.json`. Bump that value when releasing changes so Kiro's
**Check for updates** picks them up.

## License

MIT — see [LICENSE](./LICENSE).
