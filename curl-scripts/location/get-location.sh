curl "http://localhost:8000/api/locations/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo