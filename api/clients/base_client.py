import requests
from typing import Optional, Dict, Any
from ..schemas.base import APIResponse
import logging

class BaseAPIClient:
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url
        self.headers = headers or {}
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)

    def _request(self, method: str, endpoint: str, **kwargs) -> APIResponse:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=self.headers,
                **kwargs
            )
            response.raise_for_status()
            return APIResponse(
                status_code=response.status_code,
                data=response.json()
            )
        except requests.exceptions.RequestException as e:
            self.logger.error(f"API request failed: {str(e)}")
            raise

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> APIResponse:
        return self._request("POST", endpoint, json=data)

    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> APIResponse:
        return self._request("PUT", endpoint, json=data)

    def delete(self, endpoint: str) -> APIResponse:
        return self._request("DELETE", endpoint)
