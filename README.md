# SecureDesk

SecureDesk is a small Python demo: Gemini handles synthetic support tickets,
and Radware inspects the request, response, and tool calls out of path.

## Set it up

Run these commands from a normal project folder (not the macOS Trash):

```bash
git clone --recurse-submodules https://github.com/iamvinai/Agentic_safety.git
cd Agentic_safety
```

The Radware connector needs Python 3.10 or newer. Python 3.11 is a safe
choice on macOS:

```bash
brew install python@3.11
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e connector
cp .env.example .env
```

Check the version inside the environment with `python --version`; it should
show 3.10 or newer.

If `.env` already exists, skip the `cp` command so you do not overwrite it.

Open `.env` and add your keys:

```text
RADWARE_OUT_OF_PATH_API_KEY=...
GOOGLE_API_KEY=...
```

Then start the dashboard:

```bash
python -m streamlit run app/dashboard.py
```

Using `python -m ...` makes sure the commands use the virtual environment.

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
