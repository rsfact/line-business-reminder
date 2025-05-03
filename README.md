# LINE Business Reminder

## 概要

LINEの公式アカウントに届いたメッセージへの返信漏れを防ぐための仕組み

## 環境構築

```bash
python -m venv .venv
source .venv/Script/activate

pip install -r requirements.txt
```

## 開発環境

```bash
source .venv/Script/activate
python main.py
```

```bash
ngrok http 8000
```

-> WebhookURLを登録
https://manager.line.biz/account/

例: https://3035-14-224-191-227.ngrok-free.app/api/webhook/message

## 本番環境

Linuxサーバ想定

```bash
cd ~ && \
git clone http://github.com/rsfact/line-business-reminder && \
cd line-business-reminder
```

```bash
sudo apt update && \
sudo apt upgrade -y && \
sudo apt install python3.12-venv -y && \
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install -r requirements.txt && \
cp .env.example .env
vi .env
```

```bash
sudo tee /etc/systemd/system/line-business-reminder.service << 'EOF'
[Unit]
Description=LINE Business Reminder
After=network-online.target nginx.service
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=/home/user/line-business-reminder
ExecStart=/bin/bash -c 'source /home/user/line-business-reminder/.venv/bin/activate && cd /home/user/line-business-reminder && python main.py'
Restart=on-failure
RestartSec=10s
TimeoutStartSec=90

[Install]
WantedBy=multi-user.target
EOF
```

```bash
sudo systemctl daemon-reload && \
sudo systemctl enable line-business-reminder.service && \
sudo systemctl is-enabled line-business-reminder.service && \
sudo systemctl start line-business-reminder.service
```

Nginx

```bash
...
..
.
location /line-business-reminder/ {
    proxy_pass http://localhost:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
...
..
.
```
