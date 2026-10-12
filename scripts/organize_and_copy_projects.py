import os
import shutil
import zipfile

BASE_DIR = os.path.abspath(".")
ALL_PROJ_DIR = os.path.join(BASE_DIR, "All projects")

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

print("=== STARTING PROJECTS CURATION & COPY ===")

# -------------------------------------------------------------
# 01. Spielberg AI & Data Platform
# -------------------------------------------------------------
p01 = os.path.join(ALL_PROJ_DIR, "01_Spielberg_AI_Data_Platform")
print("\n--- 01: Spielberg AI Data Platform ---")
ensure_dir(os.path.join(p01, "reports"))
ensure_dir(os.path.join(p01, "presentations"))
ensure_dir(os.path.join(p01, "code"))

copy_file(os.path.join(BASE_DIR, "CV/Rapport_de_Stage_2026.pdf"), os.path.join(p01, "reports"), "Rapport_de_Stage_Spielberg_2026.pdf")
copy_file(os.path.join(BASE_DIR, "3A/rapport.tex"), os.path.join(p01, "reports"), "rapport_source.tex")
copy_file(os.path.join(BASE_DIR, "3A/soutenance.pdf"), os.path.join(p01, "presentations"), "Soutenance_Spielberg.pdf")
copy_file(os.path.join(BASE_DIR, "3A/soutenance.tex"), os.path.join(p01, "presentations"), "soutenance_source.tex")
copy_file(os.path.join(BASE_DIR, "3A/presentation_de_stage.pdf"), os.path.join(p01, "presentations"), "Presentation_Stage_ENSIIE.pdf")
copy_file(os.path.join(BASE_DIR, "2A/Stage/roadmap_stage.html"), os.path.join(p01, "code"))
copy_tree_clean(os.path.join(BASE_DIR, "2A/Stage/FastAPI"), os.path.join(p01, "code/FastAPI"))
copy_tree_clean(os.path.join(BASE_DIR, "2A/Stage/RAG"), os.path.join(p01, "code/RAG"))

# -------------------------------------------------------------
# 02. ETLia AI Data Wizard
# -------------------------------------------------------------
p02 = os.path.join(ALL_PROJ_DIR, "02_ETLia_AI_Data_Wizard")
print("\n--- 02: ETLia AI Data Wizard ---")
ensure_dir(os.path.join(p02, "assets"))
ensure_dir(os.path.join(p02, "backend"))
ensure_dir(os.path.join(p02, "frontend"))

for pyf in ["appETLia.py", "appETLiaCSS.py", "config.py", "load.py", "pym.py", "test.py"]:
    src = os.path.join(BASE_DIR, "Challenge Entreprendre", pyf)
    if os.path.exists(src):
        copy_file(src, os.path.join(p02, "backend"))

for img in ["Designsanstitre.png", "ensiie_logo_fx_RVB_0.png"]:
    src = os.path.join(BASE_DIR, "Challenge Entreprendre", img)
    if os.path.exists(src):
        copy_file(src, os.path.join(p02, "assets"))

copy_tree_clean(
    os.path.join(BASE_DIR, "Challenge Entreprendre/ETLia_website/etlia-data-wizard"),
    os.path.join(p02, "frontend"),
    ignore_dirs={'.git', 'node_modules', '.venv', '__pycache__', '.bun'}
)

# -------------------------------------------------------------
# 03. SunSejour ETL Datamart
# -------------------------------------------------------------
p03 = os.path.join(ALL_PROJ_DIR, "03_SunSejour_ETL_Datamart")
print("\n--- 03: SunSejour ETL Datamart ---")
ensure_dir(os.path.join(p03, "reports"))
ensure_dir(os.path.join(p03, "src"))
ensure_dir(os.path.join(p03, "data_samples"))

copy_file(os.path.join(BASE_DIR, "ETL Project/rapport_datamart_sunsejour.pdf"), os.path.join(p03, "reports"), "Rapport_Datamart_SunSejour.pdf")
copy_file(os.path.join(BASE_DIR, "ETL Project/rapport_datamart_sunsejour.docx"), os.path.join(p03, "reports"), "Rapport_Datamart_SunSejour.docx")
copy_file(os.path.join(BASE_DIR, "ETL Project/Rendu Projet/Guide_Utilisation_ETL_SunSejour.pdf"), os.path.join(p03, "reports"), "Guide_Utilisation_ETL_SunSejour.pdf")

for script in ["pipeline.py", "transform.py", "load.py", "validate.py", "config.py", "CA_script.py", "Dockerfile", "docker-compose.yml", "requirements.txt", "entrypoint.sh", "lancer_pipeline.bat"]:
    copy_file(os.path.join(BASE_DIR, "ETL Project", script), os.path.join(p03, "src"))

copy_tree_clean(os.path.join(BASE_DIR, "ETL Project/excursion_data"), os.path.join(p03, "data_samples/excursion_data"))
copy_tree_clean(os.path.join(BASE_DIR, "ETL Project/transfert_data"), os.path.join(p03, "data_samples/transfert_data"))

# -------------------------------------------------------------
# 04. Infinity Analytics Time Series & ML
# -------------------------------------------------------------
p04 = os.path.join(ALL_PROJ_DIR, "04_Infinity_Analytics_Time_Series_ML")
print("\n--- 04: Infinity Analytics Time Series ML ---")
ensure_dir(os.path.join(p04, "reports"))
ensure_dir(os.path.join(p04, "presentations"))
ensure_dir(os.path.join(p04, "notebooks"))
ensure_dir(os.path.join(p04, "models_and_data"))

copy_file(os.path.join(BASE_DIR, "1A/Stage/Rapport_de_Stage.pdf"), os.path.join(p04, "reports"), "Rapport_de_Stage.pdf")
copy_file(os.path.join(BASE_DIR, "1A/Stage/Rapport de Stage.docx"), os.path.join(p04, "reports"), "Rapport_de_Stage.docx")
copy_file(os.path.join(BASE_DIR, "1A/Stage/Prototype Infinity Analytics - Rapport Use Case 7.pdf"), os.path.join(p04, "reports"), "Rapport_Use_Case_7_Scoring.pdf")
copy_file(os.path.join(BASE_DIR, "1A/Stage/Prototype Infinity Analytics - Use Case 2.pdf"), os.path.join(p04, "reports"), "Rapport_Use_Case_2.pdf")
copy_file(os.path.join(BASE_DIR, "1A/Stage/Prototype Infinity Analytics - Modele de Donnees.pdf"), os.path.join(p04, "reports"), "Modele_de_Donnees.pdf")
copy_file(os.path.join(BASE_DIR, "1A/Stage/Protoptype Inifity Analytics - Use Cases ML_IA.pdf"), os.path.join(p04, "reports"), "Use_Cases_ML_IA.pdf")
copy_file(os.path.join(BASE_DIR, "1A/Stage/integrstion_ML.pdf"), os.path.join(p04, "reports"), "Integration_ML.pdf")

copy_file(os.path.join(BASE_DIR, "1A/Stage/presentation_de_stage.pdf"), os.path.join(p04, "presentations"), "Presentation_de_Stage.pdf")

for nb in ["SARIMA.ipynb", "SARIMAX.ipynb", "VAR.ipynb", "DLTS.ipynb", "usecase_2.ipynb", "usecase_7.ipynb", "ExoRW.ipynb"]:
    copy_file(os.path.join(BASE_DIR, "1A/Stage", nb), os.path.join(p04, "notebooks"))

copy_file(os.path.join(BASE_DIR, "1A/Stage/use_case_7_calib_modele.pkl"), os.path.join(p04, "models_and_data"))
copy_file(os.path.join(BASE_DIR, "1A/Stage/BAQ.csv"), os.path.join(p04, "models_and_data"))
copy_file(os.path.join(BASE_DIR, "1A/Stage/API_data_sample.csv"), os.path.join(p04, "models_and_data"))
copy_tree_clean(os.path.join(BASE_DIR, "1A/Stage/image rapport"), os.path.join(p04, "reports/figures"))

# -------------------------------------------------------------
# 05. NLP Semantic Representations & NER
# -------------------------------------------------------------
p05 = os.path.join(ALL_PROJ_DIR, "05_NLP_Semantic_Representations_NER")
print("\n--- 05: NLP Semantic Representations NER ---")
ensure_dir(os.path.join(p05, "reports"))
ensure_dir(os.path.join(p05, "src"))

zip_path = os.path.join(BASE_DIR, "3A/M2IA Shared Project/M2IA-Shared-Projects/TMC_Semantic_Representations_CISSE_DIOP.zip")
if os.path.exists(zip_path):
    temp_extract = os.path.join(p05, "_zip_tmp")
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(temp_extract)
    for root, dirs, files in os.walk(temp_extract):
        for f in files:
            sf = os.path.join(root, f)
            if f.lower().endswith('.pdf'):
                copy_file(sf, os.path.join(p05, "reports"))
            else:
                copy_file(sf, os.path.join(p05, "src"))
    shutil.rmtree(temp_extract, ignore_errors=True)

copy_file(os.path.join(BASE_DIR, "3A/M2IA Shared Project/M2IA-Shared-Projects/TMC___Rapport_TP_Embeddings 09.50.17.pdf"), os.path.join(p05, "reports"), "Rapport_TP_Embeddings.pdf")
copy_file(os.path.join(BASE_DIR, "3A/M2IA Shared Project/M2IA-Shared-Projects/embeddings.ipynb"), os.path.join(p05, "src"))
copy_file(os.path.join(BASE_DIR, "3A/M2IA Shared Project/M2IA-Shared-Projects/results_lstm_cnn.csv"), os.path.join(p05, "src"))
copy_tree_clean(os.path.join(BASE_DIR, "3A/M2IA Shared Project/M2IA-Shared-Projects/scripts"), os.path.join(p05, "src/scripts"))

# -------------------------------------------------------------
# 06. Black-Scholes PDE Solver (C++)
# -------------------------------------------------------------
p06 = os.path.join(ALL_PROJ_DIR, "06_Black_Scholes_PDE_Solver")
print("\n--- 06: Black Scholes PDE Solver ---")
ensure_dir(os.path.join(p06, "reports"))
ensure_dir(os.path.join(p06, "visuals"))
ensure_dir(os.path.join(p06, "src"))

copy_file(os.path.join(BASE_DIR, "2A/PRAV/Black-Scholes-Solver/CISSE_DAMI_projet_bs/rapport.pdf"), os.path.join(p06, "reports"), "Rapport_Black_Scholes.pdf")
copy_file(os.path.join(BASE_DIR, "2A/PRAV/Black-Scholes-Solver/CISSE_DAMI_projet_bs/rapport.tex"), os.path.join(p06, "reports"), "rapport_source.tex")
copy_file(os.path.join(BASE_DIR, "2A/PRAV/Black-Scholes-Solver/ensiie_pap_project_2_bs.pdf"), os.path.join(p06, "reports"), "Sujet_Projet.pdf")

for img in ["call.png", "Put.png", "erreur call.png", "erreur Put.png", "UML.png"]:
    copy_file(os.path.join(BASE_DIR, "2A/PRAV/Black-Scholes-Solver", img), os.path.join(p06, "visuals"))

copy_tree_clean(os.path.join(BASE_DIR, "2A/PRAV/Black-Scholes-Solver/CISSE_DAMI_projet_bs"), os.path.join(p06, "src"))

# -------------------------------------------------------------
# 07. Breast Cancer Biostatistics MERR
# -------------------------------------------------------------
p07 = os.path.join(ALL_PROJ_DIR, "07_Breast_Cancer_Biostatistics_MERR")
print("\n--- 07: Breast Cancer Biostatistics MERR ---")
ensure_dir(os.path.join(p07, "reports"))
ensure_dir(os.path.join(p07, "src"))

copy_file(os.path.join(BASE_DIR, "2A/MERR/AI-Breast-Cancer-Outcome-Detection/BINOMIAL_12_CISSE_DAMI/BINOMIAL_12_CISSE_DAMI.pdf"), os.path.join(p07, "reports"), "Rapport_Cancer_Survie_MERR.pdf")
copy_file(os.path.join(BASE_DIR, "2A/MERR/Project/BINOMIAL_12_CISSE_DAMI.docx"), os.path.join(p07, "reports"), "Rapport_Cancer_Survie_MERR.docx")
copy_file(os.path.join(BASE_DIR, "2A/MERR/Project/Infos/breast_cancer2012_nature11412.pdf"), os.path.join(p07, "reports"), "Reference_Nature_2012.pdf")

copy_file(os.path.join(BASE_DIR, "2A/MERR/AI-Breast-Cancer-Outcome-Detection/BINOMIAL_12_CISSE_DAMI.Rmd"), os.path.join(p07, "src"))
copy_file(os.path.join(BASE_DIR, "2A/MERR/AI-Breast-Cancer-Outcome-Detection/last_mrr.Rmd"), os.path.join(p07, "src"))
copy_file(os.path.join(BASE_DIR, "2A/MERR/AI-Breast-Cancer-Outcome-Detection/intro_proj.Rmd"), os.path.join(p07, "src"))
copy_file(os.path.join(BASE_DIR, "2A/MERR/AI-Breast-Cancer-Outcome-Detection/mrr_bio.Rdata"), os.path.join(p07, "src"))

# -------------------------------------------------------------
# 08. Airbnb NYC Data Analysis ANDO
# -------------------------------------------------------------
p08 = os.path.join(ALL_PROJ_DIR, "08_Airbnb_NYC_Data_Analysis_ANDO")
print("\n--- 08: Airbnb NYC Data Analysis ANDO ---")
ensure_dir(os.path.join(p08, "reports"))
ensure_dir(os.path.join(p08, "presentations"))
ensure_dir(os.path.join(p08, "notebooks"))
ensure_dir(os.path.join(p08, "data"))

copy_file(os.path.join(BASE_DIR, "2A/ANDO/Projet/Rapport data ANDO.pdf"), os.path.join(p08, "reports"), "Rapport_Analyse_Donnees_ANDO.pdf")
copy_file(os.path.join(BASE_DIR, "2A/ANDO/projet ANDO rendu/Projet-ANDO/dossier_rapport/rapport.tex"), os.path.join(p08, "reports"), "rapport_source.tex")

copy_file(os.path.join(BASE_DIR, "2A/ANDO/slide-1.pdf"), os.path.join(p08, "presentations"), "Presentation_Partie_1.pdf")
copy_file(os.path.join(BASE_DIR, "2A/ANDO/slide_2.pdf"), os.path.join(p08, "presentations"), "Presentation_Partie_2.pdf")

for nb in ["ANDO.ipynb", "projet.ipynb"]:
    src = os.path.join(BASE_DIR, "2A/ANDO/Projet", nb)
    if os.path.exists(src):
        copy_file(src, os.path.join(p08, "notebooks"))

rendu_dir = os.path.join(BASE_DIR, "2A/ANDO/projet ANDO rendu/Projet-ANDO")
if os.path.exists(rendu_dir):
    for f in os.listdir(rendu_dir):
        if f.endswith('.ipynb'):
            copy_file(os.path.join(rendu_dir, f), os.path.join(p08, "notebooks"))

copy_file(os.path.join(BASE_DIR, "2A/ANDO/Projet/Projet-ANDO/AB_NYC_2019.csv"), os.path.join(p08, "data"))

# -------------------------------------------------------------
# 09. Machine Learning Economics DAMI
# -------------------------------------------------------------
p09 = os.path.join(ALL_PROJ_DIR, "09_Machine_Learning_Economics_DAMI")
print("\n--- 09: Machine Learning Economics DAMI ---")
ensure_dir(os.path.join(p09, "reports"))
ensure_dir(os.path.join(p09, "src"))

copy_file(os.path.join(BASE_DIR, "ML_DAMI.pdf"), os.path.join(p09, "reports"), "Rapport_ML_Econometrics.pdf")
copy_file(os.path.join(BASE_DIR, "ML_DAMI.Rmd"), os.path.join(p09, "src"), "ML_Econometrics.Rmd")

# -------------------------------------------------------------
# 10. Image Processing C PRIM
# -------------------------------------------------------------
p10 = os.path.join(ALL_PROJ_DIR, "10_Image_Processing_C_PRIM")
print("\n--- 10: Image Processing C PRIM ---")
ensure_dir(os.path.join(p10, "reports"))
ensure_dir(os.path.join(p10, "src"))

copy_file(os.path.join(BASE_DIR, "1A/TP/TP PRIM/Projet de PRIM/rapport.pdf"), os.path.join(p10, "reports"), "Rapport_Projet_PRIM.pdf")
copy_tree_clean(os.path.join(BASE_DIR, "1A/TP/TP PRIM/Projet de PRIM"), os.path.join(p10, "src"))

# -------------------------------------------------------------
# 11. Functional Programming OCaml
# -------------------------------------------------------------
p11 = os.path.join(ALL_PROJ_DIR, "11_Functional_Programming_OCaml")
print("\n--- 11: Functional Programming OCaml ---")
ensure_dir(os.path.join(p11, "reports"))
ensure_dir(os.path.join(p11, "src"))

copy_file(os.path.join(BASE_DIR, "1A/TP/TP Ocaml/Projet Ocaml/rapport.pdf"), os.path.join(p11, "reports"), "Rapport_Projet_OCaml.pdf")
copy_file(os.path.join(BASE_DIR, "1A/TP/TP Ocaml/Projet Ocaml/projet.pdf"), os.path.join(p11, "reports"), "Sujet_Projet_OCaml.pdf")
copy_tree_clean(os.path.join(BASE_DIR, "1A/TP/TP Ocaml/Projet Ocaml"), os.path.join(p11, "src"))

# -------------------------------------------------------------
# 12. Card Game Probabilistic Simulation (1A Math-Info)
# -------------------------------------------------------------
p12 = os.path.join(ALL_PROJ_DIR, "12_Card_Game_Probabilistic_Simulation")
print("\n--- 12: Card Game Probabilistic Simulation ---")
ensure_dir(os.path.join(p12, "docs"))
ensure_dir(os.path.join(p12, "src"))

copy_file(os.path.join(BASE_DIR, "1A/TP/projet-math-info-grp-28/research_17/experiments/experience.pdf"), os.path.join(p12, "docs"), "Rapport_Experience_Probabiliste.pdf")
copy_file(os.path.join(BASE_DIR, "1A/TP/projet-math-info-grp-28/Gantt-Projet-Math-Info.gan"), os.path.join(p12, "docs"))
copy_tree_clean(os.path.join(BASE_DIR, "1A/TP/projet-math-info-grp-28"), os.path.join(p12, "src"))

# -------------------------------------------------------------
# 13. Kryptosphere AI Workshops
# -------------------------------------------------------------
p13 = os.path.join(ALL_PROJ_DIR, "13_Kryptosphere_AI_Workshops")
print("\n--- 13: Kryptosphere AI Workshops ---")
ensure_dir(os.path.join(p13, "presentations"))
ensure_dir(os.path.join(p13, "workshops"))

copy_file(os.path.join(BASE_DIR, "Kryptosphere IA/Formation 2/Formation_3_-_Evaluation_d_un_modèle__1_.pptx"), os.path.join(p13, "presentations"), "Formation_Evaluation_Modeles_ML.pptx")
copy_file(os.path.join(BASE_DIR, "Kryptosphere IA/Formation 2/Formation_3_-_Evaluation_d_un_modèle__1_.pdf"), os.path.join(p13, "presentations"), "Formation_Evaluation_Modeles_ML.pdf")
copy_file(os.path.join(BASE_DIR, "Kryptosphere IA/Formation 3/Clustering_.pptx"), os.path.join(p13, "presentations"), "Formation_Clustering.pptx")
copy_file(os.path.join(BASE_DIR, "Kryptosphere IA/Formation 3/Clustering.pdf"), os.path.join(p13, "presentations"), "Formation_Clustering.pdf")

copy_tree_clean(os.path.join(BASE_DIR, "Kryptosphere IA/Formation 1"), os.path.join(p13, "workshops/01_data_manipulation_viz"))
copy_tree_clean(os.path.join(BASE_DIR, "Kryptosphere IA/Formation 2"), os.path.join(p13, "workshops/02_preprocessing_evaluation"))
copy_tree_clean(os.path.join(BASE_DIR, "Kryptosphere IA/Formation 3"), os.path.join(p13, "workshops/03_clustering"))
copy_tree_clean(os.path.join(BASE_DIR, "Kryptosphere IA/Formation 4"), os.path.join(p13, "workshops/04_time_series"))

# -------------------------------------------------------------
# 14. JavaFX Expression Parser
# -------------------------------------------------------------
p14 = os.path.join(ALL_PROJ_DIR, "14_JavaFX_Expression_Parser")
print("\n--- 14: JavaFX Expression Parser ---")
copy_tree_clean(os.path.join(BASE_DIR, "1A/TP/Projet Java/HelloFX"), p14)

# -------------------------------------------------------------
# 15. Face Attributes Data Readiness
# -------------------------------------------------------------
p15 = os.path.join(ALL_PROJ_DIR, "15_Face_Attributes_Data_Readiness")
print("\n--- 15: Face Attributes Data Readiness ---")
copy_tree_clean(os.path.join(BASE_DIR, "3A/Data Readiness"), p15)

# -------------------------------------------------------------
# 16. Signal Processing Lab
# -------------------------------------------------------------
p16 = os.path.join(ALL_PROJ_DIR, "16_Signal_Processing_Lab")
print("\n--- 16: Signal Processing Lab ---")
ensure_dir(p16)
for tp in ["TP1", "TP2", "TP3"]:
    copy_tree_clean(os.path.join(BASE_DIR, "3A/Signal Processing", tp), os.path.join(p16, tp))

print("\n=== ALL PROJECTS COPIED SUCCESSFULLY ===")
