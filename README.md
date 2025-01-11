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
cookiecutter git@gitlab.com:danisco-nutrition-and-biosciences/lighthouse/automation/app-api-base-repos-tmpl.git

# if you use HTTPS for git
cookiecutter https://gitlab.com/danisco-nutrition-and-biosciences/lighthouse/automation/app-api-base-repos-tmpl.git
```
### Development environment
Use [Gitlab repository](https://gitlab.com/danisco-nutrition-and-biosciences/lighthouse/automation/gitlab) to create your project fillowing [doc](https://iffprod.atlassian.net/wiki/spaces/KCD/pages/102924326/Managing+GitLab+projects+with+Terraform)
[Project name](https://gitlab.com/danisco-nutrition-and-biosciences/lighthouse/automation/gitlab/energy-v2/-/blob/main/config.yaml?ref_type=heads#L3) variable will be used for deployment

Clone the repository in your local development environemnt


cookiecutter -f -o 'path to directory which contains your cloned repo' https://gitlab.com/danisco-nutrition-and-biosciences/lighthouse/automation/app-api-base-repos-tmpl.git 

During the execution you will be asked to provide variables 
* project_name - (!!!) should be the same as you provided during the creation of Terraform template 
* project_main_python_module - in most cases can be left default
* project_description" - description that will be visible in OpenAPI decumentation
* project_group - name of the repository group that the application belongs to eg. cedar, rochester, cork etc.

Follow the instruction in application README file to start it.
There are files with suffix 'tmpl'. Before first commit the files should be adjusted to project needs and suffix should be removed