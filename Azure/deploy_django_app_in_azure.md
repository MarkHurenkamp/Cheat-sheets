# Deploying a Django application using Microsoft Azure
##### Per December 2021
<br>
<br>
Here's a quick overview of the steps taken to deploy a Django web app on Azure.

1. Register a (free) account at [Azure.com](https://azure.com)
2. Download and install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
3. Login using:
> az login
4. Copy and install a sample project:
```cmd
git clone https://github.com/Azure-Samples/python-docs-hello-django
cd python-docs-hello-django
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
5. Verify the sample project works by starting the development server:
> python manage.py runserver
6. Open [http://localhost:8000](http://localhost:8000/) to verify the app works
7. Close the dev. server (ctrl-C)
8. Deploy into Azure
> az webapp up --sku FREE --location westeurope --name <app-name>
*Note that FREE refers to the basic pricing, without this argument, a premium category is selected*
*The app-name must be globally unique*
*For a list of locations, use the following command:*
> az appservice list-locations --sku FREE
9. Once deployed, visit your website at https://<app-name>.azurewebsites.net 
10. In case of changes, update the local files and update the app via the following command:
> az webapp up
