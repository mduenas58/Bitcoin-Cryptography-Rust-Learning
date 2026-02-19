Practicing `kubectl` hands-on is the best way to solidify your understanding of Kubernetes. Based on your request for sample labs, I've put together a guide that combines conceptual learning with direct application.

We'll start with a reference for common commands and then move into structured, practical exercises you can run on a live cluster.

### 📚 **Your `kubectl` Command Reference**

Before diving into the labs, here's a quick overview of essential `kubectl` commands, categorized by what they do. You can refer back to this as you practice.

| Category | Command Example | Description |
| :--- | :--- | :--- |
| **Cluster Info** | `kubectl cluster-info` | Displays information about the cluster . |
| | `kubectl get nodes` | Lists all the nodes (machines) in your cluster . |
| | `kubectl version` | Shows the version of both the client and the server . |
| **Resource Management** | `kubectl get pods` | Lists all pods in the current namespace . |
| | `kubectl get pods -o wide` | Lists pods with more details, like the node they're on . |
| | `kubectl get all` | Shows a summary of common resources like pods, services, and deployments. |
| | `kubectl describe pod <pod-name>` | Shows detailed status and events for a specific pod . |
| | `kubectl delete pod <pod-name>` | Deletes a specific pod . |
| | `kubectl logs <pod-name>` | Prints the logs from a container in a pod . |
| **Creation & Configuration** | `kubectl create deployment <name> --image=<image>` | Creates a deployment that manages a pod running a specified container image . |
| | `kubectl apply -f <filename.yaml>` | Creates or updates resources defined in a YAML file . |
| | `kubectl delete -f <filename.yaml>` | Deletes resources defined in a YAML file . |
| | `kubectl label pod <pod-name> <key>=<value>` | Adds or updates a label on a pod . |
| **Troubleshooting** | `kubectl exec -it <pod-name> -- /bin/sh` | Starts an interactive shell inside a running container . |
| | `kubectl logs -f <pod-name>` | Streams logs from a pod in real-time . |
| | `kubectl get events` | Shows recent events in the cluster . |
| | `kubectl port-forward pod/<pod-name> <local-port>:<pod-port>` | Forwards a local port to a port on the pod . |

### 🧪 **Hands-on Lab Practice Exercises**

These exercises are designed to be done in sequence. They start with verifying your environment and progress through creating, inspecting, and modifying resources. You can run these on any Kubernetes cluster, including the **free KodeKloud labs** you mentioned, **Minikube** , or a cloud-based cluster like AKS .

#### **⚙️ Exercise 1: Environment Setup and Basic Inspection**

This first exercise ensures your `kubectl` is talking to a cluster and helps you explore its basic components.

1.  **Check Cluster Status:** First, let's confirm `kubectl` is installed and can communicate with your cluster. Run `kubectl version --short` to see both client and server versions . Then, get an overview of the cluster's health and address with `kubectl cluster-info` .
2.  **List Nodes:** See the machines that make up your cluster. Run `kubectl get nodes` . You should see at least one node in a `Ready` state. To get more details about a specific node (e.g., its capacity, labels, and status), use `kubectl describe nodes <node-name-from-previous-command>`.

#### **🚀 Exercise 2: Deploying and Exposing Your First Application**

Now you'll create a real application and make it accessible.

1.  **Create a Deployment:** Deploy an instance of a web application. In your terminal, run:
    ```bash
    kubectl create deployment hello-world --image=registry.k8s.io/echoserver:1.4
    ```
    This command creates a deployment named `hello-world` that runs a container from the specified image . You can verify it worked by listing your deployments with `kubectl get deployments`.
2.  **Inspect the Pod:** Your deployment created a pod to run the container. List all pods to see it: `kubectl get pods -o wide` . Notice the pod's name, its status, and which node it's running on. To see deeper details about the pod's lifecycle and configuration, run `kubectl describe pod <pod-name-from-previous-command>`.
3.  **Expose the Deployment as a Service:** By default, the pod is only accessible inside the cluster. To make it available to you, you'll expose it via a service. Run:
    ```bash
    kubectl expose deployment hello-world --type=NodePort --port=8080 --target-port=8080
    ```
    This creates a service that opens a port on the node itself .
4.  **Access Your Application:**
    *   First, find the port assigned to your service: `kubectl get service hello-world`. Look for the `PORT(S)` column; it will show something like `8080:3xxxx/TCP`. The high-numbered port (e.g., `3xxxx`) is the `NodePort`.
    *   To access it, you'll need your node's address. If using Minikube, you can simply run `minikube service hello-world`. In other environments, you might use `kubectl port-forward service/hello-world 7080:8080` and then open `http://localhost:7080` in your browser .
5.  **View Logs:** Generate some traffic to your app (by refreshing the page a few times) and then view its logs: `kubectl logs -f <pod-name>` . The `-f` flag lets you "follow" the logs in real-time.

#### **🏷️ Exercise 3: Working with Pod Labels**

Labels are key-value pairs that help you organize and select subsets of resources . This exercise builds on the previous one.

1.  **Add a Label:** Add a new label to your running pod. Identify your pod name and then run:
    ```bash
    kubectl label pod <pod-name> environment=test
    ```
2.  **View Labels:** See the labels on your pod by running `kubectl get pods --show-labels` . You should see your new `environment=test` label in the list.
3.  **Update a Label:** Labels can be changed. Update your label from `test` to `development`. Because the label already exists, you must use the `--overwrite` flag:
    ```bash
    kubectl label pod <pod-name> environment=development --overwrite
    ```
    Verify the change with `kubectl get pods --show-labels` .
4.  **Delete a Label:** Remove the label entirely. The syntax for deleting a label is to add a hyphen (`-`) at the end of the key name:
    ```bash
    kubectl label pod <pod-name> environment-
    ```
    Run `kubectl get pods --show-labels` again to confirm the label is gone .

#### **🩺 Exercise 4: Basic Troubleshooting**

This exercise simulates a common task: debugging a misconfigured application.

1.  **Create a Pod with an Issue:** Let's create a pod that tries to use an image that doesn't exist. In your terminal, run the following command:
    ```bash
    kubectl run faulty-app --image=thisimagedoesnotexist:latest
    ```
2.  **Watch What Happens:** Immediately check the pod's status: `kubectl get pods`. You'll see `faulty-app` might show a status like `ErrImagePull` or `ImagePullBackOff`.
3.  **Investigate the Issue:**
    *   To get a human-readable explanation of what's happening, use `kubectl describe pod faulty-app` . Look towards the bottom in the `Events:` section. You should see a clear error message indicating that it failed to pull the image.
    *   To see the raw logs from the container's attempt to run, use `kubectl logs faulty-app`. Since the container never started, there might not be any application logs, which is also a clue.
4.  **Clean Up:** Once you've finished your investigation, delete the faulty pod: `kubectl delete pod faulty-app` .

These exercises cover the core workflow of a developer or operator: deploying, inspecting, configuring, and debugging applications on Kubernetes. By working through them, you're building muscle memory for the commands you'll use every day.

What aspect of `kubectl` would you like to explore next? We could dive into managing applications with YAML configuration files, or perhaps look at how to scale your `hello-world` deployment up and down.