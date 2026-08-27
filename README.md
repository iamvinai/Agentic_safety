# SecureDesk

SecureDesk is a small Python demo: Gemini handles synthetic support tickets,
and Radware inspects the request, response, and tool calls out of path.

## Set it up

Run these commands from a normal project folder (not the macOS Trash):

```bash
git clone --recurse-submodules https://github.com/iamvinai/Agentic_safety.git
cd Agentic_safety
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pip install -e connector
cp .env.example .env
```

If `.env` already exists, skip the `cp` command so you do not overwrite it.

Open `.env` and add your keys:

```text
RADWARE_OUT_OF_PATH_API_KEY=...
GOOGLE_API_KEY=...
```

Then start the dashboard:

```bash
python3 -m streamlit run app/dashboard.py
```

Using `python3 -m streamlit` makes sure Streamlit runs from the virtual
environment instead of the system Python.

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
