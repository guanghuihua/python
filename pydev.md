# pydev: 基于 tmux + Vim 的 Python 开发环境说明文档

本说明文档介绍如何使用 `tmux` 搭建一个名为 **pydev** 的开发环境，实现以下目标：

1. 创建并进入一个名为 `pydev` 的 tmux 会话。  
2. 左侧 pane 使用 **Vim** 编辑 Python 文件。  
3. 右侧 pane 自动监听、运行、调试 Python 文件。  
4. 调试完成后，退出两个 pane。  
5. 最终退出并关闭 `pydev` 会话。  

---

## 0. 依赖工具

在开始之前，请确保系统安装了以下工具：

- `tmux` —— 终端复用器
- `vim` —— 编辑器（可用 `nvim` 替代）
- `python3` —— Python 解释器
- `entr` —— 文件监听工具（根据文件修改自动运行命令）

### 安装命令（Ubuntu/Debian）

```bash
sudo apt update
sudo apt install -y tmux vim python3 python3-pip entr
pip3 install --user pytest   # 可选，用于测试
````

macOS: `brew install tmux vim entr`
Fedora: `sudo dnf install tmux vim python3 entr`
Arch: `sudo pacman -S tmux vim python entr`

---

## 1. 一键启动脚本

在项目根目录下创建脚本 `pydev.sh`：

```bash
!/usr/bin/env bash

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

```

---

## 2. 使用方法

### 启动 pydev 会话

```bash
./pydev.sh
```

* 左 pane：Vim 打开 `main.py`，可直接编辑。
* 右 pane：自动监听所有 Python 文件，每次保存都会重新运行。

### 编辑代码

在左 pane 中用 Vim 编辑：

* 保存：`:w`
* 退出：`:q` 或 `:qa`

### 运行调试

* 每次保存后，右 pane 会自动重新运行代码。
* 也可以把 `entr` 命令替换为 `pytest`，让右 pane 运行测试。

### 退出 pane

* 左 pane (Vim)：`:q`
* 右 pane (监听器)：`Ctrl-C` 然后输入 `exit`

### 退出 tmux 会话

在 tmux 外部：

```bash
tmux kill-session -t pydev
```

---

## 3. 手动操作（不使用脚本）

如果你想手动执行：

```bash
# 创建并进入会话
tmux new-session -s pydev
# 分屏
Ctrl-b %          # 水平分屏
# 左边：vim main.py
# 右边：find . -name "*.py" | entr -cd python3 main.py
```

退出方式同上。

---

## 4. 常用命令速查

* `tmux new -s pydev` —— 新建会话
* `tmux ls` —— 查看会话列表
* `tmux attach -t pydev` —— 重新进入会话
* `tmux kill-session -t pydev` —— 关闭会话
* `Ctrl-b d` —— 暂时退出（保持后台运行）

---

## 5. 总结

通过本说明文档，你可以：

* 一键启动一个 **pydev** 开发环境，左边写代码，右边自动运行。
* 快速调试和测试 Python 程序。
* 清晰退出和关闭会话，避免残留进程。

这是一个高效的 **终端内开发工作流**，特别适合 Python 项目。


