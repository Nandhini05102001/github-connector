from fastapi import APIRouter, HTTPException
from app.services.github_services import get_repos, create_issue,list_issues
from app.schemas import IssueCreate

router = APIRouter()

@router.get("/repos/{username}")
def fetch_repos(username: str):
    try:
        return get_repos(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create-issue")
def create_new_issue(issue: IssueCreate):
    try:
        return create_issue(issue)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/list-issues")
def get_issues(owner: str, repo: str):
    try:
        return list_issues(owner, repo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))