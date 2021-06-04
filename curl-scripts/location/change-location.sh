curl "http://localhost:8000/api/change-location/${id}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "location": "'"${LOCATION}"'"
  }'

echo