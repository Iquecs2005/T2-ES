import config from "../config";

const BASE_URL = "http://localhost:5000"

export async function addRecipe(data) {

    const res = await fetch(`${config.apiUrl}/receita`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data),
    });

    if(!res.ok) {
        throw new Error("Failed to add new recipe.")
    }

    return res.json();
}