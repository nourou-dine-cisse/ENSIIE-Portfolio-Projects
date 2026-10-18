# SPIELBERG Core Data Platform POC

POC local FastAPI + Stitch pour démontrer une plateforme data staffing/projets à partir de Teamium et de mocks locaux.

## Principes de sécurité

- Aucun scraping Internet. L’assistant et les pages ne travaillent que sur les données locales du repo.
- Aucun accès direct base de données. Toute lecture passe par les endpoints FastAPI gouvernés.
- `SAFE_MODE=true` par défaut.
- En `SAFE_MODE`, aucune PII brute n’est renvoyée par le chat ni par les nouvelles vues ressources/planning/projets.
- Si `ENABLE_OPENAI=true`, OpenAI ne reçoit jamais de lignes brutes Teamium ni de noms/emails. Seulement des sorties d’outils sécurisées et agrégées.

## Structure

```text
SPIELBERG_POC/
├── backend/
│   ├── data_loader.py
│   ├── llm.py
│   ├── main.py
│   ├── security.py
│   ├── services.py
│   └── requirements.txt
├── data/
│   ├── Booking-Personal.xlsx
│   └── mocks/
│       ├── altair.json
│       ├── altair_projects.json
│       ├── oneclick.json
│       ├── oneclick_absences.json
│       ├── oneclick_people.json
│       └── roar.json
│       └── roar_timesheets.json
├── frontend/
│   ├── analytics.html
│   ├── assistant.html
│   ├── index.html
│   ├── planning.html
│   ├── projects.html
│   ├── timesheets.html
│   ├── assets/
│   └── static/
├── .env.example
├── Dockerfile
└── docker-compose.yml
```

## Variables d’environnement

Copiez `.env.example` vers `.env` à la racine du projet si vous voulez personnaliser le lancement.

```env
SAFE_MODE=true
ENABLE_OPENAI=false
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini
BASIC_AUTH_USER=
BASIC_AUTH_PASS=
DEMO_MODE_DEFAULT=false
INTERNAL_DEMO_NAMES=false
```

### Notes env

- `SAFE_MODE=true` : pseudonymisation `EMP-XXXXXXXX` et blocage des réponses nominatives.
- `ENABLE_OPENAI=false` : mode 100% local, déterministe, sans dépendance LLM externe.
- `BASIC_AUTH_USER` + `BASIC_AUTH_PASS` : si les deux sont définis, tout est protégé en Basic Auth sauf `GET /api/health`.
- `DEMO_MODE_DEFAULT=true|false` : état initial du toggle `Demo Mode` côté UI.
- `INTERNAL_DEMO_NAMES=true|false` : active un mode interne contrôlé pour afficher `display_name` dans l’UI tout en conservant `employee_key` pour les jointures.

## Run avec Docker

Pré-requis : Docker Desktop ou OrbStack.

```bash
cd ~/DEV/SPIELBERG/SPIELBERG_POC
docker compose up --build
```

Puis ouvrez `http://localhost:8000`.

## Run avec venv

Pré-requis : Python 3.11+.

```bash
cd ~/DEV/SPIELBERG/SPIELBERG_POC
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload --port 8000
```

Puis ouvrez `http://localhost:8000`.

## Pages

- `/` : home Stitch réaligné, avec cartes `Booking / FINANCIALS / TEAM / INTELLIGENCE / ADMIN / ACCOUNT / AUTOMATION` et redirections de démo sobres
- `/planning` : vue planning Stitch réalignée avec filtres de dates, échelle `D / W / M`, overlay absences OneClick et modal projet gouverné
- `/projects` : catalogue projets + détail staffing enrichi avec BF Altair, actuals rOar et signaux OneClick
- `/analytics` : portefeuille global ou vue client, avec dates éditables, sold amount, cost budget, actual hours, estimated margin et watchlist BF
- `/timesheets` : helper hebdo rOar à partir du planning Teamium, avec total heures, warnings et message helper only
- `/assistant` : assistant outillé / MCP-like avec prompts guidés et bannière `MCP-ready local tool routing on governed internal demo data`
- `Demo Mode` : toggle global qui fige la plage de dates, le BF vedette, le salarié démo et l’export PDF gouverné sans PII

## Endpoints

### Existants conservés

- `GET /api/health`
- `GET /api/kpis/projects`
- `GET /api/kpis/people`
- `GET /api/bookings`
- `POST /api/chat`

### Nouveaux endpoints gouvernés

- `GET /api/kpis/summary`
- `GET /api/resources`
- `GET /api/projects`
- `GET /api/projects/{id}`
- `GET /api/planning`
- `GET /api/analytics`
- `GET /api/altair/projects`
- `GET /api/altair/projects/{bf_id}`
- `GET /api/roar/timesheets`
- `GET /api/oneclick/absences`
- `GET /api/people`
- `GET /api/availability`
- `GET /api/timesheets/helper`
- `GET /api/analytics/client-risk`
- `GET /api/demo/config`
- `GET /api/export/snapshot.pdf`
- `GET /api/governance/sources`

## Assistant / MCP-like

Le chat appelle des tools Python internes sur le dataset déjà chargé :

- `tool_find_available_resources(criteria)`
- `tool_find_people_who_worked_for_client(client)`
- `tool_project_budget_vs_actual(bf_id, range)`
- `tool_weekly_timesheet_helper(employee_key, range)`
- `tool_client_project_risk(client, range)`

Chaque réponse renvoie :

- un résumé humain dans `answer`
- le tool appelé dans `tool_used`
- un résumé de raisonnement dans `reasoning_summary`
- une liste de preuves gouvernées dans `evidence`
- une structure `data.cards` + `data.table` pour le rendu UI
- une section `data.raw` pour la traçabilité gouvernée côté backend

Par défaut, il répond localement. Avec `ENABLE_OPENAI=true`, il ne transmet qu’une sortie sécurisée des tools internes.

En `Demo Mode`, l’Assistant propose 3 prompts guidés avec action `Copy demo prompt` :

- `Staffing`
- `Risk Lens`
- `Timesheet`

## Mocks dérivés

Les fichiers `Altair / rOar / OneClick` sont régénérés au startup à partir de `data/Booking-Personal.xlsx`.

- `altair_projects.json` : BF / budgets / estimate / work codes / vendors
- `roar_timesheets.json` : timesheets journaliers dérivés des bookings avec `source` et `confidence_note`
- `oneclick_people.json` : core people fields pseudonymisés
- `oneclick_absences.json` : absences locales cohérentes avec les fenêtres de staffing, enrichies avec `source` et `confidence_note`

Les champs de démonstration ajoutés pour lundi incluent notamment :

- `risk_level`
- `budget_variance_pct`
- `absence_overlap`
- `source=teamium_derived`
- `confidence_note`

Le master reste Teamium. Les IDs projet et BF sont stables et cohérents entre les mocks.

## Notes PII

`data/Booking-Personal.xlsx` contient des données nominatives RH réelles.

- Ne publiez pas ce repo tel quel.
- Ne désactivez `SAFE_MODE` que dans un contexte maîtrisé.
- Les pages Home/Planning/Projects/Analytics/Assistant sont conçues pour une démo safe par défaut.
- `INTERNAL_DEMO_NAMES=true` est réservé à une démo interne contrôlée ; il n’enlève pas les `employee_key` ni la pseudonymisation métier côté backend.

## Script de démo 2-3 minutes

1. Ouvrir `/`.
   Expliquer que la démo repose sur `Teamium real extract + derived Altair/rOar/OneClick demo datasets`, en `SAFE_MODE`.
2. Cliquer `Find available people`.
   Montrer le shortlist gouverné pour la semaine figée : free days, availability %, historique Renault, absence overlap, overload.
3. Cliquer `Generate weekly timesheet help`.
   Montrer comment le planning Teamium devient une proposition rOar hebdo avec BF, work codes, total heures et warnings, sans writeback.
4. Ouvrir `/analytics?client=COTY`.
   Montrer la vue portefeuille client : sold amount, cost budget, actual hours to date, estimated margin et top BF à surveiller.
5. Aller sur `/assistant`.
   Lancer successivement les 3 prompts guidés pour montrer que l’assistant appelle des tools internes gouvernés, sans scraping et sans PII.
6. Si utile, cliquer `Export snapshot (PDF)`.
   Montrer qu’on peut sortir un résumé gouverné sans noms ni emails pour le BF courant.
