import { config } from "../config.js";

export async function addRecipe(data) 
{
    let url = config.apiUrl + '/receita';

    try
    {
        const res = await fetch(url, {
            method: 'post',
            body: data
        })
        .then((response) => response.json())
        .catch((error) => {
          console.error('Error:', error);
        });
        
        return res;
    }
    catch (error)
    {
        console.error("Error adding recipe:", error);
        throw error
    }
}

export async function getRecipe(id) 
{
    let url = config.apiUrl + `/get_receita?id=${encodeURIComponent(id)}`;
    let recipe;

    try
    {
        const res = await fetch(url, {
            method: 'post',
        })
        .then((response) => response.json())
        .then((data) => recipe = data)
        .catch((error) => {
          console.error('Error:', error);
        });
        
        return recipe;
    }
    catch (error)
    {
        console.error("Error adding recipe:", error);
        throw error
    }
}