# daily-quotes — experimental quote automation

Historical Python scripts for selecting quotes, working with CSV/Excel data, querying Wikipedia, and experimenting with an email-delivery workflow.

## Source inventory

- `main.py` — imports pandas, configuration parsing, mail-related modules, Wikipedia API tooling, and date/random helpers; inspect its actual execution flow before running.
- `wiki.py` — simple Wikipedia API experiment.
- `quotes.csv`, `quotes.xlsx`, `used.csv`, `run.bat` — quote data/output and a Windows runner.
- `english-word-list-*.csv` — supporting lexical data.
- `main/` — additional project files.
- Tracked PDF documents and **`Accounts_History.csv`** — must be classified before publishing, mirroring, or indexing; their contents were **not** inspected in this README audit.

## Safe evaluation

This is not a verified scheduled email service. Do **not** enable live SMTP sending or task scheduling until the source is reviewed for intended recipients, credential handling, deduplication, retries, and rate limits. Test on synthetic quote records with a fake mail transport. Wikipedia/provider availability and schemas can change.

**Privacy caution:** a filename resembling account history in a public repository is a reason to inspect it privately, **not** evidence that it contains sensitive financial data. If it does, remove/replace active copies, assess Git history and mirrors, and follow any appropriate disclosure/incident process.

There is no locked dependency manifest or verified test command. No data files, mailboxes, third-party APIs, or schedulers were used by this documentation update.
