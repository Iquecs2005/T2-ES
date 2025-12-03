import { addUser } from "../../api/login.js";

const API_BASE = "http://127.0.0.1:5000";


const form = document.getElementById("auth-form");
const statusBox = document.getElementById("status-box");
const toggleBtn = document.getElementById("toggle-btn");
const toggleCopy = document.getElementById("toggle-copy");
const formTitle = document.getElementById("form-title");
const formSubtitle = document.getElementById("form-subtitle");
const submitBtn = document.getElementById("submit-btn");
const passwordInput = document.getElementById("password");
const togglePasswordBtn = document.getElementById("toggle-password");

const showStatus = (message, type) => {
  statusBox.textContent = message;
  statusBox.className = `status show ${type}`;
  statusBox.style.display = "block";
};


const clearStatus = () => {
  statusBox.textContent = "";
  statusBox.className = "status";
  statusBox.style.display = "none";
};


toggleBtn.addEventListener("click", () => {
  setMode(mode === "login" ? "signup" : "login");
});


togglePasswordBtn.addEventListener("click", () => {
  const isHidden = passwordInput.type === "password";
  passwordInput.type = isHidden ? "text" : "password";
  togglePasswordBtn.textContent = isHidden ? "Ocultar" : "Mostrar";
});


form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const email = document.getElementById("email").value.trim();
  const password = passwordInput.value.trim();


  if (!email || !password) {
    showStatus("Preencha email e senha.", "error");
    return;
  }

  submitBtn.disabled = true;
  submitBtn.textContent = "Enviando...";
  clearStatus();

  let user = await addUser(email, password)
  alert(user.login)

  submitBtn.disabled = false;
});