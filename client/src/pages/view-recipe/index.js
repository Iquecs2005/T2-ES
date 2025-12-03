import { getRecipe } from "../../api/recipes.js";

async function loadRecipe() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");

    if (!id) {
        console.error("Recipe ID does not exist.");
        return;
    }

    try {
        const recipe = await getRecipe(id);

        document.getElementById("title").value = recipe.titulo;
        document.getElementById("description").value = recipe.descricao;
        document.getElementById("prepmethod").value = recipe.modo_preparo;
        document.getElementById("price").value = recipe.preco;

    } catch (err) {
        console.error(err);
    }
}

loadRecipe();