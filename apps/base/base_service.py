from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from apps.admins.models import Admin

http_basic = HTTPBasic()


def check_active(credentials: HTTPBasicCredentials = Depends(http_basic)):
    active = Admin.objects.get(is_active=True)
    if active == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )


def check_admin(credentials: HTTPBasicCredentials = Depends(http_basic)):
    role = Admin.objects.filter(role="admin")
    if not role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can access this route",
        )


def check_company(credentials: HTTPBasicCredentials = Depends(http_basic)):
    role = Admin.objects.filter(role="company")
    if not role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can access this route",
        )
