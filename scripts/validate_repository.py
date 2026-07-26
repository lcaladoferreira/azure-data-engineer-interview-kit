from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
checks={
"SQL coding":("sql/coding/180-solved-problems.md",180),"SQL theory":("sql/theoretical-qa.md",175),
"NumPy":("python/coding/numpy-45.md",45),"pandas":("python/coding/pandas-75.md",75),
"Python frequent":("python/coding/29-frequent-programs.md",29),"Python basic":("python/coding/85-basic-programs.md",85),
"Python theory":("python/theoretical-qa.md",35),"PySpark coding":("pyspark/coding/105-hands-on-problems.md",105),
"PySpark theory":("pyspark/theoretical-qa.md",160),"Warehousing":("data-warehousing/30-in-depth-qa.md",30),
"Modeling":("data-modeling/30-in-depth-qa.md",30),"Linux":("linux/100-commands.md",100),
"Git Q&A":("git/65-in-depth-qa.md",65),"CI/CD":("cicd/55-in-depth-qa.md",55),
"DSA":("dsa/54-solved-problems.md",54),"DP-700":("certification/dp-700/120-scenario-concept-questions.md",120),
"ADF scenario":("azure/azure-data-factory/scenario-qa.md",55),"ADF theory":("azure/azure-data-factory/theoretical-qa.md",225),
"Databricks scenario":("azure/databricks/scenario-qa.md",85),"Databricks theory":("azure/databricks/theoretical-qa.md",165),
"Synapse scenario":("azure/synapse/scenario-qa.md",55),"Synapse theory":("azure/synapse/theoretical-qa.md",155),
"ADLS scenario":("azure/adls-gen2/scenario-qa.md",35),"ADLS theory":("azure/adls-gen2/theoretical-qa.md",105),
"Fabric detailed":("azure/microsoft-fabric/scenario-qa.md",75),"Fabric theory":("azure/microsoft-fabric/theoretical-qa.md",120),
"Functions scenario":("azure/azure-functions/scenario-qa.md",30),"Functions theory":("azure/azure-functions/theoretical-qa.md",35),
"Logic Apps scenario":("azure/logic-apps/scenario-qa.md",42),"Logic Apps theory":("azure/logic-apps/theoretical-qa.md",34),
"Stream scenario":("azure/stream-analytics/scenario-qa.md",45),"Stream theory":("azure/stream-analytics/theoretical-qa.md",80),
"Blob scenario":("azure/blob-storage/scenario-qa.md",30),"Blob theory":("azure/blob-storage/theoretical-qa.md",80),
"Cosmos scenario":("azure/cosmos-db/scenario-qa.md",65),"Cosmos theory":("azure/cosmos-db/theoretical-qa.md",60),
"HDInsight scenario":("azure/hdinsight/scenario-qa.md",40),"HDInsight theory":("azure/hdinsight/theoretical-qa.md",45),
"Projects":("projects/20-end-to-end-projects.md",20),"Interview experiences":("career/30-interview-experiences.md",30)}
errors=[]
for name,(path,want) in checks.items():
    text=(root/path).read_text()
    got=len(re.findall(r"^## \d+\. ",text,re.M))
    if got < want: errors.append(f"{name}: expected >= {want}, got {got}")
file_checks=[("SQL books","sql/books/*.md",5),("SQL cheatsheets","sql/cheatsheets/*.md",3),
("Python books","python/books/*.md",5),("Python cheatsheets","python/cheatsheets/*.md",6),
("PySpark books","pyspark/book/*.md",1),("PySpark notes","pyspark/notes/*.md",5),
("ADF notes","azure/azure-data-factory/notes/*.md",5),("Resumes","career/resume-templates/*.md",6)]
for name,pat,want in file_checks:
    got=len(list(root.glob(pat)))
    if got < want: errors.append(f"{name}: expected >= {want}, got {got}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"PASS: {len(checks)} count checks and {len(file_checks)} file-group checks")
