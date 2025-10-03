#!/usr/bin/env bash
#
# pydev.sh — 启动 / 连接 tmux “pydev”，左边编辑，右边监听 + 运行
#

set -euo pipefail

# ========== 配置参数与默认值 ==========
SESSION="pydev"
PROJECT_DIR="$(pwd)"
TARGET="${1:-main.py}"    # 支持通过第一个参数指定目标文件，默认为 main.py
LAYOUT="even"             # 布局（左右均分，目前只一种）

# ========== 验证和准备目标文件 ==========
if [[ ! -f "$TARGET" ]]; then
  if [[ "$TARGET" == "main.py" ]]; then
    # 自动创建示例 main.py
    cat > "$TARGET" <<'PY'
#!/usr/bin/env python3
def main():
    print("Hello from main.py. Edit me and save to rerun automatically.")
if __name__ == "__main__":
    main()
PY
    chmod +x "$TARGET"
    echo "已创建示例文件：$TARGET"
  else
    echo "错误：指定的目标文件不存在：$TARGET"
    exit 1
  fi
fi

# ========== 检查依赖 ==========
if ! command -v tmux >/dev/null 2>&1; then
  echo "错误：未安装 tmux"
  exit 1
fi

if ! command -v vim >/dev/null 2>&1; then
  # vim 可选，这里假设你用 vim
  echo "警告：未安装 vim，左边 pane 无法启动编辑器"
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "错误：未安装 python3"
  exit 1
fi
if ! command -v entr >/dev/null 2>&1; then
  echo "错误：未安装 entr，无法监听文件变动"
  exit 1
fi

# ========== 如果 session 已存在则 attach ==========
if tmux has-session -t "$SESSION" 2>/dev/null; then
  exec tmux attach -t "$SESSION"
fi

# ========== 创建 tmux 会话和窗格 ==========
tmux new-session -d -s "$SESSION" -c "$PROJECT_DIR"
tmux split-window -h -l 15 -t "$SESSION":0

# 左 pane：打开 Vim 编辑目标文件
tmux send-keys -t "$SESSION":0.0 "vim \"$TARGET\"" C-m

# 右 pane：监听 *.py 变动并运行目标脚本
tmux send-keys -t "$SESSION":0.1 "find . -name '*.py' | entr -cd python3 \"$TARGET\"" C-m

# 焦点回到左 pane（方便开始编辑）
tmux select-pane -t "$SESSION":0.0

# 最后 attach 到 tmux 会话
tmux attach -t "$SESSION"
