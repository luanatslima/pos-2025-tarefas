const BASE_URL = 'https://jsonplaceholder.typicode.com'

export async function getPosts() {
  const res = await fetch(`${BASE_URL}/posts`)
  return res.json()
}

export async function getPosts() {
  const res = await fetch(`${BASE_URL}/users`)
  return res.json()
}
