from pydantic import BaseModel, Field
from typing import Optional


class Settings(BaseModel):
    userEmail: str
    awsAccessKey: Optional[str] = None
    awsSecret: Optional[str] = None
    awsRegion: Optional[str] = None
    noSqlProvider: Optional[str] = None
    documentTableName: Optional[str] = None
    parsingApiKey: Optional[str] = None
    bucketsList: Optional[str] = None
    scanBucket: Optional[str] = None
    elasticSearchIndex: Optional[str] = None
    elasticSearchHost: Optional[str] = None
    elasticSearchPort: Optional[int] = None
    elasticSearchApiKey: Optional[str] = None
    searchDocumentDb: Optional[bool] = None
    searchElasticSearch: Optional[bool] = None
    storeLogsInDb: Optional[bool] = None
