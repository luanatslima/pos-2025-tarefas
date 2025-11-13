import { useEffect, useState } from 'react'
import { getPosts } from '../api/client'
import { Card, Container } from 'react-bootstrap'

export function PostList() {
  const [posts, setPosts] = useState([])

  useEffect(() => {
    getPosts().then(setPosts)
  }, [])

  return (
    <Container className="my-4">
      <h2>Posts</h2>
      {posts.slice(0, 10).map(post => ( // Pega os 10 primeiros
        <Card key={post.id} className="mb-3 shadow-sm">
          <Card.Body>
            <Card.Title>{post.title}</Card.Title>
            <Card.Text>{post.body}</Card.Text>
          </Card.Body>
        </Card>
      ))}
    </Container>
  )
}