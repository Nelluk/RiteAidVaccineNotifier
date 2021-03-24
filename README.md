# RiteAidVaccineNotifier
 Notifier for Rite Aid COVID-19 vaccine appointment slots. Primarily uses MacOS desktop notifications, but can also push to mobile (iOS or Android) with the Pushsafer app (free for the first 50 notifications).

# Installation instructions
- `git clone <repo URL>`
- `python3 -m venv /new/repo/directory`
- `cd /new/repo/directory`
- `source bin/activate`
- `pip install -r requirements.txt`
- `cp config_EXAMPLE.py config.py`
- Edit `config.py` with your preferred store numbers and other settings
- `python3 notify.py`
