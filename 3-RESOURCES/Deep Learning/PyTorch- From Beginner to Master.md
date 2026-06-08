# PyTorch: From Beginner to Master

A complete guide to PyTorch — what it is, why it matters, five worked examples, and a structured path to mastery.

---

## Table of Contents

1. [What Is PyTorch?](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#1-what-is-pytorch)
2. [What PyTorch Is Used For](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#2-what-pytorch-is-used-for)
3. [Core Concepts You Must Know](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#3-core-concepts-you-must-know)
4. [Installation](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#4-installation)
5. [Five Worked Examples](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#5-five-worked-examples)
    - [Example 1: Tensors & Autograd (Beginner)](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#example-1-tensors--autograd-beginner)
    - [Example 2: Linear Regression from Scratch (Beginner)](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#example-2-linear-regression-from-scratch-beginner)
    - [Example 3: Image Classifier with a Neural Net (Intermediate)](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#example-3-image-classifier-with-a-neural-net-intermediate)
    - [Example 4: Convolutional Neural Network on CIFAR-10 (Intermediate/Advanced)](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#example-4-convolutional-neural-network-on-cifar-10-intermediateadvanced)
    - [Example 5: Transfer Learning with a Pretrained Model (Advanced)](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#example-5-transfer-learning-with-a-pretrained-model-advanced)
6. [Learning Path: Beginner to Master](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#6-learning-path-beginner-to-master)
7. [Resources](https://claude.ai/cowork/local_4700e376-246a-464d-8de8-5744eebbd1bf#7-resources)

---

## 1. What Is PyTorch?

**PyTorch** is an open-source machine learning framework, originally developed by Meta AI (Facebook) and now governed by the PyTorch Foundation under the Linux Foundation. It is one of the two dominant deep learning frameworks in the world (the other being TensorFlow), and it is the framework of choice for the majority of academic research and a growing share of production systems.

At its heart, PyTorch gives you three things:

- **A powerful n-dimensional array (`Tensor`)** — like NumPy arrays, but able to run on GPUs (and other accelerators) for massive speedups.
- **Automatic differentiation (`autograd`)** — it automatically computes gradients (derivatives) of your computations, which is the engine that powers neural network training.
- **A deep learning library (`torch.nn`)** — pre-built layers, loss functions, and optimizers to build and train models quickly.

The defining design choice is its **dynamic computation graph** (also called "define-by-run"). The graph of operations is built on the fly as your code executes, so you can use ordinary Python control flow (loops, `if` statements, recursion) inside your models and debug them with normal Python tools. This makes PyTorch feel intuitive and "Pythonic," which is a big reason for its popularity.

---

## 2. What PyTorch Is Used For

PyTorch is general-purpose, but it powers a few major domains especially well:

- **Computer Vision** — image classification, object detection, segmentation, generation. Companion library: `torchvision`.
- **Natural Language Processing & Large Language Models** — transformers, translation, chatbots, embeddings. Most modern LLM research and many production models (and frameworks like Hugging Face Transformers) are built on PyTorch.
- **Audio & Speech** — speech recognition, text-to-speech, music generation. Companion library: `torchaudio`.
- **Generative AI** — diffusion models (image generation), GANs, variational autoencoders.
- **Reinforcement Learning** — training agents for games, robotics, and control.
- **Scientific & Tabular ML** — recommendation systems, time-series forecasting, physics simulation, drug discovery.
- **Research & prototyping** — its flexibility makes it the standard tool for inventing and testing new model architectures.

In short: if a task involves training a model to learn patterns from data — especially with neural networks — PyTorch is a leading tool for the job.

---

## 3. Core Concepts You Must Know

Before the examples, here is the mental model. Almost everything in PyTorch revolves around these pieces:

|Concept|What it is|
|---|---|
|`torch.Tensor`|The fundamental data structure: a multi-dimensional array that can live on CPU or GPU.|
|`autograd`|The automatic differentiation engine. Set `requires_grad=True` and PyTorch tracks operations to compute gradients via `.backward()`.|
|`torch.nn.Module`|The base class for all models and layers. You subclass it to define your network.|
|Loss function|Measures how wrong the model is (e.g., `nn.MSELoss`, `nn.CrossEntropyLoss`).|
|Optimizer|Updates model weights to reduce loss (e.g., `torch.optim.SGD`, `torch.optim.Adam`).|
|`Dataset` / `DataLoader`|Tools to load, batch, and shuffle data efficiently.|
|Device|`cpu` or `cuda` (GPU) / `mps` (Apple Silicon). You move tensors/models with `.to(device)`.|

**The universal training loop.** Nearly every PyTorch program you will ever write follows this five-step pattern:

```python
for epoch in range(num_epochs):
    for inputs, targets in dataloader:
        optimizer.zero_grad()        # 1. Reset gradients from the previous step
        outputs = model(inputs)      # 2. Forward pass: make predictions
        loss = loss_fn(outputs, targets)  # 3. Compute how wrong we are
        loss.backward()              # 4. Backward pass: compute gradients
        optimizer.step()             # 5. Update the weights
```

Internalize these five lines and you understand 90% of PyTorch.

---

## 4. Installation

Use the official selector at [pytorch.org](https://pytorch.org/get-started/locally/) to get the exact command for your OS and hardware. Common cases:

```bash
# CPU-only (works everywhere)
pip install torch torchvision torchaudio

# NVIDIA GPU (CUDA) — pick the index URL matching your CUDA version from pytorch.org
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Verify the install and check whether a GPU is available:

```python
import torch
print(torch.__version__)
print("CUDA available:", torch.cuda.is_available())          # NVIDIA GPU
print("MPS available:", torch.backends.mps.is_available())   # Apple Silicon
```

---

## 5. Five Worked Examples

Each example builds on the previous one and includes an explanation of _why_ the code does what it does.

### Example 1: Tensors & Autograd (Beginner)

**Goal:** understand tensors and see automatic differentiation in action — the single most important idea in PyTorch.

```python
import torch

# Create tensors (like NumPy arrays, but GPU-capable and differentiable)
a = torch.tensor([2.0, 3.0])
b = torch.tensor([4.0, 5.0])
print("Sum:", a + b)            # element-wise: tensor([6., 8.])
print("Dot product:", a @ b)    # 2*4 + 3*5 = 23

# --- Autograd: the heart of PyTorch ---
# Tell PyTorch to track operations on x so it can compute gradients.
x = torch.tensor(3.0, requires_grad=True)

# Define a function y = x^2 + 2x + 1
y = x**2 + 2*x + 1

# Compute dy/dx automatically.
y.backward()

# The derivative of x^2 + 2x + 1 is 2x + 2. At x=3 that is 2*3 + 2 = 8.
print("Gradient dy/dx at x=3:", x.grad)   # tensor(8.)
```

**Explanation.** A `Tensor` behaves like a NumPy array but adds two superpowers: it can run on a GPU, and it can record the operations performed on it. When you set `requires_grad=True`, PyTorch quietly builds a graph of every operation. Calling `.backward()` walks that graph backward and fills in `x.grad` with the derivative. Neural network training is nothing more than doing this for millions of parameters at once and nudging each one in the direction that reduces error.

---

### Example 2: Linear Regression from Scratch (Beginner)

**Goal:** train your first model — fit a straight line `y = wx + b` to data — using the full training loop manually.

```python
import torch

# Synthetic data: true relationship is y = 2x + 1 (plus a little noise)
X = torch.linspace(0, 10, 50).unsqueeze(1)        # shape (50, 1)
y = 2 * X + 1 + torch.randn(X.size()) * 0.5       # noisy targets

# Parameters we want to learn, initialized randomly.
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

lr = 0.01  # learning rate

for epoch in range(1000):
    # Forward pass: prediction
    y_pred = X * w + b

    # Loss: mean squared error
    loss = ((y_pred - y) ** 2).mean()

    # Backward pass: compute gradients of loss w.r.t. w and b
    loss.backward()

    # Manually update parameters (gradient descent).
    # Wrap in no_grad() so these updates aren't themselves tracked.
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
        # Reset gradients to zero for the next iteration.
        w.grad.zero_()
        b.grad.zero_()

    if epoch % 100 == 0:
        print(f"Epoch {epoch:4d} | loss {loss.item():.4f} | w {w.item():.3f} | b {b.item():.3f}")

print(f"\nLearned: y = {w.item():.2f}x + {b.item():.2f}  (true: y = 2x + 1)")
```

**Explanation.** This is gradient descent in its rawest form. We start with random `w` and `b`, measure how far our predictions are from the truth (mean squared error), and use `backward()` to learn which direction to push each parameter. Subtracting `lr * grad` moves the parameters slightly toward lower loss. After 1000 repetitions, `w` and `b` converge to roughly 2 and 1 — the model has "learned" the underlying relationship. The `with torch.no_grad()` block is important: parameter updates are bookkeeping, not part of the model's math, so we exclude them from gradient tracking, and we must zero the gradients each step because PyTorch _accumulates_ them by default.

---

### Example 3: Image Classifier with a Neural Net (Intermediate)

**Goal:** use the proper high-level API (`nn.Module`, an optimizer, a `DataLoader`) to classify handwritten digits from the MNIST dataset.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1. Data: download MNIST, convert images to tensors, normalize.
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)),  # MNIST mean/std
])
train_ds = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
train_loader = DataLoader(train_ds, batch_size=64, shuffle=True)

# 2. Model: a simple feed-forward network. 28x28 image -> 10 digit classes.
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),            # 28x28 -> 784
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10),       # 10 output classes
        )

    def forward(self, x):
        return self.net(x)

model = Net().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# 3. Training loop (the five steps again).
model.train()
for epoch in range(3):
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = loss_fn(outputs, labels)
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1} | last batch loss {loss.item():.4f}")

print("Training complete.")
```

**Explanation.** This is "real" PyTorch. Instead of managing parameters by hand, we subclass `nn.Module` and let PyTorch track all the weights. `nn.Sequential` chains layers; `nn.Linear` is a fully-connected layer; `nn.ReLU` is the nonlinearity that lets the network model complex functions. `CrossEntropyLoss` is the standard loss for classification (it expects raw scores, called logits, and applies softmax internally). `Adam` is a smarter optimizer than plain gradient descent. The `DataLoader` automatically batches and shuffles the 60,000 training images. Notice the training loop is the exact same five steps from Example 2 — only the model and data grew up.

---

### Example 4: Convolutional Neural Network on CIFAR-10 (Intermediate/Advanced)

**Goal:** build a CNN — the architecture designed for images — and add a proper evaluation loop. CIFAR-10 is 60,000 small color photos across 10 classes (airplane, cat, ship, etc.).

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])
train_ds = datasets.CIFAR10("./data", train=True,  download=True, transform=transform)
test_ds  = datasets.CIFAR10("./data", train=False, download=True, transform=transform)
train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
test_loader  = DataLoader(test_ds,  batch_size=256, shuffle=False)

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),  # 3 color channels in, 32 filters out
            nn.ReLU(),
            nn.MaxPool2d(2),                              # 32x32 -> 16x16
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),                              # 16x16 -> 8x8
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 8 * 8, 256),
            nn.ReLU(),
            nn.Dropout(0.5),                             # regularization to fight overfitting
            nn.Linear(256, 10),
        )

    def forward(self, x):
        x = self.features(x)
        return self.classifier(x)

model = CNN().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# --- Training ---
for epoch in range(5):
    model.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        loss = loss_fn(model(images), labels)
        loss.backward()
        optimizer.step()

    # --- Evaluation (no gradients needed, so it's faster) ---
    model.eval()
    correct = total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            preds = model(images).argmax(dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    print(f"Epoch {epoch+1} | test accuracy {100*correct/total:.2f}%")
```

**Explanation.** Fully-connected layers ignore the spatial structure of an image; **convolutional layers** (`nn.Conv2d`) don't — they slide small learnable filters across the image to detect edges, textures, and shapes, which is why CNNs dominate vision. `MaxPool2d` shrinks the spatial dimensions while keeping the strongest signals, and `Dropout` randomly disables neurons during training to prevent the model from memorizing the training set (overfitting). The new and important addition here is the **evaluation loop**: `model.eval()` switches dropout/batchnorm into inference mode, `torch.no_grad()` disables gradient tracking for speed, and we measure accuracy on data the model never trained on — the only honest way to judge a model.

---

### Example 5: Transfer Learning with a Pretrained Model (Advanced)

**Goal:** instead of training from scratch, take a model already trained on millions of images (ResNet-18) and adapt it to a new task. This is how most real-world computer vision is done.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, datasets, transforms
from torch.utils.data import DataLoader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1. Load a model pretrained on ImageNet (1000 classes, 1.2M images).
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

# 2. Freeze all existing weights — we keep the learned visual features.
for param in model.parameters():
    param.requires_grad = False

# 3. Replace the final classification layer to match OUR number of classes.
#    Only this new layer will be trained.
num_classes = 2  # e.g., a cats-vs-dogs task
model.fc = nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)

# 4. Use the input pipeline the pretrained model expects (resize + ImageNet norm).
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

# Point this at your own folder of images organized as root/class_name/*.jpg
# train_ds = datasets.ImageFolder("path/to/train", transform=transform)
# train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)

loss_fn = nn.CrossEntropyLoss()
# Only optimize the parameters that are still trainable (the new final layer).
optimizer = optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()), lr=1e-3
)

# 5. Same five-step training loop as always:
# for images, labels in train_loader:
#     images, labels = images.to(device), labels.to(device)
#     optimizer.zero_grad()
#     loss = loss_fn(model(images), labels)
#     loss.backward()
#     optimizer.step()

print("Pretrained ResNet-18 ready for fine-tuning on", num_classes, "classes.")
```

**Explanation.** Training a strong image model from scratch needs huge datasets and a lot of compute. **Transfer learning** sidesteps this: a model like ResNet-18, pretrained on ImageNet, has already learned general-purpose visual features (edges, textures, object parts) in its early layers. We _freeze_ those layers (`requires_grad = False`) and replace only the final classifier (`model.fc`) with a fresh layer sized to our task. Now we train just that small new layer on a few hundred images and get excellent results in minutes. This pattern — take a pretrained backbone, swap the head, fine-tune — is the foundation of practical deep learning across vision _and_ language (the same idea underlies fine-tuning large language models).

---

## 6. Learning Path: Beginner to Master

A realistic, staged roadmap. Don't rush — each stage assumes the previous one is comfortable.

**Stage 0 — Prerequisites (before PyTorch)**

- Solid Python (functions, classes, list comprehensions).
- NumPy basics (arrays, broadcasting, indexing).
- A working intuition for: derivatives/gradients, vectors and matrices, and what "training a model" means. You don't need heavy math, but the more linear algebra and calculus you have, the deeper you'll go.

**Stage 1 — Beginner (Weeks 1–3)**

- Master tensors: creation, shapes, indexing, broadcasting, reshaping, moving to GPU.
- Understand `autograd` and `.backward()` cold (Example 1).
- Write linear and logistic regression by hand (Example 2).
- Learn the five-step training loop until it's muscle memory.
- _Milestone:_ train a model on MNIST and reach >97% accuracy (Example 3).

**Stage 2 — Intermediate (Weeks 4–8)**

- `nn.Module`, `nn.Sequential`, common layers, activations, losses, optimizers.
- `Dataset` and `DataLoader`; writing custom datasets.
- CNNs for images (Example 4); proper train/validation/test splits and evaluation.
- Regularization: dropout, weight decay, data augmentation, early stopping.
- Saving/loading models (`torch.save`, `state_dict`), learning-rate scheduling.
- _Milestone:_ build and evaluate a CNN on CIFAR-10 and diagnose overfitting.

**Stage 3 — Advanced (Months 3–5)**

- Transfer learning and fine-tuning pretrained models (Example 5).
- Sequence models and the Transformer architecture; tokenization and embeddings.
- Use the Hugging Face `transformers` ecosystem (built on PyTorch) for NLP/LLMs.
- Mixed-precision training (`torch.cuda.amp`), gradient clipping, custom loss functions.
- Experiment tracking (Weights & Biases or TensorBoard) and hyperparameter tuning.
- _Milestone:_ fine-tune a pretrained model on a dataset you collected yourself.

**Stage 4 — Master (Months 6+)**

- Write custom `autograd.Function`s and custom layers/kernels.
- Distributed and multi-GPU training (`DistributedDataParallel`, FSDP).
- Performance: `torch.compile`, profiling, memory optimization, data pipeline tuning.
- Deployment: TorchScript, ONNX export, `torchserve`, quantization for inference.
- Read and reproduce research papers; contribute to open-source; design novel architectures.
- _Milestone:_ take a paper with no official code and reproduce its results.

**Habits that separate masters from beginners:** read the official docs and source code, always build a baseline first, debug by printing tensor `.shape` constantly, version your experiments, and reproduce others' work before inventing your own.

---

## 7. Resources

**Official (start here, always current)**

- PyTorch official tutorials — https://pytorch.org/tutorials/ (especially "Learn the Basics" and the 60-Minute Blitz)
- PyTorch documentation — https://pytorch.org/docs/stable/index.html
- PyTorch Examples repo — https://github.com/pytorch/examples
- PyTorch forums — https://discuss.pytorch.org/

**Free courses & books**

- "Deep Learning with PyTorch" (free official book by Stevens, Antiga, Viehmann) — https://pytorch.org/assets/deep-learning/Deep-Learning-with-PyTorch.pdf
- fast.ai "Practical Deep Learning for Coders" — https://course.fast.ai/ (top-down, project-first)
- Daniel Bourke's "Learn PyTorch for Deep Learning" (free) — https://www.learnpytorch.io/
- Dive into Deep Learning (interactive book, PyTorch version) — https://d2l.ai/

**NLP / LLM ecosystem**

- Hugging Face course — https://huggingface.co/learn (transformers, datasets, fine-tuning)

**Practice**

- Kaggle — https://www.kaggle.com/ (datasets, competitions, free GPU notebooks)
- Google Colab — https://colab.research.google.com/ (free GPU to run every example above)
- Papers with Code — https://paperswithcode.com/ (papers paired with implementations)

**Math foundations (if you need them)**

- 3Blue1Brown "Neural Networks" and "Essence of Linear Algebra" on YouTube
- Andrew Ng's Deep Learning Specialization (Coursera)

---

_Tip: open Google Colab, paste in Examples 1 through 4, and run them top to bottom. Nothing accelerates learning like watching the loss actually go down on your own screen._