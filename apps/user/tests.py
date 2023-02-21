# apps/user/tests.py
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from apps.user.models import User, Nationality

class TestUser(APITestCase):
    """
        users app의 API 3개(회원가입, 로그인, 회원탈퇴) unit test
    """
    def setUp(self):
        self.nationality = Nationality(
            country_idx   = 1,
            country_code  = "KR",
            country_dcode = "+82",
            country_name  = "South Korea",
        )
        self.nationality.save()

        self.user = User(
            username    = "test",
            password    = make_password("test"),
            name        = "HyeonsooKim",
            email       = "test@test.com",
            birth_date  = "2000-01-03",
            gender      = "Female",
            nationality = self.nationality,
            city        = "Seoul",
        )

        self.user.save()
        
    def test_register_success(self):
        """ 회원가입 성공 테스트 """

        self.user_data = {
            "username"      : "test1",
            "password"      : "111222333",
            "password_check": "111222333",
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            "gender"        : "Male",
            "birth_date"    : "1984-07-07",
            "nationality"   : 1,
            "city"          : "Seoul"
            }

        self.register_url = "/api/users/sign-up/"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_register_id_ckeck_fail(self):
        """ 회원가입 중복아이디 테스트 """
        
        self.user_data = {
            "username"      : "test",
            "password"      : "111222333",
            "password_check": "111222333",
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            "gender"        : "Male",
            "birth_date"    : "1984-07-07",
            "nationality"   : 1,
            "city"          : "Seoul"                     
            }

        self.register_url = "/api/users/sign-up/"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_password_check_fail(self):
        """ 회원 가입시 패스워드 확인 실패 테스트 """
        
        self.user_data = {
            "username"      : "test2",
            "password"      : "111222333",
            "password_check": "111111111", # 패스워드 확인 오류
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            "gender"        : "Male",
            "birth_date"    : "1984-07-07",
            "nationality"   : 1,
            "city"          : "Seoul"                 
            }

        self.register_url = "/api/users/sign-up/"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_success(self):
        """ 로그인 성공 테스트 """

        self.login_url = "/api/users/sign-in/"
        data = {
                "username": "test",
                "password": "test",
            }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_password_fail(self):
        """ 비밀번호 불일치 테스트 """

        self.login_url = "/api/users/sign-in/"
        data= {
                "username": "test",
                "password": "test1",
            }
        response= self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'username': "{'detail': 'No active account found with the given credentials'}"})

    def test_withdraw_success(self):
        """ 회원탈퇴 테스트 """

        self.withdraw_url = f"/api/users/{self.user.id}/withdraw/"

        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.delete(self.withdraw_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)