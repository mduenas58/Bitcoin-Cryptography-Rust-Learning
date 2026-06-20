# Install Tools

Set up Kubernetes tools on your computer.

- 1: [Install and Set Up kubectl on Linux](https://kubernetes.io/docs/tasks/tools/_print/#pg-37b6179f23c8ad977cb9daa6d2da748a)
- 2: [Install and Set Up kubectl on macOS](https://kubernetes.io/docs/tasks/tools/_print/#pg-961fc70b732cb8df4fd11a3463b6545c)
- 3: [Install and Set Up kubectl on Windows](https://kubernetes.io/docs/tasks/tools/_print/#pg-2cc93d3011d707aeb6564bab02048f7a)

#### Note:

See the [Learning environment](https://kubernetes.io/docs/setup/learning-environment/) page to set up a practice environment.

## kubectl[](https://kubernetes.io/docs/tasks/tools/_print/#kubectl)

The Kubernetes command-line tool, [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/), allows you to run commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs. For more information including a complete list of kubectl operations, see the [`kubectl` reference documentation](https://kubernetes.io/docs/reference/kubectl/).

kubectl is installable on a variety of Linux platforms, macOS and Windows. Find your preferred operating system below.

- [Install kubectl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
- [Install kubectl on macOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
- [Install kubectl on Windows](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)

## kind[](https://kubernetes.io/docs/tasks/tools/_print/#kind)

[`kind`](https://kind.sigs.k8s.io/) lets you run Kubernetes on your local computer. This tool requires that you have either [Docker](https://www.docker.com/) or [Podman](https://podman.io/) installed.

The kind [Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/) page shows you what you need to do to get up and running with kind.

## minikube[](https://kubernetes.io/docs/tasks/tools/_print/#minikube)

Like `kind`, [`minikube`](https://minikube.sigs.k8s.io/) is a tool that lets you run Kubernetes locally. `minikube` runs an all-in-one or a multi-node local Kubernetes cluster on your personal computer (including Windows, macOS and Linux PCs) so that you can try out Kubernetes, or for daily development work.

You can follow the official [Get Started!](https://minikube.sigs.k8s.io/docs/start/) guide if your focus is on getting the tool installed.

Once you have `minikube` working, you can use it to [run a sample application](https://kubernetes.io/docs/tutorials/hello-minikube/).

## kubeadm[](https://kubernetes.io/docs/tasks/tools/_print/#kubeadm)

You can use the [kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/) tool to create and manage Kubernetes clusters. It performs the actions necessary to get a minimum viable, secure cluster up and running in a user friendly way.

[Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) shows you how to install kubeadm. Once installed, you can use it to [create a cluster](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/).

# 1 - Install and Set Up kubectl on Linux[](https://kubernetes.io/docs/tasks/tools/_print/#pg-37b6179f23c8ad977cb9daa6d2da748a)

## Before you begin[](https://kubernetes.io/docs/tasks/tools/_print/#before-you-begin)

You must use a kubectl version that is within one minor version difference of your cluster. For example, a v1.35 client can communicate with v1.34, v1.35, and v1.36 control planes. Using the latest compatible version of kubectl helps avoid unforeseen issues.

## Install kubectl on Linux[](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-on-linux)

The following methods exist for installing kubectl on Linux:

- [Install kubectl binary with curl on Linux](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-binary-with-curl-on-linux)
- [Install using native package management](https://kubernetes.io/docs/tasks/tools/_print/#install-using-native-package-management)
- [Install using other package management](https://kubernetes.io/docs/tasks/tools/_print/#install-using-other-package-management)

### Install kubectl binary with curl on Linux[](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-binary-with-curl-on-linux)

1. Download the latest release with the command:
    
    - [x86-64](https://kubernetes.io/docs/tasks/tools/_print/#download-binary-linux-0)
    - [ARM64](https://kubernetes.io/docs/tasks/tools/_print/#download-binary-linux-1)
    
    ```bash
    
       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
       
    ```
    
    #### Note:
    
    To download a specific version, replace the `$(curl -L -s https://dl.k8s.io/release/stable.txt)` portion of the command with the specific version.
    
    For example, to download version 1.35.0 on Linux x86-64, type:
    
    ```bash
    curl -LO https://dl.k8s.io/release/v1.35.0/bin/linux/amd64/kubectl
    ```
    
    And for Linux ARM64, type:
    
    ```bash
    curl -LO https://dl.k8s.io/release/v1.35.0/bin/linux/arm64/kubectl
    ```
    
2. Validate the binary (optional)
    
    Download the kubectl checksum file:
    
    - [x86-64](https://kubernetes.io/docs/tasks/tools/_print/#download-checksum-linux-0)
    - [ARM64](https://kubernetes.io/docs/tasks/tools/_print/#download-checksum-linux-1)
    
    ```bash
    
       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
       
    ```
    
    Validate the kubectl binary against the checksum file:
    
    ```bash
    echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
    ```
    
    If valid, the output is:
    
    ```console
    kubectl: OK
    ```
    
    If the check fails, `sha256` exits with nonzero status and prints output similar to:
    
    ```console
    kubectl: FAILED
    sha256sum: WARNING: 1 computed checksum did NOT match
    ```
    
    #### Note:
    
    Download the same version of the binary and checksum.
    
3. Install kubectl
    
    ```bash
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    ```
    
    #### Note:
    
    If you do not have root access on the target system, you can still install kubectl to the `~/.local/bin` directory:
    
    ```bash
    chmod +x kubectl
    mkdir -p ~/.local/bin
    mv ./kubectl ~/.local/bin/kubectl
    # and then append (or prepend) ~/.local/bin to $PATH
    ```
    
4. Test to ensure the version you installed is up-to-date:
    
    ```bash
    kubectl version --client
    ```
    
    Or use this for detailed view of version:
    
    ```cmd
    kubectl version --client --output=yaml
    ```
    

### Install using native package management[](https://kubernetes.io/docs/tasks/tools/_print/#install-using-native-package-management)

- [Debian-based distributions](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-install-0)
- [Red Hat-based distributions](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-install-1)
- [SUSE-based distributions](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-install-2)

1. Update the `apt` package index and install packages needed to use the Kubernetes `apt` repository:
    
    ```shell
    sudo apt-get update
    # apt-transport-https may be a dummy package; if so, you can skip that package
    sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
    ```
    
2. Download the public signing key for the Kubernetes package repositories. The same signing key is used for all repositories so you can disregard the version in the URL:
    
    ```shell
    # If the folder `/etc/apt/keyrings` does not exist, it should be created before the curl command, read the note below.
    # sudo mkdir -p -m 755 /etc/apt/keyrings
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.35/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg # allow unprivileged APT programs to read this keyring
    ```
    

#### Note:

In releases older than Debian 12 and Ubuntu 22.04, folder `/etc/apt/keyrings` does not exist by default, and it should be created before the curl command.

3. Add the appropriate Kubernetes `apt` repository. If you want to use Kubernetes version different than v1.35, replace v1.35 with the desired minor version in the command below:
    
    ```shell
    # This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
    echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.35/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
    sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list   # helps tools such as command-not-found to work correctly
    ```
    

#### Note:

To upgrade kubectl to another minor release, you'll need to bump the version in `/etc/apt/sources.list.d/kubernetes.list` before running `apt-get update` and `apt-get upgrade`. This procedure is described in more detail in [Changing The Kubernetes Package Repository](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/change-package-repository/).

4. Update `apt` package index, then install kubectl:
    
    ```shell
    sudo apt-get update
    sudo apt-get install -y kubectl
    ```
    

### Install using other package management[](https://kubernetes.io/docs/tasks/tools/_print/#install-using-other-package-management)

- [Snap](https://kubernetes.io/docs/tasks/tools/_print/#other-kubectl-install-0)
- [Homebrew](https://kubernetes.io/docs/tasks/tools/_print/#other-kubectl-install-1)

If you are on Ubuntu or another Linux distribution that supports the [snap](https://snapcraft.io/docs/core/install) package manager, kubectl is available as a [snap](https://snapcraft.io/) application.

```shell
snap install kubectl --classic
kubectl version --client
```

## Verify kubectl configuration[](https://kubernetes.io/docs/tasks/tools/_print/#verify-kubectl-configuration)

In order for kubectl to find and access a Kubernetes cluster, it needs a [kubeconfig file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/), which is created automatically when you create a cluster using [kube-up.sh](https://github.com/kubernetes/kubernetes/blob/master/cluster/kube-up.sh) or successfully deploy a Minikube cluster. By default, kubectl configuration is located at `~/.kube/config`.

Check that kubectl is properly configured by getting the cluster state:

```shell
kubectl cluster-info
```

If you see a URL response, kubectl is correctly configured to access your cluster.

If you see a message similar to the following, kubectl is not configured correctly or is not able to connect to a Kubernetes cluster.

```
The connection to the server <server-name:port> was refused - did you specify the right host or port?
```

For example, if you are intending to run a Kubernetes cluster on your laptop (locally), you will need a tool like [Minikube](https://minikube.sigs.k8s.io/docs/start/) to be installed first and then re-run the commands stated above.

If `kubectl cluster-info` returns the url response, but you can't access your cluster, check whether it is configured properly using the following command:

```shell
kubectl cluster-info dump
```

### Troubleshooting the 'No Auth Provider Found' error message[](https://kubernetes.io/docs/tasks/tools/_print/#no-auth-provider-found)

In Kubernetes 1.26, kubectl removed the built-in authentication for the following cloud providers' managed Kubernetes offerings. These providers have released kubectl plugins to provide the cloud-specific authentication. For instructions, refer to the following provider documentation:

- Azure AKS: [kubelogin plugin](https://azure.github.io/kubelogin/)
- Google Kubernetes Engine: [gke-gcloud-auth-plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin)

There could also be other causes for the same error message that are unrelated to that change.

## Optional kubectl configurations and plugins[](https://kubernetes.io/docs/tasks/tools/_print/#optional-kubectl-configurations-and-plugins)

### Enable shell autocompletion[](https://kubernetes.io/docs/tasks/tools/_print/#enable-shell-autocompletion)

kubectl provides autocompletion support for Bash, Zsh, Fish, and PowerShell, which can save you a lot of typing.

Below are the procedures to set up autocompletion for Bash, Fish, and Zsh.

- [Bash](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-autocompletion-0)
- [Fish](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-autocompletion-1)
- [Zsh](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-autocompletion-2)

### Introduction[](https://kubernetes.io/docs/tasks/tools/_print/#introduction)

The kubectl completion script for Bash can be generated with the command `kubectl completion bash`. Sourcing the completion script in your shell enables kubectl autocompletion.

However, the completion script depends on [**bash-completion**](https://github.com/scop/bash-completion), which means that you have to install this software first (you can test if you have bash-completion already installed by running `type _init_completion`).

### Install bash-completion[](https://kubernetes.io/docs/tasks/tools/_print/#install-bash-completion)

bash-completion is provided by many package managers (see [here](https://github.com/scop/bash-completion#installation)). You can install it with `apt-get install bash-completion` or `yum install bash-completion`, etc.

The above commands create `/usr/share/bash-completion/bash_completion`, which is the main script of bash-completion. Depending on your package manager, you have to manually source this file in your `~/.bashrc` file.

To find out, reload your shell and run `type _init_completion`. If the command succeeds, you're already set, otherwise add the following to your `~/.bashrc` file:

```bash
source /usr/share/bash-completion/bash_completion
```

Reload your shell and verify that bash-completion is correctly installed by typing `type _init_completion`.

### Enable kubectl autocompletion[](https://kubernetes.io/docs/tasks/tools/_print/#enable-kubectl-autocompletion)

#### Bash[](https://kubernetes.io/docs/tasks/tools/_print/#bash)

You now need to ensure that the kubectl completion script gets sourced in all your shell sessions. There are two ways in which you can do this:

- [User](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-bash-autocompletion-0)
- [System](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-bash-autocompletion-1)

```bash

echo 'source <(kubectl completion bash)' >>~/.bashrc
```

If you have an alias for kubectl, you can extend shell completion to work with that alias:

```bash
echo 'alias k=kubectl' >>~/.bashrc
echo 'complete -o default -F __start_kubectl k' >>~/.bashrc
```

#### Note:

bash-completion sources all completion scripts in `/etc/bash_completion.d`.

Both approaches are equivalent. After reloading your shell, kubectl autocompletion should be working. To enable bash autocompletion in current session of shell, source the ~/.bashrc file:

```bash
source ~/.bashrc
```

### Configure kuberc[](https://kubernetes.io/docs/tasks/tools/_print/#configure-kuberc)

See [kuberc](https://kubernetes.io/docs/reference/kubectl/kuberc/) for more information.

### Install `kubectl convert` plugin[](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-convert-plugin)

A plugin for Kubernetes command-line tool `kubectl`, which allows you to convert manifests between different API versions. This can be particularly helpful to migrate manifests to a non-deprecated api version with newer Kubernetes release. For more info, visit [migrate to non deprecated apis](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#migrate-to-non-deprecated-apis)

1. Download the latest release with the command:
    
    - [x86-64](https://kubernetes.io/docs/tasks/tools/_print/#download-convert-binary-linux-0)
    - [ARM64](https://kubernetes.io/docs/tasks/tools/_print/#download-convert-binary-linux-1)
    
    ```bash
    
       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert"
       
    ```
    
2. Validate the binary (optional)
    
    Download the kubectl-convert checksum file:
    
    - [x86-64](https://kubernetes.io/docs/tasks/tools/_print/#download-convert-checksum-linux-0)
    - [ARM64](https://kubernetes.io/docs/tasks/tools/_print/#download-convert-checksum-linux-1)
    
    ```bash
    
       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert.sha256"
       
    ```
    
    Validate the kubectl-convert binary against the checksum file:
    
    ```bash
    echo "$(cat kubectl-convert.sha256) kubectl-convert" | sha256sum --check
    ```
    
    If valid, the output is:
    
    ```console
    kubectl-convert: OK
    ```
    
    If the check fails, `sha256` exits with nonzero status and prints output similar to:
    
    ```console
    kubectl-convert: FAILED
    sha256sum: WARNING: 1 computed checksum did NOT match
    ```
    
    #### Note:
    
    Download the same version of the binary and checksum.
    
3. Install kubectl-convert
    
    ```bash
    sudo install -o root -g root -m 0755 kubectl-convert /usr/local/bin/kubectl-convert
    ```
    
4. Verify plugin is successfully installed
    
    ```shell
    kubectl convert --help
    ```
    
    If you do not see an error, it means the plugin is successfully installed.
    
5. After installing the plugin, clean up the installation files:
    
    ```bash
    rm kubectl-convert kubectl-convert.sha256
    ```
    

## What's next[](https://kubernetes.io/docs/tasks/tools/_print/#what-s-next)

- [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)
- See the [getting started guides](https://kubernetes.io/docs/setup/) for more about creating clusters.
- [Learn how to launch and expose your application.](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/)
- If you need access to a cluster you didn't create, see the [Sharing Cluster Access document](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/).
- Read the [kubectl reference docs](https://kubernetes.io/docs/reference/kubectl/kubectl/)

# 2 - Install and Set Up kubectl on macOS[](https://kubernetes.io/docs/tasks/tools/_print/#pg-961fc70b732cb8df4fd11a3463b6545c)

## Before you begin[](https://kubernetes.io/docs/tasks/tools/_print/#before-you-begin)

You must use a kubectl version that is within one minor version difference of your cluster. For example, a v1.35 client can communicate with v1.34, v1.35, and v1.36 control planes. Using the latest compatible version of kubectl helps avoid unforeseen issues.

## Install kubectl on macOS[](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-on-macos)

The following methods exist for installing kubectl on macOS:

- [Install kubectl on macOS](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-on-macos)
    - [Install kubectl binary with curl on macOS](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-binary-with-curl-on-macos)
    - [Install with Homebrew on macOS](https://kubernetes.io/docs/tasks/tools/_print/#install-with-homebrew-on-macos)
    - [Install with Macports on macOS](https://kubernetes.io/docs/tasks/tools/_print/#install-with-macports-on-macos)
- [Verify kubectl configuration](https://kubernetes.io/docs/tasks/tools/_print/#verify-kubectl-configuration)
- [Optional kubectl configurations and plugins](https://kubernetes.io/docs/tasks/tools/_print/#optional-kubectl-configurations-and-plugins)
    - [Enable shell autocompletion](https://kubernetes.io/docs/tasks/tools/_print/#enable-shell-autocompletion)
    - [Install `kubectl convert` plugin](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-convert-plugin)

### Install kubectl binary with curl on macOS[](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-binary-with-curl-on-macos)

1. Download the latest release:
    
    - [Intel](https://kubernetes.io/docs/tasks/tools/_print/#download-binary-macos-0)
    - [Apple Silicon](https://kubernetes.io/docs/tasks/tools/_print/#download-binary-macos-1)
    
    ```bash
    
       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
       
    ```
    
    #### Note:
    
    To download a specific version, replace the `$(curl -L -s https://dl.k8s.io/release/stable.txt)` portion of the command with the specific version.
    
    For example, to download version 1.35.0 on Intel macOS, type:
    
    ```bash
    curl -LO "https://dl.k8s.io/release/v1.35.0/bin/darwin/amd64/kubectl"
    ```
    
    And for macOS on Apple Silicon, type:
    
    ```bash
    curl -LO "https://dl.k8s.io/release/v1.35.0/bin/darwin/arm64/kubectl"
    ```
    
2. Validate the binary (optional)
    
    Download the kubectl checksum file:
    
    - [Intel](https://kubernetes.io/docs/tasks/tools/_print/#download-checksum-macos-0)
    - [Apple Silicon](https://kubernetes.io/docs/tasks/tools/_print/#download-checksum-macos-1)
    
    ```bash
    
       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl.sha256"
       
    ```
    
    Validate the kubectl binary against the checksum file:
    
    ```bash
    echo "$(cat kubectl.sha256)  kubectl" | shasum -a 256 --check
    ```
    
    If valid, the output is:
    
    ```console
    kubectl: OK
    ```
    
    If the check fails, `shasum` exits with nonzero status and prints output similar to:
    
    ```console
    kubectl: FAILED
    shasum: WARNING: 1 computed checksum did NOT match
    ```
    
    #### Note:
    
    Download the same version of the binary and checksum.
    
3. Make the kubectl binary executable.
    
    ```bash
    chmod +x ./kubectl
    ```
    
4. Move the kubectl binary to a file location on your system `PATH`.
    
    ```bash
    sudo mv ./kubectl /usr/local/bin/kubectl
    sudo chown root: /usr/local/bin/kubectl
    ```
    
    #### Note:
    
    Make sure `/usr/local/bin` is in your PATH environment variable.
    
5. Test to ensure the version you installed is up-to-date:
    
    ```bash
    kubectl version --client
    ```
    
    Or use this for detailed view of version:
    
    ```cmd
    kubectl version --client --output=yaml
    ```
    
6. After installing and validating kubectl, delete the checksum file:
    
    ```bash
    rm kubectl.sha256
    ```
    

### Install with Homebrew on macOS[](https://kubernetes.io/docs/tasks/tools/_print/#install-with-homebrew-on-macos)

If you are on macOS and using [Homebrew](https://brew.sh/) package manager, you can install kubectl with Homebrew.

1. Run the installation command:
    
    ```bash
    brew install kubectl
    ```
    
    or
    
    ```bash
    brew install kubernetes-cli
    ```
    
2. Test to ensure the version you installed is up-to-date:
    
    ```bash
    kubectl version --client
    ```
    

### Install with Macports on macOS[](https://kubernetes.io/docs/tasks/tools/_print/#install-with-macports-on-macos)

If you are on macOS and using [Macports](https://macports.org/) package manager, you can install kubectl with Macports.

1. Run the installation command:
    
    ```bash
    sudo port selfupdate
    sudo port install kubectl
    ```
    
2. Test to ensure the version you installed is up-to-date:
    
    ```bash
    kubectl version --client
    ```
    

## Verify kubectl configuration[](https://kubernetes.io/docs/tasks/tools/_print/#verify-kubectl-configuration)

In order for kubectl to find and access a Kubernetes cluster, it needs a [kubeconfig file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/), which is created automatically when you create a cluster using [kube-up.sh](https://github.com/kubernetes/kubernetes/blob/master/cluster/kube-up.sh) or successfully deploy a Minikube cluster. By default, kubectl configuration is located at `~/.kube/config`.

Check that kubectl is properly configured by getting the cluster state:

```shell
kubectl cluster-info
```

If you see a URL response, kubectl is correctly configured to access your cluster.

If you see a message similar to the following, kubectl is not configured correctly or is not able to connect to a Kubernetes cluster.

```
The connection to the server <server-name:port> was refused - did you specify the right host or port?
```

For example, if you are intending to run a Kubernetes cluster on your laptop (locally), you will need a tool like [Minikube](https://minikube.sigs.k8s.io/docs/start/) to be installed first and then re-run the commands stated above.

If `kubectl cluster-info` returns the url response, but you can't access your cluster, check whether it is configured properly using the following command:

```shell
kubectl cluster-info dump
```

### Troubleshooting the 'No Auth Provider Found' error message[](https://kubernetes.io/docs/tasks/tools/_print/#no-auth-provider-found)

In Kubernetes 1.26, kubectl removed the built-in authentication for the following cloud providers' managed Kubernetes offerings. These providers have released kubectl plugins to provide the cloud-specific authentication. For instructions, refer to the following provider documentation:

- Azure AKS: [kubelogin plugin](https://azure.github.io/kubelogin/)
- Google Kubernetes Engine: [gke-gcloud-auth-plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin)

There could also be other causes for the same error message that are unrelated to that change.

## Optional kubectl configurations and plugins[](https://kubernetes.io/docs/tasks/tools/_print/#optional-kubectl-configurations-and-plugins)

### Enable shell autocompletion[](https://kubernetes.io/docs/tasks/tools/_print/#enable-shell-autocompletion)

kubectl provides autocompletion support for Bash, Zsh, Fish, and PowerShell which can save you a lot of typing.

Below are the procedures to set up autocompletion for Bash, Fish, and Zsh.

- [Bash](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-autocompletion-0)
- [Fish](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-autocompletion-1)
- [Zsh](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-autocompletion-2)

### Introduction[](https://kubernetes.io/docs/tasks/tools/_print/#introduction)

The kubectl completion script for Bash can be generated with `kubectl completion bash`. Sourcing this script in your shell enables kubectl completion.

However, the kubectl completion script depends on [**bash-completion**](https://github.com/scop/bash-completion) which you thus have to previously install.

#### Warning:

There are two versions of bash-completion, v1 and v2. V1 is for Bash 3.2 (which is the default on macOS), and v2 is for Bash 4.1+. The kubectl completion script **doesn't work** correctly with bash-completion v1 and Bash 3.2. It requires **bash-completion v2** and **Bash 4.1+**. Thus, to be able to correctly use kubectl completion on macOS, you have to install and use Bash 4.1+ ([_instructions_](https://apple.stackexchange.com/a/292760)). The following instructions assume that you use Bash 4.1+ (that is, any Bash version of 4.1 or newer).

### Upgrade Bash[](https://kubernetes.io/docs/tasks/tools/_print/#upgrade-bash)

The instructions here assume you use Bash 4.1+. You can check your Bash's version by running:

```bash
echo $BASH_VERSION
```

If it is too old, you can install/upgrade it using Homebrew:

```bash
brew install bash
```

Reload your shell and verify that the desired version is being used:

```bash
echo $BASH_VERSION $SHELL
```

Homebrew usually installs it at `/usr/local/bin/bash`.

### Install bash-completion[](https://kubernetes.io/docs/tasks/tools/_print/#install-bash-completion)

#### Note:

As mentioned, these instructions assume you use Bash 4.1+, which means you will install bash-completion v2 (in contrast to Bash 3.2 and bash-completion v1, in which case kubectl completion won't work).

You can test if you have bash-completion v2 already installed with `type _init_completion`. If not, you can install it with Homebrew:

```bash
brew install bash-completion@2
```

As stated in the output of this command, add the following to your `~/.bash_profile` file:

```bash
brew_etc="$(brew --prefix)/etc" && [[ -r "${brew_etc}/profile.d/bash_completion.sh" ]] && . "${brew_etc}/profile.d/bash_completion.sh"
```

Reload your shell and verify that bash-completion v2 is correctly installed with `type _init_completion`.

### Enable kubectl autocompletion[](https://kubernetes.io/docs/tasks/tools/_print/#enable-kubectl-autocompletion)

You now have to ensure that the kubectl completion script gets sourced in all your shell sessions. There are multiple ways to achieve this:

- Source the completion script in your `~/.bash_profile` file:
    
    ```bash
    echo 'source <(kubectl completion bash)' >>~/.bash_profile
    ```
    
- Add the completion script to the `/usr/local/etc/bash_completion.d` directory:
    
    ```bash
    kubectl completion bash >/usr/local/etc/bash_completion.d/kubectl
    ```
    
- If you have an alias for kubectl, you can extend shell completion to work with that alias:
    
    ```bash
    echo 'alias k=kubectl' >>~/.bash_profile
    echo 'complete -o default -F __start_kubectl k' >>~/.bash_profile
    ```
    
- If you installed kubectl with Homebrew (as explained [here](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/#install-with-homebrew-on-macos)), then the kubectl completion script should already be in `/usr/local/etc/bash_completion.d/kubectl`. In that case, you don't need to do anything.
    
    #### Note:
    
    The Homebrew installation of bash-completion v2 sources all the files in the `BASH_COMPLETION_COMPAT_DIR` directory, that's why the latter two methods work.
    

In any case, after reloading your shell, kubectl completion should be working.

### Configure kuberc[](https://kubernetes.io/docs/tasks/tools/_print/#configure-kuberc)

See [kuberc](https://kubernetes.io/docs/reference/kubectl/kuberc/) for more information.

### Install `kubectl convert` plugin[](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-convert-plugin)

A plugin for Kubernetes command-line tool `kubectl`, which allows you to convert manifests between different API versions. This can be particularly helpful to migrate manifests to a non-deprecated api version with newer Kubernetes release. For more info, visit [migrate to non deprecated apis](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#migrate-to-non-deprecated-apis)

1. Download the latest release with the command:
    
    - [Intel](https://kubernetes.io/docs/tasks/tools/_print/#download-convert-binary-macos-0)
    - [Apple Silicon](https://kubernetes.io/docs/tasks/tools/_print/#download-convert-binary-macos-1)
    
    ```bash
    
       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl-convert"
       
    ```
    
2. Validate the binary (optional)
    
    Download the kubectl-convert checksum file:
    
    - [Intel](https://kubernetes.io/docs/tasks/tools/_print/#download-convert-checksum-macos-0)
    - [Apple Silicon](https://kubernetes.io/docs/tasks/tools/_print/#download-convert-checksum-macos-1)
    
    ```bash
    
       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl-convert.sha256"
       
    ```
    
    Validate the kubectl-convert binary against the checksum file:
    
    ```bash
    echo "$(cat kubectl-convert.sha256)  kubectl-convert" | shasum -a 256 --check
    ```
    
    If valid, the output is:
    
    ```console
    kubectl-convert: OK
    ```
    
    If the check fails, `shasum` exits with nonzero status and prints output similar to:
    
    ```console
    kubectl-convert: FAILED
    shasum: WARNING: 1 computed checksum did NOT match
    ```
    
    #### Note:
    
    Download the same version of the binary and checksum.
    
3. Make kubectl-convert binary executable
    
    ```bash
    chmod +x ./kubectl-convert
    ```
    
4. Move the kubectl-convert binary to a file location on your system `PATH`.
    
    ```bash
    sudo mv ./kubectl-convert /usr/local/bin/kubectl-convert
    sudo chown root: /usr/local/bin/kubectl-convert
    ```
    
    #### Note:
    
    Make sure `/usr/local/bin` is in your PATH environment variable.
    
5. Verify plugin is successfully installed
    
    ```shell
    kubectl convert --help
    ```
    
    If you do not see an error, it means the plugin is successfully installed.
    
6. After installing the plugin, clean up the installation files:
    
    ```bash
    rm kubectl-convert kubectl-convert.sha256
    ```
    

### Uninstall kubectl on macOS[](https://kubernetes.io/docs/tasks/tools/_print/#uninstall-kubectl-on-macos)

Depending on how you installed `kubectl`, use one of the following methods.

### Uninstall kubectl using the command-line[](https://kubernetes.io/docs/tasks/tools/_print/#uninstall-kubectl-using-the-command-line)

1. Locate the `kubectl` binary on your system:
    
    ```bash
    which kubectl
    ```
    
2. Remove the `kubectl` binary:
    
    ```bash
    sudo rm <path>
    ```
    
    Replace `<path>` with the path to the `kubectl` binary from the previous step. For example, `sudo rm /usr/local/bin/kubectl`.
    

### Uninstall kubectl using homebrew[](https://kubernetes.io/docs/tasks/tools/_print/#uninstall-kubectl-using-homebrew)

If you installed `kubectl` using Homebrew, run the following command:

```bash
brew remove kubectl
```

## What's next[](https://kubernetes.io/docs/tasks/tools/_print/#what-s-next)

- [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)
- See the [getting started guides](https://kubernetes.io/docs/setup/) for more about creating clusters.
- [Learn how to launch and expose your application.](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/)
- If you need access to a cluster you didn't create, see the [Sharing Cluster Access document](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/).
- Read the [kubectl reference docs](https://kubernetes.io/docs/reference/kubectl/kubectl/)

# 3 - Install and Set Up kubectl on Windows[](https://kubernetes.io/docs/tasks/tools/_print/#pg-2cc93d3011d707aeb6564bab02048f7a)

## Before you begin[](https://kubernetes.io/docs/tasks/tools/_print/#before-you-begin)

You must use a kubectl version that is within one minor version difference of your cluster. For example, a v1.35 client can communicate with v1.34, v1.35, and v1.36 control planes. Using the latest compatible version of kubectl helps avoid unforeseen issues.

## Install kubectl on Windows[](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-on-windows)

The following methods exist for installing kubectl on Windows:

- [Install kubectl binary on Windows (via direct download or curl)](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-binary-on-windows-via-direct-download-or-curl)
- [Install on Windows using Chocolatey, Scoop, or winget](https://kubernetes.io/docs/tasks/tools/_print/#install-nonstandard-package-tools)

### Install kubectl binary on Windows (via direct download or curl)[](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-binary-on-windows-via-direct-download-or-curl)

1. You have two options for installing kubectl on your Windows device
    
    - Direct download:
        
        Download the latest 1.35 patch release binary directly for your specific architecture by visiting the [Kubernetes release page](https://kubernetes.io/releases/download/#binaries). Be sure to select the correct binary for your architecture (e.g., amd64, arm64, etc.).
        
    - Using curl:
        
        If you have `curl` installed, use this command:
        
        ```powershell
        curl.exe -LO "https://dl.k8s.io/release/v1.35.0/bin/windows/amd64/kubectl.exe"
        ```
        
    
    #### Note:
    
    To find out the latest stable version (for example, for scripting), take a look at [https://dl.k8s.io/release/stable.txt](https://dl.k8s.io/release/stable.txt).
    
2. Validate the binary (optional)
    
    Download the `kubectl` checksum file:
    
    ```powershell
    curl.exe -LO "https://dl.k8s.io/v1.35.0/bin/windows/amd64/kubectl.exe.sha256"
    ```
    
    Validate the `kubectl` binary against the checksum file:
    
    - Using Command Prompt to manually compare `CertUtil`'s output to the checksum file downloaded:
        
        ```cmd
        CertUtil -hashfile kubectl.exe SHA256
        type kubectl.exe.sha256
        ```
        
    - Using PowerShell to automate the verification using the `-eq` operator to get a `True` or `False` result:
        
        ```powershell
         $(Get-FileHash -Algorithm SHA256 .\kubectl.exe).Hash -eq $(Get-Content .\kubectl.exe.sha256)
        ```
        
3. Append or prepend the `kubectl` binary folder to your `PATH` environment variable.
    
4. Test to ensure the version of `kubectl` is the same as downloaded:
    
    ```cmd
    kubectl version --client
    ```
    
    Or use this for detailed view of version:
    
    ```cmd
    kubectl version --client --output=yaml
    ```
    

#### Note:

[Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/#kubernetes) adds its own version of `kubectl` to `PATH`. If you have installed Docker Desktop before, you may need to place your `PATH` entry before the one added by the Docker Desktop installer or remove the Docker Desktop's `kubectl`.

### Install on Windows using Chocolatey, Scoop, or winget[](https://kubernetes.io/docs/tasks/tools/_print/#install-nonstandard-package-tools)

1. To install kubectl on Windows you can use either [Chocolatey](https://chocolatey.org/) package manager, [Scoop](https://scoop.sh/) command-line installer, or [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/) package manager.
    
    - [choco](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-win-install-0)
    - [scoop](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-win-install-1)
    - [winget](https://kubernetes.io/docs/tasks/tools/_print/#kubectl-win-install-2)
    
    ```powershell
    choco install kubernetes-cli
    ```
    
2. Test to ensure the version you installed is up-to-date:
    
    ```powershell
    kubectl version --client
    ```
    
3. Navigate to your home directory:
    
    ```powershell
    # If you're using cmd.exe, run: cd %USERPROFILE%
    cd ~
    ```
    
4. Create the `.kube` directory:
    
    ```powershell
    mkdir .kube
    ```
    
5. Change to the `.kube` directory you just created:
    
    ```powershell
    cd .kube
    ```
    
6. Configure kubectl to use a remote Kubernetes cluster:
    
    ```powershell
    New-Item config -type file
    ```
    

#### Note:

Edit the config file with a text editor of your choice, such as Notepad.

## Verify kubectl configuration[](https://kubernetes.io/docs/tasks/tools/_print/#verify-kubectl-configuration)

In order for kubectl to find and access a Kubernetes cluster, it needs a [kubeconfig file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/), which is created automatically when you create a cluster using [kube-up.sh](https://github.com/kubernetes/kubernetes/blob/master/cluster/kube-up.sh) or successfully deploy a Minikube cluster. By default, kubectl configuration is located at `~/.kube/config`.

Check that kubectl is properly configured by getting the cluster state:

```shell
kubectl cluster-info
```

If you see a URL response, kubectl is correctly configured to access your cluster.

If you see a message similar to the following, kubectl is not configured correctly or is not able to connect to a Kubernetes cluster.

```
The connection to the server <server-name:port> was refused - did you specify the right host or port?
```

For example, if you are intending to run a Kubernetes cluster on your laptop (locally), you will need a tool like [Minikube](https://minikube.sigs.k8s.io/docs/start/) to be installed first and then re-run the commands stated above.

If `kubectl cluster-info` returns the url response, but you can't access your cluster, check whether it is configured properly using the following command:

```shell
kubectl cluster-info dump
```

### Troubleshooting the 'No Auth Provider Found' error message[](https://kubernetes.io/docs/tasks/tools/_print/#no-auth-provider-found)

In Kubernetes 1.26, kubectl removed the built-in authentication for the following cloud providers' managed Kubernetes offerings. These providers have released kubectl plugins to provide the cloud-specific authentication. For instructions, refer to the following provider documentation:

- Azure AKS: [kubelogin plugin](https://azure.github.io/kubelogin/)
- Google Kubernetes Engine: [gke-gcloud-auth-plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin)

There could also be other causes for the same error message that are unrelated to that change.

## Optional kubectl configurations and plugins[](https://kubernetes.io/docs/tasks/tools/_print/#optional-kubectl-configurations-and-plugins)

### Enable shell autocompletion[](https://kubernetes.io/docs/tasks/tools/_print/#enable-shell-autocompletion)

kubectl provides autocompletion support for Bash, Zsh, Fish, and PowerShell, which can save you a lot of typing.

Below are the procedures to set up autocompletion for PowerShell.

The kubectl completion script for PowerShell can be generated with the command `kubectl completion powershell`.

To do so in all your shell sessions, add the following line to your `$PROFILE` file:

```powershell
kubectl completion powershell | Out-String | Invoke-Expression
```

This command will regenerate the auto-completion script on every PowerShell start up. You can also add the generated script directly to your `$PROFILE` file.

To add the generated script to your `$PROFILE` file, run the following line in your powershell prompt:

```powershell
kubectl completion powershell >> $PROFILE
```

After reloading your shell, kubectl autocompletion should be working.

### Configure kuberc[](https://kubernetes.io/docs/tasks/tools/_print/#configure-kuberc)

See [kuberc](https://kubernetes.io/docs/reference/kubectl/kuberc/) for more information.

### Install `kubectl convert` plugin[](https://kubernetes.io/docs/tasks/tools/_print/#install-kubectl-convert-plugin)

A plugin for Kubernetes command-line tool `kubectl`, which allows you to convert manifests between different API versions. This can be particularly helpful to migrate manifests to a non-deprecated api version with newer Kubernetes release. For more info, visit [migrate to non deprecated apis](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#migrate-to-non-deprecated-apis)

1. Download the latest release with the command:
    
    ```powershell
    curl.exe -LO "https://dl.k8s.io/release/v1.35.0/bin/windows/amd64/kubectl-convert.exe"
    ```
    
2. Validate the binary (optional).
    
    Download the `kubectl-convert` checksum file:
    
    ```powershell
    curl.exe -LO "https://dl.k8s.io/v1.35.0/bin/windows/amd64/kubectl-convert.exe.sha256"
    ```
    
    Validate the `kubectl-convert` binary against the checksum file:
    
    - Using Command Prompt to manually compare `CertUtil`'s output to the checksum file downloaded:
        
        ```cmd
        CertUtil -hashfile kubectl-convert.exe SHA256
        type kubectl-convert.exe.sha256
        ```
        
    - Using PowerShell to automate the verification using the `-eq` operator to get a `True` or `False` result:
        
        ```powershell
        $($(CertUtil -hashfile .\kubectl-convert.exe SHA256)[1] -replace " ", "") -eq $(type .\kubectl-convert.exe.sha256)
        ```
        
3. Append or prepend the `kubectl-convert` binary folder to your `PATH` environment variable.
    
4. Verify the plugin is successfully installed.
    
    ```shell
    kubectl convert --help
    ```
    
    If you do not see an error, it means the plugin is successfully installed.
    
5. After installing the plugin, clean up the installation files:
    
    ```powershell
    del kubectl-convert.exe
    del kubectl-convert.exe.sha256
    ```