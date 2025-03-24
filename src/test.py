import requests
import time


# Test de l'authentification JWT :
# Vérifiez que l'authentification échoue si le jeton JWT est manquant ou invalide.
# Vérifiez que l'authentification échoue si le jeton JWT a expiré.
# Vérifiez que l'authentification réussit avec un jeton JWT valide.

# Test de l'API de connexion :
# Vérifiez que l'API renvoie un jeton JWT valide pour des identifiants utilisateur corrects.
# Vérifiez que l'API renvoie une erreur 401 pour des identifiants utilisateur incorrects.

# Test de l'API de prédiction :
# Vérifiez que l'API renvoie une erreur 401 si le jeton JWT est manquant ou invalide.
# Vérifiez que l'API renvoie une prédiction valide pour des données d'entrée correctes.
# Vérifiez que l'API renvoie une erreur pour des données d'entrée invalides.

# The URL of the login and prediction endpoints
login_url = "http://127.0.0.1:3000/login"
predict_url = "http://127.0.0.1:3000/predict"

# Données de connexion
credentials = {
    "username": "user456",
    "password": "password456"
}

# Data to be sent to the prediction endpoint
data = {
    "gre": 300,
    "toefl": 103,
    "univ_ranking": 4,
    "sop": 4,
    "lor": 5,
    "cgpa": 8.4,
    "research": 0
}

# def test_1_1_JWT_missing_token():
#     # Send a POST request to the prediction
#     response = requests.post(
#         predict_url,
#         headers={
#             "Content-Type": "application/json"
#         },
#         json=data
#     )
#     assert response.status_code == 401

# def test_1_1_JWT_invalid_token():
#     # Send a POST request to the prediction
#     token = "Fake token"
#     response = requests.post(
#         predict_url,
#         headers={
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {token}"
#         },
#         json=data
#     )
#     assert response.status_code == 401

# def test_1_2_JWT_expired_token():
#     login_response = requests.post(
#         login_url,
#         headers={"Content-Type": "application/json"},
#         json=credentials
#     )
#     # Send a POST request to the prediction
#     token = login_response.json().get("token")
#     time.sleep(10)
#     response = requests.post(
#         predict_url,
#         headers={
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {token}"
#         },
#         json=data
#     )
#     assert response.status_code == 401

# def test_1_3_JWT_valid_token():
#     login_response = requests.post(
#         login_url,
#         headers={"Content-Type": "application/json"},
#         json=credentials
#     )
#     # Send a POST request to the prediction
#     token = login_response.json().get("token")
#     response = requests.post(
#         predict_url,
#         headers={
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {token}"
#         },
#         json=data
#     )
#     assert response.status_code == 200


def test_2_1_login_correct_user_id():
    login_response = requests.post(
        login_url,
        headers={"Content-Type": "application/json"},
        json=credentials
    )

    assert login_response.status_code == 200

def test_2_2_login_wrong_user_id():
    wrong_credentials = {
        "username": "wrong user id",
        "password": "password456"
    }
    login_response = requests.post(
        login_url,
        headers={"Content-Type": "application/json"},
        json=wrong_credentials
    )
    assert login_response.status_code is not 200

# # Check if the login was successful
# if login_response.status_code == 200:
#     token = login_response.json().get("token")
#     # print("Token JWT obtenu:", token)


#     # print("Wait 10 seconds to make the JWT token expire")
#     # time.sleep(10)

#     # Send a POST request to the prediction
#     response = requests.post(
#         predict_url,
#         headers={
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {token}"
#         },
#         json=data
#     )

#     print("Réponse de l'API de prédiction:", response.text)
# else:
#     print("Erreur lors de la connexion:", login_response.text)