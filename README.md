#### EXAMPLE : [CSV TO API on AZURE](https://csvapitest.azurewebsites.net/)

## Directions

1. Pull Repo 
2. Create venv in python ```py -m venv .venv``` (Windows) ```python3 -m venv .venv``` (macOS/Linux)
3. Enter venv with  ```venv\Scripts\activate``` (Windows) ```source .venv/bin/activate``` (macOS/Linux)
4. Run ```pip install -r requirments.txt```
5. Uncomment ALLOWED_HOSTS = ['localhost'] and Comment out ALLOWED_HOSTS = ['.azurewebsites.net'] 
6. Create Instance 
- ```manage.py makemigrations```
- ```manage.py migrate```
- ```manage.py createsuperuser```
7. Test Locally
- ```manage.py runserver```

8. Comment out ALLOWED_HOSTS = ['localhost'] and Uncomment ALLOWED_HOSTS = ['.azurewebsites.net'] 
9. [Follow Microsoft directions](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=django%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli) on delpoying on Azure Apps (Free Teir and VScode method recomended)