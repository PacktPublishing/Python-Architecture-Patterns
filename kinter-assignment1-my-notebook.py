#!/usr/bin/env python
# coding: utf-8

# In[2]:


from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

# authenticate
credential = DefaultAzureCredential()

SUBSCRIPTION = "5343c674-1284-4684-bb76-3207c0187e6d"
RESOURCE_GROUP = "WeatherPrediction"
WS_NAME = "WeatherPrediction"
# Get a handle to the workspace
ml_client = MLClient(
    credential=credential,
    subscription_id=SUBSCRIPTION,
    resource_group_name=RESOURCE_GROUP,
    workspace_name=WS_NAME,
)


# In[3]:


ws = ml_client.workspaces.get(WS_NAME)
print(ws.location, ":", ws.resource_group)


# In[4]:


import os

train_src_dir = "./src"
os.makedirs(train_src_dir, exist_ok=True)


# In[5]:


get_ipython().run_cell_magic('writefile', '{train_src_dir}/main.py', 'import os\nimport argparse\nimport pandas as pd\nimport mlflow\nimport mlflow.sklearn\nfrom sklearn.ensemble import GradientBoostingClassifier\nfrom sklearn.metrics import classification_report\nfrom sklearn.model_selection import train_test_split\n\ndef main():\n    """Main function of the script."""\n\n    # input and output arguments\n    parser = argparse.ArgumentParser()\n    parser.add_argument("--data", type=str, help="path to input data")\n    parser.add_argument("--test_train_ratio", type=float, required=False, default=0.25)\n    parser.add_argument("--n_estimators", required=False, default=100, type=int)\n    parser.add_argument("--learning_rate", required=False, default=0.1, type=float)\n    parser.add_argument("--registered_model_name", type=str, help="model name")\n    args = parser.parse_args()\n   \n    # Start Logging\n    mlflow.start_run()\n\n    # enable autologging\n    mlflow.sklearn.autolog()\n\n    ###################\n    #<prepare the data>\n    ###################\n    print(" ".join(f"{k}={v}" for k, v in vars(args).items()))\n\n    print("input data:", args.data)\n    \n    credit_df = pd.read_csv(args.data, header=1, index_col=0)\n\n    mlflow.log_metric("num_samples", credit_df.shape[0])\n    mlflow.log_metric("num_features", credit_df.shape[1] - 1)\n\n    train_df, test_df = train_test_split(\n        credit_df,\n        test_size=args.test_train_ratio,\n    )\n    ####################\n    #</prepare the data>\n    ####################\n\n    ##################\n    #<train the model>\n    ##################\n    # Extracting the label column\n    y_train = train_df.pop("default payment next month")\n\n    # convert the dataframe values to array\n    X_train = train_df.values\n\n    # Extracting the label column\n    y_test = test_df.pop("default payment next month")\n\n    # convert the dataframe values to array\n    X_test = test_df.values\n\n    print(f"Training with data of shape {X_train.shape}")\n\n    clf = GradientBoostingClassifier(\n        n_estimators=args.n_estimators, learning_rate=args.learning_rate\n    )\n    clf.fit(X_train, y_train)\n\n    y_pred = clf.predict(X_test)\n\n    print(classification_report(y_test, y_pred))\n    ###################\n    #</train the model>\n    ###################\n\n    ##########################\n    #<save and register model>\n    ##########################\n    # Registering the model to the workspace\n    print("Registering the model via MLFlow")\n    mlflow.sklearn.log_model(\n        sk_model=clf,\n        registered_model_name=args.registered_model_name,\n        artifact_path=args.registered_model_name,\n    )\n\n    # Saving the model to a file\n    mlflow.sklearn.save_model(\n        sk_model=clf,\n        path=os.path.join(args.registered_model_name, "trained_model"),\n    )\n    ###########################\n    #</save and register model>\n    ###########################\n    \n    # Stop Logging\n    mlflow.end_run()\n\nif __name__ == "__main__":\n    main()\n')


# In[6]:


from azure.ai.ml import command
from azure.ai.ml import Input

registered_model_name = "credit_defaults_model"

job = command(
    inputs=dict(
        data=Input(
            type="uri_file",
            path="https://azuremlexamples.blob.core.windows.net/datasets/credit_card/default_of_credit_card_clients.csv",
        ),
        test_train_ratio=0.2,
        learning_rate=0.25,
        registered_model_name=registered_model_name,
    ),
    code="./src/",  # location of source code
    command="python main.py --data ${{inputs.data}} --test_train_ratio ${{inputs.test_train_ratio}} --learning_rate ${{inputs.learning_rate}} --registered_model_name ${{inputs.registered_model_name}}",
    environment="AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest",
    display_name="credit_default_prediction",
)


# In[7]:


ml_client.create_or_update(job)


# In[8]:


import uuid

# Creating a unique name for the endpoint
online_endpoint_name = "credit-endpoint-" + str(uuid.uuid4())[:8]


# In[9]:


# Expect the endpoint creation to take a few minutes
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Model,
    Environment,
)

# create an online endpoint
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="this is an online endpoint",
    auth_mode="key",
    tags={
        "training_dataset": "credit_defaults",
        "model_type": "sklearn.GradientBoostingClassifier",
    },
)

endpoint = ml_client.online_endpoints.begin_create_or_update(endpoint).result()

print(f"Endpoint {endpoint.name} provisioning state: {endpoint.provisioning_state}")


# In[10]:


endpoint = ml_client.online_endpoints.get(name=online_endpoint_name)

print(
    f'Endpoint "{endpoint.name}" with provisioning state "{endpoint.provisioning_state}" is retrieved'
)


# In[11]:


# Let's pick the latest version of the model
latest_model_version = max(
    [int(m.version) for m in ml_client.models.list(name=registered_model_name)]
)
print(f'Latest model is version "{latest_model_version}" ')


# In[18]:


# picking the model to deploy. Here we use the latest version of our registered model
model = ml_client.models.get(name=registered_model_name, version=latest_model_version)

# Expect this deployment to take approximately 6 to 8 minutes.
# create an online deployment.
# if you run into an out of quota error, change the instance_type to a comparable VM that is available.
# Learn more on https://azure.microsoft.com/en-us/pricing/details/machine-learning/.
blue_deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=online_endpoint_name,
    model=model,
    instance_type="STANDARD_DS2_V2",
    instance_count=1,
)

blue_deployment = ml_client.begin_create_or_update(blue_deployment).result()


# In[19]:


deploy_dir = "./deploy"
os.makedirs(deploy_dir, exist_ok=True)


# In[22]:


# test the blue deployment with some sample data
ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    request_file="./deploy/sample-request.json",
    deployment_name="blue",
)

