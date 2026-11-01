#!/usr/bin/env python3
"""Report an agent's step to Tierra de Agentes by editing data/mundo.json.

Usage:
  python3 tools/reportar.py <agent-id> <state> "<note>" [--tarea "..."] [--proyecto <id>] [--archivo data/mundo.json]

  state: trabajando (working), esperando (waiting), halt, listo (done) or inactivo (idle)

Examples:
  python3 tools/reportar.py correo trabajando "Sorting the inbox" --tarea "Sort the inbox"
  python3 tools/reportar.py correo listo "Inbox sorted: 42 emails, 3 need you"

What it does:
  - sets the agent's estado (and tarea, proyecto) and stamps actualizado;
  - adds an entry to eventos, so it shows in the log;
  - when the state is "listo", gives the dragon +10 coins.
If the agent id does not exist yet, it creates a simple one so you can see it on the map.
The page re-reads data/mundo.json every few seconds while nothing has been edited in the browser.
Only the Python standard library is used.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

ESTADOS = ("trabajando", "esperando", "halt", "listo", "inactivo")


def main():
    ap = argparse.ArgumentParser(description="Report an agent's step to data/mundo.json")
    ap.add_argument("agente", help="agent id, the key under 'agentes' in mundo.json")
    ap.add_argument("estado", choices=ESTADOS)
    ap.add_argument("nota", nargs="?", default="", help="one line for the log")
    ap.add_argument("--tarea", help="what the agent is doing now")
    ap.add_argument("--proyecto", help="project id, the key under 'proyectos'")
    ap.add_argument("--archivo", default=os.path.join(os.path.dirname(__file__), "..", "data", "mundo.json"))
    a = ap.parse_args()

    with open(a.archivo, encoding="utf-8") as f:
        mundo = json.load(f)
    # once someone reports, the file is a real world: the page should show it instead of the demo
    mundo.pop("mostrarDemo", None)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    agentes = mundo.setdefault("agentes", {})
    ag = agentes.setdefault(a.agente, {
        "personaje": a.agente, "nombre": "Agente", "descripcion": "", "sala": next(iter(mundo.get("salas", {})), ""),
        "estado": "inactivo", "apariencia": {"raza": "hombre", "tunica": "#1F62D0", "piernas": "#1B1D24"}})
    ag["estado"] = a.estado
    ag["actualizado"] = now
    if a.tarea is not None:
        ag["tarea"] = a.tarea
    if a.proyecto is not None:
        ag["proyecto"] = a.proyecto

    ev = {"agente": a.agente, "estado": a.estado, "nota": a.nota, "ts": now}
    if a.proyecto or ag.get("proyecto"):
        ev["proyecto"] = a.proyecto or ag.get("proyecto")
    mundo.setdefault("eventos", {})[now.replace("-", "").replace(":", "") + "-" + a.agente] = ev

    if a.estado == "listo":
        t = mundo.setdefault("tesoro", {}).setdefault("dragon", {"monedas": 0, "joyas": 0, "cofres": 0})
        t["monedas"] = int(t.get("monedas", 0)) + 10

    tmp = a.archivo + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(mundo, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, a.archivo)
    print(f"{a.agente}: {a.estado}" + (f" - {a.nota}" if a.nota else ""))


if __name__ == "__main__":
    sys.exit(main())
