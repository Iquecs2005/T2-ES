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


let mode = "signup";


const setMode = (newMode, clear = true) => {
  mode = newMode;
  const isLogin = mode === "login";
  formTitle.textContent = isLogin ? "Login" : "Cadastro";
  formSubtitle.textContent = isLogin
    ? "Acesse sua conta para continuar"
    : "Crie sua conta para pedir receitas";
  toggleCopy.textContent = isLogin ? "Não possui conta?" : "Já tem conta?";
  toggleBtn.textContent = isLogin ? "Cadastre-se" : "Entrar";
  submitBtn.textContent = isLogin ? "Entrar" : "Criar conta";
  if (clear) clearStatus();
};


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


  try {
    const endpoint = mode === "login" ? "/auth/login" : "/auth/signup";
    const response = await fetch(`${API_BASE}${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });


    const data = await response.json().catch(() => ({}));


    if (!response.ok) {
      let errMsg = "Erro ao processar requisição.";
      if (response.status === 401) {
        errMsg = data?.error || "Email ou senha incorreto.";
      } else if (response.status === 409) {
        errMsg = "Email já registrado.";
      } else if (Array.isArray(data) && data.length && data[0]?.msg) {
        errMsg = data.map((e) => e.msg).join(" | ");
      } else if (data?.error) {
        errMsg = data.error;
      } else if (response.status >= 500) {
        errMsg = "Erro interno do servidor.";
      }
      showStatus(errMsg, "error");
    } else {
      const successMsg =
        mode === "login" ? "Login realizado!" : "Conta criada! Agora é só entrar.";
      showStatus(successMsg, "success");
      form.reset();
      if (mode === "signup") setMode("login", false);
    }
  } catch (error) {
    showStatus("Não foi possível conectar ao servidor.", "error");
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = mode === "login" ? "Entrar" : "Criar conta";
  }
});


setMode("signup");