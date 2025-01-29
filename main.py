from github import Github
from difflib import SequenceMatcher
import ast

#Authenticate with github API
access_token = "SECRET_KEY"
g = Github(access_token)

#search for code in Github repo
qeury = "Granton"
results = g.search_code(qeury)

for result in results:
    print(f"Repository: {result.repository.full_name}")
    print(f"File path: {result.path}")
    print(f"URL: {result.html_url}")
    print("-------")

# works replace code1 nd code2 with actual code
def code_similarity(code1, code2):
    return SequenceMatcher(None, code1, code2).ratio()

code1 = "print(Hello, world)"
code2 = "print(hELLO, world)"
similarity = code_similarity(code1, code2)
print(f"Similarity: {similarity * 100:.2f}")

def normalize_code(code):
    tree = ast.parse(code)
    normalized_code = ast.unparse(tree)
    return normalized_code