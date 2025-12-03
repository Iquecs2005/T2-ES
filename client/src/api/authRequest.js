export const authRequest = async (mode, email, password) => {
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
        throw new Error(errMsg);
    }

    return data;
};
