import { addRecipe } from "../../api/recipes.js";

const form  = document.getElementById("add-recipe-form");

form.addEventListener("submit", async(event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('titulo', document.getElementById("title").value);
    formData.append('descricao', document.getElementById("description").value);
    formData.append('modo_preparo', document.getElementById("prepmethod").value);
    formData.append('preco', document.getElementById("price").value);

    let res = addRecipe(formData)
    
    // try {
    //     const response = await addRecipe(data);
    //     console.log("Recipe Added:", response);
    // } catch (error)
    // {
    //     console.error(error);
    // }

})
