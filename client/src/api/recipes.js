const BASE_URL = "http://localhost:8000";

export async function getRecipe(recipe_id) {

    const res = await fetch(`${BASE_URL}/receita/${recipe_id}`);

    if (!res.ok) {
        throw new Error("Failed to get recipe.");
    }

    return res.json();
}

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

