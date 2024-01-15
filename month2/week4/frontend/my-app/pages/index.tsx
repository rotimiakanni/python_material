import { getUsers } from "../utils"
import { useEffect, useState } from "react"

export default function Home() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    const fetchUsers = async () => {
      const users = await getUsers()
      console.log("USERS", users)
      setUsers(users)
    }
    fetchUsers()

  }, [])

  return (
    <main>
      <h1 className="text-4xl font-bold text-center">Hello World</h1>
    </main>
  )
}
