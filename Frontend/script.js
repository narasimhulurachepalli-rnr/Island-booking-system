const API_BASE = "http://127.0.0.1:8001";

// Global Session helpers
function getCurrentUser() {
    const user = localStorage.getItem("islandUser");
    return user ? JSON.parse(user) : null;
}

function setCurrentUser(user) {
    localStorage.setItem("islandUser", JSON.stringify(user));
}

function isAdminLoggedIn() {
    return localStorage.getItem("adminLoggedIn") === "true";
}

function logout() {
    localStorage.removeItem("islandUser");
    localStorage.removeItem("adminLoggedIn");
    showAlert("Logged out successfully", "success");
    setTimeout(() => {
        window.location.href = "index.html";
    }, 1000);
}

// Fetch helper
async function apiFetch(endpoint, options = {}) {
    const url = `${API_BASE}${endpoint}`;
    
    if (!options.headers) {
        options.headers = {};
    }
    if (!(options.body instanceof FormData) && !options.headers['Content-Type']) {
        options.headers['Content-Type'] = 'application/json';
    }

    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            const errData = await response.json().catch(() => ({}));
            throw new Error(errData.error || `HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`API Fetch Error (${endpoint}):`, error);
        throw error;
    }
}

// Alert utility
function showAlert(message, type = 'success') {
    let alertDiv = document.getElementById("alert-popup");
    if (!alertDiv) {
        alertDiv = document.createElement("div");
        alertDiv.id = "alert-popup";
        alertDiv.className = "alert-popup";
        document.body.appendChild(alertDiv);
    }
    
    alertDiv.className = `alert-popup ${type} active`;
    alertDiv.innerHTML = `
        <span class="alert-icon">${type === 'success' ? '✓' : '✗'}</span>
        <span class="alert-msg">${message}</span>
    `;

    setTimeout(() => {
        alertDiv.classList.remove("active");
    }, 3000);
}

// Navbar dynamic rendering
function renderNavBar() {
    const navContainer = document.getElementById("navbar-container");
    if (!navContainer) return;

    const user = getCurrentUser();
    const admin = isAdminLoggedIn();
    
    let navHTML = `
        <nav class="navbar">
            <a href="index.html" class="nav-brand">
                <span style="font-size: 1.85rem;">🌴</span> IslandGate Vacation
            </a>
            <ul class="nav-links">
                <li><a href="index.html" class="nav-item ${isActivePage('index.html')}">Home</a></li>
                <li><a href="islands.html" class="nav-item ${isActivePage('islands.html')}">Islands</a></li>
                <li><a href="packages.html" class="nav-item ${isActivePage('packages.html')}">Packages</a></li>
    `;

    if (admin) {
        navHTML += `
                <li><a href="admin_dashboard.html" class="nav-item ${isActivePage('admin_dashboard.html')}">Admin Panel</a></li>
                <li class="user-profile-nav">
                    <div class="user-avatar">AD</div>
                    <span style="font-weight:600; color:var(--text-primary);">Administrator</span>
                </li>
                <li><button onclick="logout()" class="btn-nav-login" style="background-color: var(--danger-light); color: var(--danger);">Logout</button></li>
        `;
    } else if (user) {
        navHTML += `
                <li><a href="customer_dashboard.html" class="nav-item ${isActivePage('customer_dashboard.html')}">My Dashboard</a></li>
                <li class="user-profile-nav">
                    <div class="user-avatar">${getInitials(user.full_name)}</div>
                    <span style="font-weight:600; color:var(--text-primary);">${user.full_name}</span>
                </li>
                <li><button onclick="logout()" class="btn-nav-login" style="background-color: var(--danger-light); color: var(--danger);">Logout</button></li>
        `;
    } else {
        navHTML += `
                <li><a href="login.html" class="btn-nav-login">Login</a></li>
                <li><a href="register.html" class="btn-nav-login" style="background-color: var(--primary); color: var(--text-white);">Register</a></li>
        `;
    }

    navHTML += `
            </ul>
        </nav>
    `;
    navContainer.innerHTML = navHTML;
}

function isActivePage(pageName) {
    const path = window.location.pathname;
    // For default path / or index.html
    if (pageName === 'index.html' && (path.endsWith('/') || path.endsWith('/index.html') || path === '')) {
        return 'active';
    }
    return path.includes(pageName) ? 'active' : '';
}

function getInitials(name) {
    if (!name) return "US";
    return name.split(" ").map(n => n[0]).join("").toUpperCase().substring(0, 2);
}

// Global page checks
document.addEventListener("DOMContentLoaded", () => {
    renderNavBar();
    
    // Page auth protection
    const path = window.location.pathname;
    
    const customerPages = [
        "customer_dashboard.html",
        "booking.html",
        "payment.html"
    ];
    
    const adminPages = [
        "admin_dashboard.html"
    ];

    const isCustomerPage = customerPages.some(page => path.includes(page));
    const isAdminPage = adminPages.some(page => path.includes(page));

    if (isCustomerPage && !getCurrentUser()) {
        localStorage.setItem("postLoginRedirect", window.location.href);
        window.location.href = "login.html?error=login_required";
    }

    if (isAdminPage && !isAdminLoggedIn()) {
        window.location.href = "login.html?error=admin_required";
    }
});
