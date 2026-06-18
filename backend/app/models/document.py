"""Document and DocumentChunk Models"""

from sqlalchemy import Column, String, Text, JSON, Integer, ForeignKey
from .base import BaseModel


class Document(BaseModel):
    """Source Document Model"""

    __tablename__ = "documents"

    source = Column(String(50), nullable=False)
    source_id = Column(String(255), nullable=False)
    title = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)
    
    authors = Column(JSON, default=list)
    publication_date = Column(String(50))
    url = Column(String(500))
    doi = Column(String(255))
    pmid = Column(String(50))
    
    metadata = Column(JSON, default=dict)
    is_indexed = Column(String(36), default=False)


class DocumentChunk(BaseModel):
    """Document Chunk for RAG Model"""

    __tablename__ = "document_chunks"

    document_id = Column(String(36), ForeignKey("documents.id"), nullable=False)
    
    chunk_index = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    
    embedding_id = Column(String(255))
    embedding = Column(JSON)
    
    metadata = Column(JSON, default=dict)
