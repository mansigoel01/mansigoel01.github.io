import os
import shutil

dir_path = '_teaching'
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
os.makedirs(dir_path)

teachings = [
    {
        "title": "Computational Gastronomy",
        "date": "2024-08-01 00:01:00 +0800",
        "pub": "IIIT-Delhi",
        "pub_date": "Monsoon 21, 22, 23, 24",
        "abstract": "Assisted in coursework, project evaluations, and bridging the gap between food science and computation.",
        "authors": ["Mansi Goel (Teaching Assistant)"]
    },
    {
        "title": "Analysis of Design and Algorithms",
        "date": "2023-01-01 00:01:00 +0800",
        "pub": "IIIT-Delhi",
        "pub_date": "Winter 23",
        "abstract": "Guided students through complex algorithmic design and problem-solving techniques.",
        "authors": ["Mansi Goel (Teaching Assistant)"]
    },
    {
        "title": "Network Science",
        "date": "2024-01-01 00:01:00 +0800",
        "pub": "IIIT-Delhi",
        "pub_date": "Winter 21, 22, 24",
        "abstract": "Supported the instruction of network theory, data structures, and practical applications in social networks and biological systems.",
        "authors": ["Mansi Goel (Teaching Assistant)"]
    }
]

for i, t in enumerate(teachings):
    filename = os.path.join('_teaching', f"teaching-{i+1}.md")
    authors_yaml = "\n".join([f"  - {a}" for a in t['authors']])
    content = f"""---
title: "{t['title']}"
date: {t['date']}
pub: "{t['pub']}"
pub_date: "{t['pub_date']}"
abstract: >-
  {t['abstract']}
authors:
{authors_yaml}
---
"""
    with open(filename, 'w') as f:
        f.write(content)
