import os
import shutil

# Remove existing publications and news/showcase dummies
for d in ['_publications', '_news', '_showcase']:
    dir_path = os.path.join('.', d)
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.makedirs(dir_path)

publications = [
    {
        "title": "ToxinPredictor: Computational Models To Predict the Toxicity of Molecules",
        "date": "2024-12-01 00:01:00 +0800",
        "pub": "Chemosphere",
        "url": "https://pubmed.ncbi.nlm.nih.gov/39701316/",
        "authors": ["Mansi Goel", "Arav Amawate", "Angadjeet Singh", "Ganesh Bagler"],
        "pub_date": "2024",
        "selected": "true",
        "abstract": "Computational Models To Predict the Toxicity of Molecules."
    },
    {
        "title": "FlavorDB2: An Updated Database of Flavor Molecules",
        "date": "2024-10-01 00:01:00 +0800",
        "pub": "Journal of Food Science",
        "url": "https://ift.onlinelibrary.wiley.com/doi/full/10.1111/1750-3841.17298",
        "authors": ["Mansi Goel", "Nishant Grover", "Devansh Batra", "Neelansh Garg", "Rudraksh Tuwani", "Apuroop Sethupathy", "Ganesh Bagler"],
        "pub_date": "2024",
        "selected": "true",
        "abstract": "An Updated Database of Flavor Molecules."
    },
    {
        "title": "Cultural Context Shapes The Carbon Footprints Of Recipes",
        "date": "2024-09-01 00:01:00 +0800",
        "pub": "International Journal of Gastronomy and Food Science",
        "url": "https://www.sciencedirect.com/science/article/abs/pii/S1878450X24001501",
        "authors": ["Mansi Goel", "Vishva Nathavani", "Sumit Dharaiya", "Vidhya Kothadia", "Saloni Srivastava", "Ganesh Bagler"],
        "pub_date": "2024",
        "selected": "true",
        "abstract": "Cultural Context Shapes The Carbon Footprints Of Recipes."
    },
    {
        "title": "Computational gastronomy: capturing culinary creativity by making food computable",
        "date": "2024-08-01 00:01:00 +0800",
        "pub": "npj Systems Biology and Applications",
        "url": "https://www.nature.com/articles/s41540-024-00399-5",
        "authors": ["Ganesh Bagler", "Mansi Goel"],
        "pub_date": "2024",
        "selected": "true",
        "abstract": "This article provides a perspective on Computational Gastronomy."
    },
    {
        "title": "Machine Learning Models To Predict Sweetness Of Molecules",
        "date": "2022-10-01 00:01:00 +0800",
        "pub": "Computers in Biology and Medicine",
        "url": "https://www.sciencedirect.com/science/article/abs/pii/S0010482522011490",
        "authors": ["Mansi Goel", "Aditi Sharma", "Ayush Chilwal", "Sakshi Kumari", "Ayush Kumar", "Ganesh Bagler"],
        "pub_date": "2022",
        "selected": "true",
        "abstract": "This paper proposes a novel machine-learning approach for predicting the sweetness of molecules with high accuracy."
    },
    {
        "title": "Computational Gastronomy: A Data Science Approach To Food",
        "date": "2022-09-01 00:01:00 +0800",
        "pub": "Journal of Biosciences",
        "url": "https://link.springer.com/article/10.1007/s12038-021-00248-1",
        "authors": ["Mansi Goel", "Ganesh Bagler"],
        "pub_date": "2022",
        "selected": "true",
        "abstract": "A Data Science Approach To Food."
    },
    {
        "title": "Deep Learning Based Named Entity Recognition Models for Recipes",
        "date": "2024-07-01 00:01:00 +0800",
        "pub": "Proceedings of LREC-COLING 2024",
        "url": "https://aclanthology.org/2024.lrec-main.406.pdf",
        "authors": ["Mansi Goel", "Ayush Agrawal", "Shubham Agrawal", "Janak Kapuriya", "Akhil Vamshi", "Rishabh Gupta", "Shrey Rastogi", "Niharika", "Ganesh Bagler"],
        "pub_date": "2024",
        "selected": "true",
        "abstract": "Deep Learning Based Named Entity Recognition Models for Recipes."
    },
    {
        "title": "Dish Detection in Indian Food Platters: A Computational Framework for Diet Management",
        "date": "2023-10-01 00:01:00 +0800",
        "pub": "CVIP 2023",
        "url": "https://link.springer.com/chapter/10.1007/978-3-031-58181-6_20",
        "authors": ["Mansi Goel", "et al."],
        "pub_date": "2023",
        "selected": "true",
        "abstract": "A Computational Framework for Diet Management."
    },
    {
        "title": "Ratatouille: A Tool for Novel Recipe Generation",
        "date": "2022-08-01 00:01:00 +0800",
        "pub": "IEEE ICDEW 2022",
        "url": "https://ieeexplore.ieee.org/document/9814641/",
        "authors": ["Mansi Goel", "Pallab Chakraborty", "Vijay Ponnaganti", "Minnet Khan", "Sritanaya Tatipamala", "Aakanksha Saini", "Ganesh Bagler"],
        "pub_date": "2022",
        "selected": "true",
        "abstract": "A Tool for Novel Recipe Generation."
    },
    {
        "title": "Object Detection in Indian Food Platters using Transfer Learning with YOLOv4",
        "date": "2022-07-01 00:01:00 +0800",
        "pub": "IEEE ICDEW 2022",
        "url": "https://ieeexplore.ieee.org/document/9814702/",
        "authors": ["Deepanshu Pandey", "Purva Parmar", "Gauri Toshniwal", "Mansi Goel", "Vishesh Agrawal", "Shivangi Dhiman", "Lavanya Gupta", "Ganesh Bagler"],
        "pub_date": "2022",
        "selected": "true",
        "abstract": "BEST PAPER AWARD."
    }
]

for i, p in enumerate(publications):
    filename = os.path.join('_publications', f"pub-{i+1}.md")
    authors_yaml = "\n".join([f"  - {a}" for a in p['authors']])
    content = f"""---
title: "{p['title']}"
date: {p['date']}
selected: {p['selected']}
pub: "{p['pub']}"
pub_date: "{p['pub_date']}"
abstract: >-
  {p['abstract']}
authors:
{authors_yaml}
links:
  Paper: {p['url']}
---
"""
    with open(filename, 'w') as f:
        f.write(content)
