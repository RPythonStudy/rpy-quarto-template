# scripts/setup/setup_repository_urls.py
# git remote URL과 wiki 서브모듈 URL을 변경하고, 모든 서브모듈을 master 브랜치로 체크아웃
# last modified: 2025-09-24
# log_info(f"[setup_repository_urls] ...") 형태로 출력


from common.logger import log_info
from pathlib import Path
import subprocess

# 프로젝트 루트 기준 repo명 추출
repo = Path.cwd().name
account = 'BenKorea' if repo == 'access-pet-data' else 'RPythonStudy'
url = f'git@github.com:{account}/{repo}.git'
subprocess.run(['git', 'remote', 'set-url', 'origin', url], check=True)
log_info(f"[setup_repository_urls] Changed remote URL to {url}")

# submodule wiki url 변경
wiki_url = f'git@github.com:{account}/{repo}.wiki.git'
subprocess.run(['git', 'submodule', 'set-url', 'wiki', wiki_url], check=True)
log_info(f"[setup_repository_urls] Changed submodule 'wiki' URL to {wiki_url}")

# 모든 서브모듈을 master 브랜치로 체크아웃
try:
    subprocess.run(['git', 'submodule', 'foreach', 'git checkout master'], check=True)
    log_info(f"[setup_repository_urls] 모든 서브모듈을 master 브랜치로 체크아웃 완료")
except Exception as e:
    log_info(f"[setup_repository_urls] 서브모듈 브랜치 체크아웃 실패: {e}")
