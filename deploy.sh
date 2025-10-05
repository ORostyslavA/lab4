#!/bin/bash
set -e
cd /home/ubuntu/lab4

# Ensure branch matches what GH pushes (update the branch name as needed)
BRANCH="lab-ec2"

# --- Step 1: Backup app.yml if it exists ---
#if [ -f "flask_project/app/config/app.yml" ]; then
# echo "Backing up app.yml..."
#  cp flask_project/app/config/app.yml /tmp/app.yml.backup
#fi

# --- Step 2: Pull latest code safely ---
echo "Updating code..."
git fetch origin
git stash  true
git checkout $BRANCH
git pull origin $BRANCH

# --- Step 3: Restore app.yml if needed ---
#if [ -f "/tmp/app.yml.backup" ]; then
#  echo "Restoring app.yml..."
#  mv /tmp/app.yml.backup flask_project/app/config/app.yml
#fi

# --- Step 4: Ensure virtual environment and dependencies ---
cd /home/ubuntu
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate
cd /home/ubuntu/lab4/app
pip install --upgrade pip
pip install -r requirements.txt

# --- Step 5: Restart Flask app ---
#echo "Restarting Flask app..."
#pkill -f "python3 app.py"  true
#nohup python3 app.py > app.log 2>&1 &

echo "✅ Deployment complete!"
