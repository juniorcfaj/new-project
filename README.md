# New Project on Udacity
Build a CI/CD Pipeline to Udacity

## Project Plan

* Trello board: https://trello.com/b/yuFaFEEq/build-a-ci-cd-pipeline
* Spreadsheet: https://docs.google.com/spreadsheets/d/1YAxcaTxExw9aZCUxsD3dbJK6kDFH-tC8g1qA7hfC3zA/edit?usp=sharing

## Instructions

Create a repo on GitHub and clone it

```
git clone <repo link>
cd <repo directory>
git pull
make all

# Create a new App Service
az webapp up -n <your-appservice>
```

* Project running on Azure App Service

![image](https://user-images.githubusercontent.com/46963611/144729359-f8f05971-d680-407d-b2f3-ca3906ecae93.png)

* Project cloned into Azure Cloud Shell

![git-clone](https://user-images.githubusercontent.com/46963611/144729365-58b7f48f-38c4-4400-9c52-0d1a60bc3598.PNG)

* Passing tests that are displayed after running the make all command from the Makefile

![make-all-complete](https://user-images.githubusercontent.com/46963611/144729369-42cbfb80-1254-44d0-8fdc-7f806e3d5d63.PNG)

* Output of a test run

![image](https://user-images.githubusercontent.com/46963611/144729382-8376fd67-3d62-4f86-bdd5-d538596b16b9.png)

* Successful deploy of the project in Azure Pipelines

![image](https://user-images.githubusercontent.com/46963611/144729400-d1ee6ca3-2a65-46f7-9c70-4f301644bea6.png)

![pipeline working](https://user-images.githubusercontent.com/46963611/144729394-66dcce3e-5c08-4fb8-aadd-cc4f6e278cc0.PNG)

* Running Azure App Service from Azure Pipelines automatic deployment

![image](https://user-images.githubusercontent.com/46963611/144729407-809e72c2-3b2c-495a-8ea1-573de9c3087d.png)

* Successful prediction from deployed flask app in Azure Cloud Shell.

![image](https://user-images.githubusercontent.com/46963611/144729926-70a1d0b1-d601-42f6-a261-59000a754fc3.png)

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

![image](https://user-images.githubusercontent.com/46963611/144729426-51dab074-2788-48dd-a52e-45e9e906222a.png)

## GitHub Actions Build: Passed

![Python application test with Github Actions](https://github.com/noahgift/azure-devops/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

Build process must run and complete

![github-actions-test-passed](https://user-images.githubusercontent.com/46963611/144727471-fdd19be7-9390-4c61-81bc-d329d72471ae.PNG)

## Enhancements

To improve the application, you can just modify the source code on GitHub and it will update automaticly.

Source code: https://github.com/juniorcfaj/new-project

## Demo

Watch the project steps on YouTube
https://youtu.be/1ojfYCiaS-4
