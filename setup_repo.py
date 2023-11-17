import subprocess
import re

proc = subprocess.run(['git','remote','-v'],stdout=subprocess.PIPE)
output = proc.stdout.decode()

link = re.search('http.+(?=\s\(fetch\))',output)[0]

update_master_code = f'git add remote template {link}\n'
update_master_code+="""
# Fetch updates from the template repository
git fetch template

# Merge updates into the current branch
git merge template/main --allow-unrelated-histories -m "Merge updates from template" 
"""
with open('updateRepoFromMaster.py','w+') as f:
  f.write(update_master_code)
  
subprocess.run(['git','add','.'])
subprocess.run(['git','commit','-a','-m','.'])
