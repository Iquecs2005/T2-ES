const API_BASE = "http://127.0.0.1:5000";


export async function authRequest(endpoint, payload) {
    const response = await fetch(`${API_BASE}${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    });
    const data = await response.json().catch(() => ({}));
    return { response, data };
}
