# Tierra de Agentes

*[English below](#english)*

Un mundo de fantasía en 3D, con figuras de juguete, para darle un lugar a tus agentes. Cada agente vive en un pueblo, un bosque o una ciudad del mapa, tiene un personaje, una apariencia y una función, y muestra su estado con una linterna: trabajando, en espera, HALT, listo o inactivo.

El mundo viene vacío a propósito. Trae once lugares y cinco equipos como plantillas, y tres agentes de ejemplo sin función. Lo llenas tú.

## Qué trae

- **El mapa**: once lugares con su paisaje (un valle con cascada, una ciudad blanca, un puerto, una forja, minas, bosques) unidos por caminos y un río.
- **Los agentes**: figuras con oficio, linterna de estado y ficha. Los coordinadores llevan estandarte, y un Gran Maestro recorre el mapa.
- **El editor**: crea, edita y borra agentes desde la página (botón «+ Nuevo agente» en el panel «Agentes y bitácora»).
- **La Torre del Vigía**: tus proyectos, ordenados por plazo. Cada proyecto en marcha es un anillo que gira alrededor de la llama.
- **La Crónica y el registro de actividad**: todo lo que reportan los agentes, por día, con sesiones y duraciones.
- **Brasa, el dragón guardián**: su tesoro crece con cada tarea terminada (+10 monedas) y cada proyecto enviado o logrado (cofres).

## Cómo abrirlo

El navegador no deja leer `data/mundo.json` si abres `index.html` con doble clic. Sirve la carpeta con cualquier servidor local:

```bash
python3 -m http.server 8000
```

Y entra a <http://localhost:8000>. También funciona tal cual en GitHub Pages (Settings → Pages → rama `main`, carpeta `/`).

Necesita conexión a internet para cargar Three.js y las fuentes desde sus CDN.

## Cómo se guardan los cambios

1. Al abrir, la página lee `data/mundo.json`.
2. Lo que cambies en la página (agentes, proyectos, estados) se guarda en el `localStorage` de tu navegador. Solo lo ves tú, en ese navegador.
3. Para conservarlo o compartirlo, usa **Descargar mundo.json** (al final del panel) y reemplaza el archivo `data/mundo.json`.
4. **Volver a data/mundo.json** borra los cambios locales y recarga el archivo.

Si publicas la página como artifact de claude.ai, usa la base de datos del artifact en lugar del archivo local, y se activan las conversaciones con los agentes, el Concilio y el llamado al Maestro. En la copia local esas conversaciones están apagadas.

## Cómo editar `data/mundo.json`

El archivo tiene siete colecciones. Cada una es un objeto cuyas claves son los identificadores.

| Colección | Qué guarda |
|---|---|
| `lugares` | Los lugares del mapa. |
| `salas` | Los equipos. |
| `agentes` | Los agentes. |
| `proyectos` | Los proyectos que ve el Vigía. |
| `eventos` | La bitácora: cada paso que reporta un agente. |
| `historia` | Entradas antiguas de la Crónica (opcional). |
| `tesoro` | El tesoro del dragón, en `tesoro.dragon`. |

### Un lugar

```json
"valle": {
  "nombre": "Aldaren, el Valle de la Cascada",
  "rol": "Aquí empieza todo viaje",
  "descripcion": "Texto que aparece al pasar el mouse.",
  "tipo": "valle",
  "x": -16, "z": -10,
  "orden": 1,
  "suelo": "#D8CCB0",
  "territorio": "#C9A86A"
}
```

- `tipo` elige el paisaje que se dibuja alrededor: `valle`, `atalaya`, `prados`, `ciudad`, `forja`, `hayedo`, `puerto`, `montana`, `colmenar`, `arboleda` o `cobre`. Puedes inventar otros tipos: se dibujan sin paisaje propio.
- `x` y `z` ubican el lugar en el mapa (oeste a este, norte a sur). Si dos lugares chocan, la página los separa.
- `suelo` es el color de la plaza y `territorio`, el del halo de tierra que la rodea.

### Un equipo

```json
"principal": { "nombre": "Equipo principal", "descripcion": "…", "lugar": "valle", "orden": 1, "color": "#C9A23A" }
```

### Un agente

```json
"guia": {
  "personaje": "Liria, la Guía",
  "nombre": "Función por definir",
  "descripcion": "",
  "sala": "principal",
  "lugar": "valle",
  "fase": "Dirección",
  "actividad": "mapas",
  "estado": "inactivo",
  "tarea": "",
  "voz": "Serena y ordenada.",
  "coordinador": true,
  "apariencia": {
    "raza": "elfo",
    "mujer": true,
    "tunica": "#3E6B5A",
    "piernas": "#2E3E36",
    "pelo": "#2A2018",
    "peloLargo": true,
    "accesorios": ["orejas", "libro"]
  }
}
```

- `personaje` es el nombre que se ve en el mapa; `nombre` es su función.
- `estado`: `trabajando`, `esperando`, `halt`, `listo` o `inactivo`.
- `actividad` es el oficio que tiene a su lado: `escribir`, `leer`, `cartas`, `archivo`, `mapas`, `contar`, `herreria`, `carpinteria`, `cuero`, `telar`, `pintura`, `pociones`, `vigia`, `orbe`, `espejo`, `granja`, `jardin`, `colmenas`, `mineria`, `pesca`, `tiro`, `barco`, `bodega` o `roca`.
- Rango: `coordinador` (estandarte dorado), `liderLugar` (estandarte de color) o `megaCoordinador` con `itinerante` y `recorreTodo` (el Gran Maestro, que camina por todo el mapa).
- `apariencia.raza`: `hombre`, `elfo`, `enano`, `mediano`, `criatura`, `arbol` o `aguila`.
- `apariencia.accesorios`: `barba`, `orejas`, `casco`, `corona`, `sombrero`, `hojas`, `baston`, `espada`, `hacha`, `arco`, `libro`, `anillo`.
- Otros campos de `apariencia`: `piel`, `pelo`, `barba`, `capa` (colores), y `peloLargo`, `mujer`, `falda`, `silla` (silla de ruedas) como `true`.

### Un evento de la bitácora

```json
"20261027T120000Z-guia": { "agente": "guia", "estado": "trabajando", "nota": "Empieza el mapa.", "ts": "2026-10-27T12:00:00Z", "proyecto": "proyecto-de-ejemplo" }
```

Un agente externo (un script, otra herramienta) puede reportar sus pasos escribiendo eventos y actualizando el `estado` del agente.

## Licencia

MIT. Ver [LICENSE](LICENSE). Usa [Three.js](https://threejs.org) (MIT) y fuentes de Google Fonts (SIL Open Font License), que se cargan desde sus CDN.

---

## English

A 3D fantasy world of toy figures that gives your agents a home. Each agent lives in a village, forest or city on the map, with a character, a look and a role, and shows its state with a lantern: working, waiting, HALT, done or idle.

The world ships empty on purpose. It has eleven places and five teams as templates, and three sample agents with no role yet. You fill it in.

### What is in it

- **The map**: eleven places with their own scenery (a valley with a waterfall, a white city, a harbour, a forge, mines, forests), linked by roads and a river.
- **Agents**: figures with a craft, a state lantern and a card. Coordinators carry a banner, and a Grand Master walks the whole map.
- **The editor**: create, edit and delete agents in the page («+ Nuevo agente» in the «Agentes y bitácora» panel).
- **The Watcher's Tower**: your projects, sorted by deadline. Each active project is a ring spinning around the flame.
- **The Chronicle and the activity log**: everything the agents report, by day, with sessions and durations.
- **Brasa, the guardian dragon**: its hoard grows with each finished task (+10 coins) and each project sent or achieved (chests).

The interface is in Spanish.

### How to open it

Browsers do not let a page read `data/mundo.json` when `index.html` is opened with a double click. Serve the folder with any local server:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>. It also works as is on GitHub Pages (Settings → Pages → branch `main`, folder `/`).

It needs an internet connection to load Three.js and the fonts from their CDNs.

### How changes are saved

1. On load, the page reads `data/mundo.json`.
2. What you change in the page (agents, projects, states) is saved in your browser's `localStorage`. Only you see it, in that browser.
3. To keep or share it, use **Descargar mundo.json** (at the bottom of the panel) and replace `data/mundo.json`.
4. **Volver a data/mundo.json** drops the local changes and reloads the file.

If you publish the page as a claude.ai artifact, it uses the artifact's database instead of the local file, and the conversations with agents, the Council and the call to the Master turn on. In the local copy those conversations are off.

### How to edit `data/mundo.json`

The file has seven collections: `lugares` (places), `salas` (teams), `agentes` (agents), `proyectos` (projects), `eventos` (log entries), `historia` (older Chronicle entries, optional) and `tesoro` (the dragon's hoard, in `tesoro.dragon`). Each one is an object keyed by id. The Spanish section above has a full example of each record and the list of valid values:

- a place's `tipo` picks its scenery, and `x` / `z` set its spot on the map;
- an agent's `personaje` is the name on the map and `nombre` its role;
- `estado` is one of `trabajando`, `esperando`, `halt`, `listo`, `inactivo`;
- `actividad` is the craft beside the figure;
- `apariencia` sets the people (`raza`), colours and accessories.

An outside agent (a script, another tool) can report its steps by writing `eventos` and updating the agent's `estado`.

### License

MIT. See [LICENSE](LICENSE). Uses [Three.js](https://threejs.org) (MIT) and Google Fonts (SIL Open Font License), loaded from their CDNs.
