# Textos de lanzamiento (borrador, no publicado)

Borradores para que los revises y publiques tú. Ninguno menciona para qué usas el proyecto, tu trabajo ni tu nombre: hablan solo del mundo y de cómo conectarlo.

Antes de publicar:

- Haz merge del PR a `main` y espera a que GitHub Pages se actualice (1 o 2 minutos).
- Abre la demo en el celular y en el computador, y confirma que se mueve.
- Sube `docs/social-preview.png` en **Settings → General → Social preview** del repositorio.
- Publica de a uno, con un día o dos de distancia, para poder responder comentarios.

Enlaces:

- Demo: https://unadani.github.io/tierra-de-agentes/
- Repositorio: https://github.com/unadani/tierra-de-agentes
- GIF: `docs/demo.gif` (súbelo como imagen o video donde se pueda)

---

## Reddit · r/ClaudeAI

Elige el flair **Built with Claude** (o el que el subreddit use para proyectos).

**Título:** I gave my Claude agents a toy-brick fantasy world to live in (open source, no build step)

**Texto:**

> I wanted to see what my agents were doing at a glance, so I built a tiny world for them. Each agent is a little plastic figure on a 3D fantasy map. Its lantern shows its state: working, waiting for me, HALT, or done. A dragon earns coins every time a task finishes.
>
> - Live demo (10 sample agents doing their thing): https://unadani.github.io/tierra-de-agentes/
> - Code: https://github.com/unadani/tierra-de-agentes
>
> How it connects: agents write their state to one JSON file. There is a small Python script for that, and an example Claude skill that makes Claude report every start, question, HALT and finish. Run it locally and the map updates live; on GitHub Pages it updates on push.
>
> It is one HTML file (Three.js) plus one JSON. Fork it, turn on Pages, done. The UI is in Spanish for now.
>
> I'd love to hear what agents you would put in it, and what states you would want to see.

---

## Reddit · r/LocalLLaMA

Este subreddit es exigente con la autopromoción: el texto pone por delante que sirve con cualquier modelo local.

**Título:** A 3D toy-brick map to watch your agents work: works with any model or framework, just writes a JSON

**Texto:**

> Small side project: a fantasy map where every agent is a toy figure with a status lantern (working / waiting / HALT / done). It does not care which model you run. Your agent loop only has to update a JSON file, either directly or with a one-line call:
>
> `python3 tools/reportar.py coder halt "3 tests failing after the refactor"`
>
> Served locally, the page re-reads the file every few seconds, so you can leave it open on a second screen while a local agent grinds through a task list.
>
> - Demo: https://unadani.github.io/tierra-de-agentes/
> - Repo (MIT, no build step, no backend): https://github.com/unadani/tierra-de-agentes
>
> Ideas welcome, especially an Ollama or llama.cpp example to ship with it.

---

## Hacker News · Show HN

**Título:** Show HN: Tierra de Agentes – a toy-brick 3D world to watch your AI agents work

**URL:** https://unadani.github.io/tierra-de-agentes/

**Primer comentario (lo publicas tú apenas sale el post):**

> Hi HN. I wanted a glanceable way to see which of my AI agents were working, which were waiting on me, and which had stopped. Instead of another dashboard, I built a small fantasy map where each agent is a toy figure with a status lantern.
>
> Technical bits: a single HTML file with Three.js r147, no build step. State lives in one JSON file. Agents report by editing it (there is a small stdlib-only Python helper and an example Claude skill). Served locally, the page polls the file every 4 seconds; on GitHub Pages you push. Figures and bricks are procedural (merged brick geometries with studs, a repeating stud texture on the baseplate), so it runs on phones.
>
> The demo has 10 sample agents that change state on their own. Fork, enable Pages, and it is yours. The UI is Spanish for now.
>
> Repo: https://github.com/unadani/tierra-de-agentes

---

## X / Twitter

**Post 1 (con el GIF):**

> Gave my AI agents a world to live in 🧱🐉
>
> Each agent is a toy figure on a 3D fantasy map. Its lantern shows if it's working, waiting for you, stopped, or done. A dragon earns coins for every finished task.
>
> Demo → https://unadani.github.io/tierra-de-agentes/
> Open source, one HTML file.

**Post 2 (respuesta al primero):**

> Connecting an agent is one line:
>
> python3 tools/reportar.py coder listo "PR merged"
>
> Works with Claude, local models, cron jobs, anything that can write a file. There's an example Claude skill in the repo:
> https://github.com/unadani/tierra-de-agentes

---

## LinkedIn

> Construí un mundo pequeño para mis agentes de IA.
>
> Cada agente es una figurita de juguete en un mapa de fantasía en 3D. Su linterna muestra si está trabajando, si espera una respuesta mía, si se detuvo por un problema o si terminó. Un dragón suma monedas cada vez que un agente cierra una tarea.
>
> Quería ver de un vistazo qué agente necesitaba algo, sin otro panel de control lleno de tablas. Es de código abierto, funciona con cualquier agente que pueda escribir un archivo y se instala con un fork.
>
> Demo: https://unadani.github.io/tierra-de-agentes/
> Código: https://github.com/unadani/tierra-de-agentes
>
> ¿Qué agentes pondrías tú en tu mundo?

*Versión en inglés, si la prefieres:*

> I built a tiny world for my AI agents. Each one is a toy figure on a 3D fantasy map, and its lantern shows whether it is working, waiting for me, stopped, or done. A dragon earns coins for every finished task. It is open source and works with any agent that can write a file. Demo: https://unadani.github.io/tierra-de-agentes/

---

## Product Hunt

**Nombre:** Tierra de Agentes

**Tagline (máx. 60 caracteres):** Give your AI agents a toy-brick world to live in

**Descripción (máx. 260 caracteres):**

> A 3D fantasy map where each AI agent is a toy figure with a status lantern: working, waiting, HALT or done. Agents report by writing one JSON file. Open source, no build step: fork it and turn on GitHub Pages.

**Temas:** Artificial Intelligence, Developer Tools, Open Source, Productivity

**Galería:** `docs/social-preview.png` como portada y `docs/demo.gif` como segunda imagen.

**Primer comentario del maker:**

> Hi Product Hunt! I made Tierra de Agentes to *see* agents at work instead of reading logs. In the demo each one lives somewhere on the map: the email agent in the valley, the coding agent at the forge, the travel agent at the harbour. When one gets stuck it lights up red, and when one finishes the dragon gets paid.
>
> It works with any agent or model: they only write to a JSON file (a helper script and a Claude skill are included). Try the demo, then fork it for your own crew. I'd love feedback on what to add next.
