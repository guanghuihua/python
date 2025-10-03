#!/usr/bin/env bash

SESSION="pydev"
PROJECT_DIR="$(pwd)"
TARGET="${1:-main.py}"  # 如果没有参数，默认为 main.py

# 验证 TARGET 文件是否存在
if [[ ! -f "$TARGET" ]]; then
  echo "错误：指定的文件不存在：$TARGET"
  exit 1
fi

# 如果 TARGET 是 main.py 且该文件不存在，则创建一个示例文件
if [[ "$TARGET" == "main.py" && ! -f "$TARGET" ]]; then
  cat > "$TARGET" <<'PY'
#!/usr/bin/env python3
def main():
    print("Hello from main.py. Edit me and save to rerun automatically.")
if __name__ == "__main__":
    main()
PY
  chmod +x "$TARGET"
  echo "已创建示例文件：$TARGET"
fi

# 如果会话已存在则直接进入
if tmux has-session -t $SESSION 2>/dev/null; then
  exec tmux attach -t $SESSION
fi

# 创建新的 tmux 会话并进入工作目录
tmux new-session -d -s $SESSION -c "$PROJECT_DIR"

# 水平分屏创建第二个窗格
tmux split-window -h -l 15 -t $SESSION:0

# 在第一个窗格中打开 vim
tmux send-keys -t $SESSION:0.0 "vim $TARGET" C-m

# 在第二个窗格中使用 entr 监听文件变化并执行
tmux send-keys -t $SESSION:0.1 "find . -name '*.py' | entr -cd python3 $TARGET" C-m

# 选择第一个窗格
tmux select-pane -t $SESSION:0.0

# 附加到会话
tmux attach -t $SESSION
