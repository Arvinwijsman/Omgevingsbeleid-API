import logging
from typing import Any, List
from uuid import UUID
from devtools import debug

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps
from app.core.exceptions import EmptySearchCriteria
from app.schemas.search import SearchResultWrapper
from app.services import search_service
from app.util import get_filtered_search_criteria

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get(
    "/search",
    response_model=List[schemas.SearchResult],
)
def search(
    query: str,
    db: Session = Depends(deps.get_db),
    current_gebruiker: models.Gebruiker = Depends(deps.get_current_active_gebruiker),
) -> Any:
    """
    Fetches items matching the search query parameters
    """
    # Sanitize stopwords or other word filters
    try:
        search_criteria = get_filtered_search_criteria(query)
    except EmptySearchCriteria:
        raise HTTPException(status_code=403, detail="Search query empty after filtering")

    search_results = search_service.search_all(search_criteria=search_criteria)

    results = list()
    for item in search_results:
        search_description = item.object.get_search_fields().description

        try:
            description = getattr(item.object, search_description[0].key)
            search_result = schemas.SearchResult(
                Omschrijving=description,
                Type=item.object.__tablename__,
                RANK=item.rank, 
                UUID=item.object.UUID
            )
            results.append(search_result)
        except AttributeError:
            logger.debug(f"Description value not found for {type(item.object)}: {item.object.UUID}")

    return results


@router.get(
    "/geo-search",
    response_model=SearchResultWrapper,
)
def geo_search(
    query: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Lookup geo-searchable entities related to a 'Werkingsgebied'
    """
    try:
        query_list = [uuid for uuid in query.split(",")]
    except Exception:
        raise HTTPException(status_code=403, detail="Invalid list of Werkingsgebied UUIDs")

    search_results = search_service.geo_search(query_list)

    return {
        "results": search_results,
        "count": len(search_results)
    }


