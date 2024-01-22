#this is my code
#co-authored with Jonathan Raigosa during his student-hosted Coderie
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -v -E "[^zonciar]+" | grep -E ".{4,}"