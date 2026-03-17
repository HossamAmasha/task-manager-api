const API_BASE = "http://127.0.0.1:8000/api/v1";

function getToken() {
    return localStorage.getItem("token");
}

function setToken(token) {
    localStorage.setItem("token", token);
}

function removeToken() {
    localStorage.removeItem("token");
}
async function registerUser(username, password) {

    const response = await fetch(`${API_BASE}/auth/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    });
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Failed to register user");
    }

    return response.json();
}

async function loginUser(username, password) {
    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    const response = await fetch(`${API_BASE}/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData
    });

    if (!response.ok) {
        throw new Error("Invalid username or password");
    }

    return response.json();
}

async function getCurrentUser() {
    const response = await fetch(`${API_BASE}/auth/me`, {
        headers: {
            "Authorization": `Bearer ${getToken()}`
        }
    });

    if (!response.ok) {
        throw new Error("Unauthorized");
    }

    return response.json();
}

async function getTasks() {
    const response = await fetch(`${API_BASE}/tasks`, {
        headers: {
            "Authorization": `Bearer ${getToken()}`
        }
    });

    if (!response.ok) {
        throw new Error("Failed to fetch tasks");
    }

    return response.json();
}

async function getTaskStats() {
    const response = await fetch(`${API_BASE}/tasks/stats`, {
        headers: {
            "Authorization": `Bearer ${getToken()}`
        }
    });

    if (!response.ok) {
        throw new Error("Failed to fetch task stats");
    }

    return response.json();
}

async function createTask(title) {
    const response = await fetch(`${API_BASE}/tasks`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${getToken()}`
        },
        body: JSON.stringify({
            title: title,
            completed: false
        })
    });

    if (!response.ok) {
        throw new Error("Failed to create task");
    }

    return response.json();
}

async function patchTask(taskId, updatedFields) {
    const response = await fetch(`${API_BASE}/tasks/${taskId}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${getToken()}`
        },
        body: JSON.stringify(updatedFields)
    });

    if (!response.ok) {
        throw new Error("Failed to update task");
    }

    return response.json();
}

async function deleteTask(taskId) {
    const response = await fetch(`${API_BASE}/tasks/${taskId}`, {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${getToken()}`
        }
    });

    if (!response.ok) {
        throw new Error("Failed to delete task");
    }

    return response.json();
}

function renderTasks(tasks) {
    const tasksList = document.getElementById("tasks-list");
    if (!tasksList) return;

    tasksList.innerHTML = "";

    if (tasks.length === 0) {
        tasksList.innerHTML = "<p>No tasks yet.</p>";
        return;
    }

    tasks.forEach(task => {
        const taskItem = document.createElement("div");
        taskItem.className = "task-item";

        taskItem.innerHTML = `
            <div class="task-info">
                <span class="task-title ${task.completed ? "completed" : ""}">${task.title}</span>
                <small>Created: ${new Date(task.created_at).toLocaleString()}</small>
            </div>
            <div class="task-actions">
                <button class="toggle-btn" onclick="toggleTask(${task.id}, ${task.completed})">
                    ${task.completed ? "Undo" : "Complete"}
                </button>
                <button class="delete-btn" onclick="removeTask(${task.id})">Delete</button>
            </div>
        `;

        tasksList.appendChild(taskItem);
    });
}

async function loadDashboard() {
    try {
        const user = await getCurrentUser();
        const tasks = await getTasks();
        const stats = await getTaskStats();

        const welcomeText = document.getElementById("welcome-text");
        if (welcomeText) {
            welcomeText.textContent = `Welcome, ${user.username}`;
        }

        const totalTasks = document.getElementById("total-tasks");
        const completedTasks = document.getElementById("completed-tasks");
        const pendingTasks = document.getElementById("pending-tasks");

        if (totalTasks) totalTasks.textContent = stats.total;
        if (completedTasks) completedTasks.textContent = stats.completed;
        if (pendingTasks) pendingTasks.textContent = stats.pending;

        renderTasks(tasks);
    } catch (error) {
        removeToken();
        window.location.href = "login.html";
    }
}

async function toggleTask(taskId, currentCompleted) {
    try {
        await patchTask(taskId, { completed: !currentCompleted });
        loadDashboard();
    } catch (error) {
        alert(error.message);
    }
}

async function removeTask(taskId) {
    try {
        await deleteTask(taskId);
        loadDashboard();
    } catch (error) {
        alert(error.message);
    }
}

const registerForm = document.getElementById("register-form");
if (registerForm) {
    registerForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const username = document.getElementById("register-username").value.trim();
        const password = document.getElementById("register-password").value.trim();
        const message_failed = document.getElementById("register-message-failed");
        const message_success = document.getElementById("register-message-success");
        try {
            await registerUser(username, password);
            message_failed.textContent = "";
            message_success.textContent = "Registration successful. Please login.";
        } catch (error) {
            message_failed.textContent = error.message;
            message_success.textContent = "";
        }
    });
}

const loginForm = document.getElementById("login-form");
if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();
        const message = document.getElementById("login-message");

        try {
            const data = await loginUser(username, password);
            setToken(data.access_token);
            window.location.href = "dashboard.html";
        } catch (error) {
            message.textContent = error.message;
        }
    });
}

const taskForm = document.getElementById("task-form");
if (taskForm) {
    taskForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const titleInput = document.getElementById("task-title");
        const title = titleInput.value.trim();

        if (!title) return;

        try {
            await createTask(title);
            titleInput.value = "";
            loadDashboard();
        } catch (error) {
            alert(error.message);
        }
    });
}

const logoutBtn = document.getElementById("logout-btn");
if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
        removeToken();
        window.location.href = "login.html";
    });
}

if (window.location.pathname.includes("dashboard.html") && getToken()) {
    loadDashboard();
}

if (window.location.pathname.includes("dashboard.html") && !getToken()) {
    window.location.href = "login.html";
}

if ((window.location.pathname.includes("register.html") || window.location.pathname.includes("login.html")) && getToken()) {
    window.location.href = "dashboard.html";
}
