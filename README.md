# Examen BentoML

Etapes à suivre :

1. Copy paste dans la racine (ou dossier X) du bento_image.tar
2. Dans la racine (ou dossier X) cloner ce repo :
```bash       
git clone https://github.com/maquirog/examen_bentoml.git
```
3. Entrez dans examen_bentoml/ :
```bash       
cd examen_bentoml/
```
4. Executez setup.sh avec la commande source :
```bash       
source setup.sh
```
C'est setup.sh qui execute pytest
```bash       
python3 -m pytest -o log_cli=1 -o log_cli_level=INFO test.py
```
Plus besoin de le faire directement

Voilà. Tout est bon. Rien d'autre à faire.

Resultat attendu :

![image](https://github.com/user-attachments/assets/5e4e5275-d27b-4924-a4eb-79424a3e73d3)
