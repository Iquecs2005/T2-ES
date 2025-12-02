import { addRecipe } from "../../api/recipes";

const form  = document.getElementById("add-recipe-form");

form.addEventListener("submit", async(event) => {
    event.preventDefault();

    const data = {
        title: document.getElementById("title").value,
        description: document.getElementById("description").value,
        preparation_method: document.getElementById("prepmethod").value,
        price: document.getElementById("price").value
    }

    try {
        const response = await addRecipe(data);
        console.log("Recipe Added:", response);
    } catch (error)
    {
        console.error(error);
    }

})
