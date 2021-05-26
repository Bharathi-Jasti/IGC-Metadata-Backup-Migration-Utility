import os
import sys
import pandas as pd
usr = sys.argv[1]
passwd = sys.argv[2]
file = sys.argv[3]
cmd = "all"
if len(sys.argv) > 4:
    cmd = sys.argv[4]
    if not  cmd in ["all","backup","qa","prd","prd_import","qa_import"]:
        cmd = "all"


curr_dir = os.path.dirname(os.path.realpath(__file__))
path = "c:\\ibm\\InformationServer11_5\\Clients\\istools\\cli"
cmds = {
"prd_export":"call istool export -dom P2ERSCBA0705 -u %s -p %s -v -ar   \"%s\\prd\\{host}_{db}_{schema}_{table_}.tbl.isx\" -cm '\"/{host}/{db}/{schema}/{table}.tbl\"'"%(usr,passwd,curr_dir),
"qa_export":"call istool export -dom p1erscba0860 -u %s -p %s -v -ar   \"%s\\qa\\{host}_{db}_{schema}_{table_}.tbl.isx\" -cm '\"/{host}/{db}/{schema}/{table}.tbl\"'"%(usr,passwd,curr_dir),
"prd_import":"call istool import -dom P2ERSCBA0705 -u %s -p %s -v -ar   \"%s\\qa\\{host}_{db}_{schema}_{table_}.tbl.isx\" -cm '-allowDuplicates' -replace"%(usr,passwd,curr_dir),
"qa_import":"call istool import -dom p1erscba0860 -u %s -p %s -v -ar   \"%s\\imp\\{host}_{db}_{schema}_{table_}.tbl.isx\" -cm '-allowDuplicates' -replace"%(usr,passwd,curr_dir),
}

df = pd.read_csv(file)
os.chdir(path)

# Create backup folders
qa_path = os.path.join(curr_dir,"qa")
prd_path = os.path.join(curr_dir,"prd")
for directory in [qa_path,prd_path]:
    if not os.path.exists(directory):
        os.makedirs(directory)

for index, row in df.iterrows():
    print((index,row))
    table_= row["table"]
    if row["table"]=="*":
        table_ = "_"
    if cmd in ["all", "backup"]:
        # QA & PROD export
        pcmds = [
            cmds["prd_export"].replace("{host}",row["host"]).replace("{db}",row["db"]).replace("{schema}",row["schema"]).replace("{table}",row["table"]).replace("{table_}",table_),
            cmds["qa_export"].replace("{host}",row["host"]).replace("{db}",row["db"]).replace("{schema}",row["schema"]).replace("{table}",row["table"]).replace("{table_}",table_),
        ]

    if cmd in ["qa"]:
        # QA & PROD export
        pcmds = [
            cmds["qa_export"].replace("{host}",row["host"]).replace("{db}",row["db"]).replace("{schema}",row["schema"]).replace("{table}",row["table"]).replace("{table_}",table_),
        ]
    if cmd in ["prd"]:
        # QA & PROD export
        pcmds = [
            cmds["prd_export"].replace("{host}",row["host"]).replace("{db}",row["db"]).replace("{schema}",row["schema"]).replace("{table}",row["table"]).replace("{table_}",table_),
        ]
    if cmd in ["qa","prd","all","backup"]:
        for tcmd in pcmds:
            print(tcmd)
            os.system(tcmd)
# Import specific Tables into PRD
if cmd in ["all","prd_import"]:
    for index, row in df.iterrows():
        table_= row["table"]
        if row["table"]=="*":
            table_ = "_"

        # QA & PROD export
        pcmds = [
            cmds["prd_import"].replace("{host}",row["host"]).replace("{db}",row["db"]).replace("{schema}",row["schema"]).replace("{table}",row["table"]).replace("{table_}",table_),
        ]

        for tcmd in pcmds:
            print(tcmd)
            os.system(tcmd)
# Import specific Tables into QA
if cmd in ["qa_import"]:
    for index, row in df.iterrows():
        table_= row["table"]
        if row["table"]=="*":
            table_ = "_"

        # QA Import
        pcmds = [
            cmds["qa_import"].replace("{host}",row["host"]).replace("{db}",row["db"]).replace("{schema}",row["schema"]).replace("{table}",row["table"]).replace("{table_}",table_),
        ]

        for tcmd in pcmds:
            print(tcmd)
            os.system(tcmd)

os.chdir(curr_dir)


