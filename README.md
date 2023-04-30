
Cloud Native Monitoring Application
===================================

**Introduction**
----------------

The System Monitoring web application is designed to provide real-time monitoring of system resources such as CPU and memory utilization. The application is built using Python and Flask web framework, with data visualization using the Plotly library. The application is deployed on Kubernetes using Minikube, allowing for easy scaling and management.

**Requirements**
----------------

To run the System Monitoring web application, you will need the following:

*   Python 3 installed on your system

*   Flask, Plotly, and psutil Python packages installed

*   A Kubernetes cluster, such as Minikube

*   A web browser to view the application

**Agenda**
----------

The System Monitoring web application will display the current CPU and memory utilization of the system, as well as provide a message if either value exceeds 80%. The agenda for the project is as follows:

1.  Install required Python packages.

2.  Build the Flask web application with data visualization using Plotly.

3.  Deploy the application to Kubernetes using Minikube.

4.  Test the application and verify that it is displaying system resource utilization data correctly.

5.  Scale the application and verify that the data is updated in real-time.

**Execution**
-------------

### **1\. Install Required Python Packages**

Before building the web application, you will need to install the necessary Python packages using the following command:

    pip install Flask Plotly psutil

This will install the Flask web framework, Plotly library for data visualization, and the psutil package for system monitoring.

### **2\. Build the Flask Web Application**

The web application is built using Flask and Plotly, and the code is provided in the `**app.py**` file. Run the following command to start the application on your local machine:

    python app.py

This will start a local web server and the application will be accessible at `**http://localhost:5000**`.

### **3\. Deploy the Application to Kubernetes**

To deploy the application to Kubernetes, you will first need to start a Minikube cluster by running the following command:

    minikube start

This will start a single-node Kubernetes cluster on your local machine. Next, run the following command to deploy the application to Kubernetes:

    kubectl apply -f deployment.yaml

This will create a deployment and a service for the application.

### **4\. Test the Application**

To test the application, you can access it by running the following command to get the IP address and port number of the application:

    
    minikube service my-flask-app-service --url

This will return a URL that you can open in your web browser to access the application. Verify that the CPU and memory utilization data is displayed correctly.

### **5\. Scale the Application**

To scale the application, you can run the following command to increase the number of replicas of the deployment:

    kubectl scale deployment my-flask-app-deployment --replicas=3

This will create two additional replicas of the application, allowing you to test that the data is updated in real-time.

**Result**
----------

After completing the steps above, you should have a fully functional System Monitoring web application deployed on Kubernetes, displaying real-time system resource utilization data. The application can be easily scaled to handle increased traffic and monitor more resources.
