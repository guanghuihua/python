# Create the repo first on GitHub, then add files via browser
# GitHub → “New repository” → create it → “Uploading an existing file” → drag-and-drop files → “Commit changes”.
# This is fine for small projects; for ongoing work, use Git locally (Option A).

# First-time setup tips (one-time)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"


# SSH setup (optional but convenient):

ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub
# copy to GitHub → Settings → SSH and GPG keys

# Nice to include before the first commit
# README
echo "# Project Title" > README.md

# .gitignore (Python example)
echo -e "__pycache__/\n*.pyc\n.venv/\n.env" > .gitignore
# C++ example
echo -e "build/\n*.o\n*.out\n*.exe\nCMakeFiles/\nCMakeCache.txt" > .gitignore

# License (MIT)
cat > LICENSE <<'EOF'
MIT License
<your name and year>
EOF