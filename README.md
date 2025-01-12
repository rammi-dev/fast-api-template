# Project template for Microservice Backend Application project

The templates serves as a single process async microservices application baseline.
Concentrate on work that actually matters and create your project repository in minutes using [Cookiecutter](https://cookiecutter.readthedocs.io) template.

---

## Usage
### Playground environment
```bash
pip install cookiecutter

During the execution you will be asked to provide variables 
* project_name - project name of your choice
* project_main_python_module - in most cases can be left default
* project_description" - description that will be visible in OpenAPI decumentation
* project_group - name of the repository group that the application belongs to eg. cedar, rochester, cork etc.

# if you use SSH for git
cookiecutter git@github.com:rammi-dev/fast-api-template.git

# if you use HTTPS for git
cookiecutter https://github/rammi-dev/fast-api-template.git
```


Clone the repository in your local development environemnt


cookiecutter -f -o 'path to directory which contains your cloned repo' git@github.com:rammi-dev/fast-api-template.git

During the execution you will be asked to provide variables 
* project_name - (!!!) should be the same as you provided during the creation of Terraform template 
* project_main_python_module - in most cases can be left default
* project_description" - description that will be visible in OpenAPI decumentation
* project_group - name of the repository group that the application belongs to 

Follow the instruction in application README file to start it.
There are files with suffix 'tmpl'. Before first commit the files should be adjusted to project needs and suffix should be removed
