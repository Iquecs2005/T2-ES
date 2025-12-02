import { addRecipe } from "../../api/recipes";

const form  = document.getElementById("add-recipe-form");

form.addEventListener("submit", async(event) => {
    event.preventDefault();

    const data = {
        title: document.getElementById("title"),
        description: document.getElementById("description"),
        preparation_method: document.getElementById("prepmethod"),
        price: document.getElementById("price")
    }

    try {
        const response = await addRecipe(data);
        console.log("Recipe Added:", response);
    } catch (error)
    {
        console.error(error);
    }

})
