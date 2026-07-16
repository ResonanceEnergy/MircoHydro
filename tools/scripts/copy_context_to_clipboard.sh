
#!/bin/zsh
python3 scripts/context_for_chat.py --out artifacts/chat_context/CHAT_CONTEXT.md
cat artifacts/chat_context/CHAT_CONTEXT.md | pbcopy
echo "Copied artifacts/chat_context/CHAT_CONTEXT.md to clipboard."

