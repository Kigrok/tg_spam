# Telegram Spam Bot "TGSpam"

![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![\[Telegram\] pyrogram live](https://img.shields.io/badge/telegram-pyrogram-red.svg?style=flat-square)

![Banner](https://lh3.googleusercontent.com/u/0/drive-viewer/AJc5JmRKrWswxARv8xsg_01v5fkWu5HU9mA8JJCesobbNCn7_eb5gpKUFHsYCtnpyqk0uCfTJ-L1zpgSDcnCumV7aF603ED-=w1366-h663)

### _The bot collects chat participants (no more than 10,000 people) and sends them a message._

---

## Install 

### Clone repository
```sh
git clone https://github.com/Kigrok/tg_spam.git
cd tg_spam
```

### Installing the virtual environment and packages

```sh
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

### Add to `config.yml` telegram account
1.  Log in [Telegram](https://my.telegram.org/auth).
2.  Create App.
3.  Add to config file `tg_spam/data/config.yml` 'api_id', 'api_hash', 'app_title'.

### Add message and media
1. Add media in `tg_spam/data` (image or video).
    > If just a message, don't add anything.
2. Add message in `tg_spam/data/message.py`.

----

# Start

```sh
python3 spam.py -c <telegram chat (chat name or link)>
```
