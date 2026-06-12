# Claude Onboarding Tools

An onboarding curriculum for the Claude ecosystem, aimed at current undergraduate students from all
majors — no technical background required. The interactive guide is the hub; everything
else is the lab.

**New here?** Open [`guide/index.html`](guide/index.html) in your browser (no install,
no server — it's a single self-contained file) and work through the 10 modules. Each
folder below pairs with a module in the guide.

## Repo map

| Folder | What's inside | Start here if… |
|---|---|---|
| [`guide/`](guide/) | The interactive guide — 10 modules with quizzes. **The hub for everything else.** | …you're new. Open `guide/index.html` in a browser. |
| [`prompts/`](prompts/) | Copy-paste prompt templates for studying, career, writing, research, and everyday life. | …you want results in the next five minutes. |
| [`claude-code-demos/`](claude-code-demos/) | Hands-on Claude Code exercises with sample projects, from first session to building a portfolio site. | …you're ready to try the terminal. |
| [`cowork-workflows/`](cowork-workflows/) | Step-by-step Cowork recipes with fake practice files included. | …you want to delegate file work safely. |
| [`troubleshooting/`](troubleshooting/) | Symptom-based FAQs for every tool, plus how to escalate. | …something isn't working. |
| [`workshop/`](workshop/) | Facilitator guide, slide deck, exercises, and handouts for running this as a live session. | …you're teaching this to a group. |

Each folder's README links back to the guide module it pairs with.

## Project structure

```
.
├── guide/                  # Interactive guide (single HTML file, no build step)
├── prompts/                # Prompt templates, one file per life area
├── claude-code-demos/      # Runnable exercises, numbered by difficulty
│   ├── 01-first-session/
│   ├── 02-claude-md-workshop/
│   ├── 03-build-a-portfolio-site/
│   └── 04-data-cleanup/
├── cowork-workflows/       # Cowork recipes + sample-files/ practice data
├── troubleshooting/        # Symptom-based FAQs, one file per product
├── workshop/               # Facilitator guide, slides, exercises, handouts
├── CHANGELOG.md
├── CLAUDE.md               # Conventions and rules for working on this repo
├── CONTRIBUTING.md
└── LICENSE
```

## Notes

- All sample data (names, vendors, figures) is fake — invented for practice.
- Plan pricing and usage limits change often, so docs link to
  [support.claude.com](https://support.claude.com) and
  [docs.claude.com](https://docs.claude.com) instead of hardcoding them.
- Want to contribute? See [`CONTRIBUTING.md`](CONTRIBUTING.md).
