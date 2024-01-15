import axios from "axios"

const serverUrl = "http://localhost:8000"

export const getUsers = async () => {
    try {
        const { data } = await axios.get(`${serverUrl}/users`)
        return data
    } catch (error) {
        console.log(error)
    }
}
