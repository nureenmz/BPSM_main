# sending an email containing git logs
DATE=$(date)
git log | grep "Date:" > message_to_someone
mail -s "$USER $HOSTNAME $DATE" < message_to_someone <insertemailhere>
