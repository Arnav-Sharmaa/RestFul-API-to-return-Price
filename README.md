
# **Assignment Submission**
## **About the project**

<p>A RestFul API that returns the price mentioned on this <a href="https://www.metal.com/Lithium-ion-Battery/202303240001"> Website</a> .
<br>
 Every time the API is hit,  python's beautiful soup library scrapping script is run which returns the latest price of the mentioned article to the Django view , which is then updated to the database using Object-relational mapping and the returned to the django API view.
 <br>
 <a href="https://dolphin-app-5muqt.ondigitalocean.app/price/">Deployed API Link </a>
</p>


## **Technologies Used**


<div align="left">
 <code><img height="50" src="https://static.djangoproject.com/img/logos/django-logo-negative.png" alt="Django" title="Django" /></code>
 <code><img height="50" src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white" alt="DRF" title="DRF" /></code>
 
</div>


## **Project Local Setup**

1. Install Virtual environment.
   ```
   pip install virtualenv
   ```
2. Create and Activate Virtual environment
    ```
    virtualenv venv
    ```
    ```
    venv/Scripts/Activate
    ```
3. Clone the repository
    ```
    git clone https://github.com/Arnav-Sharmaa/RestFul-API-to-return-Price.git
    ```
4. Go to the Project Folder
    ```
    cd PriceAPI
    ```
5. Install the Requirements
    ```
    pip install -r requirements.txt
    ```
6. Run server
    ```
    python manage.py runserver
    ```
