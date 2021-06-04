curl "http://localhost:8000/api/locations/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "location": {
      "name": "'"${LOCATION}"'"
      }
  }'

echo