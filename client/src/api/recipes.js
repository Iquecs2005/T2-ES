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