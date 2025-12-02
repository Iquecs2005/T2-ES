const BASE_URL = "http://localhost:8000"

export async function addRecipe(data) {

    const res = await fetch(`${BASE_URL}/receitas/add`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data),
    });

    if(!res.ok) {
        throw new Error("Failed to add new recipe.")
    }

    return res.json();
}