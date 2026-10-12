import os
import shutil
import json
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

BASE_ENSIIE = os.path.abspath(".")
ALL_PROJ_DIR = os.path.join(BASE_ENSIIE, "All projects")
MCMASTER_DIR = "/Users/nouroudine/Documents/McMaster"

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def copy_file(src, dst_dir, new_name=None):
    if not os.path.exists(src):
        print(f"  [WARN] Source file not found: {src}")
        return None
    ensure_dir(dst_dir)
    target_name = new_name if new_name else os.path.basename(src)
    dst = os.path.join(dst_dir, target_name)
    if os.path.abspath(src) == os.path.abspath(dst):
        return dst
    shutil.copy2(src, dst)
    print(f"  [COPY FILE] {os.path.basename(src)} -> {dst}")
    return dst

def copy_tree_clean(src, dst, ignore_dirs=None, ignore_exts=None):
    if not os.path.exists(src):
        print(f"  [WARN] Source dir not found: {src}")
        return
    if ignore_dirs is None:
        ignore_dirs = {'.git', '.venv', 'venv', '__pycache__', 'node_modules', '.idea', '.vscode'}
    if ignore_exts is None:
        ignore_exts = {'.pyc', '.DS_Store', '.zip.bak'}

    ensure_dir(dst)
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith('.')]
        rel = os.path.relpath(root, src)
        cur_dst = dst if rel == '.' else os.path.join(dst, rel)
        ensure_dir(cur_dst)
        for f in files:
            if any(f.endswith(ext) for ext in ignore_exts) or f.startswith('.'):
                continue
            sf = os.path.join(root, f)
            df = os.path.join(cur_dst, f)
            if os.path.abspath(sf) != os.path.abspath(df):
                shutil.copy2(sf, df)
    print(f"  [COPY TREE] {src} -> {dst}")

print("=== IMPORTING MCMASTER PROJECTS ===")

# -------------------------------------------------------------
# 17. McMaster MATH 4FM3 : Nash-DQN Multi-Agent Trading
# -------------------------------------------------------------
p17 = os.path.join(ALL_PROJ_DIR, "17_McMaster_Nash_DQN_MultiAgent_Trading")
print("\n--- 17: McMaster Nash-DQN Multi-Agent Trading ---")
ensure_dir(os.path.join(p17, "reports"))
ensure_dir(os.path.join(p17, "visuals"))
ensure_dir(os.path.join(p17, "src"))

src17 = os.path.join(MCMASTER_DIR, "MATH 4FM3/MATH 4FM3 Project/Nash-DQN-Deep-Q-Learning-for-Nash-Equilibria-in-Multi-Agent-Optimal-Trading")
copy_file(os.path.join(src17, "Project.pdf"), os.path.join(p17, "reports"), "Rapport_Nash_DQN_Optimal_Trading.pdf")
copy_file(os.path.join(src17, "Project.tex"), os.path.join(p17, "reports"), "Rapport_source.tex")
copy_file(os.path.join(MCMASTER_DIR, "MATH 4FM3/MATH4FM3_NashDQN_Roadmap.pdf"), os.path.join(p17, "reports"), "Project_Roadmap.pdf")

copy_file(os.path.join(MCMASTER_DIR, "MATH 4FM3/brownian_paths.png"), os.path.join(p17, "visuals"))
copy_file(os.path.join(MCMASTER_DIR, "MATH 4FM3/all_agents_rewards.png"), os.path.join(p17, "visuals"))

copy_tree_clean(src17, os.path.join(p17, "src"))

# -------------------------------------------------------------
# 18. McMaster DATASCI 3ML3 : Financial News Sentiment (BiLSTM)
# -------------------------------------------------------------
p18 = os.path.join(ALL_PROJ_DIR, "18_McMaster_Financial_News_Sentiment_BiLSTM")
print("\n--- 18: McMaster Financial News Sentiment BiLSTM ---")
ensure_dir(os.path.join(p18, "reports"))
ensure_dir(os.path.join(p18, "src"))

src18 = os.path.join(MCMASTER_DIR, "ML & NN/Project")
copy_file(os.path.join(src18, "report.pdf"), os.path.join(p18, "reports"), "Financial_News_Sentiment_Classification_Report.pdf")
copy_file(os.path.join(src18, "FinalProject 15.29.36.pdf"), os.path.join(p18, "reports"), "Sujet_FinalProject.pdf")
copy_file(os.path.join(src18, "Project.ipynb"), os.path.join(p18, "src"))
copy_file(os.path.join(src18, "NLP.ipynb"), os.path.join(p18, "src"))

# -------------------------------------------------------------
# 19. McMaster STATS 4A03 : Canadian Retail Seasonal Forecasting
# -------------------------------------------------------------
p19 = os.path.join(ALL_PROJ_DIR, "19_McMaster_Canadian_Retail_Time_Series")
print("\n--- 19: McMaster Canadian Retail Time Series ---")
ensure_dir(os.path.join(p19, "reports"))
ensure_dir(os.path.join(p19, "src"))

src19 = os.path.join(MCMASTER_DIR, "Time Series/Project")
copy_file(os.path.join(src19, "report.pdf"), os.path.join(p19, "reports"), "Canadian_Retail_Time_Series_Forecasting_Report.pdf")
copy_file(os.path.join(src19, "Project.Rmd"), os.path.join(p19, "src"))
copy_file(os.path.join(src19, "Project.R"), os.path.join(p19, "src"))

# -------------------------------------------------------------
# 20. McMaster MECHENG 4AI3 : Visual Question Answering (VQA)
# -------------------------------------------------------------
p20 = os.path.join(ALL_PROJ_DIR, "20_McMaster_Visual_Question_Answering_VQA")
print("\n--- 20: McMaster Visual Question Answering VQA ---")
ensure_dir(os.path.join(p20, "reports"))
ensure_dir(os.path.join(p20, "src"))

src20 = os.path.join(MCMASTER_DIR, "Applied AI/Applied AI VQA Project")
copy_file(os.path.join(src20, "VQA Roadmap Revised.pdf"), os.path.join(p20, "reports"), "VQA_Project_Roadmap.pdf")
copy_tree_clean(os.path.join(src20, "visual-question-answering"), os.path.join(p20, "src"))

# -------------------------------------------------------------
# 21. McMaster STATS 4GLM : Generalized Linear Models
# -------------------------------------------------------------
p21 = os.path.join(ALL_PROJ_DIR, "21_McMaster_Generalized_Linear_Models")
print("\n--- 21: McMaster Generalized Linear Models ---")
ensure_dir(os.path.join(p21, "reports"))
ensure_dir(os.path.join(p21, "src"))

src21 = os.path.join(MCMASTER_DIR, "Generalized Linear Model")
copy_tree_clean(os.path.join(src21, "Assignments"), os.path.join(p21, "assignments_and_reports"))
copy_tree_clean(os.path.join(src21, "Lecture R code"), os.path.join(p21, "src"))

print("=== ALL MCMASTER PROJECTS IMPORTED SUCCESSFULLY ===")
