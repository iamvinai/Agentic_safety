# SecureDesk

SecureDesk is a small Python demo: Gemini handles synthetic support tickets,
and Radware inspects the request, response, and tool calls out of path.

## Run it

```bash
source .venv/bin/activate
streamlit run app/dashboard.py
```

Add these values to `.env` first:

```text
RADWARE_OUT_OF_PATH_API_KEY=...
GOOGLE_API_KEY=...
```

The app uses `gemini-3.6-flash` by default because that is the model tested with
the current LangChain tool-calling path.

## What to try

- Run the benign ticket and read the summary.
- Select the poisoned ticket and enable red-team mode.
- Confirm Radware blocks the simulated `shell_exec` call before it runs.

The shell tool is only a recorder. It never runs a command or reads a real
file.

## Code layout

- `app/agent.py` — the `SecureDesk` backend service.
- `app/ticketing.py` — two synthetic tickets and two safe tools.
- `app/dashboard.py` — the Streamlit UI.
- `connector/` — the Radware connector repository.

Run the tests with:

```bash
.venv/bin/pytest -q
```
