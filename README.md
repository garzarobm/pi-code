# pi-code

## Python setup (virtualenv)

Recent Raspberry Pi OS (Bookworm+) blocks system-wide `pip install`
(PEP 668), so use a virtual environment:

```bash
# one-time system packages
sudo apt update
sudo apt install -y python3-venv python3-pip ffmpeg

# create and activate the venv (from the repo root)
python3 -m venv .venv
source .venv/bin/activate

# core dependencies (webdav/nextcloud upload, recording, numpy/opencv)
pip install --upgrade pip
pip install -r requirements.txt
```

Extras, depending on what you're running:

```bash
# on the Pi itself (GPIO scripts) — adds RPi.GPIO
pip install -r requirements-pi.txt
```

```bash
# machine-learning/run.py — adds tensorflow (on a Pi, use tflite-runtime instead)
pip install -r requirements-ml.txt
```

Camera support on the Pi comes from apt, not pip
(`sudo apt install -y python3-picamera2`); if you need it inside the venv,
create the venv with `python3 -m venv --system-site-packages .venv` so the
apt-installed module is visible.

Reactivate later with `source .venv/bin/activate`; leave with `deactivate`.
A full pinned freeze from a working Pi 4 image lives at
`rpi/pi4/recording/requirements.txt` if you need exact versions.

## Credentials

No passwords live in this repo — the upload scripts read them from
environment variables. Set the ones you need before running
(e.g. in `~/.profile`, or an `Environment=` line in a systemd service):

```bash
# Nextcloud (rpi/pi4/main/upload_files.py, rpi/pi4/nextcloud_client/)
export NEXTCLOUD_USER="youruser"
export NEXTCLOUD_PASSWORD="yourpassword"
export NEXTCLOUD_PUBLIC_LINK="https://your-server/nextcloud/index.php/s/XXXXXXXX"
```

```bash
# easywebdav (rpi/pi4/main/easywebdav.py)
export WEBDAV_HOST="webdav.your-server.com"
export WEBDAV_USER="youruser"
export WEBDAV_PASSWORD="yourpassword"
```

```bash
# webdavclient3 (webdav/run_webdav3.py)
export WEBDAV_HOSTNAME="https://your-server/nextcloud/remote.php/dav/files/youruser/"
export WEBDAV_LOGIN="youruser"
export WEBDAV_PASSWORD="yourpassword"
```

## Dependencies
a.ffmpgeg
I. To install ffmpeg
sudo apt-get install ffmpeg

record.py:
	record with camera in x second clips. omit audio, subtitles and data.

using 

