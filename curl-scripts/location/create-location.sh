curl "http://localhost:8000/api/locations" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "location": {
      "name": "'"${LOCATION}"'"
      }
  }'

echo