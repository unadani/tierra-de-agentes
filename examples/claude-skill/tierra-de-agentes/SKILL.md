---
name: tierra-de-agentes
description: Report each step of your work to a Tierra de Agentes map (start, waiting for the user, HALT, done) so the user can watch their agents on a 3D toy-brick world. Use whenever you start or finish a task, stop to ask the user something, or stop because something is wrong.
---

# Report to Tierra de Agentes

The user keeps a Tierra de Agentes world in a git repository. Each agent is a figure on the map, and its lantern shows its state. You report your steps with one command, run from the root of that repository:

```bash
python3 tools/reportar.py <agent-id> <state> "<one-line note>" [--tarea "<current task>"] [--proyecto <project-id>]
```

`<agent-id>` is your key under `agentes` in `data/mundo.json`. If the user did not tell you which one is yours, read the file, pick the agent whose `nombre` (role) matches your job, and say which one you picked.

## When to report

| Moment | State | Note |
|---|---|---|
| You start a task | `trabajando` | What you are about to do. Pass `--tarea`. |
| You stop to ask the user something | `esperando` | The question, in a few words. |
| You stop because something is wrong (a failing check, missing data, a risky action) | `halt` | The reason. |
| You finish | `listo` | One sentence on the result. The dragon gets +10 coins. |

One command per step. Keep notes short, and never put passwords, tokens or personal data in them: the file may be public.

## Publishing the change

The page re-reads `data/mundo.json` every few seconds when it is served locally (`python3 -m http.server`). If the world lives on GitHub Pages, commit and push `data/mundo.json` after your last report of the task, unless the user told you not to push.
