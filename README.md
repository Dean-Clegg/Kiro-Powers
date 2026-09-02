# Kiro Powers

A collection of [Kiro Powers](https://kiro.dev/docs/powers/) by Dean Clegg.
Each power lives in its own directory and can be installed independently.

## Powers

| Power | Description |
|-------|-------------|
| [`ui-architect`](./ui-architect) | UI/UX architect that designs and reviews UI one screen at a time, building from your own design system. |
| [`research-desk`](./research-desk) | Evidence-first research assistant that cites every claim and can export findings to Markdown, CSV, or PDF. |
| [`engineering-principles`](./engineering-principles) | Portable, stack-agnostic engineering judgment rules (reuse before create, extend-or-flag, follow existing structure). |

## Installing a power

This repository holds multiple powers, each in its own subdirectory. To install
a single power, use its **`/tree/main/<power>` URL** — not the bare repo URL.

Steps in Kiro:

1. Open the Powers panel (Ghosty icon with the lightning bolt).
2. **Add Custom Power → Import power from GitHub**.
3. Paste the power's URL below and click **Install**.

> **Important:** paste the full `/tree/main/<power>` path. Pasting the bare repo
> URL (`https://github.com/Dean-Clegg/Kiro-Powers`) installs the entire repo as
> one power instead of the individual power you want.

### Install URLs

Each URL is in its own code block — on GitHub, hover the block and use the
one-click **copy** button in the top-right corner.

**ui-architect**

```
https://github.com/Dean-Clegg/Kiro-Powers/tree/main/ui-architect
```

**research-desk**

```
https://github.com/Dean-Clegg/Kiro-Powers/tree/main/research-desk
```

**engineering-principles**

```
https://github.com/Dean-Clegg/Kiro-Powers/tree/main/engineering-principles
```

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
`plugin.json`. Bump that value and push to `main` when releasing changes so
Kiro's **Check for updates** picks them up. The install URLs above pin to the
`main` branch, so publishing on `main` is what makes updates flow.

## License

MIT — see [LICENSE](./LICENSE).
