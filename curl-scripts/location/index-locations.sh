curl "http://localhost:8000/api/locations" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo