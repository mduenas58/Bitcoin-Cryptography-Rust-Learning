
## Lab Overview

This lab simulates a real-world collaborative development scenario where two developers work together on a Node.js website using Git and GitHub. You'll practice branching, merging, resolving conflicts, and collaborative workflows.

**Duration:** 2-3 hours

**Difficulty:** Intermediate

**Prerequisites:** Basic Git knowledge, Node.js installed, GitHub account
  
---
## Scenario
  
**Project:** TaskMaster Pro - A task management web application

**Tech Stack:** Node.js, Express.js, EJS templates, CSS

**Team:**

- **Developer A (Alex):** Works on backend features and API endpoints

- **Developer B (Blake):** Works on frontend UI and styling

Both developers will collaborate on this project using Git feature branches, pull requests, and proper merge strategies.

---
## Lab Setup

### Part 1: Initial Repository Setup (Developer A)

#### Step 1: Create Local Project Structure

```bash

# Create project directory

mkdir taskmaster-pro

cd taskmaster-pro

# Initialize Git repository

git init

# Configure Git (if not already configured)

git config user.name "Alex Developer"

git config user.email "alex@example.com"

```

#### Step 2: Create Initial File Structure

Create the following files and directories:

```

taskmaster-pro/

├── .gitignore

├── README.md

├── package.json

├── server.js

├── public/

│ ├── css/

│ │ └── style.css

│ └── js/

│ └── main.js

├── views/

│ ├── index.ejs

│ └── partials/

│ ├── header.ejs

│ └── footer.ejs

└── routes/

└── tasks.js

```

#### Step 3: Create .gitignore

```bash

cat > .gitignore << 'EOF'

# Dependencies

node_modules/

# Environment variables

.env

.env.local

# Logs

logs/

*.log

npm-debug.log*


# OS files

.DS_Store

Thumbs.db


# IDE files

.vscode/

.idea/

*.swp

*.swo


# Build outputs

dist/

build/

EOF

```

#### Step 4: Create README.md

```bash

cat > README.md << 'EOF'

# TaskMaster Pro


A modern task management web application built with Node.js and Express.


## Features


- Create, read, update, and delete tasks

- Mark tasks as complete/incomplete

- Filter tasks by status

- Responsive design

  
## Tech Stack

  
- **Backend:** Node.js, Express.js

- **Frontend:** EJS templates, Vanilla JavaScript

- **Styling:** Custom CSS

  
## Installation


```bash

# Clone the repository

git clone https://github.com/yourusername/taskmaster-pro.git


# Navigate to project directory

cd taskmaster-pro


# Install dependencies

npm install


# Start the server

npm start

```

## Usage

Navigate to `http://localhost:3000` in your browser.

## API Endpoints

- `GET /api/tasks` - Get all tasks

- `POST /api/tasks` - Create a new task

- `PUT /api/tasks/:id` - Update a task

- `DELETE /api/tasks/:id` - Delete a task

## Contributing

1. Fork the repository

2. Create your feature branch (`git checkout -b feature/AmazingFeature`)

3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

## License

MIT License

## Authors

- Alex Developer

- Blake Developer

EOF

```

#### Step 5: Create package.json

  

```bash

cat > package.json << 'EOF'

{

"name": "taskmaster-pro",

"version": "1.0.0",

"description": "A modern task management web application",

"main": "server.js",

"scripts": {

"start": "node server.js",

"dev": "nodemon server.js"

},

"keywords": ["task", "management", "nodejs", "express"],

"author": "Alex & Blake",

"license": "MIT",

"dependencies": {

"express": "^4.18.2",

"ejs": "^3.1.9",

"body-parser": "^1.20.2"

},

"devDependencies": {

"nodemon": "^3.0.1"

}

}

EOF

```

#### Step 6: Create server.js

```bash

cat > server.js << 'EOF'

const express = require('express');

const bodyParser = require('body-parser');

const path = require('path');


const app = express();

const PORT = process.env.PORT || 3000;


// Middleware

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static('public'));

  
// View engine setup

app.set('view engine', 'ejs');

app.set('views', path.join(__dirname, 'views'));

  
// In-memory task storage (will be replaced with database later)

let tasks = [

{ id: 1, title: 'Setup project structure', completed: true },

{ id: 2, title: 'Create initial routes', completed: false },

{ id: 3, title: 'Design UI mockups', completed: false }

];

  
// Routes

app.get('/', (req, res) => {

res.render('index', { tasks });

});

  
// Import task routes

const taskRoutes = require('./routes/tasks');

app.use('/api/tasks', taskRoutes);

  
// Start server

app.listen(PORT, () => {

console.log(`TaskMaster Pro server running on http://localhost:${PORT}`);

});

EOF

```

#### Step 7: Create routes/tasks.js

```bash

mkdir -p routes

cat > routes/tasks.js << 'EOF'

const express = require('express');

const router = express.Router();


// In-memory task storage (shared with server.js - will refactor later)

let tasks = [

{ id: 1, title: 'Setup project structure', completed: true },

{ id: 2, title: 'Create initial routes', completed: false },

{ id: 3, title: 'Design UI mockups', completed: false }

];


// GET all tasks

router.get('/', (req, res) => {

res.json(tasks);

});


// POST create new task

router.post('/', (req, res) => {

const newTask = {

id: tasks.length + 1,

title: req.body.title,

completed: false

};

tasks.push(newTask);

res.status(201).json(newTask);

});


// PUT update task

router.put('/:id', (req, res) => {

const taskId = parseInt(req.params.id);

const task = tasks.find(t => t.id === taskId);

if (!task) {

return res.status(404).json({ error: 'Task not found' });

}

task.title = req.body.title || task.title;

task.completed = req.body.completed !== undefined ? req.body.completed : task.completed;

res.json(task);

});


// DELETE task

router.delete('/:id', (req, res) => {

const taskId = parseInt(req.params.id);

const taskIndex = tasks.findIndex(t => t.id === taskId);

if (taskIndex === -1) {

return res.status(404).json({ error: 'Task not found' });

}

tasks.splice(taskIndex, 1);

res.status(204).send();

});


module.exports = router;

EOF

```

#### Step 8: Create Views

```bash

mkdir -p views/partials

  

cat > views/partials/header.ejs << 'EOF'

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>TaskMaster Pro</title>

<link rel="stylesheet" href="/css/style.css">

</head>

<body>

<header>

<h1>📝 TaskMaster Pro</h1>

</header>

EOF

  
cat > views/partials/footer.ejs << 'EOF'

<footer>

<p>&copy; 2024 TaskMaster Pro. All rights reserved.</p>

</footer>

<script src="/js/main.js"></script>

</body>

</html>

EOF
 

cat > views/index.ejs << 'EOF'

<%- include('partials/header') %>


<main class="container">

<section class="add-task-section">

<h2>Add New Task</h2>

<form id="add-task-form">

<input type="text" id="task-input" placeholder="Enter task description..." required>

<button type="submit">Add Task</button>

</form>

</section>

  
<section class="tasks-section">

<h2>Your Tasks</h2>

<div class="filter-buttons">

<button class="filter-btn active" data-filter="all">All</button>

<button class="filter-btn" data-filter="active">Active</button>

<button class="filter-btn" data-filter="completed">Completed</button>

</div>

<ul id="task-list" class="task-list">

<% tasks.forEach(task => { %>

<li class="task-item <%= task.completed ? 'completed' : '' %>" data-id="<%= task.id %>">

<input type="checkbox" <%= task.completed ? 'checked' : '' %>>

<span class="task-title"><%= task.title %></span>

<button class="delete-btn">Delete</button>

</li>

<% }); %>

</ul>

</section>

</main>

  

<%- include('partials/footer') %>

EOF

```

#### Step 9: Create Frontend Files

```bash

mkdir -p public/css public/js

  

cat > public/css/style.css << 'EOF'

* {

margin: 0;

padding: 0;

box-sizing: border-box;

}


body {

font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

min-height: 100vh;

padding: 20px;

}


header {

text-align: center;

color: white;

padding: 30px 0;

}


header h1 {

font-size: 3em;

text-shadow: 2px 2px 4px rgba(0,0,0,0.3);

}

.container {

max-width: 800px;

margin: 0 auto;

background: white;

border-radius: 15px;

box-shadow: 0 10px 30px rgba(0,0,0,0.3);

padding: 30px;

}

.add-task-section {

margin-bottom: 30px;

}


.add-task-section h2 {

color: #667eea;

margin-bottom: 15px;

}
  

#add-task-form {

display: flex;

gap: 10px;

}
 

#task-input {

flex: 1;

padding: 12px;

border: 2px solid #e0e0e0;

border-radius: 8px;

font-size: 16px;

}
 

#task-input:focus {

outline: none;

border-color: #667eea;

}
 

button {

padding: 12px 24px;

background: #667eea;

color: white;

border: none;

border-radius: 8px;

cursor: pointer;

font-size: 16px;

transition: background 0.3s;

}


button:hover {

background: #5568d3;

}


.tasks-section h2 {

color: #667eea;

margin-bottom: 15px;

}  

.filter-buttons {

display: flex;

gap: 10px;

margin-bottom: 20px;

}

  
.filter-btn {

padding: 8px 16px;

background: #f0f0f0;

color: #333;

font-size: 14px;

}

  
.filter-btn.active {

background: #667eea;

color: white;

}

  
.task-list {

list-style: none;

}
 

.task-item {

display: flex;

align-items: center;

padding: 15px;

border-bottom: 1px solid #e0e0e0;

transition: background 0.2s;

}

  
.task-item:hover {

background: #f9f9f9;

}

  
.task-item input[type="checkbox"] {

width: 20px;

height: 20px;

margin-right: 15px;

cursor: pointer;

}

  
.task-title {

flex: 1;

font-size: 16px;

}

  
.task-item.completed .task-title {

text-decoration: line-through;

color: #999;

}

  
.delete-btn {

padding: 6px 12px;

background: #ff6b6b;

font-size: 14px;

}

  
.delete-btn:hover {

background: #ee5a52;

}

  
footer {

text-align: center;

color: white;

padding: 20px 0;

margin-top: 30px;

}

EOF
 

cat > public/js/main.js << 'EOF'

// Wait for DOM to load

document.addEventListener('DOMContentLoaded', () => {

const addTaskForm = document.getElementById('add-task-form');

const taskInput = document.getElementById('task-input');

const taskList = document.getElementById('task-list');

const filterButtons = document.querySelectorAll('.filter-btn');

  
// Add task

addTaskForm.addEventListener('submit', async (e) => {

e.preventDefault();

const title = taskInput.value.trim();

if (!title) return;


try {

const response = await fetch('/api/tasks', {

method: 'POST',

headers: {

'Content-Type': 'application/json'

},

body: JSON.stringify({ title })

});


if (response.ok) {

taskInput.value = '';

window.location.reload();

}

} catch (error) {

console.error('Error adding task:', error);

}

});

  
// Delete task

taskList.addEventListener('click', async (e) => {

if (e.target.classList.contains('delete-btn')) {

const taskItem = e.target.closest('.task-item');

const taskId = taskItem.dataset.id;
 

try {

const response = await fetch(`/api/tasks/${taskId}`, {

method: 'DELETE'

});

  
if (response.ok) {

window.location.reload();

}

} catch (error) {

console.error('Error deleting task:', error);

}

}

});


// Toggle task completion

taskList.addEventListener('change', async (e) => {

if (e.target.type === 'checkbox') {

const taskItem = e.target.closest('.task-item');

const taskId = taskItem.dataset.id;

const completed = e.target.checked;

  
try {

const response = await fetch(`/api/tasks/${taskId}`, {

method: 'PUT',

headers: {

'Content-Type': 'application/json'

},

body: JSON.stringify({ completed })

});

  
if (response.ok) {

taskItem.classList.toggle('completed', completed);

}

} catch (error) {

console.error('Error updating task:', error);

}

}

});

  
// Filter tasks

filterButtons.forEach(button => {

button.addEventListener('click', () => {

filterButtons.forEach(btn => btn.classList.remove('active'));

button.classList.add('active');

  
const filter = button.dataset.filter;

const tasks = document.querySelectorAll('.task-item');

  
tasks.forEach(task => {

switch (filter) {

case 'all':

task.style.display = 'flex';

break;

case 'active':

task.style.display = task.classList.contains('completed') ? 'none' : 'flex';

break;

case 'completed':

task.style.display = task.classList.contains('completed') ? 'flex' : 'none';

break;

}

});

});

});

});

EOF

```

#### Step 10: Initial Commit

```bash

# Stage all files

git add .

# Create initial commit

git commit -m "Initial commit: Project structure and basic functionality"

# View commit history

git log --oneline

```

#### Step 11: Create GitHub Repository and Push

1. Go to GitHub and create a new repository named `taskmaster-pro`

2. Do NOT initialize with README, .gitignore, or license (we already have these)

3. Copy the repository URL

```bash

# Add remote repository

git remote add origin https://github.com/YOUR_USERNAME/taskmaster-pro.git

  

# Rename branch to main (if needed)

git branch -M main

# Push to GitHub

git push -u origin main

```

---

## Part 2: Developer B Clones and Sets Up

Developer B (Blake) now joins the project.

```bash

# Clone the repository

git clone https://github.com/YOUR_USERNAME/taskmaster-pro.git

cd taskmaster-pro


# Configure Git for Developer B

git config user.name "Blake Developer"

git config user.email "blake@example.com"
 

# Install dependencies

npm install


# Test the application

npm start

# Visit http://localhost:3000 to verify it works

```

---

## Part 3: Parallel Development (Feature Branches)

### Developer A: Add Priority Feature to Tasks

```bash

# Create and switch to feature branch

git checkout -b feature/task-priority

# Modify routes/tasks.js to add priority field

# Update the in-memory tasks array and add priority handling

```

**Update routes/tasks.js:**

```javascript

// Replace the tasks array at the top with:

let tasks = [

{ id: 1, title: 'Setup project structure', completed: true, priority: 'low' },

{ id: 2, title: 'Create initial routes', completed: false, priority: 'high' },

{ id: 3, title: 'Design UI mockups', completed: false, priority: 'medium' }

];

// Update the POST route to include priority:

router.post('/', (req, res) => {

const newTask = {

id: tasks.length + 1,

title: req.body.title,

completed: false,

priority: req.body.priority || 'medium'

};

tasks.push(newTask);

res.status(201).json(newTask);

});

// Update the PUT route to include priority:

router.put('/:id', (req, res) => {

const taskId = parseInt(req.params.id);

const task = tasks.find(t => t.id === taskId);

if (!task) {

return res.status(404).json({ error: 'Task not found' });

}

task.title = req.body.title || task.title;

task.completed = req.body.completed !== undefined ? req.body.completed : task.completed;

task.priority = req.body.priority || task.priority;

res.json(task);

});

```

**Update server.js tasks array to match:**

```javascript

let tasks = [

{ id: 1, title: 'Setup project structure', completed: true, priority: 'low' },

{ id: 2, title: 'Create initial routes', completed: false, priority: 'high' },

{ id: 3, title: 'Design UI mockups', completed: false, priority: 'medium' }

];

```

**Update README.md to document priority feature:**

Add under the API Endpoints section:

```markdown

### Task Object Structure


```json

{

"id": 1,

"title": "Task description",

"completed": false,

"priority": "high" // Options: "low", "medium", "high"

}

```

  
```bash

# Stage and commit changes

git add routes/tasks.js server.js README.md

git commit -m "Add priority field to tasks with high/medium/low options"

  

# Push feature branch to GitHub

git push -u origin feature/task-priority

```

  

### Developer B: Improve UI Styling and Add Dark Mode

  

```bash

# Ensure you're on main branch

git checkout main

  

# Pull latest changes (good practice)

git pull origin main

  

# Create and switch to feature branch

git checkout -b feature/dark-mode-ui

```

  

**Create new file public/css/dark-mode.css:**

  

```css

/* Dark mode styles */

body.dark-mode {

background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);

}

  

body.dark-mode .container {

background: #0f3460;

color: #e4e4e4;

}

  

body.dark-mode .add-task-section h2,

body.dark-mode .tasks-section h2 {

color: #e94560;

}

  

body.dark-mode #task-input {

background: #1a1a2e;

color: #e4e4e4;

border-color: #16213e;

}

  

body.dark-mode .task-item {

border-bottom-color: #16213e;

}

  

body.dark-mode .task-item:hover {

background: #16213e;

}

  

body.dark-mode .filter-btn {

background: #16213e;

color: #e4e4e4;

}

  

body.dark-mode .filter-btn.active {

background: #e94560;

}

  

/* Theme toggle button */

.theme-toggle {

position: fixed;

top: 20px;

right: 20px;

padding: 10px 20px;

background: rgba(255, 255, 255, 0.2);

backdrop-filter: blur(10px);

border-radius: 25px;

cursor: pointer;

z-index: 1000;

}

  

.theme-toggle:hover {

background: rgba(255, 255, 255, 0.3);

}

```

  

**Update views/partials/header.ejs to include dark mode CSS:**

  

```html

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>TaskMaster Pro</title>

<link rel="stylesheet" href="/css/style.css">

<link rel="stylesheet" href="/css/dark-mode.css">

</head>

<body>

<button class="theme-toggle">🌙 Toggle Theme</button>

<header>

<h1>📝 TaskMaster Pro</h1>

</header>

```

  

**Update public/js/main.js to add theme toggle functionality:**

  

Add at the beginning of the DOMContentLoaded event listener:

  

```javascript

// Theme toggle

const themeToggle = document.querySelector('.theme-toggle');

const body = document.body;

  

// Load saved theme

const savedTheme = localStorage.getItem('theme');

if (savedTheme === 'dark') {

body.classList.add('dark-mode');

themeToggle.textContent = '☀️ Toggle Theme';

}

  

themeToggle.addEventListener('click', () => {

body.classList.toggle('dark-mode');

if (body.classList.contains('dark-mode')) {

themeToggle.textContent = '☀️ Toggle Theme';

localStorage.setItem('theme', 'dark');

} else {

themeToggle.textContent = '🌙 Toggle Theme';

localStorage.setItem('theme', 'light');

}

});

```

  

**Update public/css/style.css for better animations:**

  

Add at the end:

  

```css

/* Smooth transitions */

body {

transition: background 0.3s ease;

}

  

.container {

transition: background 0.3s ease, color 0.3s ease;

}

  

.task-item {

animation: slideIn 0.3s ease;

}

  

@keyframes slideIn {

from {

opacity: 0;

transform: translateX(-20px);

}

to {

opacity: 1;

transform: translateX(0);

}

}

  

/* Responsive design */

@media (max-width: 768px) {

header h1 {

font-size: 2em;

}

.container {

padding: 20px;

}

#add-task-form {

flex-direction: column;

}

.filter-buttons {

flex-wrap: wrap;

}

}

```

  

```bash

# Stage and commit changes

git add public/css/dark-mode.css public/css/style.css public/js/main.js views/partials/header.ejs

git commit -m "Add dark mode toggle and improve UI with animations and responsive design"

  

# Push feature branch to GitHub

git push -u origin feature/dark-mode-ui

```

  

---

  

## Part 4: Creating Pull Requests

  

### Developer A: Create Pull Request for Priority Feature

  

1. Go to GitHub repository

2. Click "Pull requests" → "New pull request"

3. Select `feature/task-priority` as the compare branch

4. Title: "Add priority field to tasks"

5. Description:

```

## Changes

- Added priority field to task object (high, medium, low)

- Updated API endpoints to handle priority

- Updated README with task structure documentation

## Testing

- Tested POST, PUT endpoints with priority field

- Verified backward compatibility

```

6. Create pull request

  

### Developer B: Create Pull Request for Dark Mode

  

1. Go to GitHub repository

2. Click "Pull requests" → "New pull request"

3. Select `feature/dark-mode-ui` as the compare branch

4. Title: "Add dark mode and UI improvements"

5. Description:

```

## Changes

- Added dark mode toggle with localStorage persistence

- Improved UI animations and transitions

- Added responsive design for mobile devices

- Created separate dark-mode.css for better organization

## Testing

- Tested on Chrome, Firefox, Safari

- Verified mobile responsiveness

- Confirmed theme preference saves across sessions

```

6. Create pull request

  

---

  

## Part 5: Code Review and Merging

  

### Review and Merge Priority Feature (Developer B reviews)

  

```bash

# Developer B checks out the priority feature branch

git fetch origin

git checkout feature/task-priority

  

# Test the changes

npm start

# Test the API endpoints

  

# If approved, merge via GitHub:

# 1. Go to the pull request

# 2. Click "Merge pull request"

# 3. Choose "Squash and merge" or "Create a merge commit"

# 4. Confirm merge

```

  

### Review and Merge Dark Mode Feature (Developer A reviews)

  

```bash

# Developer A checks out the dark mode feature branch

git fetch origin

git checkout feature/dark-mode-ui

  

# Test the changes

npm start

# Test the UI and dark mode toggle

  

# If approved, merge via GitHub

```

  

---

  

## Part 6: Handling Merge Conflicts

  

Now both developers will work on the same file simultaneously to practice conflict resolution.

  

### Developer A: Add Search Functionality

  

```bash

# Pull latest main

git checkout main

git pull origin main

  

# Create new feature branch

git checkout -b feature/search-tasks

  

# Update public/js/main.js

```

  

Add after the filter buttons event listeners in main.js:

  

```javascript

// Search functionality

const searchInput = document.createElement('input');

searchInput.type = 'text';

searchInput.id = 'search-input';

searchInput.placeholder = 'Search tasks...';

searchInput.style.cssText = 'width: 100%; padding: 12px; margin-bottom: 20px; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 16px;';

document.querySelector('.tasks-section').insertBefore(searchInput, document.querySelector('.filter-buttons'));

searchInput.addEventListener('input', (e) => {

const searchTerm = e.target.value.toLowerCase();

const tasks = document.querySelectorAll('.task-item');

tasks.forEach(task => {

const title = task.querySelector('.task-title').textContent.toLowerCase();

task.style.display = title.includes(searchTerm) ? 'flex' : 'none';

});

});

```

  

```bash

git add public/js/main.js

git commit -m "Add search functionality to filter tasks by title"

git push -u origin feature/search-tasks

```

  

### Developer B: Add Task Counter

  

```bash

# Pull latest main

git checkout main

git pull origin main

  

# Create new feature branch

git checkout -b feature/task-counter

  

# Update public/js/main.js

```

  

Add after the filter buttons event listeners in main.js:

  

```javascript

// Task counter

function updateTaskCounter() {

const tasks = document.querySelectorAll('.task-item');

const completedTasks = document.querySelectorAll('.task-item.completed');

const counter = document.createElement('div');

counter.id = 'task-counter';

counter.style.cssText = 'text-align: center; margin-bottom: 20px; font-size: 18px; color: #667eea; font-weight: bold;';

counter.textContent = `${completedTasks.length} of ${tasks.length} tasks completed`;

const existingCounter = document.getElementById('task-counter');

if (existingCounter) {

existingCounter.textContent = counter.textContent;

} else {

document.querySelector('.tasks-section').insertBefore(counter, document.querySelector('.filter-buttons'));

}

}

updateTaskCounter();

// Update counter when tasks change

taskList.addEventListener('change', updateTaskCounter);

```

  

```bash

git add public/js/main.js

git commit -m "Add task counter showing completion progress"

git push -u origin feature/task-counter

```

  

### Merge First Feature (Search)

  

Developer A's pull request is reviewed and merged first via GitHub.

  

### Developer B Encounters Conflict

  

```bash

# Developer B tries to create pull request but sees conflicts

# Pull the latest main with the search feature

git checkout main

git pull origin main

  

# Try to merge main into your feature branch

git checkout feature/task-counter

git merge main

  

# CONFLICT! Git shows:

# Auto-merging public/js/main.js

# CONFLICT (content): Merge conflict in public/js/main.js

# Automatic merge failed; fix conflicts and then commit the result.

```

  

### Resolving the Conflict

  

```bash

# Open public/js/main.js in your editor

# You'll see conflict markers like this:

  

<<<<<<< HEAD

// Task counter

function updateTaskCounter() {

// ... Blake's code ...

}

=======

// Search functionality

const searchInput = document.createElement('input');

// ... Alex's code ...

>>>>>>> main

  

# Resolve by keeping BOTH features:

```

  

**Resolved public/js/main.js** (relevant section):

  

```javascript

// Search functionality (from Alex)

const searchInput = document.createElement('input');

searchInput.type = 'text';

searchInput.id = 'search-input';

searchInput.placeholder = 'Search tasks...';

searchInput.style.cssText = 'width: 100%; padding: 12px; margin-bottom: 20px; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 16px;';

document.querySelector('.tasks-section').insertBefore(searchInput, document.querySelector('.filter-buttons'));

searchInput.addEventListener('input', (e) => {

const searchTerm = e.target.value.toLowerCase();

const tasks = document.querySelectorAll('.task-item');

tasks.forEach(task => {

const title = task.querySelector('.task-title').textContent.toLowerCase();

task.style.display = title.includes(searchTerm) ? 'flex' : 'none';

});

});

  

// Task counter (from Blake)

function updateTaskCounter() {

const tasks = document.querySelectorAll('.task-item');

const completedTasks = document.querySelectorAll('.task-item.completed');

const counter = document.createElement('div');

counter.id = 'task-counter';

counter.style.cssText = 'text-align: center; margin-bottom: 20px; font-size: 18px; color: #667eea; font-weight: bold;';

counter.textContent = `${completedTasks.length} of ${tasks.length} tasks completed`;

const existingCounter = document.getElementById('task-counter');

if (existingCounter) {

existingCounter.textContent = counter.textContent;

} else {

document.querySelector('.tasks-section').insertBefore(counter, document.querySelector('.filter-buttons'));

}

}

updateTaskCounter();

// Update counter when tasks change

taskList.addEventListener('change', updateTaskCounter);

```

  

```bash

# Stage the resolved file

git add public/js/main.js

  

# Complete the merge

git commit -m "Merge main into feature/task-counter and resolve conflicts

  

- Combined search functionality with task counter

- Both features now work together

- Tested integration of both features"

  

# Push the updated branch

git push origin feature/task-counter

  

# Now the pull request can be merged on GitHub

```

  

---

  

## Part 7: Advanced Git Operations

  

### Viewing History and Differences

  

```bash

# View detailed commit history

git log --graph --oneline --all --decorate

  

# View changes in a specific commit

git show <commit-hash>

  

# Compare branches

git diff main..feature/task-counter

  

# View file history

git log --follow public/js/main.js

  

# See who changed what

git blame public/js/main.js

```

  

### Tagging Releases

  

```bash

# Create a version tag

git checkout main

git pull origin main

  

# Create annotated tag for v1.0.0

git tag -a v1.0.0 -m "Version 1.0.0: Initial release with core features"

  

# Push tags to GitHub

git push origin v1.0.0

  

# List all tags

git tag -l

  

# Create a GitHub release from the tag

# Go to GitHub > Releases > Create new release > Select tag

```

  

### Working with Stash

  

```bash

# Save work in progress without committing

git stash save "WIP: Adding email notifications"

  

# List stashes

git stash list

  

# Apply most recent stash

git stash apply

  

# Apply and remove stash

git stash pop

  

# Drop a stash

git stash drop stash@{0}

```

  

### Cherry-picking Commits

  

```bash

# Apply a specific commit from another branch

git cherry-pick <commit-hash>

  

# Cherry-pick without committing (for review)

git cherry-pick --no-commit <commit-hash>

```

  

---

  

## Part 8: Best Practices Demonstrated

  

### 1. Commit Message Conventions

  

**Good commit messages follow this format:**

  

```

<type>: <subject>

  

<body>

  

<footer>

```

  

**Types:**

- `feat`: New feature

- `fix`: Bug fix

- `docs`: Documentation changes

- `style`: Formatting, missing semicolons, etc.

- `refactor`: Code refactoring

- `test`: Adding tests

- `chore`: Maintenance tasks

  

**Examples:**

  

```bash

git commit -m "feat: Add dark mode toggle with localStorage persistence"

  

git commit -m "fix: Resolve task counter not updating after deletion

  

The counter was only updating on checkbox changes. Added event

listener for delete operations to keep count accurate.

  

Closes #42"

  

git commit -m "docs: Update README with priority field documentation"

  

git commit -m "refactor: Extract task filtering logic into separate function"

```

  

### 2. Branch Naming Conventions

  

```bash

# Feature branches

feature/task-priority

feature/user-authentication

feature/export-tasks

  

# Bug fix branches

bugfix/delete-button-crash

bugfix/dark-mode-flickering

  

# Hotfix branches (for production)

hotfix/critical-security-patch

  

# Release branches

release/v1.0.0

release/v2.0.0-beta

```

  

### 3. Gitignore Best Practices

  

Your `.gitignore` should include:

  

```

# Dependencies

node_modules/

package-lock.json # Only if using yarn

  

# Environment variables

.env

.env.local

.env.*.local

  

# Build outputs

dist/

build/

*.log

  

# IDE-specific

.vscode/

.idea/

*.swp

  

# OS-specific

.DS_Store

Thumbs.db

  

# Testing

coverage/

.nyc_output/

```

  

### 4. Pull Request Templates

  

Create `.github/pull_request_template.md`:

  

```markdown

## Description

<!-- Describe your changes -->

  

## Type of Change

- [ ] Bug fix

- [ ] New feature

- [ ] Breaking change

- [ ] Documentation update

  

## Testing

<!-- Describe the tests you ran -->

  

## Checklist

- [ ] My code follows the project's style guidelines

- [ ] I have performed a self-review of my code

- [ ] I have commented my code where necessary

- [ ] I have updated the documentation

- [ ] My changes generate no new warnings

- [ ] I have tested my changes locally

  

## Screenshots (if applicable)

<!-- Add screenshots here -->

```

  

---

  

## Part 9: Troubleshooting Common Issues

  

### Issue 1: Accidentally Committed to Main

  

```bash

# Undo last commit, keep changes

git reset --soft HEAD~1

  

# Create proper feature branch

git checkout -b feature/my-feature

  

# Re-commit

git add .

git commit -m "feat: Add my feature"

```

  

### Issue 2: Need to Update Commit Message

  

```bash

# Update most recent commit message

git commit --amend -m "New commit message"

  

# Update older commit messages (interactive rebase)

git rebase -i HEAD~3

# Change 'pick' to 'reword' for commits you want to edit

```

  

### Issue 3: Accidentally Deleted Branch

  

```bash

# Find the commit hash

git reflog

  

# Recreate branch

git checkout -b feature/recovered-branch <commit-hash>

```

  

### Issue 4: Merge vs Rebase

  

**When to use merge:**

```bash

# Preserves complete history

git merge feature/my-feature

```

  

**When to use rebase:**

```bash

# Creates linear history (use for cleaning up feature branches)

git rebase main

```

  

### Issue 5: Sync Forked Repository

  

```bash

# Add upstream remote

git remote add upstream https://github.com/original/taskmaster-pro.git

  

# Fetch upstream changes

git fetch upstream

  

# Merge upstream main into your main

git checkout main

git merge upstream/main

  

# Push to your fork

git push origin main

```

  

---

  

## Part 10: Advanced Collaboration Scenarios

  

### Scenario A: Hotfix Production Bug

  

```bash

# Create hotfix from main

git checkout main

git pull origin main

git checkout -b hotfix/critical-bug-fix

  

# Make fixes

# ... edit files ...

  

git add .

git commit -m "hotfix: Fix critical security vulnerability in auth"

  

# Push hotfix

git push -u origin hotfix/critical-bug-fix

  

# Create pull request with "HOTFIX" label

# After merge, tag the release

git checkout main

git pull origin main

git tag -a v1.0.1 -m "Hotfix: Security patch"

git push origin v1.0.1

```

  

### Scenario B: Long-Running Feature Branch

  

```bash

# Keep feature branch updated with main

git checkout feature/long-feature

git fetch origin

git rebase origin/main

  

# If conflicts occur during rebase

# Fix conflicts in each commit

git add .

git rebase --continue

  

# Force push (rebase rewrites history)

git push -f origin feature/long-feature

```

  

### Scenario C: Pair Programming

  

```bash

# Developer A starts work

git checkout -b feature/pair-programming

  

# Commits some work

git add .

git commit -m "feat: Start authentication module"

git push -u origin feature/pair-programming

  

# Developer B takes over

git fetch origin

git checkout feature/pair-programming

  

# Makes changes

git add .

git commit -m "feat: Add password hashing"

git push origin feature/pair-programming

  

# Continue alternating...

```

  

---

  

## Part 11: Git Hooks for Automation

  

### Pre-commit Hook (Code Quality)

  

Create `.git/hooks/pre-commit`:

  

```bash

#!/bin/bash

  

echo "Running pre-commit checks..."

  

# Run linter

npm run lint

if [ $? -ne 0 ]; then

echo "❌ Linting failed. Please fix errors before committing."

exit 1

fi

  

# Run tests

npm test

if [ $? -ne 0 ]; then

echo "❌ Tests failed. Please fix failing tests before committing."

exit 1

fi

  

echo "✅ All pre-commit checks passed!"

exit 0

```

  

```bash

# Make executable

chmod +x .git/hooks/pre-commit

```

  

### Commit-msg Hook (Enforce Commit Format)

  

Create `.git/hooks/commit-msg`:

  

```bash

#!/bin/bash

  

commit_msg_file=$1

commit_msg=$(cat "$commit_msg_file")

  

# Check commit message format

if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|test|chore):"; then

echo "❌ Invalid commit message format!"

echo "Format: <type>: <subject>"

echo "Types: feat, fix, docs, style, refactor, test, chore"

exit 1

fi

  

echo "✅ Commit message format is valid"

exit 0

```

  

```bash

chmod +x .git/hooks/commit-msg

```

  

---

  

## Part 12: GitHub Actions for CI/CD

  

Create `.github/workflows/ci.yml`:

  

```yaml

name: CI/CD Pipeline

  

on:

push:

branches: [ main ]

pull_request:

branches: [ main ]

  

jobs:

test:

runs-on: ubuntu-latest

strategy:

matrix:

node-version: [16.x, 18.x, 20.x]

steps:

- uses: actions/checkout@v3

- name: Use Node.js ${{ matrix.node-version }}

uses: actions/setup-node@v3

with:

node-version: ${{ matrix.node-version }}

- name: Install dependencies

run: npm install

- name: Run tests

run: npm test

- name: Run linter

run: npm run lint

  

build:

needs: test

runs-on: ubuntu-latest

steps:

- uses: actions/checkout@v3

- name: Build application

run: |

npm install

npm run build

```

  

---

  

## Summary and Key Takeaways

  

### Git Commands Reference

  

| Command | Purpose |

|---------|---------|

| `git init` | Initialize repository |

| `git clone <url>` | Clone remote repository |

| `git status` | Check working directory status |

| `git add <file>` | Stage changes |

| `git commit -m "message"` | Commit staged changes |

| `git push` | Push to remote |

| `git pull` | Fetch and merge from remote |

| `git branch <name>` | Create branch |

| `git checkout <branch>` | Switch branch |

| `git checkout -b <name>` | Create and switch branch |

| `git merge <branch>` | Merge branch |

| `git rebase <branch>` | Rebase current branch |

| `git stash` | Save uncommitted changes |

| `git log` | View commit history |

| `git diff` | View differences |

| `git tag` | Create tag |

  

### Collaboration Workflow Summary

  

1. **Clone repository** and create feature branch

2. **Make changes** in feature branch

3. **Commit regularly** with meaningful messages

4. **Push** feature branch to GitHub

5. **Create pull request** for review

6. **Code review** by team member

7. **Resolve conflicts** if necessary

8. **Merge** into main branch

9. **Delete** feature branch after merge

10. **Pull latest** main before starting new feature

  

### Best Practices

  

✅ **DO:**

- Commit often with descriptive messages

- Use feature branches for all changes

- Pull before pushing

- Review your own code before requesting review

- Write meaningful commit messages

- Keep commits focused and atomic

- Delete branches after merging

  

❌ **DON'T:**

- Commit directly to main

- Force push to shared branches (without coordination)

- Commit sensitive data (.env files, API keys)

- Use generic commit messages ("fixed stuff", "updates")

- Leave branches unmaintained

- Commit large binary files

  

---

  

## Lab Completion Checklist

  

- [ ] Set up initial repository structure

- [ ] Created and pushed to GitHub remote

- [ ] Both developers cloned repository

- [ ] Created feature branches for both developers

- [ ] Made commits with proper messages

- [ ] Pushed feature branches

- [ ] Created pull requests

- [ ] Performed code reviews

- [ ] Merged pull requests

- [ ] Encountered and resolved merge conflict

- [ ] Used git log, diff, and other inspection tools

- [ ] Created version tags

- [ ] Implemented Git hooks

- [ ] Set up CI/CD pipeline

- [ ] Practiced stashing and cherry-picking

  

---

  

## Additional Exercises

  

1. **Exercise: Implement User Authentication**

- Developer A: Backend authentication routes

- Developer B: Login/signup UI

- Practice conflict resolution

  

2. **Exercise: Add Database Integration**

- Replace in-memory storage with MongoDB/PostgreSQL

- Use feature branch workflow

- Create comprehensive pull request

  

3. **Exercise: Implement Testing**

- Developer A: Write backend tests

- Developer B: Write frontend tests

- Set up test automation in CI/CD

  

---

  

## Resources

  

- [Git Documentation](https://git-scm.com/doc)

- [GitHub Guides](https://guides.github.com/)

- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

- [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)

- [Conventional Commits](https://www.conventionalcommits.org/)

  

---

  

**Congratulations!** You've completed a comprehensive Git lab covering real-world collaborative development scenarios. You now have hands-on experience with branching, merging, conflict resolution, and professional Git workflows.