import os
import re

CONFIG_PATH = "config.toml"
CONTENT_DIR = "content"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config_content = f.read()

# Витягуємо всі типи готелів
types = set(re.findall(r'type\s*=\s*"([^"]+)"', config_content))

# Витягуємо пункти меню
menu_items = re.findall(r'\[\[menu\.main\]\](.*?)\n(?=\[\[|$)', config_content, re.DOTALL)

for item in menu_items:
    url_match = re.search(r'url\s*=\s*["\']([^"\']+)["\']', item)
    name_match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', item)

    if url_match and name_match:
        url = url_match.group(1).strip("/")
        title = name_match.group(1)

        # Генеруємо файл ТІЛЬКИ якщо цей URL є типом готелю
        if url in types:
            file_path = os.path.join(CONTENT_DIR, f"{url}.md")
            os.makedirs(CONTENT_DIR, exist_ok=True)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"""---
title: "{title}"
layout: "hotels"
type: "page"
---
""")

print("✅ Тільки готельні категорії згенеровані 🎯")
