import { config } from "../config.js";

export async function getUser(login, senha) 
{
    let url = config.apiUrl + `/user?login=${encodeURIComponent(login)}&senha=${encodeURIComponent(senha)}`;
    let user;

    try
    {
        const res = await fetch(url, {
            method: 'get',
        })
        .then((response) => response.json())
        .then((data) => user = data)
        .catch((error) => {
          console.error('Error:', error);
        });
        
        return user;
    }
    catch (error)
    {
        console.error("Error getting user:", error);
        throw error
    }
}

export async function addUser(login, senha) 
{
    let url = config.apiUrl + `/user`;

    let formData = new FormData()
    formData.append('login', login)
    formData.append('senha', senha)

    let user;

    try
    {
        const res = await fetch(url, {
            method: 'post',
            body: formData,
        })
        .then((response) => response.json())
        .then((data) => user = data)
        .catch((error) => {
          console.error('Error:', error);
        });
        
        return user;
    }
    catch (error)
    {
        console.error("Error getting user:", error);
        throw error
    }
}