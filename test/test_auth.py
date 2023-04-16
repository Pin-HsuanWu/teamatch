import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app  # Flask instance of the API

client = TestClient(app)


@pytest.fixture(scope="module")
def get_server_api():
    server_name = "http://localhost:8000"
    return server_name


# test
def test_google_auth(get_server_api):
    # credential = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjZGEzNjBmYjM2Y2QxNWZmODNhZjgzZTE3M2Y0N2ZmYzM2ZDExMWMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2ODExNDM4MjYsImF1ZCI6Ijc2ODMwNTUzMzI1Ni1lZzNpZnQ5NnNwb2xndG02OWJvNnIzNDIzZGYxM2M3My5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNTA2NzU1OTQ2Mjc4NTI3NTc5OCIsImVtYWlsIjoic2RtMjAyMy5ubzJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF6cCI6Ijc2ODMwNTUzMzI1Ni1lZzNpZnQ5NnNwb2xndG02OWJvNnIzNDIzZGYxM2M3My5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsIm5hbWUiOiJTRCBNIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FHTm15eFlOc0hQQVBjOHAzMkFzMzF3QXlmdU12elN2NXhrTEM0ZGNfLWFPPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IlNEIiwiZmFtaWx5X25hbWUiOiJNIiwiaWF0IjoxNjgxMTQ0MTI2LCJleHAiOjE2ODExNDc3MjYsImp0aSI6IjYyNThlZmNhYzFhNjcxNDIxNjJkMWYwMmU0MmI0ZGQ2OGFlODBjMmEifQ.bdDiJjnfuU-d2TLxnVfCocDSPVIhCtHA4A1pTBL3kjNBVGFi66DJZxS3w-gC_UKEytZnWaPjuWcjYaGKF4fjz1qlnPLuZiIPGq6z5tvf72RZ7s-tqPIemGHXoFxZdHaKc3JY3ys14jDdeSPUD7JYdGiVklKwdsNc1j8IvShHEnBIm8dnPQ-ozRKyT7gWPrEmF0zmA6rkYuiXsdHeHQ9-73cTmA-E-bhqKaVYDP7Jbhe7k0KPCpkIzQOyE4j-uuytSutU31yXB0d2I-6IpCDw0P8BDmqvwfIwXdYkU_7xbK_BRV4k6DnfnOysSOEuNqPrYqF4QNSyEYBzI7C-kDnPMw"
    # 不會過期的token
    credential = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjZGEzNjBmYjM2Y2QxNWZmODNhZjgzZTE3M2Y0N2ZmYzM2ZDExMWMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI3NjgzMDU1MzMyNTYtZWczaWZ0OTZzcG9sZ3RtNjlibzZyMzQyM2RmMTNjNzMuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI3NjgzMDU1MzMyNTYtZWczaWZ0OTZzcG9sZ3RtNjlibzZyMzQyM2RmMTNjNzMuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDUwNjc1NTk0NjI3ODUyNzU3OTgiLCJlbWFpbCI6InNkbTIwMjMubm8yQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoic3NlZG5xZG1pRUoza1NaU0hDeU5WQSIsIm5hbWUiOiJTRCBNIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FHTm15eFlOc0hQQVBjOHAzMkFzMzF3QXlmdU12elN2NXhrTEM0ZGNfLWFPPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IlNEIiwiZmFtaWx5X25hbWUiOiJNIiwibG9jYWxlIjoiemgtVFciLCJpYXQiOjE2ODExNTIxMzgsImV4cCI6MTY4MTE1NTczOH0.ZwzUKzyIwsQl6qqxIu9SbnBjed7pgiHKbGdlIq_3jxiicNrhR7DcHRdVCdG1XDydCiOnhTdS9FFnVm43UVYC_jjQEOM1Wehs6khqO_SFsumsT42xSFszr1TdEF1M-RsTVzzyeC4HH_iFp-HH0OFhJoJtmWLVk5NY0QPphYIqAL8Y8E2Pp41JOxp5_g_Tfh0HxSiQRppciWEe15lpV6LeqUKBnepTqJQ9zZhkW3Hb1heuT5e19brsaf3SQEbsFVVZwmGfsfuHkJPYEYLxdqU2O78ZiV6ebeeoiZdpvK4xMAeLxmVuGL_FCIRhUwohcFI7fpApEPj1laW9zMjNeXyg0Q"
    data = {"credential": credential}
    response = client.post(
        f"{get_server_api}{settings.API_V1_STR}/auth/sso-login", json=data
    )
    client.get(f"{get_server_api}{settings.API_V1_STR}/users/logout")
    assert response.status_code == 200
