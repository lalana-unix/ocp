# ocp
OpenShift container platform
Steps to Deploy a Streamlit App on OpenShift using s2i
Create a Streamlit App or use an existing one
Add a requirements.txt file with the app's dependencies
Add a .s2i/bin/run file with the following content:
APP_PORT=${APP_PORT:-"8080"}
streamlit run --server.port ${APP_PORT} app.py
Create a new OpenShift Project or use an existing one
From the OpenShift Web Console ("Developer" view, not Administrator), select the project you want to deploy the app into
Click the '+Add' option on the left-hand menu and select 'Import from Git'
Provide your Git repository's 'clone' URL.
Click 'Show advanced Git options'. Make sure your update the 'Git reference' value to match the branch you want to pull from, which is usually main
After the URL is validated, click 'Create' (accept the default options for the form that appears)
Wait for the build to complete and the app to be deployed
Access the app by clicking on the Route that is created for the app

Ref. https://github.com/redhat-na-ssa/streamlit-on-openshift