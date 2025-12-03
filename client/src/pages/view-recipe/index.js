import { getRecipe } from "../../api/recipes.js";

const form  = document.getElementById("add-recipe-form");

form.addEventListener("submit", async(event) => {
    event.preventDefault();

    let res = await getRecipe(Number(document.getElementById("id").value));
    
    document.getElementById("title").innerHTML = res.titulo
    document.getElementById("description").innerHTML = res.descricao
    document.getElementById("prepare_mode").innerHTML = res.modo_preparo
    document.getElementById("price").innerHTML = res.preco

    // try {
    //     const response = await addRecipe(data);
    //     console.log("Recipe Added:", response);
    // } catch (error)
    // {
    //     console.error(error);
    // }
})
