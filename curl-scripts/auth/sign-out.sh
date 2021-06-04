curl "http://localhost:8000/api/sign-out/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}" \

echo