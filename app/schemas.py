from pydantic import BaseModel

class IssueCreate(BaseModel):
    repo_owner: str
    repo_name: str
    title: str
    body: str