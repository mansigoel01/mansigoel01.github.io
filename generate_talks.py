import os
import shutil

dir_path = '_talks'
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
os.makedirs(dir_path)

talks = [
    {
        "title": "Deep Learning Based Named Entity Recognition Models for Recipes",
        "date": "2024-05-01 00:01:00 +0800",
        "pub": "LREC COLING, Turin, Italy",
        "pub_date": "2024",
        "abstract": "Presented research findings on NER models for recipe texts.",
        "authors": ["Mansi Goel (Presenter)"]
    },
    {
        "title": "Dish Detection in Indian Food Platters: A Computational Framework for Diet Management",
        "date": "2023-11-01 00:01:00 +0800",
        "pub": "8th IEEE International Conference on Computer Vision and Image Processing (CVIP), IIT-Jammu, India",
        "pub_date": "2023",
        "abstract": "Presented computational frameworks for analyzing Indian food platters.",
        "authors": ["Mansi Goel (Presenter)"]
    },
    {
        "title": "Tech Lead Presentation for Foodoscope Technologies",
        "date": "2023-08-01 00:01:00 +0800",
        "pub": "Symposium on Computational Gastronomy, IIIT-Delhi, India",
        "pub_date": "2023",
        "abstract": "Represented Foodoscope Technologies Private Limited as Tech Lead.",
        "authors": ["Mansi Goel (Presenter)"]
    },
    {
        "title": "Can a Computer Think like a Chef?",
        "date": "2022-09-01 00:01:00 +0800",
        "pub": "Symposium on Computational Gastronomy, IIIT-Delhi, India",
        "pub_date": "2022",
        "abstract": "Delivered a talk exploring the cognitive and computational parallels of recipe creation.",
        "authors": ["Mansi Goel (Presenter)"]
    },
    {
        "title": "Ratatouille: A Tool for Novel Recipe Generation",
        "date": "2022-08-01 00:01:00 +0800",
        "pub": "38th IEEE International Conference on Data Engineering Workshops (DECOR2022), Malaysia (Virtual)",
        "pub_date": "2022",
        "abstract": "Presented generative models for creating novel cultural recipes.",
        "authors": ["Mansi Goel (Presenter)"]
    },
    {
        "title": "Research Posters Showcase",
        "date": "2022-04-01 00:01:00 +0800",
        "pub": "Research Innovation and Incubation Showcase (RIISE), IIIT-Delhi, India",
        "pub_date": "2022",
        "abstract": "Presented research posters at the annual RIISE symposium.",
        "authors": ["Mansi Goel (Presenter)"]
    }
]

for i, t in enumerate(talks):
    filename = os.path.join(dir_path, f"talk-{i+1}.md")
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
