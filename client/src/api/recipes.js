import { config } from "../config.js";

export async function addRecipe(data) {

    let url = config.apiUrl + '/receita';

    const res = fetch(url, {
        method: 'post',
        body: data
    })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });

    return response;
}