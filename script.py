import os
import sys
import boto3
from botocore.exceptions import NoCredentialsError

# --- CONFIGURATION DU SYSTÈME DE SAUVEGARDE ---
AWS_ACCESS_KEY = "FLAG{GIT_LEAKED_CREDS_BAD}"  
BUCKET_NAME = "grc99"
REGION_NAME = "eu-west-3"

def verifier_connexion_s3():
    """Vérifie l'accès au bucket de l'entreprise avant la sauvegarde"""
    print(f"[*] Connexion au bucket S3 : {BUCKET_NAME} ({REGION_NAME})...")
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=REGION_NAME
        )
        # Test de listage pour valider les droits du script
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix="confidentiel/")
        if 'Contents' in response:
            print("[+] Connexion établie. Dossier de sauvegarde détecté.")
            return True
        else:
            print("[-] Erreur : Dossier cible introuvable.")
            return False
    except NoCredentialsError:
        print("[-] Erreur : Identifiants AWS invalides.")
        return False
    except Exception as e:
        print(f"[-] Une erreur est survenue : {e}")
        return False

if __name__ == "__main__":
    print("=== Outil de Sauvegarde Automatique - v1.4.2 ===")
    if verifier_connexion_s3():
        print("[*] Prêt pour l'archivage des données de l'équipe...")
        # La suite du script de sauvegarde (simulation)
    else:
        sys.exit(1)
