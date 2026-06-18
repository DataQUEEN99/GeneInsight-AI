"""Embedding and Vector Database Utilities"""

from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
from app.config import settings
import logging

logger = logging.getLogger(__name__)

try:
    embedding_model = SentenceTransformer(settings.embedding_model)
except Exception as e:
    logger.error(f"Failed to load embedding model: {e}")
    embedding_model = None


def get_embeddings(texts: List[str]) -> List[List[float]]:
    if not embedding_model:
        logger.warning("Embedding model not loaded")
        return [[0.0] * 384 for _ in texts]
    
    try:
        embeddings = embedding_model.encode(texts, convert_to_numpy=True)
        return embeddings.tolist()
    except Exception as e:
        logger.error(f"Failed to generate embeddings: {e}")
        raise


def get_embedding(text: str) -> List[float]:
    return get_embeddings([text])[0]


def calculate_similarity(embedding1: List[float], embedding2: List[float]) -> float:
    arr1 = np.array(embedding1)
    arr2 = np.array(embedding2)
    
    dot_product = np.dot(arr1, arr2)
    magnitude1 = np.linalg.norm(arr1)
    magnitude2 = np.linalg.norm(arr2)
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return float(dot_product / (magnitude1 * magnitude2))
