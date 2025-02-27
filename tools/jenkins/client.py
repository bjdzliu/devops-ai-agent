import jenkins
import logging
from typing import Optional, Dict, Any
from ...api.schemas.base import APIResponse

class JenkinsClient:
    def __init__(self, url: str, username: str, token: str):
        self.server = jenkins.Jenkins(
            url=url,
            username=username,
            password=token
        )
        self.logger = logging.getLogger(__name__)

    def get_job_info(self, job_name: str) -> APIResponse:
        try:
            job_info = self.server.get_job_info(job_name)
            return APIResponse(
                status_code=200,
                data=job_info
            )
        except jenkins.JenkinsException as e:
            self.logger.error(f"Jenkins job info request failed: {str(e)}")
            return APIResponse(
                status_code=500,
                error=str(e)
            )

    def trigger_build(self, job_name: str, parameters: Optional[Dict[str, str]] = None) -> APIResponse:
        try:
            queue_id = self.server.build_job(job_name, parameters=parameters or {})
            return APIResponse(
                status_code=202,
                data={"queue_id": queue_id}
            )
        except jenkins.JenkinsException as e:
            self.logger.error(f"Jenkins build trigger failed: {str(e)}")
            return APIResponse(
                status_code=500,
                error=str(e)
            )
