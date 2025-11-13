import { useEffect, useState } from 'react'
import { getUsers } from '../api/client'
import { Card, Container } from 'react-bootstrap'

export function UserList() {
  const [posts, setUsers] = useState([])

  useEffect(() => {
    getUsers().then(setUsers)
  }, [])

  return (
    <Container className="my-4">
      <h2>Posts</h2>
      {posts.slice(0, 10).map(post => ( // Pega os 10 primeiros
        <Card key={post.id} className="mb-3 shadow-sm">
          <Card.Body>
            <ul>
              <li> </li>
            </ul>
          </Card.Body>
        </Card>
      ))}
    </Container>
  )
}