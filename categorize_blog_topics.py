import re
import os
from datetime import datetime

# Define categories and their keywords
CATEGORIES = {
    "Performance Tuning & Monitoring": [
        "sql", "tune", "tuning", "optimiz", "hint", "plan", "wait", "event", "ash", "awr", 
        "monitor", "trace", "stat", "advisor", "index", "join", "sort", "hash", "loop", 
        "scan", "bloom", "cardinality", "selectivity", "histogram", "profile", "baseline",
        "lock", "latch", "enqueue", "contention", "metric", "top", "report"
    ],
    "Backup & Recovery": [
        "backup", "restore", "recover", "rman", "flashback", "pump", "export", "import", 
        "dp", "dump", "undo", "redo", "archive", "logminer", "clone", "migrate", "migration"
    ],
    "High Availability (RAC & ASM)": [
        "rac", "asm", "cluster", "crs", "vote", "ocr", "vip", "scan", "interconnect", 
        "grid", "exadata", "dataguard", "standby", "switchover", "failover"
    ],
    "Architecture & Internals": [
        "architect", "internal", "memory", "sga", "pga", "buffer", "cache", "process", 
        "background", "lgwr", "dbwr", "ckpt", "smon", "pmon", "block", "header", "segment", 
        "extent", "rowid", "chain", "migrate", "compress", "structure"
    ],
    "Database Administration": [
        "admin", "user", "role", "privilege", "grant", "revoke", "security", "audit", 
        "parameter", "spfile", "pfile", "dictionary", "view", "table", "tablespace", 
        "datafile", "temp", "shrink", "resize", "move", "ddl", "create", "alter", "drop",
        "partition", "constraint", "sequence", "synonym", "link", "dblink", "job", "scheduler"
    ],
    "Development (PL/SQL & SQL)": [
        "pl/sql", "plsql", "procedure", "function", "trigger", "package", "type", "var", 
        "loop", "cursor", "exception", "pragma", "lob", "xml", "json", "regexp", "string", 
        "date", "math", "convert", "analytic", "window", "model", "pivot", "rollup", "cube"
    ]
}

UNCATEGORIZED = "Others / General"

def categorize_topic(topic):
    topic_lower = topic.lower()
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in topic_lower:
                return category
    return UNCATEGORIZED

def generate_mdx(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Sort lines alphabetically? Or assume the user's order is meaningful?
    # User's file seems sorted alphabetically/hangul.
    # Grouping them will break the sort order, but that's the point of categorization.
    
    grouped_topics = {cat: [] for cat in CATEGORIES}
    grouped_topics[UNCATEGORIZED] = []

    for line in lines:
        if len(line) < 2: continue # Skip single chars like headers A, B, C if strictly just headers
        # Filter out simple alphabetical headers if desired, but user might want them.
        # Let's keep everything that looks like a topic.
        category = categorize_topic(line)
        grouped_topics[category].append(line)

    # Generate MDX Content
    today = datetime.now().strftime('%Y-%m-%d')
    mdx_content = f"""---
title: Oracle Database Master Study Guide
date: '{today}'
tags: ['Oracle', 'Available', 'Study', 'Roadmap', 'TOC']
draft: false
summary: Oracle 데이터베이스 학습을 위한 마스터 로드맵입니다. {len(lines)}여 개의 주제를 카테고리별로 분류하여 정리했습니다. 각 항목을 클릭하여 학습 상태를 체크하고 내용을 채워갈 수 있습니다.
---

# Oracle Database Master Study RoadMap

이 문서는 Oracle 데이터베이스의 방대한 지식 체계를 정리한 마스터 인덱스입니다.
지속적으로 내용을 업데이트하고 테스트 결과를 링크하여 나만의 지식 베이스를 구축할 예정입니다.

<TOCInline toc={{props.toc}} exclude="Introduction" />

"""

    for category, topics in grouped_topics.items():
        if not topics: continue
        
        mdx_content += f"## {category}\n\n"
        for topic in topics:
            # Checkbox format [ ] Topic
            mdx_content += f"- [ ] **{topic}**\n"
        mdx_content += "\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(mdx_content)
    
    print(f"Successfully generated MDX at: {output_file}")

if __name__ == "__main__":
    input_path = r"c:\Users\한병헌\Desktop\internal\note\test.txt"
    output_path = r"c:\Users\한병헌\Desktop\internal\note\tech-blog\data\blog\oracle-study-roadmap.mdx"
    generate_mdx(input_path, output_path)
